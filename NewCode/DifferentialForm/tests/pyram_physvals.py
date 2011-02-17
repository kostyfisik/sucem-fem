from __future__ import division
import numpy as N

#All for FourPyram mesh.
oneform_edge0 = N.array([[[[-1,0,1/3],[-1/2,0,1/6],[0,0,0],[0,0,1/3],[0,0,1/6],[0,0,0],[1,0,1/3],[1/2,0,1/6],[0,0,0],[-101/200,0,101/600],[-101/400,0,101/1200],[0,0,0],[0,0,101/600],[0,0,101/1200],[0,0,0],[101/200,0,101/600],[101/400,0,101/1200],[0,0,0],[-1/100,0,1/300],[-1/200,0,1/600],[0,0,0],[0,0,1/300],[0,0,1/600],[0,0,0],[1/100,0,1/300],[1/200,0,1/600],[0,0,0]],[[-1,1/2,0],[0,1/2,0],[1,1/2,0],[-1/2,1/4,0],[0,1/4,0],[1/2,1/4,0],[0,0,0],[0,0,0],[0,0,0],[-101/200,101/400,0],[0,101/400,0],[101/200,101/400,0],[-101/400,101/800,0],[0,101/800,0],[101/400,101/800,0],[0,0,0],[0,0,0],[0,0,0],[-1/100,1/200,0],[0,1/200,0],[1/100,1/200,0],[-1/200,1/400,0],[0,1/400,0],[1/200,1/400,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[-1/2,1/4,0],[0,1/4,0],[1/2,1/4,0],[-1,1/2,0],[0,1/2,0],[1,1/2,0],[0,0,0],[0,0,0],[0,0,0],[-101/400,101/800,0],[0,101/800,0],[101/400,101/800,0],[-101/200,101/400,0],[0,101/400,0],[101/200,101/400,0],[0,0,0],[0,0,0],[0,0,0],[-1/200,1/400,0],[0,1/400,0],[1/200,1/400,0],[-1/100,1/200,0],[0,1/200,0],[1/100,1/200,0]],[[0,0,0],[-1/2,0,1/6],[-1,0,1/3],[0,0,0],[0,0,1/6],[0,0,1/3],[0,0,0],[1/2,0,1/6],[1,0,1/3],[0,0,0],[-101/400,0,101/1200],[-101/200,0,101/600],[0,0,0],[0,0,101/1200],[0,0,101/600],[0,0,0],[101/400,0,101/1200],[101/200,0,101/600],[0,0,0],[-1/200,0,1/600],[-1/100,0,1/300],[0,0,0],[0,0,1/600],[0,0,1/300],[0,0,0],[1/200,0,1/600],[1/100,0,1/300]],[[2,0,0],[1,0,0],[0,0,0],[1,0,0],[1/2,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[101/100,99/400,33/200],[301/400,99/400,33/400],[99/200,99/400,0],[301/400,99/800,33/200],[1/2,99/800,33/400],[99/400,99/800,0],[99/200,0,33/200],[99/400,0,33/400],[0,0,0],[1/50,99/200,33/100],[101/200,99/200,33/200],[99/100,99/200,0],[101/200,99/400,33/100],[1/2,99/400,33/200],[99/200,99/400,0],[99/100,0,33/100],[99/200,0,33/200],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[1,0,0],[1/2,0,0],[0,0,0],[2,0,0],[1,0,0],[0,0,0],[99/200,0,-33/200],[99/400,0,-33/400],[0,0,0],[301/400,99/800,-33/200],[1/2,99/800,-33/400],[99/400,99/800,0],[101/100,99/400,-33/200],[301/400,99/400,-33/400],[99/200,99/400,0],[99/100,0,-33/100],[99/200,0,-33/200],[0,0,0],[101/200,99/400,-33/100],[1/2,99/400,-33/200],[99/200,99/400,0],[1/50,99/200,-33/100],[101/200,99/200,-33/200],[99/100,99/200,0]],[[0,0,0],[1,0,0],[2,0,0],[0,0,0],[1/2,0,0],[1,0,0],[0,0,0],[0,0,0],[0,0,0],[99/200,-99/400,0],[301/400,-99/400,33/400],[101/100,-99/400,33/200],[99/400,-99/800,0],[1/2,-99/800,33/400],[301/400,-99/800,33/200],[0,0,0],[99/400,0,33/400],[99/200,0,33/200],[99/100,-99/200,0],[101/200,-99/200,33/200],[1/50,-99/200,33/100],[99/200,-99/400,0],[1/2,-99/400,33/200],[101/200,-99/400,33/100],[0,0,0],[99/200,0,33/200],[99/100,0,33/100]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[1/2,0,0],[1,0,0],[0,0,0],[1,0,0],[2,0,0],[0,0,0],[99/400,0,-33/400],[99/200,0,-33/200],[99/400,-99/800,0],[1/2,-99/800,-33/400],[301/400,-99/800,-33/200],[99/200,-99/400,0],[301/400,-99/400,-33/400],[101/100,-99/400,-33/200],[0,0,0],[99/200,0,-33/200],[99/100,0,-33/100],[99/200,-99/400,0],[1/2,-99/400,-33/200],[101/200,-99/400,-33/100],[99/100,-99/200,0],[101/200,-99/200,-33/200],[1/50,-99/200,-33/100]]],[[[1,0,1/3],[1/2,0,1/6],[0,0,0],[0,0,1/3],[0,0,1/6],[0,0,0],[-1,0,1/3],[-1/2,0,1/6],[0,0,0],[101/200,0,101/600],[101/400,0,101/1200],[0,0,0],[0,0,101/600],[0,0,101/1200],[0,0,0],[-101/200,0,101/600],[-101/400,0,101/1200],[0,0,0],[1/100,0,1/300],[1/200,0,1/600],[0,0,0],[0,0,1/300],[0,0,1/600],[0,0,0],[-1/100,0,1/300],[-1/200,0,1/600],[0,0,0]],[[1,1/2,0],[0,1/2,0],[-1,1/2,0],[1/2,1/4,0],[0,1/4,0],[-1/2,1/4,0],[0,0,0],[0,0,0],[0,0,0],[101/200,101/400,0],[0,101/400,0],[-101/200,101/400,0],[101/400,101/800,0],[0,101/800,0],[-101/400,101/800,0],[0,0,0],[0,0,0],[0,0,0],[1/100,1/200,0],[0,1/200,0],[-1/100,1/200,0],[1/200,1/400,0],[0,1/400,0],[-1/200,1/400,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[1/2,1/4,0],[0,1/4,0],[-1/2,1/4,0],[1,1/2,0],[0,1/2,0],[-1,1/2,0],[0,0,0],[0,0,0],[0,0,0],[101/400,101/800,0],[0,101/800,0],[-101/400,101/800,0],[101/200,101/400,0],[0,101/400,0],[-101/200,101/400,0],[0,0,0],[0,0,0],[0,0,0],[1/200,1/400,0],[0,1/400,0],[-1/200,1/400,0],[1/100,1/200,0],[0,1/200,0],[-1/100,1/200,0]],[[0,0,0],[1/2,0,1/6],[1,0,1/3],[0,0,0],[0,0,1/6],[0,0,1/3],[0,0,0],[-1/2,0,1/6],[-1,0,1/3],[0,0,0],[101/400,0,101/1200],[101/200,0,101/600],[0,0,0],[0,0,101/1200],[0,0,101/600],[0,0,0],[-101/400,0,101/1200],[-101/200,0,101/600],[0,0,0],[1/200,0,1/600],[1/100,0,1/300],[0,0,0],[0,0,1/600],[0,0,1/300],[0,0,0],[-1/200,0,1/600],[-1/100,0,1/300]],[[-2,0,0],[-1,0,0],[0,0,0],[-1,0,0],[-1/2,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[-101/100,99/400,33/200],[-301/400,99/400,33/400],[-99/200,99/400,0],[-301/400,99/800,33/200],[-1/2,99/800,33/400],[-99/400,99/800,0],[-99/200,0,33/200],[-99/400,0,33/400],[0,0,0],[-1/50,99/200,33/100],[-101/200,99/200,33/200],[-99/100,99/200,0],[-101/200,99/400,33/100],[-1/2,99/400,33/200],[-99/200,99/400,0],[-99/100,0,33/100],[-99/200,0,33/200],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[-1,0,0],[-1/2,0,0],[0,0,0],[-2,0,0],[-1,0,0],[0,0,0],[-99/200,0,-33/200],[-99/400,0,-33/400],[0,0,0],[-301/400,99/800,-33/200],[-1/2,99/800,-33/400],[-99/400,99/800,0],[-101/100,99/400,-33/200],[-301/400,99/400,-33/400],[-99/200,99/400,0],[-99/100,0,-33/100],[-99/200,0,-33/200],[0,0,0],[-101/200,99/400,-33/100],[-1/2,99/400,-33/200],[-99/200,99/400,0],[-1/50,99/200,-33/100],[-101/200,99/200,-33/200],[-99/100,99/200,0]],[[0,0,0],[-1,0,0],[-2,0,0],[0,0,0],[-1/2,0,0],[-1,0,0],[0,0,0],[0,0,0],[0,0,0],[-99/200,-99/400,0],[-301/400,-99/400,33/400],[-101/100,-99/400,33/200],[-99/400,-99/800,0],[-1/2,-99/800,33/400],[-301/400,-99/800,33/200],[0,0,0],[-99/400,0,33/400],[-99/200,0,33/200],[-99/100,-99/200,0],[-101/200,-99/200,33/200],[-1/50,-99/200,33/100],[-99/200,-99/400,0],[-1/2,-99/400,33/200],[-101/200,-99/400,33/100],[0,0,0],[-99/200,0,33/200],[-99/100,0,33/100]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[-1/2,0,0],[-1,0,0],[0,0,0],[-1,0,0],[-2,0,0],[0,0,0],[-99/400,0,-33/400],[-99/200,0,-33/200],[-99/400,-99/800,0],[-1/2,-99/800,-33/400],[-301/400,-99/800,-33/200],[-99/200,-99/400,0],[-301/400,-99/400,-33/400],[-101/100,-99/400,-33/200],[0,0,0],[-99/200,0,-33/200],[-99/100,0,-33/100],[-99/200,-99/400,0],[-1/2,-99/400,-33/200],[-101/200,-99/400,-33/100],[-99/100,-99/200,0],[-101/200,-99/200,-33/200],[-1/50,-99/200,-33/100]]],[[[0,-1/2,1/3],[0,-1/4,1/6],[0,0,0],[0,0,1/3],[0,0,1/6],[0,0,0],[0,1/2,1/3],[0,1/4,1/6],[0,0,0],[0,-101/400,101/600],[0,-101/800,101/1200],[0,0,0],[0,0,101/600],[0,0,101/1200],[0,0,0],[0,101/400,101/600],[0,101/800,101/1200],[0,0,0],[0,-1/200,1/300],[0,-1/400,1/600],[0,0,0],[0,0,1/300],[0,0,1/600],[0,0,0],[0,1/200,1/300],[0,1/400,1/600],[0,0,0]],[[1,-1/2,0],[1,0,0],[1,1/2,0],[1/2,-1/4,0],[1/2,0,0],[1/2,1/4,0],[0,0,0],[0,0,0],[0,0,0],[101/200,-101/400,0],[101/200,0,0],[101/200,101/400,0],[101/400,-101/800,0],[101/400,0,0],[101/400,101/800,0],[0,0,0],[0,0,0],[0,0,0],[1/100,-1/200,0],[1/100,0,0],[1/100,1/200,0],[1/200,-1/400,0],[1/200,0,0],[1/200,1/400,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[1/2,-1/4,0],[1/2,0,0],[1/2,1/4,0],[1,-1/2,0],[1,0,0],[1,1/2,0],[0,0,0],[0,0,0],[0,0,0],[101/400,-101/800,0],[101/400,0,0],[101/400,101/800,0],[101/200,-101/400,0],[101/200,0,0],[101/200,101/400,0],[0,0,0],[0,0,0],[0,0,0],[1/200,-1/400,0],[1/200,0,0],[1/200,1/400,0],[1/100,-1/200,0],[1/100,0,0],[1/100,1/200,0]],[[0,0,0],[0,-1/4,1/6],[0,-1/2,1/3],[0,0,0],[0,0,1/6],[0,0,1/3],[0,0,0],[0,1/4,1/6],[0,1/2,1/3],[0,0,0],[0,-101/800,101/1200],[0,-101/400,101/600],[0,0,0],[0,0,101/1200],[0,0,101/600],[0,0,0],[0,101/800,101/1200],[0,101/400,101/600],[0,0,0],[0,-1/400,1/600],[0,-1/200,1/300],[0,0,0],[0,0,1/600],[0,0,1/300],[0,0,0],[0,1/400,1/600],[0,1/200,1/300]],[[0,1,0],[0,1/2,0],[0,0,0],[0,1/2,0],[0,1/4,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[99/200,101/200,33/200],[99/200,301/800,33/400],[99/200,99/400,0],[99/400,301/800,33/200],[99/400,1/4,33/400],[99/400,99/800,0],[0,99/400,33/200],[0,99/800,33/400],[0,0,0],[99/100,1/100,33/100],[99/100,101/400,33/200],[99/100,99/200,0],[99/200,101/400,33/100],[99/200,1/4,33/200],[99/200,99/400,0],[0,99/200,33/100],[0,99/400,33/200],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,1/2,0],[0,1/4,0],[0,0,0],[0,1,0],[0,1/2,0],[0,0,0],[0,99/400,-33/200],[0,99/800,-33/400],[0,0,0],[99/400,301/800,-33/200],[99/400,1/4,-33/400],[99/400,99/800,0],[99/200,101/200,-33/200],[99/200,301/800,-33/400],[99/200,99/400,0],[0,99/200,-33/100],[0,99/400,-33/200],[0,0,0],[99/200,101/400,-33/100],[99/200,1/4,-33/200],[99/200,99/400,0],[99/100,1/100,-33/100],[99/100,101/400,-33/200],[99/100,99/200,0]],[[0,0,0],[0,1/2,0],[0,1,0],[0,0,0],[0,1/4,0],[0,1/2,0],[0,0,0],[0,0,0],[0,0,0],[-99/200,99/400,0],[-99/200,301/800,33/400],[-99/200,101/200,33/200],[-99/400,99/800,0],[-99/400,1/4,33/400],[-99/400,301/800,33/200],[0,0,0],[0,99/800,33/400],[0,99/400,33/200],[-99/100,99/200,0],[-99/100,101/400,33/200],[-99/100,1/100,33/100],[-99/200,99/400,0],[-99/200,1/4,33/200],[-99/200,101/400,33/100],[0,0,0],[0,99/400,33/200],[0,99/200,33/100]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,1/4,0],[0,1/2,0],[0,0,0],[0,1/2,0],[0,1,0],[0,0,0],[0,99/800,-33/400],[0,99/400,-33/200],[-99/400,99/800,0],[-99/400,1/4,-33/400],[-99/400,301/800,-33/200],[-99/200,99/400,0],[-99/200,301/800,-33/400],[-99/200,101/200,-33/200],[0,0,0],[0,99/400,-33/200],[0,99/200,-33/100],[-99/200,99/400,0],[-99/200,1/4,-33/200],[-99/200,101/400,-33/100],[-99/100,99/200,0],[-99/100,101/400,-33/200],[-99/100,1/100,-33/100]]],[[[0,1/2,1/3],[0,1/4,1/6],[0,0,0],[0,0,1/3],[0,0,1/6],[0,0,0],[0,-1/2,1/3],[0,-1/4,1/6],[0,0,0],[0,101/400,101/600],[0,101/800,101/1200],[0,0,0],[0,0,101/600],[0,0,101/1200],[0,0,0],[0,-101/400,101/600],[0,-101/800,101/1200],[0,0,0],[0,1/200,1/300],[0,1/400,1/600],[0,0,0],[0,0,1/300],[0,0,1/600],[0,0,0],[0,-1/200,1/300],[0,-1/400,1/600],[0,0,0]],[[1,1/2,0],[1,0,0],[1,-1/2,0],[1/2,1/4,0],[1/2,0,0],[1/2,-1/4,0],[0,0,0],[0,0,0],[0,0,0],[101/200,101/400,0],[101/200,0,0],[101/200,-101/400,0],[101/400,101/800,0],[101/400,0,0],[101/400,-101/800,0],[0,0,0],[0,0,0],[0,0,0],[1/100,1/200,0],[1/100,0,0],[1/100,-1/200,0],[1/200,1/400,0],[1/200,0,0],[1/200,-1/400,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[1/2,1/4,0],[1/2,0,0],[1/2,-1/4,0],[1,1/2,0],[1,0,0],[1,-1/2,0],[0,0,0],[0,0,0],[0,0,0],[101/400,101/800,0],[101/400,0,0],[101/400,-101/800,0],[101/200,101/400,0],[101/200,0,0],[101/200,-101/400,0],[0,0,0],[0,0,0],[0,0,0],[1/200,1/400,0],[1/200,0,0],[1/200,-1/400,0],[1/100,1/200,0],[1/100,0,0],[1/100,-1/200,0]],[[0,0,0],[0,1/4,1/6],[0,1/2,1/3],[0,0,0],[0,0,1/6],[0,0,1/3],[0,0,0],[0,-1/4,1/6],[0,-1/2,1/3],[0,0,0],[0,101/800,101/1200],[0,101/400,101/600],[0,0,0],[0,0,101/1200],[0,0,101/600],[0,0,0],[0,-101/800,101/1200],[0,-101/400,101/600],[0,0,0],[0,1/400,1/600],[0,1/200,1/300],[0,0,0],[0,0,1/600],[0,0,1/300],[0,0,0],[0,-1/400,1/600],[0,-1/200,1/300]],[[0,-1,0],[0,-1/2,0],[0,0,0],[0,-1/2,0],[0,-1/4,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[99/200,-101/200,33/200],[99/200,-301/800,33/400],[99/200,-99/400,0],[99/400,-301/800,33/200],[99/400,-1/4,33/400],[99/400,-99/800,0],[0,-99/400,33/200],[0,-99/800,33/400],[0,0,0],[99/100,-1/100,33/100],[99/100,-101/400,33/200],[99/100,-99/200,0],[99/200,-101/400,33/100],[99/200,-1/4,33/200],[99/200,-99/400,0],[0,-99/200,33/100],[0,-99/400,33/200],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,-1/2,0],[0,-1/4,0],[0,0,0],[0,-1,0],[0,-1/2,0],[0,0,0],[0,-99/400,-33/200],[0,-99/800,-33/400],[0,0,0],[99/400,-301/800,-33/200],[99/400,-1/4,-33/400],[99/400,-99/800,0],[99/200,-101/200,-33/200],[99/200,-301/800,-33/400],[99/200,-99/400,0],[0,-99/200,-33/100],[0,-99/400,-33/200],[0,0,0],[99/200,-101/400,-33/100],[99/200,-1/4,-33/200],[99/200,-99/400,0],[99/100,-1/100,-33/100],[99/100,-101/400,-33/200],[99/100,-99/200,0]],[[0,0,0],[0,-1/2,0],[0,-1,0],[0,0,0],[0,-1/4,0],[0,-1/2,0],[0,0,0],[0,0,0],[0,0,0],[-99/200,-99/400,0],[-99/200,-301/800,33/400],[-99/200,-101/200,33/200],[-99/400,-99/800,0],[-99/400,-1/4,33/400],[-99/400,-301/800,33/200],[0,0,0],[0,-99/800,33/400],[0,-99/400,33/200],[-99/100,-99/200,0],[-99/100,-101/400,33/200],[-99/100,-1/100,33/100],[-99/200,-99/400,0],[-99/200,-1/4,33/200],[-99/200,-101/400,33/100],[0,0,0],[0,-99/400,33/200],[0,-99/200,33/100]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,-1/4,0],[0,-1/2,0],[0,0,0],[0,-1/2,0],[0,-1,0],[0,0,0],[0,-99/800,-33/400],[0,-99/400,-33/200],[-99/400,-99/800,0],[-99/400,-1/4,-33/400],[-99/400,-301/800,-33/200],[-99/200,-99/400,0],[-99/200,-301/800,-33/400],[-99/200,-101/200,-33/200],[0,0,0],[0,-99/400,-33/200],[0,-99/200,-33/100],[-99/200,-99/400,0],[-99/200,-1/4,-33/200],[-99/200,-101/400,-33/100],[-99/100,-99/200,0],[-99/100,-101/400,-33/200],[-99/100,-1/100,-33/100]]],[[[0,1/2,-1/3],[0,1/4,-1/6],[0,0,0],[0,1/2,0],[0,1/4,0],[0,0,0],[0,1/2,1/3],[0,1/4,1/6],[0,0,0],[0,101/400,-101/600],[0,101/800,-101/1200],[0,0,0],[0,101/400,0],[0,101/800,0],[0,0,0],[0,101/400,101/600],[0,101/800,101/1200],[0,0,0],[0,1/200,-1/300],[0,1/400,-1/600],[0,0,0],[0,1/200,0],[0,1/400,0],[0,0,0],[0,1/200,1/300],[0,1/400,1/600],[0,0,0]],[[1,0,-1/3],[1,0,0],[1,0,1/3],[1/2,0,-1/6],[1/2,0,0],[1/2,0,1/6],[0,0,0],[0,0,0],[0,0,0],[101/200,0,-101/600],[101/200,0,0],[101/200,0,101/600],[101/400,0,-101/1200],[101/400,0,0],[101/400,0,101/1200],[0,0,0],[0,0,0],[0,0,0],[1/100,0,-1/300],[1/100,0,0],[1/100,0,1/300],[1/200,0,-1/600],[1/200,0,0],[1/200,0,1/600],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[1/2,0,-1/6],[1/2,0,0],[1/2,0,1/6],[1,0,-1/3],[1,0,0],[1,0,1/3],[0,0,0],[0,0,0],[0,0,0],[101/400,0,-101/1200],[101/400,0,0],[101/400,0,101/1200],[101/200,0,-101/600],[101/200,0,0],[101/200,0,101/600],[0,0,0],[0,0,0],[0,0,0],[1/200,0,-1/600],[1/200,0,0],[1/200,0,1/600],[1/100,0,-1/300],[1/100,0,0],[1/100,0,1/300]],[[0,0,0],[0,1/4,-1/6],[0,1/2,-1/3],[0,0,0],[0,1/4,0],[0,1/2,0],[0,0,0],[0,1/4,1/6],[0,1/2,1/3],[0,0,0],[0,101/800,-101/1200],[0,101/400,-101/600],[0,0,0],[0,101/800,0],[0,101/400,0],[0,0,0],[0,101/800,101/1200],[0,101/400,101/600],[0,0,0],[0,1/400,-1/600],[0,1/200,-1/300],[0,0,0],[0,1/400,0],[0,1/200,0],[0,0,0],[0,1/400,1/600],[0,1/200,1/300]],[[0,0,2/3],[0,0,1/3],[0,0,0],[0,0,1/3],[0,0,1/6],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[99/200,99/400,101/300],[99/200,99/800,301/1200],[99/200,0,33/200],[99/400,99/400,301/1200],[99/400,99/800,1/6],[99/400,0,33/400],[0,99/400,33/200],[0,99/800,33/400],[0,0,0],[99/100,99/200,1/150],[99/100,99/400,101/600],[99/100,0,33/100],[99/200,99/200,101/600],[99/200,99/400,1/6],[99/200,0,33/200],[0,99/200,33/100],[0,99/400,33/200],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,1/3],[0,0,1/6],[0,0,0],[0,0,2/3],[0,0,1/3],[0,0,0],[0,-99/400,33/200],[0,-99/800,33/400],[0,0,0],[99/400,-99/400,301/1200],[99/400,-99/800,1/6],[99/400,0,33/400],[99/200,-99/400,101/300],[99/200,-99/800,301/1200],[99/200,0,33/200],[0,-99/200,33/100],[0,-99/400,33/200],[0,0,0],[99/200,-99/200,101/600],[99/200,-99/400,1/6],[99/200,0,33/200],[99/100,-99/200,1/150],[99/100,-99/400,101/600],[99/100,0,33/100]],[[0,0,0],[0,0,1/3],[0,0,2/3],[0,0,0],[0,0,1/6],[0,0,1/3],[0,0,0],[0,0,0],[0,0,0],[-99/200,0,33/200],[-99/200,99/800,301/1200],[-99/200,99/400,101/300],[-99/400,0,33/400],[-99/400,99/800,1/6],[-99/400,99/400,301/1200],[0,0,0],[0,99/800,33/400],[0,99/400,33/200],[-99/100,0,33/100],[-99/100,99/400,101/600],[-99/100,99/200,1/150],[-99/200,0,33/200],[-99/200,99/400,1/6],[-99/200,99/200,101/600],[0,0,0],[0,99/400,33/200],[0,99/200,33/100]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,1/6],[0,0,1/3],[0,0,0],[0,0,1/3],[0,0,2/3],[0,0,0],[0,-99/800,33/400],[0,-99/400,33/200],[-99/400,0,33/400],[-99/400,-99/800,1/6],[-99/400,-99/400,301/1200],[-99/200,0,33/200],[-99/200,-99/800,301/1200],[-99/200,-99/400,101/300],[0,0,0],[0,-99/400,33/200],[0,-99/200,33/100],[-99/200,0,33/200],[-99/200,-99/400,1/6],[-99/200,-99/200,101/600],[-99/100,0,33/100],[-99/100,-99/400,101/600],[-99/100,-99/200,1/150]]],[[[0,1/2,1/3],[0,1/4,1/6],[0,0,0],[0,1/2,0],[0,1/4,0],[0,0,0],[0,1/2,-1/3],[0,1/4,-1/6],[0,0,0],[0,101/400,101/600],[0,101/800,101/1200],[0,0,0],[0,101/400,0],[0,101/800,0],[0,0,0],[0,101/400,-101/600],[0,101/800,-101/1200],[0,0,0],[0,1/200,1/300],[0,1/400,1/600],[0,0,0],[0,1/200,0],[0,1/400,0],[0,0,0],[0,1/200,-1/300],[0,1/400,-1/600],[0,0,0]],[[1,0,1/3],[1,0,0],[1,0,-1/3],[1/2,0,1/6],[1/2,0,0],[1/2,0,-1/6],[0,0,0],[0,0,0],[0,0,0],[101/200,0,101/600],[101/200,0,0],[101/200,0,-101/600],[101/400,0,101/1200],[101/400,0,0],[101/400,0,-101/1200],[0,0,0],[0,0,0],[0,0,0],[1/100,0,1/300],[1/100,0,0],[1/100,0,-1/300],[1/200,0,1/600],[1/200,0,0],[1/200,0,-1/600],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[1/2,0,1/6],[1/2,0,0],[1/2,0,-1/6],[1,0,1/3],[1,0,0],[1,0,-1/3],[0,0,0],[0,0,0],[0,0,0],[101/400,0,101/1200],[101/400,0,0],[101/400,0,-101/1200],[101/200,0,101/600],[101/200,0,0],[101/200,0,-101/600],[0,0,0],[0,0,0],[0,0,0],[1/200,0,1/600],[1/200,0,0],[1/200,0,-1/600],[1/100,0,1/300],[1/100,0,0],[1/100,0,-1/300]],[[0,0,0],[0,1/4,1/6],[0,1/2,1/3],[0,0,0],[0,1/4,0],[0,1/2,0],[0,0,0],[0,1/4,-1/6],[0,1/2,-1/3],[0,0,0],[0,101/800,101/1200],[0,101/400,101/600],[0,0,0],[0,101/800,0],[0,101/400,0],[0,0,0],[0,101/800,-101/1200],[0,101/400,-101/600],[0,0,0],[0,1/400,1/600],[0,1/200,1/300],[0,0,0],[0,1/400,0],[0,1/200,0],[0,0,0],[0,1/400,-1/600],[0,1/200,-1/300]],[[0,0,-2/3],[0,0,-1/3],[0,0,0],[0,0,-1/3],[0,0,-1/6],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[99/200,99/400,-101/300],[99/200,99/800,-301/1200],[99/200,0,-33/200],[99/400,99/400,-301/1200],[99/400,99/800,-1/6],[99/400,0,-33/400],[0,99/400,-33/200],[0,99/800,-33/400],[0,0,0],[99/100,99/200,-1/150],[99/100,99/400,-101/600],[99/100,0,-33/100],[99/200,99/200,-101/600],[99/200,99/400,-1/6],[99/200,0,-33/200],[0,99/200,-33/100],[0,99/400,-33/200],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,-1/3],[0,0,-1/6],[0,0,0],[0,0,-2/3],[0,0,-1/3],[0,0,0],[0,-99/400,-33/200],[0,-99/800,-33/400],[0,0,0],[99/400,-99/400,-301/1200],[99/400,-99/800,-1/6],[99/400,0,-33/400],[99/200,-99/400,-101/300],[99/200,-99/800,-301/1200],[99/200,0,-33/200],[0,-99/200,-33/100],[0,-99/400,-33/200],[0,0,0],[99/200,-99/200,-101/600],[99/200,-99/400,-1/6],[99/200,0,-33/200],[99/100,-99/200,-1/150],[99/100,-99/400,-101/600],[99/100,0,-33/100]],[[0,0,0],[0,0,-1/3],[0,0,-2/3],[0,0,0],[0,0,-1/6],[0,0,-1/3],[0,0,0],[0,0,0],[0,0,0],[-99/200,0,-33/200],[-99/200,99/800,-301/1200],[-99/200,99/400,-101/300],[-99/400,0,-33/400],[-99/400,99/800,-1/6],[-99/400,99/400,-301/1200],[0,0,0],[0,99/800,-33/400],[0,99/400,-33/200],[-99/100,0,-33/100],[-99/100,99/400,-101/600],[-99/100,99/200,-1/150],[-99/200,0,-33/200],[-99/200,99/400,-1/6],[-99/200,99/200,-101/600],[0,0,0],[0,99/400,-33/200],[0,99/200,-33/100]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,-1/6],[0,0,-1/3],[0,0,0],[0,0,-1/3],[0,0,-2/3],[0,0,0],[0,-99/800,-33/400],[0,-99/400,-33/200],[-99/400,0,-33/400],[-99/400,-99/800,-1/6],[-99/400,-99/400,-301/1200],[-99/200,0,-33/200],[-99/200,-99/800,-301/1200],[-99/200,-99/400,-101/300],[0,0,0],[0,-99/400,-33/200],[0,-99/200,-33/100],[-99/200,0,-33/200],[-99/200,-99/400,-1/6],[-99/200,-99/200,-101/600],[-99/100,0,-33/100],[-99/100,-99/400,-101/600],[-99/100,-99/200,-1/150]]]], N.float64)

D_oneform_edge0 = N.array([[[[-1/6,1,-1/2],[-1/6,2/3,-1/2],[-1/6,1/3,-1/2],[-1/6,1,0],[-1/6,2/3,0],[-1/6,1/3,0],[-1/6,1,1/2],[-1/6,2/3,1/2],[-1/6,1/3,1/2],[-1/6,1,-1/2],[-1/6,2/3,-1/2],[-1/6,1/3,-1/2],[-1/6,1,0],[-1/6,2/3,0],[-1/6,1/3,0],[-1/6,1,1/2],[-1/6,2/3,1/2],[-1/6,1/3,1/2],[-1/6,1,-1/2],[-1/6,2/3,-1/2],[-1/6,1/3,-1/2],[-1/6,1,0],[-1/6,2/3,0],[-1/6,1/3,0],[-1/6,1,1/2],[-1/6,2/3,1/2],[-1/6,1/3,1/2]],[[1/6,1/3,-3/2],[1/6,0,-3/2],[1/6,-1/3,-3/2],[1/6,1/3,-1],[1/6,0,-1],[1/6,-1/3,-1],[1/6,1/3,-1/2],[1/6,0,-1/2],[1/6,-1/3,-1/2],[1/6,1/3,-3/2],[1/6,0,-3/2],[1/6,-1/3,-3/2],[1/6,1/3,-1],[1/6,0,-1],[1/6,-1/3,-1],[1/6,1/3,-1/2],[1/6,0,-1/2],[1/6,-1/3,-1/2],[1/6,1/3,-3/2],[1/6,0,-3/2],[1/6,-1/3,-3/2],[1/6,1/3,-1],[1/6,0,-1],[1/6,-1/3,-1],[1/6,1/3,-1/2],[1/6,0,-1/2],[1/6,-1/3,-1/2]],[[-1/6,-1/3,-1/2],[-1/6,0,-1/2],[-1/6,1/3,-1/2],[-1/6,-1/3,-1],[-1/6,0,-1],[-1/6,1/3,-1],[-1/6,-1/3,-3/2],[-1/6,0,-3/2],[-1/6,1/3,-3/2],[-1/6,-1/3,-1/2],[-1/6,0,-1/2],[-1/6,1/3,-1/2],[-1/6,-1/3,-1],[-1/6,0,-1],[-1/6,1/3,-1],[-1/6,-1/3,-3/2],[-1/6,0,-3/2],[-1/6,1/3,-3/2],[-1/6,-1/3,-1/2],[-1/6,0,-1/2],[-1/6,1/3,-1/2],[-1/6,-1/3,-1],[-1/6,0,-1],[-1/6,1/3,-1],[-1/6,-1/3,-3/2],[-1/6,0,-3/2],[-1/6,1/3,-3/2]],[[1/6,1/3,1/2],[1/6,2/3,1/2],[1/6,1,1/2],[1/6,1/3,0],[1/6,2/3,0],[1/6,1,0],[1/6,1/3,-1/2],[1/6,2/3,-1/2],[1/6,1,-1/2],[1/6,1/3,1/2],[1/6,2/3,1/2],[1/6,1,1/2],[1/6,1/3,0],[1/6,2/3,0],[1/6,1,0],[1/6,1/3,-1/2],[1/6,2/3,-1/2],[1/6,1,-1/2],[1/6,1/3,1/2],[1/6,2/3,1/2],[1/6,1,1/2],[1/6,1/3,0],[1/6,2/3,0],[1/6,1,0],[1/6,1/3,-1/2],[1/6,2/3,-1/2],[1/6,1,-1/2]],[[0,-4/3,2],[0,-2/3,2],[0,0,2],[0,-4/3,1],[0,-2/3,1],[0,0,1],[0,-4/3,0],[0,-2/3,0],[0,0,0],[0,-4/3,2],[0,-2/3,2],[0,0,2],[0,-4/3,1],[0,-2/3,1],[0,0,1],[0,-4/3,0],[0,-2/3,0],[0,0,0],[0,-4/3,2],[0,-2/3,2],[0,0,2],[0,-4/3,1],[0,-2/3,1],[0,0,1],[0,-4/3,0],[0,-2/3,0],[0,0,0]],[[0,4/3,0],[0,2/3,0],[0,0,0],[0,4/3,1],[0,2/3,1],[0,0,1],[0,4/3,2],[0,2/3,2],[0,0,2],[0,4/3,0],[0,2/3,0],[0,0,0],[0,4/3,1],[0,2/3,1],[0,0,1],[0,4/3,2],[0,2/3,2],[0,0,2],[0,4/3,0],[0,2/3,0],[0,0,0],[0,4/3,1],[0,2/3,1],[0,0,1],[0,4/3,2],[0,2/3,2],[0,0,2]],[[0,0,-2],[0,-2/3,-2],[0,-4/3,-2],[0,0,-1],[0,-2/3,-1],[0,-4/3,-1],[0,0,0],[0,-2/3,0],[0,-4/3,0],[0,0,-2],[0,-2/3,-2],[0,-4/3,-2],[0,0,-1],[0,-2/3,-1],[0,-4/3,-1],[0,0,0],[0,-2/3,0],[0,-4/3,0],[0,0,-2],[0,-2/3,-2],[0,-4/3,-2],[0,0,-1],[0,-2/3,-1],[0,-4/3,-1],[0,0,0],[0,-2/3,0],[0,-4/3,0]],[[0,0,0],[0,2/3,0],[0,4/3,0],[0,0,-1],[0,2/3,-1],[0,4/3,-1],[0,0,-2],[0,2/3,-2],[0,4/3,-2],[0,0,0],[0,2/3,0],[0,4/3,0],[0,0,-1],[0,2/3,-1],[0,4/3,-1],[0,0,-2],[0,2/3,-2],[0,4/3,-2],[0,0,0],[0,2/3,0],[0,4/3,0],[0,0,-1],[0,2/3,-1],[0,4/3,-1],[0,0,-2],[0,2/3,-2],[0,4/3,-2]]],[[[-1/6,-1,1/2],[-1/6,-2/3,1/2],[-1/6,-1/3,1/2],[-1/6,-1,0],[-1/6,-2/3,0],[-1/6,-1/3,0],[-1/6,-1,-1/2],[-1/6,-2/3,-1/2],[-1/6,-1/3,-1/2],[-1/6,-1,1/2],[-1/6,-2/3,1/2],[-1/6,-1/3,1/2],[-1/6,-1,0],[-1/6,-2/3,0],[-1/6,-1/3,0],[-1/6,-1,-1/2],[-1/6,-2/3,-1/2],[-1/6,-1/3,-1/2],[-1/6,-1,1/2],[-1/6,-2/3,1/2],[-1/6,-1/3,1/2],[-1/6,-1,0],[-1/6,-2/3,0],[-1/6,-1/3,0],[-1/6,-1,-1/2],[-1/6,-2/3,-1/2],[-1/6,-1/3,-1/2]],[[1/6,-1/3,3/2],[1/6,0,3/2],[1/6,1/3,3/2],[1/6,-1/3,1],[1/6,0,1],[1/6,1/3,1],[1/6,-1/3,1/2],[1/6,0,1/2],[1/6,1/3,1/2],[1/6,-1/3,3/2],[1/6,0,3/2],[1/6,1/3,3/2],[1/6,-1/3,1],[1/6,0,1],[1/6,1/3,1],[1/6,-1/3,1/2],[1/6,0,1/2],[1/6,1/3,1/2],[1/6,-1/3,3/2],[1/6,0,3/2],[1/6,1/3,3/2],[1/6,-1/3,1],[1/6,0,1],[1/6,1/3,1],[1/6,-1/3,1/2],[1/6,0,1/2],[1/6,1/3,1/2]],[[-1/6,1/3,1/2],[-1/6,0,1/2],[-1/6,-1/3,1/2],[-1/6,1/3,1],[-1/6,0,1],[-1/6,-1/3,1],[-1/6,1/3,3/2],[-1/6,0,3/2],[-1/6,-1/3,3/2],[-1/6,1/3,1/2],[-1/6,0,1/2],[-1/6,-1/3,1/2],[-1/6,1/3,1],[-1/6,0,1],[-1/6,-1/3,1],[-1/6,1/3,3/2],[-1/6,0,3/2],[-1/6,-1/3,3/2],[-1/6,1/3,1/2],[-1/6,0,1/2],[-1/6,-1/3,1/2],[-1/6,1/3,1],[-1/6,0,1],[-1/6,-1/3,1],[-1/6,1/3,3/2],[-1/6,0,3/2],[-1/6,-1/3,3/2]],[[1/6,-1/3,-1/2],[1/6,-2/3,-1/2],[1/6,-1,-1/2],[1/6,-1/3,0],[1/6,-2/3,0],[1/6,-1,0],[1/6,-1/3,1/2],[1/6,-2/3,1/2],[1/6,-1,1/2],[1/6,-1/3,-1/2],[1/6,-2/3,-1/2],[1/6,-1,-1/2],[1/6,-1/3,0],[1/6,-2/3,0],[1/6,-1,0],[1/6,-1/3,1/2],[1/6,-2/3,1/2],[1/6,-1,1/2],[1/6,-1/3,-1/2],[1/6,-2/3,-1/2],[1/6,-1,-1/2],[1/6,-1/3,0],[1/6,-2/3,0],[1/6,-1,0],[1/6,-1/3,1/2],[1/6,-2/3,1/2],[1/6,-1,1/2]],[[0,4/3,-2],[0,2/3,-2],[0,0,-2],[0,4/3,-1],[0,2/3,-1],[0,0,-1],[0,4/3,0],[0,2/3,0],[0,0,0],[0,4/3,-2],[0,2/3,-2],[0,0,-2],[0,4/3,-1],[0,2/3,-1],[0,0,-1],[0,4/3,0],[0,2/3,0],[0,0,0],[0,4/3,-2],[0,2/3,-2],[0,0,-2],[0,4/3,-1],[0,2/3,-1],[0,0,-1],[0,4/3,0],[0,2/3,0],[0,0,0]],[[0,-4/3,0],[0,-2/3,0],[0,0,0],[0,-4/3,-1],[0,-2/3,-1],[0,0,-1],[0,-4/3,-2],[0,-2/3,-2],[0,0,-2],[0,-4/3,0],[0,-2/3,0],[0,0,0],[0,-4/3,-1],[0,-2/3,-1],[0,0,-1],[0,-4/3,-2],[0,-2/3,-2],[0,0,-2],[0,-4/3,0],[0,-2/3,0],[0,0,0],[0,-4/3,-1],[0,-2/3,-1],[0,0,-1],[0,-4/3,-2],[0,-2/3,-2],[0,0,-2]],[[0,0,2],[0,2/3,2],[0,4/3,2],[0,0,1],[0,2/3,1],[0,4/3,1],[0,0,0],[0,2/3,0],[0,4/3,0],[0,0,2],[0,2/3,2],[0,4/3,2],[0,0,1],[0,2/3,1],[0,4/3,1],[0,0,0],[0,2/3,0],[0,4/3,0],[0,0,2],[0,2/3,2],[0,4/3,2],[0,0,1],[0,2/3,1],[0,4/3,1],[0,0,0],[0,2/3,0],[0,4/3,0]],[[0,0,0],[0,-2/3,0],[0,-4/3,0],[0,0,1],[0,-2/3,1],[0,-4/3,1],[0,0,2],[0,-2/3,2],[0,-4/3,2],[0,0,0],[0,-2/3,0],[0,-4/3,0],[0,0,1],[0,-2/3,1],[0,-4/3,1],[0,0,2],[0,-2/3,2],[0,-4/3,2],[0,0,0],[0,-2/3,0],[0,-4/3,0],[0,0,1],[0,-2/3,1],[0,-4/3,1],[0,0,2],[0,-2/3,2],[0,-4/3,2]]],[[[-1/2,1/3,1/2],[-1/3,1/3,1/2],[-1/6,1/3,1/2],[-1/2,1/3,0],[-1/3,1/3,0],[-1/6,1/3,0],[-1/2,1/3,-1/2],[-1/3,1/3,-1/2],[-1/6,1/3,-1/2],[-1/2,1/3,1/2],[-1/3,1/3,1/2],[-1/6,1/3,1/2],[-1/2,1/3,0],[-1/3,1/3,0],[-1/6,1/3,0],[-1/2,1/3,-1/2],[-1/3,1/3,-1/2],[-1/6,1/3,-1/2],[-1/2,1/3,1/2],[-1/3,1/3,1/2],[-1/6,1/3,1/2],[-1/2,1/3,0],[-1/3,1/3,0],[-1/6,1/3,0],[-1/2,1/3,-1/2],[-1/3,1/3,-1/2],[-1/6,1/3,-1/2]],[[-1/6,-1/3,3/2],[0,-1/3,3/2],[1/6,-1/3,3/2],[-1/6,-1/3,1],[0,-1/3,1],[1/6,-1/3,1],[-1/6,-1/3,1/2],[0,-1/3,1/2],[1/6,-1/3,1/2],[-1/6,-1/3,3/2],[0,-1/3,3/2],[1/6,-1/3,3/2],[-1/6,-1/3,1],[0,-1/3,1],[1/6,-1/3,1],[-1/6,-1/3,1/2],[0,-1/3,1/2],[1/6,-1/3,1/2],[-1/6,-1/3,3/2],[0,-1/3,3/2],[1/6,-1/3,3/2],[-1/6,-1/3,1],[0,-1/3,1],[1/6,-1/3,1],[-1/6,-1/3,1/2],[0,-1/3,1/2],[1/6,-1/3,1/2]],[[1/6,1/3,1/2],[0,1/3,1/2],[-1/6,1/3,1/2],[1/6,1/3,1],[0,1/3,1],[-1/6,1/3,1],[1/6,1/3,3/2],[0,1/3,3/2],[-1/6,1/3,3/2],[1/6,1/3,1/2],[0,1/3,1/2],[-1/6,1/3,1/2],[1/6,1/3,1],[0,1/3,1],[-1/6,1/3,1],[1/6,1/3,3/2],[0,1/3,3/2],[-1/6,1/3,3/2],[1/6,1/3,1/2],[0,1/3,1/2],[-1/6,1/3,1/2],[1/6,1/3,1],[0,1/3,1],[-1/6,1/3,1],[1/6,1/3,3/2],[0,1/3,3/2],[-1/6,1/3,3/2]],[[-1/6,-1/3,-1/2],[-1/3,-1/3,-1/2],[-1/2,-1/3,-1/2],[-1/6,-1/3,0],[-1/3,-1/3,0],[-1/2,-1/3,0],[-1/6,-1/3,1/2],[-1/3,-1/3,1/2],[-1/2,-1/3,1/2],[-1/6,-1/3,-1/2],[-1/3,-1/3,-1/2],[-1/2,-1/3,-1/2],[-1/6,-1/3,0],[-1/3,-1/3,0],[-1/2,-1/3,0],[-1/6,-1/3,1/2],[-1/3,-1/3,1/2],[-1/2,-1/3,1/2],[-1/6,-1/3,-1/2],[-1/3,-1/3,-1/2],[-1/2,-1/3,-1/2],[-1/6,-1/3,0],[-1/3,-1/3,0],[-1/2,-1/3,0],[-1/6,-1/3,1/2],[-1/3,-1/3,1/2],[-1/2,-1/3,1/2]],[[2/3,0,-2],[1/3,0,-2],[0,0,-2],[2/3,0,-1],[1/3,0,-1],[0,0,-1],[2/3,0,0],[1/3,0,0],[0,0,0],[2/3,0,-2],[1/3,0,-2],[0,0,-2],[2/3,0,-1],[1/3,0,-1],[0,0,-1],[2/3,0,0],[1/3,0,0],[0,0,0],[2/3,0,-2],[1/3,0,-2],[0,0,-2],[2/3,0,-1],[1/3,0,-1],[0,0,-1],[2/3,0,0],[1/3,0,0],[0,0,0]],[[-2/3,0,0],[-1/3,0,0],[0,0,0],[-2/3,0,-1],[-1/3,0,-1],[0,0,-1],[-2/3,0,-2],[-1/3,0,-2],[0,0,-2],[-2/3,0,0],[-1/3,0,0],[0,0,0],[-2/3,0,-1],[-1/3,0,-1],[0,0,-1],[-2/3,0,-2],[-1/3,0,-2],[0,0,-2],[-2/3,0,0],[-1/3,0,0],[0,0,0],[-2/3,0,-1],[-1/3,0,-1],[0,0,-1],[-2/3,0,-2],[-1/3,0,-2],[0,0,-2]],[[0,0,2],[1/3,0,2],[2/3,0,2],[0,0,1],[1/3,0,1],[2/3,0,1],[0,0,0],[1/3,0,0],[2/3,0,0],[0,0,2],[1/3,0,2],[2/3,0,2],[0,0,1],[1/3,0,1],[2/3,0,1],[0,0,0],[1/3,0,0],[2/3,0,0],[0,0,2],[1/3,0,2],[2/3,0,2],[0,0,1],[1/3,0,1],[2/3,0,1],[0,0,0],[1/3,0,0],[2/3,0,0]],[[0,0,0],[-1/3,0,0],[-2/3,0,0],[0,0,1],[-1/3,0,1],[-2/3,0,1],[0,0,2],[-1/3,0,2],[-2/3,0,2],[0,0,0],[-1/3,0,0],[-2/3,0,0],[0,0,1],[-1/3,0,1],[-2/3,0,1],[0,0,2],[-1/3,0,2],[-2/3,0,2],[0,0,0],[-1/3,0,0],[-2/3,0,0],[0,0,1],[-1/3,0,1],[-2/3,0,1],[0,0,2],[-1/3,0,2],[-2/3,0,2]]],[[[1/2,1/3,-1/2],[1/3,1/3,-1/2],[1/6,1/3,-1/2],[1/2,1/3,0],[1/3,1/3,0],[1/6,1/3,0],[1/2,1/3,1/2],[1/3,1/3,1/2],[1/6,1/3,1/2],[1/2,1/3,-1/2],[1/3,1/3,-1/2],[1/6,1/3,-1/2],[1/2,1/3,0],[1/3,1/3,0],[1/6,1/3,0],[1/2,1/3,1/2],[1/3,1/3,1/2],[1/6,1/3,1/2],[1/2,1/3,-1/2],[1/3,1/3,-1/2],[1/6,1/3,-1/2],[1/2,1/3,0],[1/3,1/3,0],[1/6,1/3,0],[1/2,1/3,1/2],[1/3,1/3,1/2],[1/6,1/3,1/2]],[[1/6,-1/3,-3/2],[0,-1/3,-3/2],[-1/6,-1/3,-3/2],[1/6,-1/3,-1],[0,-1/3,-1],[-1/6,-1/3,-1],[1/6,-1/3,-1/2],[0,-1/3,-1/2],[-1/6,-1/3,-1/2],[1/6,-1/3,-3/2],[0,-1/3,-3/2],[-1/6,-1/3,-3/2],[1/6,-1/3,-1],[0,-1/3,-1],[-1/6,-1/3,-1],[1/6,-1/3,-1/2],[0,-1/3,-1/2],[-1/6,-1/3,-1/2],[1/6,-1/3,-3/2],[0,-1/3,-3/2],[-1/6,-1/3,-3/2],[1/6,-1/3,-1],[0,-1/3,-1],[-1/6,-1/3,-1],[1/6,-1/3,-1/2],[0,-1/3,-1/2],[-1/6,-1/3,-1/2]],[[-1/6,1/3,-1/2],[0,1/3,-1/2],[1/6,1/3,-1/2],[-1/6,1/3,-1],[0,1/3,-1],[1/6,1/3,-1],[-1/6,1/3,-3/2],[0,1/3,-3/2],[1/6,1/3,-3/2],[-1/6,1/3,-1/2],[0,1/3,-1/2],[1/6,1/3,-1/2],[-1/6,1/3,-1],[0,1/3,-1],[1/6,1/3,-1],[-1/6,1/3,-3/2],[0,1/3,-3/2],[1/6,1/3,-3/2],[-1/6,1/3,-1/2],[0,1/3,-1/2],[1/6,1/3,-1/2],[-1/6,1/3,-1],[0,1/3,-1],[1/6,1/3,-1],[-1/6,1/3,-3/2],[0,1/3,-3/2],[1/6,1/3,-3/2]],[[1/6,-1/3,1/2],[1/3,-1/3,1/2],[1/2,-1/3,1/2],[1/6,-1/3,0],[1/3,-1/3,0],[1/2,-1/3,0],[1/6,-1/3,-1/2],[1/3,-1/3,-1/2],[1/2,-1/3,-1/2],[1/6,-1/3,1/2],[1/3,-1/3,1/2],[1/2,-1/3,1/2],[1/6,-1/3,0],[1/3,-1/3,0],[1/2,-1/3,0],[1/6,-1/3,-1/2],[1/3,-1/3,-1/2],[1/2,-1/3,-1/2],[1/6,-1/3,1/2],[1/3,-1/3,1/2],[1/2,-1/3,1/2],[1/6,-1/3,0],[1/3,-1/3,0],[1/2,-1/3,0],[1/6,-1/3,-1/2],[1/3,-1/3,-1/2],[1/2,-1/3,-1/2]],[[-2/3,0,2],[-1/3,0,2],[0,0,2],[-2/3,0,1],[-1/3,0,1],[0,0,1],[-2/3,0,0],[-1/3,0,0],[0,0,0],[-2/3,0,2],[-1/3,0,2],[0,0,2],[-2/3,0,1],[-1/3,0,1],[0,0,1],[-2/3,0,0],[-1/3,0,0],[0,0,0],[-2/3,0,2],[-1/3,0,2],[0,0,2],[-2/3,0,1],[-1/3,0,1],[0,0,1],[-2/3,0,0],[-1/3,0,0],[0,0,0]],[[2/3,0,0],[1/3,0,0],[0,0,0],[2/3,0,1],[1/3,0,1],[0,0,1],[2/3,0,2],[1/3,0,2],[0,0,2],[2/3,0,0],[1/3,0,0],[0,0,0],[2/3,0,1],[1/3,0,1],[0,0,1],[2/3,0,2],[1/3,0,2],[0,0,2],[2/3,0,0],[1/3,0,0],[0,0,0],[2/3,0,1],[1/3,0,1],[0,0,1],[2/3,0,2],[1/3,0,2],[0,0,2]],[[0,0,-2],[-1/3,0,-2],[-2/3,0,-2],[0,0,-1],[-1/3,0,-1],[-2/3,0,-1],[0,0,0],[-1/3,0,0],[-2/3,0,0],[0,0,-2],[-1/3,0,-2],[-2/3,0,-2],[0,0,-1],[-1/3,0,-1],[-2/3,0,-1],[0,0,0],[-1/3,0,0],[-2/3,0,0],[0,0,-2],[-1/3,0,-2],[-2/3,0,-2],[0,0,-1],[-1/3,0,-1],[-2/3,0,-1],[0,0,0],[-1/3,0,0],[-2/3,0,0]],[[0,0,0],[1/3,0,0],[2/3,0,0],[0,0,-1],[1/3,0,-1],[2/3,0,-1],[0,0,-2],[1/3,0,-2],[2/3,0,-2],[0,0,0],[1/3,0,0],[2/3,0,0],[0,0,-1],[1/3,0,-1],[2/3,0,-1],[0,0,-2],[1/3,0,-2],[2/3,0,-2],[0,0,0],[1/3,0,0],[2/3,0,0],[0,0,-1],[1/3,0,-1],[2/3,0,-1],[0,0,-2],[1/3,0,-2],[2/3,0,-2]]],[[[1/2,-1/3,-1/2],[1/3,-1/3,-1/2],[1/6,-1/3,-1/2],[1/2,0,-1/2],[1/3,0,-1/2],[1/6,0,-1/2],[1/2,1/3,-1/2],[1/3,1/3,-1/2],[1/6,1/3,-1/2],[1/2,-1/3,-1/2],[1/3,-1/3,-1/2],[1/6,-1/3,-1/2],[1/2,0,-1/2],[1/3,0,-1/2],[1/6,0,-1/2],[1/2,1/3,-1/2],[1/3,1/3,-1/2],[1/6,1/3,-1/2],[1/2,-1/3,-1/2],[1/3,-1/3,-1/2],[1/6,-1/3,-1/2],[1/2,0,-1/2],[1/3,0,-1/2],[1/6,0,-1/2],[1/2,1/3,-1/2],[1/3,1/3,-1/2],[1/6,1/3,-1/2]],[[1/6,-1,1/2],[0,-1,1/2],[-1/6,-1,1/2],[1/6,-2/3,1/2],[0,-2/3,1/2],[-1/6,-2/3,1/2],[1/6,-1/3,1/2],[0,-1/3,1/2],[-1/6,-1/3,1/2],[1/6,-1,1/2],[0,-1,1/2],[-1/6,-1,1/2],[1/6,-2/3,1/2],[0,-2/3,1/2],[-1/6,-2/3,1/2],[1/6,-1/3,1/2],[0,-1/3,1/2],[-1/6,-1/3,1/2],[1/6,-1,1/2],[0,-1,1/2],[-1/6,-1,1/2],[1/6,-2/3,1/2],[0,-2/3,1/2],[-1/6,-2/3,1/2],[1/6,-1/3,1/2],[0,-1/3,1/2],[-1/6,-1/3,1/2]],[[-1/6,-1/3,-1/2],[0,-1/3,-1/2],[1/6,-1/3,-1/2],[-1/6,-2/3,-1/2],[0,-2/3,-1/2],[1/6,-2/3,-1/2],[-1/6,-1,-1/2],[0,-1,-1/2],[1/6,-1,-1/2],[-1/6,-1/3,-1/2],[0,-1/3,-1/2],[1/6,-1/3,-1/2],[-1/6,-2/3,-1/2],[0,-2/3,-1/2],[1/6,-2/3,-1/2],[-1/6,-1,-1/2],[0,-1,-1/2],[1/6,-1,-1/2],[-1/6,-1/3,-1/2],[0,-1/3,-1/2],[1/6,-1/3,-1/2],[-1/6,-2/3,-1/2],[0,-2/3,-1/2],[1/6,-2/3,-1/2],[-1/6,-1,-1/2],[0,-1,-1/2],[1/6,-1,-1/2]],[[1/6,1/3,1/2],[1/3,1/3,1/2],[1/2,1/3,1/2],[1/6,0,1/2],[1/3,0,1/2],[1/2,0,1/2],[1/6,-1/3,1/2],[1/3,-1/3,1/2],[1/2,-1/3,1/2],[1/6,1/3,1/2],[1/3,1/3,1/2],[1/2,1/3,1/2],[1/6,0,1/2],[1/3,0,1/2],[1/2,0,1/2],[1/6,-1/3,1/2],[1/3,-1/3,1/2],[1/2,-1/3,1/2],[1/6,1/3,1/2],[1/3,1/3,1/2],[1/2,1/3,1/2],[1/6,0,1/2],[1/3,0,1/2],[1/2,0,1/2],[1/6,-1/3,1/2],[1/3,-1/3,1/2],[1/2,-1/3,1/2]],[[-2/3,4/3,0],[-1/3,4/3,0],[0,4/3,0],[-2/3,2/3,0],[-1/3,2/3,0],[0,2/3,0],[-2/3,0,0],[-1/3,0,0],[0,0,0],[-2/3,4/3,0],[-1/3,4/3,0],[0,4/3,0],[-2/3,2/3,0],[-1/3,2/3,0],[0,2/3,0],[-2/3,0,0],[-1/3,0,0],[0,0,0],[-2/3,4/3,0],[-1/3,4/3,0],[0,4/3,0],[-2/3,2/3,0],[-1/3,2/3,0],[0,2/3,0],[-2/3,0,0],[-1/3,0,0],[0,0,0]],[[2/3,0,0],[1/3,0,0],[0,0,0],[2/3,2/3,0],[1/3,2/3,0],[0,2/3,0],[2/3,4/3,0],[1/3,4/3,0],[0,4/3,0],[2/3,0,0],[1/3,0,0],[0,0,0],[2/3,2/3,0],[1/3,2/3,0],[0,2/3,0],[2/3,4/3,0],[1/3,4/3,0],[0,4/3,0],[2/3,0,0],[1/3,0,0],[0,0,0],[2/3,2/3,0],[1/3,2/3,0],[0,2/3,0],[2/3,4/3,0],[1/3,4/3,0],[0,4/3,0]],[[0,-4/3,0],[-1/3,-4/3,0],[-2/3,-4/3,0],[0,-2/3,0],[-1/3,-2/3,0],[-2/3,-2/3,0],[0,0,0],[-1/3,0,0],[-2/3,0,0],[0,-4/3,0],[-1/3,-4/3,0],[-2/3,-4/3,0],[0,-2/3,0],[-1/3,-2/3,0],[-2/3,-2/3,0],[0,0,0],[-1/3,0,0],[-2/3,0,0],[0,-4/3,0],[-1/3,-4/3,0],[-2/3,-4/3,0],[0,-2/3,0],[-1/3,-2/3,0],[-2/3,-2/3,0],[0,0,0],[-1/3,0,0],[-2/3,0,0]],[[0,0,0],[1/3,0,0],[2/3,0,0],[0,-2/3,0],[1/3,-2/3,0],[2/3,-2/3,0],[0,-4/3,0],[1/3,-4/3,0],[2/3,-4/3,0],[0,0,0],[1/3,0,0],[2/3,0,0],[0,-2/3,0],[1/3,-2/3,0],[2/3,-2/3,0],[0,-4/3,0],[1/3,-4/3,0],[2/3,-4/3,0],[0,0,0],[1/3,0,0],[2/3,0,0],[0,-2/3,0],[1/3,-2/3,0],[2/3,-2/3,0],[0,-4/3,0],[1/3,-4/3,0],[2/3,-4/3,0]]],[[[-1/2,1/3,-1/2],[-1/3,1/3,-1/2],[-1/6,1/3,-1/2],[-1/2,0,-1/2],[-1/3,0,-1/2],[-1/6,0,-1/2],[-1/2,-1/3,-1/2],[-1/3,-1/3,-1/2],[-1/6,-1/3,-1/2],[-1/2,1/3,-1/2],[-1/3,1/3,-1/2],[-1/6,1/3,-1/2],[-1/2,0,-1/2],[-1/3,0,-1/2],[-1/6,0,-1/2],[-1/2,-1/3,-1/2],[-1/3,-1/3,-1/2],[-1/6,-1/3,-1/2],[-1/2,1/3,-1/2],[-1/3,1/3,-1/2],[-1/6,1/3,-1/2],[-1/2,0,-1/2],[-1/3,0,-1/2],[-1/6,0,-1/2],[-1/2,-1/3,-1/2],[-1/3,-1/3,-1/2],[-1/6,-1/3,-1/2]],[[-1/6,1,1/2],[0,1,1/2],[1/6,1,1/2],[-1/6,2/3,1/2],[0,2/3,1/2],[1/6,2/3,1/2],[-1/6,1/3,1/2],[0,1/3,1/2],[1/6,1/3,1/2],[-1/6,1,1/2],[0,1,1/2],[1/6,1,1/2],[-1/6,2/3,1/2],[0,2/3,1/2],[1/6,2/3,1/2],[-1/6,1/3,1/2],[0,1/3,1/2],[1/6,1/3,1/2],[-1/6,1,1/2],[0,1,1/2],[1/6,1,1/2],[-1/6,2/3,1/2],[0,2/3,1/2],[1/6,2/3,1/2],[-1/6,1/3,1/2],[0,1/3,1/2],[1/6,1/3,1/2]],[[1/6,1/3,-1/2],[0,1/3,-1/2],[-1/6,1/3,-1/2],[1/6,2/3,-1/2],[0,2/3,-1/2],[-1/6,2/3,-1/2],[1/6,1,-1/2],[0,1,-1/2],[-1/6,1,-1/2],[1/6,1/3,-1/2],[0,1/3,-1/2],[-1/6,1/3,-1/2],[1/6,2/3,-1/2],[0,2/3,-1/2],[-1/6,2/3,-1/2],[1/6,1,-1/2],[0,1,-1/2],[-1/6,1,-1/2],[1/6,1/3,-1/2],[0,1/3,-1/2],[-1/6,1/3,-1/2],[1/6,2/3,-1/2],[0,2/3,-1/2],[-1/6,2/3,-1/2],[1/6,1,-1/2],[0,1,-1/2],[-1/6,1,-1/2]],[[-1/6,-1/3,1/2],[-1/3,-1/3,1/2],[-1/2,-1/3,1/2],[-1/6,0,1/2],[-1/3,0,1/2],[-1/2,0,1/2],[-1/6,1/3,1/2],[-1/3,1/3,1/2],[-1/2,1/3,1/2],[-1/6,-1/3,1/2],[-1/3,-1/3,1/2],[-1/2,-1/3,1/2],[-1/6,0,1/2],[-1/3,0,1/2],[-1/2,0,1/2],[-1/6,1/3,1/2],[-1/3,1/3,1/2],[-1/2,1/3,1/2],[-1/6,-1/3,1/2],[-1/3,-1/3,1/2],[-1/2,-1/3,1/2],[-1/6,0,1/2],[-1/3,0,1/2],[-1/2,0,1/2],[-1/6,1/3,1/2],[-1/3,1/3,1/2],[-1/2,1/3,1/2]],[[2/3,-4/3,0],[1/3,-4/3,0],[0,-4/3,0],[2/3,-2/3,0],[1/3,-2/3,0],[0,-2/3,0],[2/3,0,0],[1/3,0,0],[0,0,0],[2/3,-4/3,0],[1/3,-4/3,0],[0,-4/3,0],[2/3,-2/3,0],[1/3,-2/3,0],[0,-2/3,0],[2/3,0,0],[1/3,0,0],[0,0,0],[2/3,-4/3,0],[1/3,-4/3,0],[0,-4/3,0],[2/3,-2/3,0],[1/3,-2/3,0],[0,-2/3,0],[2/3,0,0],[1/3,0,0],[0,0,0]],[[-2/3,0,0],[-1/3,0,0],[0,0,0],[-2/3,-2/3,0],[-1/3,-2/3,0],[0,-2/3,0],[-2/3,-4/3,0],[-1/3,-4/3,0],[0,-4/3,0],[-2/3,0,0],[-1/3,0,0],[0,0,0],[-2/3,-2/3,0],[-1/3,-2/3,0],[0,-2/3,0],[-2/3,-4/3,0],[-1/3,-4/3,0],[0,-4/3,0],[-2/3,0,0],[-1/3,0,0],[0,0,0],[-2/3,-2/3,0],[-1/3,-2/3,0],[0,-2/3,0],[-2/3,-4/3,0],[-1/3,-4/3,0],[0,-4/3,0]],[[0,4/3,0],[1/3,4/3,0],[2/3,4/3,0],[0,2/3,0],[1/3,2/3,0],[2/3,2/3,0],[0,0,0],[1/3,0,0],[2/3,0,0],[0,4/3,0],[1/3,4/3,0],[2/3,4/3,0],[0,2/3,0],[1/3,2/3,0],[2/3,2/3,0],[0,0,0],[1/3,0,0],[2/3,0,0],[0,4/3,0],[1/3,4/3,0],[2/3,4/3,0],[0,2/3,0],[1/3,2/3,0],[2/3,2/3,0],[0,0,0],[1/3,0,0],[2/3,0,0]],[[0,0,0],[-1/3,0,0],[-2/3,0,0],[0,2/3,0],[-1/3,2/3,0],[-2/3,2/3,0],[0,4/3,0],[-1/3,4/3,0],[-2/3,4/3,0],[0,0,0],[-1/3,0,0],[-2/3,0,0],[0,2/3,0],[-1/3,2/3,0],[-2/3,2/3,0],[0,4/3,0],[-1/3,4/3,0],[-2/3,4/3,0],[0,0,0],[-1/3,0,0],[-2/3,0,0],[0,2/3,0],[-1/3,2/3,0],[-2/3,2/3,0],[0,4/3,0],[-1/3,4/3,0],[-2/3,4/3,0]]]], N.float64)
