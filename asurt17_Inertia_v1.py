# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 13:32:37 2017

@author: khale
"""

from base import grf, vector, point, ep2dcm, rot2ep
from bodies_inertia import rigid, principle_inertia, thin_rod, circular_cylinder
from constraints import spherical, revolute, universal, \
cylindrical, rotational_drive, absolute_locating,translational
from force_elements import tsda, force, tire_force
from pre_processor import topology_writer
import pandas as pd
import numpy as np
from solvers import kds, check_jacobian_dense, reactions, dds, state_space_creator
from newton_raphson import nr_kds
import matplotlib.pyplot as plt

###############################################################################
# Defining System HardPoints.
###############################################################################
origin = point('origin', [0,0,0])
bcp    = point('bcp',    [6.63, -280, 574])
bc_pr  = point('bc_pr',  [6.63, -347, 595])
bc_sh  = point('bc_sh',  [6.63, -262, 631])
cp     = point('cp',     [0.0,  -600, 0.0])
lcaf   = point('lcaf',   [-234, -213, 165])
lcao   = point('lcao',   [-7,   -483, 174])
lcar   = point('lcar',   [170,  -262, 192])
uca_pr = point('uca_pr', [6.63, -412, 360])
ch_sh  = point('ch_sh',  [6.63, -25 , 631])
tro    = point('tro',    [-121, -456, 122])
tri    = point('tri',    [-121, -227, 132])
ucaf   = point('ucaf',   [-234, -220, 343])
ucao   = point('ucao',   [7,    -480, 334])
ucar   = point('ucar',   [170,  -270, 315])
wc     = point('wc',     [0.0,  -600, 254])
d_m    = point.mid_point(ch_sh,bc_sh,'d_m')

###############################################################################
# Defining System Bodies and their inertia properties.
###############################################################################
I=np.eye(3)
cm=vector([0,0,0])
dcm=I
J=I
mass=1
ground  = rigid('ground',mass,J,cm,dcm,typ='mount')
#Chassis
########
ch_cm=vector([0,0,320])
ch_dcm=I
ch_J=I
ch_mass  = 80*1e3
chassis  = rigid('chassis',ch_mass,ch_J,ch_cm,ch_dcm)
########################################################################
uca_cm=vector([-32.44,-389.51,331.31])
Jcm=np.array([[ 1297540.37,-897778.79 ,-254075.80],
              [-897778.79 , 3490235.80, 66317.52],
              [-254075.80 , 66317.52  , 4742845.78]])
dcm,J=principle_inertia(Jcm)
uca_mass = 400
uca      = rigid('uca',uca_mass,J,uca_cm,dcm)
########################################################################
lca_cm=vector([-36.65,-394.37,172.47])
Jcm=np.array([[1571314.37,-839834.01,207103.82],
	               [-839834.01,3706559.61,39301.75],
	               [207103.82,39301.75,5235433.3]])
dcm,J=principle_inertia(Jcm)
lca_mass = 423
lca      = rigid('lca',lca_mass,J,lca_cm,dcm)
########################################################################
cm=vector([-5.21,-530.71,239.46])
Jcm=np.array([[6809559.26,-70112.53, 723753.00],
              [-70112.53, 6663047.19,-111547.75],
              [723753.00,-111547.75,1658347.31]])
dcm,J=principle_inertia(Jcm)
mass = 1329.83 
upright  = rigid('upright',mass,J,cm,dcm)
########################################################################
cm=vector([-0.02,-306.13,589.79])
Jcm=np.array([[254875.61,-52.57, 77.36],
              [-52.57, 122537.57,16178.36],
              [77.36,16178.36,193317.90]])
dcm,J=principle_inertia(Jcm)
mass = 188.68  
rocker   = rigid('rocker',mass,J,cm,dcm)
########################################################################
cm=vector([0,-391.40,472.12])
Jcm=np.array([[1950892.69, -64.01      , 16.95    ],
              [-64.01    ,  1814714.56 , 496026.64],
              [16.95     ,  496026.64  ,143774.46 ]])
dcm,J=principle_inertia(Jcm)
mass = 243.02  
push   = rigid('push',mass,J,cm,dcm)
########################################################################
tie_g = thin_rod(tri,tro,250)
cm    = tie_g.cm
dcm   = tie_g.C
J     = tie_g.J
mass  = 250 
tie   = rigid('tie',mass,J,cm,dcm)
########################################################################
d1_g  = circular_cylinder(bc_sh,d_m,15)
cm    = d1_g.cm
dcm   = d1_g.C
J     = d1_g.J
mass  = d1_g.mass 
d1    = rigid('d1',mass,J,cm,dcm)
########################################################################
d2_g  = circular_cylinder(ch_sh,d_m,35,28)
cm    = d2_g.cm
dcm   = d2_g.C
J     = d2_g.J
mass  = d2_g.mass 
d2    = rigid('d2',mass,J,cm,dcm)
########################################################################
cm     = vector([0,-613.93,254.09])
Jcm=np.array([[343952295.71, 29954.40     , -40790.37    ],
              [29954.40    , 535366217.28 , -28626.24    ],
              [-40790.37   ,-28626.24    , 343951084.62  ]])
dcm,J  = principle_inertia(Jcm)
mass   = 13377.41  
wheel  = rigid('wheel',mass,J,cm,dcm)
###############################################################################

# Defining system forces
seat1=bc_sh+(50*(ch_sh-bc_sh).unit)
seat2=bc_sh+(170*(ch_sh-bc_sh).unit)
spring_damper=tsda('f1',seat1,d1,seat2,d2,k=80*1e6,lf=140,c=-8*1e6)
nl=(160)*9.81*1e6
force_vector=np.array([[nl*1],[nl*1],[0]])
vf=force('vertical_force',force_vector,wheel,vector([0,-600,0]))
tf=tire_force('tvf',wheel,300*1e6,-1*1e6,254,vector([0,600,0]))


###############################################################################
# Defining System Joints.
###############################################################################
uca_rev     = revolute(ucaf,uca,chassis,ucaf-ucar)
#ucaf_sph    = spherical(ucaf,uca,chassis)
#ucar_sph    = spherical(ucar,uca,chassis)
lca_rev     = revolute(lcaf,lca,chassis,lcaf-lcar)
#lcaf_sph    = spherical(lcaf,lca,chassis)
#lcar_sph    = spherical(lcar,lca,chassis)
bcp_rev     = revolute(bcp,rocker,chassis,vector.normal(bc_pr,bc_sh,bcp,grf))
wheel_hub   = revolute(wc,wheel,upright,vector([0,-1,0]))

pr_uca_sph  = spherical(uca_pr,uca,push)
tie_up_sph  = spherical(tro,tie,upright)
ucao_sph    = spherical(ucao,uca,upright)
lcao_sph    = spherical(lcao,lca,upright)


damper      = cylindrical(d_m,d1,d2,bc_sh-ch_sh)

ax1         = uca_pr-bc_pr
pr_bc       = universal(bc_pr,rocker,push,ax1,bc_pr-bcp)
ax2         = bc_sh-ch_sh
sh_bc       = universal(bc_sh,rocker,d1,ax2,bc_sh-bcp)
d2_ch_uni   = universal(ch_sh,d2,chassis,ax2,-ax2)
ax3         = tro-tri
tie_ch      = universal(tri,chassis,tie,vector([0,1,0]),ax3)

wheel_drive = rotational_drive(wheel_hub)

vertical_travel=absolute_locating(wheel,'z')
wheel_lock =absolute_locating(wheel,'z')
ch_ground   = translational(origin,ground,chassis,vector([0,0,1])) 
###############################################################################




###############################################################################
# Collecting System Data in lists.
###############################################################################

points      =[bcp,bc_sh,bc_pr,ch_sh,ucaf,ucar,ucao,lcaf,lcar,lcao,tri,tro,uca_pr,cp,wc,d_m]

bodies_list =[ground,chassis,uca,lca,upright,push,tie,d1,d2,rocker,wheel]

joints_list =[uca_rev,lca_rev,bcp_rev,ucao_sph,lcao_sph,pr_uca_sph,
              tie_up_sph,d2_ch_uni,sh_bc,tie_ch,pr_bc,damper,wheel_hub,ch_ground]

actuators = [vertical_travel,wheel_drive,wheel_lock]
forces    = [spring_damper,tf]

js=pd.Series(joints_list,index=[i.name for i in joints_list])
bs=pd.Series(bodies_list,index=[i.name for i in bodies_list])
ac=pd.Series(actuators  ,index=[i.name for i in actuators])
fs=pd.Series(forces     ,index=[i.name for i in forces])

##############################################################################
# Generating system file.
##############################################################################
#topology_writer(bs,js,ac,fs,'dyn_1s')
#qn=pd.concat([i.dic for i in bodies_list])
#
##from dyn_1s import cq, eq
##vertical_travel.pos=322
##wheel_drive.pos=0
##wheel_lock.pos=254
##dd=nr_kds(eq,cq,qn,bs,js,ac,debug=True)
#
#time=np.linspace(0,2*np.pi,50)
#wheel_drive.pos_array=np.zeros((len(time),))
#wheel_lock.pos_array=254+np.zeros((len(time),))
#vertical_travel.pos_array=320+30*np.sin(2*time)
#d=kds(bs,js,ac,'dyn_1s',time)
#
#coord3='wheel.y'
#plt.figure(coord3)
#plt.plot(time,d[0][coord3][1:])
#plt.plot(d[0]['chassis.z'][1:]-254,d[0][coord3][1:])
#plt.plot(time,d[1][coord3][1:])
#plt.grid()
#plt.show()
#
#system_forces=reactions(d[0],d[1],d[2],bs,js,ac,fs,'dyn_1s')
#lamdas=system_forces[4]
#joints_reactions=1e-6*system_forces[5][1:]
#joints_reactions.plot(y='ch_sh_uni_Fy')
#joints_reactions.plot(y='wc_rev_Fz')




##############################################################################
# Dynamic Analysis.
##############################################################################
q0   = pd.concat([i.dic    for i in bodies_list])
qd0  = pd.concat([i.qd0()  for i in bodies_list])
qdd0 = pd.concat([i.qdd0() for i in bodies_list])

vertical_travel=absolute_locating(wheel,'z')
wheel_drive.pos=0
vertical_travel.pos=254
actuators = [wheel_drive]
ac=pd.Series(actuators,index=[i.name for i in actuators])

#def ssm(t,y,Cq_rec,Qt,lagr):
#        v=y[len(y)/2:]
#        dydt=[v, (1/644)*(Qt[51]-(Cq_rec.T.dot(lagr))[51])]
#        return dydt

    
topology_writer(bs,js,ac,fs,'dyn_2')

dynamic1=dds(q0,qd0,bs,js,ac,fs,'dyn_2',0.25,0.25/100)
pos,vel,acc,react=dynamic1
xaxis=np.arange(0,0.25+0.25/100,0.25/100)

plt.figure('WheelCenter Position')
plt.plot(xaxis,pos['wheel.z'],label=r'$wc_{z}$')
plt.legend()
plt.xlabel('Time (sec)')
plt.ylabel('Displacement (mm)')
plt.grid()
plt.show()

plt.figure('Half-track Change')
plt.plot(xaxis,pos['wheel.y'],label=r'$wc_{y}$')
plt.legend()
plt.xlabel('Time (sec)')
plt.ylabel('Displacement (mm)')
plt.grid()
plt.show()

plt.figure('Chassis CG Vertical Position')
plt.plot(xaxis,pos['chassis.z'],label=r'$chassis_{z}$')
plt.legend()
plt.xlabel('Time (sec)')
plt.ylabel('Displacement (mm)')
plt.grid()
plt.show()

plt.figure('WheelHub Verical Reaction Force')
plt.plot(xaxis,-1e-6*react['wc_rev_Fz'],label=r'$wc_{Fz}$')
plt.legend()
plt.xlabel('Time (sec)')
plt.ylabel('Force (N)')
plt.grid()
plt.show()

plt.figure('UCA Mount Reaction')
plt.plot(xaxis,1e-6*react['ucaf_rev_Fx'],label=r'$F_{x}$')
plt.plot(xaxis,1e-6*react['ucaf_rev_Fy'],label=r'$F_{y}$')
#plt.plot(xaxis[1:],1e-6*react['ucaf_rev_Fz'],label=r'$F_{z}$')
plt.legend()
plt.xlabel('Time (sec)')
plt.ylabel('Force (N)')
plt.grid()
plt.show()

plt.figure('Shock Mount Reaction')
#plt.plot(xaxis,1e-6*react['ch_sh_uni_Fx'],label=r'$F_{x}$')
plt.plot(xaxis,-1e-6*react['ch_sh_uni_Fy'],label=r'$F_{y}$')
#plt.plot(xaxis,1e-6*react['ch_sh_uni_Fz'],label=r'$F_{z}$')
plt.legend()
plt.xlabel('Time (sec)')
plt.ylabel('Force (N)')
plt.grid()
plt.show()
#plt.figure('Damper Force')
#plt.plot(xaxis,1e-6*springdamper['forceD'][1:])
#plt.grid()
#plt.show()
#plt.figure('spring deff')
#plt.plot(xaxis,springdamper['deff'][1:])
#plt.grid()
#plt.show()
#plt.figure('vel')
#plt.plot(xaxis,springdamper['vel'][1:])
#plt.grid()
#plt.show()






