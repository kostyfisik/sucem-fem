"""
Test driver code. Anything of lasting importance should be factored out pronto
"""
from __future__ import division
import os
import pickle
import random
import numpy as N
import scipy
from scipy import integrate

#
# Local Imports
#
import NewCode
from NewCode import Utilities
import NewCode.eMAGUSImport as eMAGUSImport
import NewCode.Mesh as Mesh
from NewCode.Meshes import BrickMesh, BrickMeshGen
from NewCode.Utilities import Struct, partial, close_to_point
from NewCode import SubDimMesh, DifferentialForm, Waveforms, PostProc, Feeds, Runners
from NewCode.DifferentialForm import Discretiser, SubDimDiscretiser, \
     SubDimDiscretiserEntities, allconstrained
from NewCode.DiscretisedSystem import CurlCurlNewmarkDirechlet, BrickCurlCurlNewmarkDirechlet 

from NewCode.Feeds import WaveguideEigenMatcher

import wg_hybrid_disc_fake

eMAGUSImport.init('workspace')
tet_mesh = Mesh.Mesh(eMAGUSImport.get_listmesh())

print 'Tet_mesh elements: ', len(tet_mesh.elements)

bfrac = 0.45
h = 1/4.
a,b,c = 1, 0.25, 5.1
bfrac = N.ceil(bfrac*c/h)*h/c

brick_mesh = BrickMesh.Mesh(
    BrickMeshGen.make_rect_cavity_brick_listmesh(a,b,c*bfrac, [h, h, h]))

print 'Brick-Mesh elements: ', len(brick_mesh.elements)


free = DifferentialForm.allfree

g_eps = 1e-10                           # Geometrical tollerance
hybrid_boundary_p = close_to_point(c*bfrac, g_eps)
a_p, b_p, c_p = (close_to_point(xx, g_eps) for xx in (a,b,c))
zero_p = close_to_point(0, g_eps)

def freeE(ent):
    x,y,z = ent.nodeCoords.T
    return not (N.all(a_p(x)) or N.all(zero_p(x)) or 
                N.all(b_p(y)) or N.all(zero_p(y)) or
                N.all(c_p(z)) or N.all(zero_p(z)))

from analytical_WG_driver import WGT

drv_fun = WGT.discrete_drv_fn
z_measure = WGT.test_z
z_measure_p = close_to_point(z_measure, g_eps)
runtime = WGT.t_final
z_port = 0.
z_port_p = close_to_point(z_port, g_eps)
a=1. ; b=0.25                           # WG x/y dim
zero_p = close_to_point(0, g_eps)
on_port = lambda ent: N.all(z_port_p(ent.nodeCoords[:,2]))
def port_free(ent):
    x,y,z = ent.nodeCoords.T
    return not (N.all(a_p(x)) or N.all(zero_p(x)) or 
                N.all(b_p(y)) or N.all(zero_p(y)))


on_measurement_port = lambda ent: N.all(z_measure_p(ent.nodeCoords[:,2]))
measurement_port_free = port_free
direch_free = lambda ent: on_port(ent) and port_free(ent)  

hybrid_boundary_p = close_to_point(c*bfrac, g_eps)
on_hbdry = lambda ent: N.all([hybrid_boundary_p(z) for (x,y,z) in ent.nodeCoords])

hyb_mesh = Struct(tet=tet_mesh, brick=brick_mesh, on_hbdry=on_hbdry)

class HybridCurlCurlNewmarkDirechlet(CurlCurlNewmarkDirechlet):
    DiscretiserModule = wg_hybrid_disc_fake
    DirechClass = BrickCurlCurlNewmarkDirechlet
    def setDirechBCs(self, DirechBCs, DirechVolBCs=allconstrained):
        self.direchSys = self.DirechClass(
            self.mesh.brick, order=self.order, BC=DirechBCs,
            volBC=DirechVolBCs, useQ=self.hasQ)
        self.direchSys.disc.setIntegrationRule(self.order*2-1)
        
class TestRun(Runners.TestRun):
    drv_fun = staticmethod(drv_fun)
    useLU = True
    SystemClass = HybridCurlCurlNewmarkDirechlet
    def __init__(self, mesh, **kwargs):
        self.system = self.SystemClass(mesh, **kwargs)

    def setupSource(self):
        self.system.drive_fun = self.drv_fun
        self.system.setDirechBCs(direch_free)
        self.sm = sm = Feeds.BrickSurfaceFieldMatcher()
        sm.initSubdim(self.system.disc.discs.brick, on_port, port_free)
        self.E_wg = E_wg = Feeds.gen_E_TE01(a,b)
        self.direch_dofArray = sm.matchKnown(E_wg)
        self.system.direchSys.dofs.dofArray[:] = self.direch_dofArray

    def setupLogging(self):
        divisor = self.log_divisor
        from NewCode import PostProc
        self.sm_m = sm_m = Feeds.BrickSurfaceFieldMatcher()
        sm_m.initSubdim(self.system.disc.discs.brick, on_measurement_port, measurement_port_free)
        self.measure_dofArray = sm_m.matchKnown(self.E_wg)
        self.tif = tif = Feeds.BrickTangentialFuncProjSurfaceIntegral(
            self.system.disc.discs.brick, on_measurement_port, measurement_port_free)
        self.test_pts = test_pts = N.array([[a/2, b/2, z_measure]], N.float64)
        test_elnos, test_el_coords = PostProc.LocatePoints(
            self.system.disc.discs.brick.mesh, test_pts)
        self.test_elnos = test_elnos ; self.test_el_coords = test_el_coords
        #self.system.addReconstructedLogger(test_elnos, test_el_coords, divisor=divisor)
        self.logged_dofnos = logged_dofnos = tif.superDOFMap
        self.system.addLogger(dofnos=logged_dofnos, divisor=divisor)
        
    def getResult(self):
        #rsv = N.array(self.system.loggedReconstructed[0]['vals'])[:,0,:]
        #point_reconstructed_ts = rsv[:,1]
        sm_m = self.sm_m
        measure_dofArray = self.measure_dofArray
        nf =  N.dot(measure_dofArray, sm_m.subDisc.matrix.mass().matvec(measure_dofArray))
        ts_modeintg_n = N.array([
            N.dot(measure_dofArray, sm_m.subDisc.matrix.mass().matvec(dof_vec))
            for dof_vec in self.system.loggedDOFs[tuple(self.logged_dofnos)].vals],
                                N.float64)/nf        
        return Struct(nf=nf, ts_modeintg_n=ts_modeintg_n)

analytical_dt = WGT.dt                  # Should be 0.0625

order = 2
TRS = TestRun(hyb_mesh, order=order, BC=freeE, useQ=False)
M = TRS.system.disc.matrix.mass()
S = TRS.system.disc.matrix.stiffness()
st = TRS.system.disc.stuff
#M = st.M_brick_l
#S = st.S_brick_l

hc_T_tetonly = st.hc_T[[i for i in range(st.hc_T.shape[0])
                        if st.hc_T[i,:].nnz > 0]].copy()

# M = hc_T_tetonly.matmat(st.M_mtet.matmat(hc_T_tetonly.T))
# S = hc_T_tetonly.matmat(st.S_mtet.matmat(hc_T_tetonly.T))


from scipy.sparse.linalg.eigen.arpack import speigs
sigma = 0.5
def sigma_solve_gen(S):
    from NewCode.MatrixUtils import MatrixSolver
    ms = MatrixSolver(5e-9)
    cnt = [0]
    def solve(b):
        print 'Starting iterative solve'
        x = ms.solve_mat_vec(S, b)
        cnt[0] += 1
        print 'Done with iterative solve %i' %cnt[0]
        return x
    return solve
#sigma_solve = sigma_solve_gen(S - sigma*M)
print "(nodofs, nnz, sparsity %)", M.shape[0], M.nnz, M.nnz/M.shape[0]**2*100
# print 'Sparse LU decomposition'
# sigma_solve = scipy.sparse.linalg.dsolve.factorized(S - sigma*M)

print 'Solving Eigenproblem'
# w,v = speigs.ARPACK_gen_eigs(M.matvec, sigma_solve, M.shape[0], sigma, 51, ncv=91)
w,v = scipy.linalg.eig(S.todense(), M.todense())
from AnalyticResults import PEC_cavity, accoustic_eigs, err_percentage

#ares = PEC_cavity['rect-white']
#ares = accoustic_eigs['rect1x0.75x0.5']
ares = PEC_cavity['rect1x0.25x5.1']

res =  N.array(sorted(N.abs(w[w > 0.0000001]))[0:10])

# print res

err = err_percentage(ares, sorted(w[w > 0.0000001])[0:10])
RMS_err = Utilities.RMS(err)
#edges = eigsys.disc.geomEntities['edge']
#faces = eigsys.disc.geomEntities['face']

print RMS_err
print err
print 'Min real eigvalue: ', N.min(N.real(w))
