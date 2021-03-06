# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 11:04:56 2017

@author: khale
"""

from base import vector, ep2dcm, B, vec2skew, G
import numpy as np

class tsda(object):
    def __init__(self,name,Pi,bodyi,Qj,bodyj,k=0,lf=0,c=0,h=0):
        self.name=name
        self.bodyi=bodyi
        self.bodyj=bodyj
        self.u_i=bodyi.dcm.T.dot(Pi-bodyi.R)
        self.u_j=bodyj.dcm.T.dot(Qj-bodyj.R)
        self.k=k
        self.c=c
        self.h=h
        self.lf=lf
        
    def equation(self,q,qdot):
        qi=q[self.bodyi.dic.index]
        qj=q[self.bodyj.dic.index]
        qi_dot=qdot[self.bodyi.dic.index]
        qj_dot=qdot[self.bodyj.dic.index]

        Ri=vector(qi[0:3]).a
        Rj=vector(qj[0:3]).a
        betai=qi[3:]
        betaj=qj[3:]
        Ai=ep2dcm(betai)
        Aj=ep2dcm(betaj)
        
        rij=Ri+Ai.dot(self.u_i)-Rj-Aj.dot(self.u_j)
        l=np.linalg.norm(rij)
        defflection=max([0,self.lf-l])
        nij=rij/l
        
        self.defflection=defflection
        

        Ri_dot=qi_dot[0:3].values.reshape((3,1))
        Rj_dot=qj_dot[0:3].values.reshape((3,1))
        betai_dot=qi_dot[3:]
        betaj_dot=qj_dot[3:]
        
        bid=betai_dot.values.reshape((4,1))
        bjd=betaj_dot.values.reshape((4,1))
        
        Bip=B(betai,self.u_i)
        Bjp=B(betaj,self.u_j)
        
        rij_dot=Ri_dot+Bip.dot(bid)-Rj_dot-Bjp.dot(bjd)
        velocity=nij.T.dot(rij_dot)
        self.velocity=velocity
        
        self.springforce=self.k*defflection
        self.damperforce=self.c*velocity
        
        force=self.k*(defflection)+self.c*velocity+self.h
        
        fi=float(force)*nij
        ni=2*G(betai).T.dot(vec2skew(self.u_i).dot(Ai.T.dot(fi)))
        Qi=np.bmat([[fi],[ni]])
        
        fj=-float(force)*nij
        nj=2*G(betaj).T.dot(vec2skew(self.u_j).dot(Aj.T.dot(fj)))
        Qj=np.bmat([[fj],[nj]])
        
        return Qi,Qj
    
    
class force(object):
    def __init__(self,name,value,bodyi,Pi):
        self.name=name
        self.bodyi=bodyi
        self.u_i=bodyi.dcm.T.dot(Pi-bodyi.R)
        self.F=value
        
    def equation(self,q,v):
        qi=q[self.bodyi.dic.index]
        betai=qi[3:]
        Ai=ep2dcm(betai)
        F=self.F
        M=2*G(betai).T.dot(vec2skew(self.u_i).dot(Ai.T.dot(F)))
        Qi=np.bmat([[F],[M]])
        return Qi

class moment(object):
    def __init__(self,name,value,bodyi,Pi):
        self.name=name
        self.bodyi=bodyi
        self.u_i=bodyi.dcm.T.dot(Pi-bodyi.R)
        self.M=value
        
    def equation(self,q):
        qi=q[self.bodyi.dic.index]
        betai=qi[3:]
        Z=np.zeros((3,1))
        M=2*G(betai).T.dot(self.M)
        Qi=np.bmat([[Z],[M]])
        return Qi        
        
class tire_force(object):
    def __init__(self,name,bodyi,k,c,r,Pi):
        self.name=name
        self.bodyi=bodyi
        self.u_i=bodyi.dcm.T.dot(Pi-bodyi.R)
        self.k=k
        self.c=c
        self.r=r
        
    def equation(self,q,qdot,road_z):
        qi=q[self.bodyi.dic.index]
        betai=qi[3:]
        Ai=ep2dcm(betai)
        rw=qi[self.bodyi.name+'.z']-road_z
        rzdot=qdot[self.bodyi.name+'.z']
        self.tire_deff=self.r-rw
        x=max([0,self.r-rw])
        
        
        F=np.array([[0,0,self.k*x+self.c*rzdot]]).T
        Z=np.zeros((4,1))
        M=2*G(betai).T.dot(vec2skew(self.u_i).dot(Ai.T.dot(F)))
        Qi=np.bmat([[F],[Z]])
        return Qi
        

class tire_force2(object):
    def __init__(self,name,bodyi,k,c,r,Pi):
        self.name=name
        self.bodyi=bodyi
        self.u_i=bodyi.dcm.T.dot(Pi-bodyi.R)
        self.k=k
        self.c=c
        self.r=r
        
    def equation(self,q,qdot):
        qi=q[self.bodyi.dic.index]
        betai=qi[3:]
        Ai=ep2dcm(betai)
        rw=qi[self.bodyi.name+'.z']
        rzdot=qdot[self.bodyi.name+'.z']
        x=max([0,self.r-rw])
        
        
        F=np.array([[0,0,self.k*x+self.c*rzdot]]).T
        Z=np.zeros((4,1))
        M=2*G(betai).T.dot(vec2skew(self.u_i).dot(Ai.T.dot(F)))
        Qi=np.bmat([[F],[Z]])
        return Qi
    



        
