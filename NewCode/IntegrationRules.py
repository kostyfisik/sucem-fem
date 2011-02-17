from __future__ import division
import numpy as N

class IntgRule(object):
    def __init__(self, weights, coords):
        assert len(weights) == len(coords)
        self.weights = weights
        self.coords = coords

class TetRule(IntgRule): pass
class TriRule(IntgRule): pass
class PyrRule(IntgRule): pass

tri_rules = {}

a,b = 2/3, 1/6

tri_rules[2] = TriRule(
    N.array([1/3]*3, N.float64),
    N.array([[a,b,b],[b,a,b],[b,b,a]], N.float64))

a = 1/3.
b1 = 0.6 ; b2 = 0.2
w_a = -0.5625 ; w_b = 0.5208333333333333333333333

tri_rules[3] = TriRule(
    N.array([w_a, w_b, w_b, w_b], N.float64),
    N.array([[a,a,a], [b1, b2, b2], [b2,b1,b2], [b2,b2,b1]], N.float64))

a = 0.816847572980459
b = 0.091576213509771
c = 0.108103018168070
d = 0.445948490915965
w_a = 0.109951743655322
w_b = 0.223381589678011

tri_rules[4] = TriRule(
    N.array([w_a]*3 + [w_b]*3, N.float64),
    N.array([[a,b,b],[b,a,b],[b,b,a],[c,d,d],[d,c,d],[d,d,c]], N.float64))

a = 0.797426985353087
b = 0.101286507323456
d = 0.470142064105115
c = 0.059715871789770
w_a = 0.225
w_b = 0.125939180544827
w_c = 0.132394152788506

tri_rules[5] = TriRule(
    N.array([w_b]*3 + [w_c]*3 + [w_a], N.float64),
    N.array([[a,b,b], [b,a,b], [b,b,a], [c,d,d],
             [d,c,d], [d,d,c], [1/3, 1/3, 1/3]], N.float64))

a1 = 0.501426509658179
b1 = 0.249286745170910
a2 = 0.873821971016996
b2 = 0.063089014491502
a3 = 0.053145049844817
b3 = 0.310352451033784
c3 = 0.636502499121399
w_a = 0.116786275726379
w_b = 0.050844906370207
w_c = 0.082851075618374

tri_rules[6] = TriRule(
    N.array([w_a]*3 + [w_b]*3 + [w_c]*6, N.float64),
    N.array([[a1,b1,b1],[b1,a1,b1],[b1,b1,a1],[a2,b2,b2],[b2,a2,b2],
             [b2,b2,a2],[a3,b3,c3],[a3,c3,b3],[b3,a3,c3],[b3,c3,a3],
             [c3,a3,b3],[c3,b3,a3]],N.float64))

a1 = 1/3.
a2 = 0.479308067841920
b2 = 0.260345966079040
a3 = 0.869739794195568
b3 = 0.065130102902216
a4 = 0.048690315425316
b4 = 0.312865496004874
c4 = 0.638444188569810
w_a = -0.149570044467682
w_b = 0.175615257433208
w_c = 0.053347235608838
w_d = 0.077113760890257

tri_rules[7] = TriRule(
    N.array([w_a] + [w_b]*3 + [w_c]*3 + [w_d]*6, N.float64),
    N.array([[a1,a1,a1],[a2,b2,b2],[b2,a2,b2],[b2,b2,a2],
             [a3,b3,b3],[b3,a3,b3],[b3,b3,a3],
             [a4,b4,c4],[a4,c4,b4],[b4,a4,c4],
             [b4,c4,a4],[c4,a4,b4],[c4,b4,a4]], N.float64))

a1 = 1/3.
a2 = 0.081414823414554
b2 = 0.459292588292723
a3 = 0.658861384496480
b3 = 0.170569307751760
a4 = 0.898905543365938
b4 = 0.050547228317031
a5 = 0.008394777409958
b5 = 0.263112829634638
c5 = 0.728492392955404
w_a = 0.144315607677787
w_b = 0.095091634267285
w_c = 0.103217370534718
w_d = 0.032458497623198
w_e = 0.027230314174435

tri_rules[8] = TriRule(
    N.array([w_a]+[w_b]*3+[w_c]*3+[w_d]*3+[w_e]*6, N.float64),
    N.array([[a1,a1,a1],[a2,b2,b2],[b2,a2,b2],[b2,b2,a2],[a3,b3,b3],[b3,a3,b3],
             [b3,b3,a3],[a4,b4,b4],[b4,a4,b4],[b4,b4,a4],[a5,b5,c5],[a5,c5,b5],
             [b5,a5,c5],[b5,c5,a5],[c5,a5,b5],[c5,b5,a5]], N.float64))

a1 = 1/3.
a2 = 0.020634961602525
b2 = 0.489682519198738
a3 = 0.125820817014127
b3 = 0.437089591492937
a4 = 0.623592928761935
b4 = 0.188203535619033
a5 = 0.910540973211095
b5 = 0.044729513394453
a6 = 0.036838412054736
b6 = 0.221962989160766
c6 = 0.741198598784498
w_a = 0.097135796282799
w_b = 0.031334700227139
w_c = 0.077827541004774
w_d = 0.079647738927210
w_e = 0.025577675658698
w_f = 0.043283539377289

tri_rules[9] = TriRule(
    N.array([w_a] + [w_b]*3 + [w_c]*3 + [w_d]*3 + [w_e]*3 + [w_f]*6, N.float64),
    N.array([[a1,a1,a1], [a2,b2,b2], [b2,a2,b2], [b2,b2,a2],
             [a3,b3,b3], [b3,a3,b3], [b3,b3,a3],
             [a4,b4,b4], [b4,a4,b4], [b4,b4,a4],
             [a5,b5,b5], [b5,a5,b5], [b5,b5,a5],
             [a6,b6,c6],[a6,c6,b6],[b6,a6,c6],
             [b6,c6,a6],[c6,a6,b6],[c6,b6,a6]], N.float64))


w_a = 0.090817990382754
w_b = 0.036725957756467
w_c = 0.045321059435528
w_d = 0.072757916845420
w_e = 0.028327242531057
w_f = 0.009421666963733
a1 = 1/3.
a2 = 0.028844733232685
b2 = 0.485577633383657
a3 = 0.781036849029926
b3 = 0.109481575485037
a4 = 0.141707219414880
b4 = 0.307939838764121
c4 = 0.550352941820999
a5 = 0.025003534762686
b5 = 0.246672560639903
c5 = 0.728323904597411
a6 = 0.009540815400299
b6 = 0.066803251012200
c6 = 0.923655933587500

tri_rules[10] = TriRule(
    N.array([w_a] + [w_b]*3 + [w_c]*3 + [w_d]*6 + [w_e]*6 + [w_f]*6, N.float64),
    N.array([[a1,a1,a1],[a2,b2,b2],[b2,a2,b2],[b2,b2,a2],[a3,b3,b3],[b3,a3,b3],
             [b3,b3,a3],[a4,b4,c4],[a4,c4,b4],[b4,a4,c4],[b4,c4,a4],[c4,a4,b4],
             [c4,b4,a4],[a5,b5,c5],[a5,c5,b5],[b5,a5,c5],[b5,c5,a5],[c5,a5,b5],
             [c5,b5,a5],[a6,b6,c6],[a6,c6,b6],[b6,a6,c6],[b6,c6,a6],[c6,a6,b6],
             [c6,b6,a6]], N.float64))

a1 = -0.069222096541517
b1 = 0.534611048270758
a2 = 0.202061394068290
b2 = 0.398969302965855
a3 = 0.593380199137435
b3 = 0.203309900431282
a4 = 0.761298175434837
b4 = 0.119350912282581
a5 = 0.935270103777448
b5 = 0.032364948111276
a6 = 0.050178138310495
b6 = 0.356620648261293
c6 = 0.593201213428213
a7 = 0.021022016536166
b7 = 0.171488980304042
c7 = 0.807489003159792

w_a = 0.000927006328961
w_b = 0.077149534914813
w_c = 0.059322977380774
w_d = 0.036184540503418
w_e = 0.013659731002678
w_f = 0.052337111962204
w_g = 0.020707659639141

tri_rules[11] = TriRule(
    N.array([w_a]*3 + [w_b]*3 + [w_c]*3 + [w_d]*3 + [w_e]*3 + [w_f]*6 + [w_g]*6,
            N.float64),
    N.array([[a1,b1,b1],[b1,a1,b1],[b1,b1,a1],[a2,b2,b2],[b2,a2,b2],[b2,b2,a2],
             [a3,b3,b3],[b3,a3,b3],[b3,b3,a3],[a4,b4,b4],[b4,a4,b4],[b4,b4,a4],
             [a5,b5,b5],[b5,a5,b5],[b5,b5,a5],
             [a6,b6,c6],[a6,c6,b6],[b6,a6,c6],[b6,c6,a6],[c6,a6,b6],[c6,b6,a6],
             [a7,b7,c7],[a7,c7,b7],[b7,a7,c7],[b7,c7,a7],[c7,a7,b7],[c7,b7,a7]],
            N.float64))

tet_rules = {}
tet_rules[2] = TetRule(
    N.array([1/4, 1/4, 1/4, 1/4], N.float64),
    N.array([[0.5854101966249685, 0.138196601125015,  0.138196601125015,  0.138196601125015],
           [0.138196601125015,  0.5854101966249685, 0.138196601125015,  0.138196601125015],
           [0.138196601125015,  0.138196601125015,  0.5854101966249685, 0.138196601125015],
           [0.138196601125015,  0.138196601125015,  0.138196601125015,  0.5854101966249685]],
          N.float64))

# Eleven point rule; degree of precision 4 [Keast; 1st N=4 rule]
# Note that Keast's rule omit a factor of 6 (volume of a "unitary" tet).
zz = 1./4.
aa = 0.714285714285714285E-01
bb = 0.785714285714285714E+00
cc = 0.399403576166799219E+00
dd = 0.100596423833200785E+00
tet_rules[4] = TetRule(
    N.array([-6.0*0.131555555555555555E-01,
           6.0*0.7622222222222222222E-02,
           6.0*0.7622222222222222222E-02,
           6.0*0.7622222222222222222E-02,
           6.0*0.7622222222222222222E-02,
           6.0*0.2488888888888888880E-01,
           6.0*0.2488888888888888880E-01,
           6.0*0.2488888888888888880E-01,
           6.0*0.2488888888888888880E-01,
           6.0*0.2488888888888888880E-01,
           6.0*0.2488888888888888880E-01],
          N.float64),
    N.array([[zz, zz, zz, zz],
           [aa, aa, aa, bb],
           [aa, aa, bb, aa],
           [aa, bb, aa, aa],
           [bb, aa, aa, aa],
           [cc, cc, dd, dd],
           [cc, dd, cc, dd],
           [cc, dd, dd, cc],
           [dd, dd, cc, cc],
           [dd, cc, dd, cc],
           [dd, cc, cc, dd]],
          N.float64))

# 24 point rule; degree of precision 6 [Keast; 1986, CMAME]
# Note that Keast's rule omit a factor of 6 (volume of a "unitary" tet).
qpoint1 = N.array([ 0.214602871259151684     , 0.214602871259151684     , 0.214602871259151684,
                  0.356191386222544953     , 6.0*0.665379170969464506E-02 ], N.float64)
qpoint2 = N.array([ 0.406739585346113397E-01 , 0.406739585346113397E-01 , 0.406739585346113397E-01,
                  0.877978124396165982     , 6.0*0.167953517588677620E-02 ], N.float64)
qpoint3 = N.array([ 0.322337890142275646     , 0.322337890142275646     , 0.322337890142275646, 
                  0.329863295731730594E-01 , 6.0*0.922619692394239843E-02 ], N.float64)
qpoint4 = N.array([ 0.636610018750175299E-01 , 0.636610018750175299E-01 , 0.269672331458315867, 
                  0.603005664791649076     , 6.0*0.803571428571428248E-02 ], N.float64)

tet_rules[6] = TetRule(
    N.array([qpoint1[4],
           qpoint1[4],
           qpoint1[4],
           qpoint1[4],
           qpoint2[4],
           qpoint2[4],
           qpoint2[4],
           qpoint2[4],
           qpoint3[4],
           qpoint3[4],
           qpoint3[4],
           qpoint3[4],
           qpoint4[4],
           qpoint4[4],
           qpoint4[4],
           qpoint4[4],
           qpoint4[4],
           qpoint4[4],
           qpoint4[4],
           qpoint4[4],
           qpoint4[4],
           qpoint4[4],
           qpoint4[4],
           qpoint4[4]],
          N.float64),
    N.array([qpoint1[[0, 1, 2, 3]],
           qpoint1[[1, 2, 3, 0]],
           qpoint1[[2, 3, 0, 1]],
           qpoint1[[3, 0, 1, 2]],
           qpoint2[[0, 1, 2, 3]],
           qpoint2[[1, 2, 3, 0]],
           qpoint2[[2, 3, 0, 1]],
           qpoint2[[3, 0, 1, 2]],
           qpoint3[[0, 1, 2, 3]],
           qpoint3[[1, 2, 3, 0]],
           qpoint3[[2, 3, 0, 1]],
           qpoint3[[3, 0, 1, 2]],
           qpoint4[[0, 1, 2, 3]],
           qpoint4[[0, 1, 3, 2]],
           qpoint4[[0, 2, 1, 3]],
           qpoint4[[0, 3, 1, 2]],
           qpoint4[[0, 2, 3, 1]],
           qpoint4[[0, 3, 2, 1]],
           qpoint4[[2, 0, 1, 3]],
           qpoint4[[3, 0, 1, 2]],
           qpoint4[[2, 0, 3, 1]],
           qpoint4[[3, 0, 2, 1]],
           qpoint4[[2, 3, 0, 1]],
           qpoint4[[3, 2, 0, 1]]],
          N.float64))

qpoint1 = N.array([0.25, 0.25, 0.25, 0.25, -6.0*(0.393270066412926145E-01)], N.float64) 
qpoint2 = N.array([0.127470936566639015, 0.127470936566639015, 0.127470936566639015, 
                 0.617587190300082967, 6.0*(0.408131605934270525E-02)], N.float64) 
qpoint3 = N.array([0.320788303926322960E-01, 0.320788303926322960E-01, 0.320788303926322960E-01, 
                 0.903763508822103123, 6.0*(0.658086773304341943E-03)], N.float64) 
qpoint4 = N.array([0.497770956432810185E-01, 0.497770956432810185E-01, 0.450222904356718978, 
             0.450222904356718978, 6.0*(0.438425882512284693E-02)], N.float64) 
qpoint5 = N.array([0.183730447398549945, 0.183730447398549945, 0.316269552601450060, 
             0.316269552601450060, 6.0*(0.138300638425098166E-01)], N.float64) 
qpoint6 = N.array([0.231901089397150906, 0.231901089397150906, 0.229177878448171174E-01, 
             0.513280033360881072, 6.0*(0.424043742468372453E-02)], N.float64) 
qpoint7 = N.array([0.379700484718286102E-01, 0.379700484718286102E-01, 0.730313427807538396, 
               0.193746475248804382, 6.0*(0.223873973961420164E-02)], N.float64) 

# 45 point rule; degree of precision 8 [Keast; 1986, CMAME]
# Note that Keast's rule omit a factor of 6 (volume of a "unitary" tet). 
#
# !!!!*N*O*T*E*!!!! The negative weight on the first point is indicated
# positive in the reference, but in the text it is indicated that the rule does
# contain negative weights. Bu setting that one negative, the rule sums to
# unity. SO: hopefully this is correct....! (and indeed it seems to be OK)
tet_rules[8] = TetRule(
    N.array([qpoint1[4],
           qpoint2[4],
           qpoint2[4],
           qpoint2[4],
           qpoint2[4],
           qpoint3[4],
           qpoint3[4],
           qpoint3[4],
           qpoint3[4],
           qpoint4[4],
           qpoint4[4],
           qpoint4[4],
           qpoint4[4],
           qpoint4[4],
           qpoint4[4],
           qpoint5[4],
           qpoint5[4],
           qpoint5[4],
           qpoint5[4],
           qpoint5[4],
           qpoint5[4],
           qpoint6[4],
           qpoint6[4],
           qpoint6[4],
           qpoint6[4],
           qpoint6[4],
           qpoint6[4],
           qpoint6[4],
           qpoint6[4],
           qpoint6[4],
           qpoint6[4],
           qpoint6[4],
           qpoint6[4],
           qpoint7[4],
           qpoint7[4],
           qpoint7[4],
           qpoint7[4],
           qpoint7[4],
           qpoint7[4],
           qpoint7[4],
           qpoint7[4],
           qpoint7[4],
           qpoint7[4],
           qpoint7[4],
           qpoint7[4]], N.float64),
    N.array([qpoint1[[0, 1, 2, 3]],
           qpoint2[[0, 1, 2, 3]],   
           qpoint2[[1, 2, 3, 0]],   
           qpoint2[[2, 3, 0, 1]],   
           qpoint2[[3, 0, 1, 2]],   
           qpoint3[[0, 1, 2, 3]],   
           qpoint3[[1, 2, 3, 0]],   
           qpoint3[[2, 3, 0, 1]],   
           qpoint3[[3, 0, 1, 2]],   
           qpoint4[[0, 1, 2, 3]],   
           qpoint4[[0, 2, 1, 3]],   
           qpoint4[[0, 2, 3, 1]],   
           qpoint4[[2, 0, 1, 3]],   
           qpoint4[[2, 0, 3, 1]],   
           qpoint4[[2, 3, 0, 1]],   
           qpoint5[[0, 1, 2, 3]],   
           qpoint5[[0, 2, 1, 3]],   
           qpoint5[[0, 2, 3, 1]],   
           qpoint5[[2, 0, 1, 3]],   
           qpoint5[[2, 0, 3, 1]],   
           qpoint5[[2, 3, 0, 1]],   
           qpoint6[[0, 1, 2, 3]],   
           qpoint6[[0, 1, 3, 2]],   
           qpoint6[[0, 2, 1, 3]],   
           qpoint6[[0, 3, 1, 2]],   
           qpoint6[[0, 2, 3, 1]],   
           qpoint6[[0, 3, 2, 1]],   
           qpoint6[[2, 0, 1, 3]],   
           qpoint6[[3, 0, 1, 2]],   
           qpoint6[[2, 0, 3, 1]],   
           qpoint6[[3, 0, 2, 1]],   
           qpoint6[[2, 3, 0, 1]],   
           qpoint6[[3, 2, 0, 1]],   
           qpoint7[[0, 1, 2, 3]],   
           qpoint7[[0, 1, 3, 2]],   
           qpoint7[[0, 2, 1, 3]],   
           qpoint7[[0, 3, 1, 2]],   
           qpoint7[[0, 2, 3, 1]],   
           qpoint7[[0, 3, 2, 1]],   
           qpoint7[[2, 0, 1, 3]],   
           qpoint7[[3, 0, 1, 2]],   
           qpoint7[[2, 0, 3, 1]],   
           qpoint7[[3, 0, 2, 1]],   
           qpoint7[[2, 3, 0, 1]],   
           qpoint7[[3, 2, 0, 1]]], N.float64))

pyr_rules = {}
# Calculated using hammer56 (table 2, m=2) and 2x2 pt quadralateral rule for
# base in Maxima. Add factor 3 to weight for unit volume.

pyr_w_2 = N.array([2.5196470519956357645839096122746e-2,2.5196470519956357645839096122746e-2,2.5196470519956357645839096122746e-2,2.5196470519956357645839096122746e-2,5.8136862813376975687494237210587e-2,5.8136862813376975687494237210587e-2,5.8136862813376975687494237210587e-2,5.8136862813376975687494237210587e-2], N.float64)*3

pyr_pts_2 = N.array([[9.6332050209530557814428375329457e-2,9.6332050209530557814428375329457e-2,3.5951610577924415338564538837503e-1,3.5951610577924415338564538837503e-1,5.4415184401122528879992623629552e-1],[9.6332050209530557814428375329457e-2,3.5951610577924415338564538837503e-1,3.5951610577924415338564538837503e-1,9.6332050209530557814428375329457e-2,5.4415184401122528879992623629552e-1],[3.5951610577924415338564538837503e-1,9.6332050209530557814428375329457e-2,9.6332050209530557814428375329457e-2,3.5951610577924415338564538837503e-1,5.4415184401122528879992623629552e-1],[3.5951610577924415338564538837503e-1,3.5951610577924415338564538837503e-1,9.6332050209530557814428375329457e-2,9.6332050209530557814428375329457e-2,5.4415184401122528879992623629552e-1],[1.8543443699738559917947243766924e-1,1.8543443699738559917947243766924e-1,6.9205074034717302295378713195961e-1,6.9205074034717302295378713195961e-1,1.2251482265544137786674043037115e-1],[1.8543443699738559917947243766924e-1,6.9205074034717302295378713195961e-1,6.9205074034717302295378713195961e-1,1.8543443699738559917947243766924e-1,1.2251482265544137786674043037115e-1],[6.9205074034717302295378713195961e-1,1.8543443699738559917947243766924e-1,1.8543443699738559917947243766924e-1,6.9205074034717302295378713195961e-1,1.2251482265544137786674043037115e-1],[6.9205074034717302295378713195961e-1,6.9205074034717302295378713195961e-1,1.8543443699738559917947243766924e-1,1.8543443699738559917947243766924e-1,1.2251482265544137786674043037115e-1]], N.float64)

pyr_rules[(2,2)] = PyrRule(pyr_w_2, pyr_pts_2)

pyr_pts_3 = N.array([[7.3593763053861537832416843785903e-2,7.3593763053861537832416843785903e-2,5.7940247090778657744581961281015e-1,5.7940247090778657744581961281015e-1,3.4700376603835188472176354340395e-1],[7.3593763053861537832416843785903e-2,3.2649811698082405763911822829803e-1,5.7940247090778657744581961281015e-1,3.2649811698082405763911822829803e-1,3.4700376603835188472176354340395e-1],[7.3593763053861537832416843785903e-2,5.7940247090778657744581961281015e-1,5.7940247090778657744581961281015e-1,7.3593763053861537832416843785902e-2,3.4700376603835188472176354340395e-1],[3.2649811698082405763911822829803e-1,7.3593763053861537832416843785903e-2,3.2649811698082405763911822829803e-1,5.7940247090778657744581961281015e-1,3.4700376603835188472176354340395e-1],[3.2649811698082405763911822829803e-1,3.2649811698082405763911822829803e-1,3.2649811698082405763911822829803e-1,3.2649811698082405763911822829803e-1,3.4700376603835188472176354340395e-1],[3.2649811698082405763911822829803e-1,5.7940247090778657744581961281015e-1,3.2649811698082405763911822829803e-1,7.3593763053861537832416843785902e-2,3.4700376603835188472176354340395e-1],[5.7940247090778657744581961281015e-1,7.3593763053861537832416843785903e-2,7.3593763053861537832416843785902e-2,5.7940247090778657744581961281015e-1,3.4700376603835188472176354340395e-1],[5.7940247090778657744581961281015e-1,3.2649811698082405763911822829803e-1,7.3593763053861537832416843785902e-2,3.2649811698082405763911822829803e-1,3.4700376603835188472176354340395e-1],[5.7940247090778657744581961281015e-1,5.7940247090778657744581961281015e-1,7.3593763053861537832416843785902e-2,7.3593763053861537832416843785902e-2,3.4700376603835188472176354340395e-1],[3.3246742228767131640929003051405e-2,3.3246742228767131640929003051405e-2,2.6175104788273448523667251936455e-1,2.6175104788273448523667251936455e-1,7.0500220988849838312239847758405e-1],[3.3246742228767131640929003051405e-2,1.4749889505575080843880076120798e-1,2.6175104788273448523667251936455e-1,1.4749889505575080843880076120798e-1,7.0500220988849838312239847758405e-1],[3.3246742228767131640929003051405e-2,2.6175104788273448523667251936455e-1,2.6175104788273448523667251936455e-1,3.3246742228767131640929003051405e-2,7.0500220988849838312239847758405e-1],[1.4749889505575080843880076120798e-1,3.3246742228767131640929003051405e-2,1.4749889505575080843880076120798e-1,2.6175104788273448523667251936455e-1,7.0500220988849838312239847758405e-1],[1.4749889505575080843880076120798e-1,1.4749889505575080843880076120798e-1,1.4749889505575080843880076120798e-1,1.4749889505575080843880076120798e-1,7.0500220988849838312239847758405e-1],[1.4749889505575080843880076120798e-1,2.6175104788273448523667251936455e-1,1.4749889505575080843880076120798e-1,3.3246742228767131640929003051405e-2,7.0500220988849838312239847758405e-1],[2.6175104788273448523667251936455e-1,3.3246742228767131640929003051405e-2,3.3246742228767131640929003051405e-2,2.6175104788273448523667251936455e-1,7.0500220988849838312239847758405e-1],[2.6175104788273448523667251936455e-1,1.4749889505575080843880076120798e-1,3.3246742228767131640929003051405e-2,1.4749889505575080843880076120798e-1,7.0500220988849838312239847758405e-1],[2.6175104788273448523667251936455e-1,2.6175104788273448523667251936455e-1,3.3246742228767131640929003051405e-2,3.3246742228767131640929003051405e-2,7.0500220988849838312239847758405e-1],[1.0447511730348066455554189070349e-1,1.0447511730348066455554189070349e-1,8.225308586233696032886201302845e-1,8.225308586233696032886201302845e-1,7.2994024073149732155837979012004e-2],[1.0447511730348066455554189070349e-1,4.63502987963425133922081010494e-1,8.225308586233696032886201302845e-1,4.63502987963425133922081010494e-1,7.2994024073149732155837979012004e-2],[1.0447511730348066455554189070349e-1,8.2253085862336960328862013028451e-1,8.225308586233696032886201302845e-1,1.0447511730348066455554189070349e-1,7.2994024073149732155837979012004e-2],[4.63502987963425133922081010494e-1,1.0447511730348066455554189070349e-1,4.63502987963425133922081010494e-1,8.225308586233696032886201302845e-1,7.2994024073149732155837979012004e-2],[4.63502987963425133922081010494e-1,4.63502987963425133922081010494e-1,4.63502987963425133922081010494e-1,4.63502987963425133922081010494e-1,7.2994024073149732155837979012004e-2],[4.63502987963425133922081010494e-1,8.2253085862336960328862013028451e-1,4.63502987963425133922081010494e-1,1.0447511730348066455554189070349e-1,7.2994024073149732155837979012004e-2],[8.2253085862336960328862013028451e-1,1.0447511730348066455554189070349e-1,1.0447511730348066455554189070349e-1,8.225308586233696032886201302845e-1,7.2994024073149732155837979012004e-2],[8.2253085862336960328862013028451e-1,4.63502987963425133922081010494e-1,1.0447511730348066455554189070349e-1,4.63502987963425133922081010494e-1,7.2994024073149732155837979012004e-2],[8.2253085862336960328862013028451e-1,8.2253085862336960328862013028451e-1,1.0447511730348066455554189070349e-1,1.0447511730348066455554189070349e-1,7.2994024073149732155837979012004e-2]], N.float64)

pyr_w_3 = N.array([1.1284434356471143673110495398475e-2,1.8055094970353829876976792637561e-2,1.1284434356471143673110495398475e-2,1.8055094970353829876976792637561e-2,2.8888151952566127803162868220097e-2,1.8055094970353829876976792637561e-2,1.1284434356471143673110495398475e-2,1.8055094970353829876976792637561e-2,1.1284434356471143673110495398475e-2,2.3110110346127081798978773731348e-3,3.6976176553803330878366037970157e-3,2.3110110346127081798978773731348e-3,3.6976176553803330878366037970157e-3,5.9161882486085329405385660752251e-3,3.6976176553803330878366037970157e-3,2.3110110346127081798978773731348e-3,3.6976176553803330878366037970157e-3,2.3110110346127081798978773731348e-3,1.2124719217969646089378458504109e-2,1.9399550748751433743005533606575e-2,1.2124719217969646089378458504109e-2,1.9399550748751433743005533606575e-2,3.103928119800229398880885377052e-2,1.9399550748751433743005533606575e-2,1.2124719217969646089378458504109e-2,1.9399550748751433743005533606575e-2,1.2124719217969646089378458504109e-2], N.float64)*3

pyr_rules[(3,3)] = PyrRule(N.array(pyr_w_3), pyr_pts_3)

pyr_pts_3_4 = N.array([[2.3007885187847947349386876599651e-2,2.3007885187847947349386876599651e-2,1.8114069691537919494223330160921e-1,1.8114069691537919494223330160921e-1,7.9585141789677285770837982179114e-1],[2.3007885187847947349386876599651e-2,1.0207429105161357114581008910443e-1,1.8114069691537919494223330160921e-1,1.0207429105161357114581008910443e-1,7.9585141789677285770837982179114e-1],[2.3007885187847947349386876599651e-2,1.8114069691537919494223330160921e-1,1.8114069691537919494223330160921e-1,2.3007885187847947349386876599651e-2,7.9585141789677285770837982179114e-1],[1.0207429105161357114581008910443e-1,2.3007885187847947349386876599651e-2,1.0207429105161357114581008910443e-1,1.8114069691537919494223330160921e-1,7.9585141789677285770837982179114e-1],[1.0207429105161357114581008910443e-1,1.0207429105161357114581008910443e-1,1.0207429105161357114581008910443e-1,1.0207429105161357114581008910443e-1,7.9585141789677285770837982179114e-1],[1.0207429105161357114581008910443e-1,1.8114069691537919494223330160921e-1,1.0207429105161357114581008910443e-1,2.3007885187847947349386876599651e-2,7.9585141789677285770837982179114e-1],[1.8114069691537919494223330160921e-1,2.3007885187847947349386876599651e-2,2.3007885187847947349386876599651e-2,1.8114069691537919494223330160921e-1,7.9585141789677285770837982179114e-1],[1.8114069691537919494223330160921e-1,1.0207429105161357114581008910443e-1,2.3007885187847947349386876599651e-2,1.0207429105161357114581008910443e-1,7.9585141789677285770837982179114e-1],[1.8114069691537919494223330160921e-1,1.8114069691537919494223330160921e-1,2.3007885187847947349386876599651e-2,2.3007885187847947349386876599651e-2,7.9585141789677285770837982179114e-1],[5.4429574141155260468178069971411e-2,5.4429574141155260468178069971411e-2,4.2852313075447723159625042164342e-1,4.2852313075447723159625042164342e-1,5.1704729510436750793557150838518e-1],[5.4429574141155260468178069971411e-2,2.4147635244781624603221424580741e-1,4.2852313075447723159625042164342e-1,2.4147635244781624603221424580741e-1,5.1704729510436750793557150838518e-1],[5.4429574141155260468178069971411e-2,4.2852313075447723159625042164342e-1,4.2852313075447723159625042164342e-1,5.442957414115526046817806997141e-2,5.1704729510436750793557150838518e-1],[2.4147635244781624603221424580741e-1,5.4429574141155260468178069971411e-2,2.4147635244781624603221424580741e-1,4.2852313075447723159625042164342e-1,5.1704729510436750793557150838518e-1],[2.4147635244781624603221424580741e-1,2.4147635244781624603221424580741e-1,2.4147635244781624603221424580741e-1,2.4147635244781624603221424580741e-1,5.1704729510436750793557150838518e-1],[2.4147635244781624603221424580741e-1,4.2852313075447723159625042164342e-1,2.4147635244781624603221424580741e-1,5.442957414115526046817806997141e-2,5.1704729510436750793557150838518e-1],[4.2852313075447723159625042164342e-1,5.4429574141155260468178069971411e-2,5.442957414115526046817806997141e-2,4.2852313075447723159625042164342e-1,5.1704729510436750793557150838518e-1],[4.2852313075447723159625042164342e-1,2.4147635244781624603221424580741e-1,5.442957414115526046817806997141e-2,2.4147635244781624603221424580741e-1,5.1704729510436750793557150838518e-1],[4.2852313075447723159625042164342e-1,4.2852313075447723159625042164342e-1,5.442957414115526046817806997141e-2,5.442957414115526046817806997141e-2,5.1704729510436750793557150838518e-1],[8.5810964896444093324174479796722e-2,8.5810964896444093324174479796722e-2,6.7558829755169360441434317697963e-1,6.7558829755169360441434317697963e-1,2.3860073755186230226148234322365e-1],[8.5810964896444093324174479796722e-2,3.8069963122406884886925882838818e-1,6.7558829755169360441434317697963e-1,3.8069963122406884886925882838818e-1,2.3860073755186230226148234322365e-1],[8.5810964896444093324174479796722e-2,6.7558829755169360441434317697963e-1,6.7558829755169360441434317697963e-1,8.581096489644409332417447979672e-2,2.3860073755186230226148234322365e-1],[3.8069963122406884886925882838818e-1,8.5810964896444093324174479796722e-2,3.8069963122406884886925882838818e-1,6.7558829755169360441434317697963e-1,2.3860073755186230226148234322365e-1],[3.8069963122406884886925882838818e-1,3.8069963122406884886925882838818e-1,3.8069963122406884886925882838818e-1,3.8069963122406884886925882838818e-1,2.3860073755186230226148234322365e-1],[3.8069963122406884886925882838818e-1,6.7558829755169360441434317697963e-1,3.8069963122406884886925882838818e-1,8.581096489644409332417447979672e-2,2.3860073755186230226148234322365e-1],[6.7558829755169360441434317697963e-1,8.5810964896444093324174479796722e-2,8.581096489644409332417447979672e-2,6.7558829755169360441434317697963e-1,2.3860073755186230226148234322365e-1],[6.7558829755169360441434317697963e-1,3.8069963122406884886925882838818e-1,8.581096489644409332417447979672e-2,3.8069963122406884886925882838818e-1,2.3860073755186230226148234322365e-1],[6.7558829755169360441434317697963e-1,6.7558829755169360441434317697963e-1,8.581096489644409332417447979672e-2,8.581096489644409332417447979672e-2,2.3860073755186230226148234322365e-1],[1.0723557268477264641523687768444e-1,1.0723557268477264641523687768444e-1,8.4426387786823002149019679571552e-1,8.4426387786823002149019679571552e-1,4.8500549446997332094566326600039e-2],[1.0723557268477264641523687768444e-1,4.7574972527650133395271683669998e-1,8.4426387786823002149019679571552e-1,4.7574972527650133395271683669998e-1,4.8500549446997332094566326600039e-2],[1.0723557268477264641523687768444e-1,8.4426387786823002149019679571552e-1,8.4426387786823002149019679571552e-1,1.0723557268477264641523687768444e-1,4.8500549446997332094566326600039e-2],[4.7574972527650133395271683669998e-1,1.0723557268477264641523687768444e-1,4.7574972527650133395271683669998e-1,8.4426387786823002149019679571552e-1,4.8500549446997332094566326600039e-2],[4.7574972527650133395271683669998e-1,4.7574972527650133395271683669998e-1,4.7574972527650133395271683669998e-1,4.7574972527650133395271683669998e-1,4.8500549446997332094566326600039e-2],[4.7574972527650133395271683669998e-1,8.4426387786823002149019679571552e-1,4.7574972527650133395271683669998e-1,1.0723557268477264641523687768444e-1,4.8500549446997332094566326600039e-2],[8.4426387786823002149019679571552e-1,1.0723557268477264641523687768444e-1,1.0723557268477264641523687768444e-1,8.4426387786823002149019679571552e-1,4.8500549446997332094566326600039e-2],[8.4426387786823002149019679571552e-1,4.7574972527650133395271683669998e-1,1.0723557268477264641523687768444e-1,4.7574972527650133395271683669998e-1,4.8500549446997332094566326600039e-2],[8.4426387786823002149019679571552e-1,8.4426387786823002149019679571552e-1,1.0723557268477264641523687768444e-1,1.0723557268477264641523687768444e-1,4.8500549446997332094566326600039e-2]], N.float64)

pyr_w_3_4 = N.array([7.9878400848133225793019676035869e-4,1.2780544135701316126883148165739e-3,7.9878400848133225793019676035869e-4,1.2780544135701316126883148165739e-3,2.0448870617122105803013037065182e-3,1.2780544135701316126883148165739e-3,7.9878400848133225793019676035869e-4,1.2780544135701316126883148165739e-3,7.9878400848133225793019676035869e-4,5.2958246275403606230478858890597e-3,8.4733194040645769968766174224955e-3,5.2958246275403606230478858890597e-3,8.4733194040645769968766174224955e-3,1.3557311046503323195002587875993e-2,8.4733194040645769968766174224955e-3,5.2958246275403606230478858890597e-3,8.4733194040645769968766174224955e-3,5.2958246275403606230478858890597e-3,1.1069351064754182789166678272142e-2,1.7710961703606692462666685235428e-2,1.1069351064754182789166678272142e-2,1.7710961703606692462666685235428e-2,2.8337538725770707940266696376684e-2,1.7710961703606692462666685235428e-2,1.1069351064754182789166678272142e-2,1.7710961703606692462666685235428e-2,1.1069351064754182789166678272142e-2,8.5562049082776226158316928491665e-3,1.3689927853244196185330708558666e-2,8.5562049082776226158316928491665e-3,1.3689927853244196185330708558666e-2,2.1903884565190713896529133693866e-2,1.3689927853244196185330708558666e-2,8.5562049082776226158316928491665e-3,1.3689927853244196185330708558666e-2,8.5562049082776226158316928491665e-3], N.float64)*3

pyr_rules[(3,4)] = PyrRule(N.array(pyr_w_3_4), pyr_pts_3_4)
