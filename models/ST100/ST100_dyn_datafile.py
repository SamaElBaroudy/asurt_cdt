import numpy as np 
import pandas as pd 
from scipy import sparse 


jac_df=pd.DataFrame([21 *[None]],columns=['ground', 'chassis', 'uca', 'lca', 'upright', 'tie', 'd1', 'd2', 'wheel', 'uca_r', 'lca_r', 'upright_r', 'tie_r', 'd1_r', 'd2_r', 'wheel_r', 'l1', 'l2', 'l3', 'l4', 'l5'],index=['ucaf_rev', 'lcaf_rev', 'ucao_sph', 'lcao_sph', 'tro_sph', 'ch_sh_uni', 'sh_lca_uni', 'tri_uni', 'd_m_cyl', 'wc_rev', 'ucaf_r_rev', 'lcaf_r_rev', 'ucao_r_sph', 'lcao_r_sph', 'tro_r_sph', 'ch_sh_r_uni', 'sh_lca_r_uni', 'tri_r_uni', 'd_m_r_cyl', 'wc_r_rev', 'origin_br', 'mount_1_rev', 'mount_2_rev', 'C1_uni', 'E_uni', 'F_uni', 'C2_sph', 'EF_cyl', 'ground', 'chassis', 'uca', 'lca', 'upright', 'tie', 'd1', 'd2', 'wheel', 'uca_r', 'lca_r', 'upright_r', 'tie_r', 'd1_r', 'd2_r', 'wheel_r', 'l1', 'l2', 'l3', 'l4', 'l5', 'wc_rev_actuator', 'wc_r_rev_actuator', 'l5.y_actuator'])
def cq(q,bodies,joints,actuators): 
	 jac_df.loc['ucaf_rev','uca']=joints['ucaf_rev'].jacobian_i(q)
	 jac_df.loc['ucaf_rev','chassis']=joints['ucaf_rev'].jacobian_j(q)
	 jac_df.loc['lcaf_rev','lca']=joints['lcaf_rev'].jacobian_i(q)
	 jac_df.loc['lcaf_rev','chassis']=joints['lcaf_rev'].jacobian_j(q)
	 jac_df.loc['ucao_sph','uca']=joints['ucao_sph'].jacobian_i(q)
	 jac_df.loc['ucao_sph','upright']=joints['ucao_sph'].jacobian_j(q)
	 jac_df.loc['lcao_sph','lca']=joints['lcao_sph'].jacobian_i(q)
	 jac_df.loc['lcao_sph','upright']=joints['lcao_sph'].jacobian_j(q)
	 jac_df.loc['tro_sph','tie']=joints['tro_sph'].jacobian_i(q)
	 jac_df.loc['tro_sph','upright']=joints['tro_sph'].jacobian_j(q)
	 jac_df.loc['ch_sh_uni','d2']=joints['ch_sh_uni'].jacobian_i(q)
	 jac_df.loc['ch_sh_uni','chassis']=joints['ch_sh_uni'].jacobian_j(q)
	 jac_df.loc['sh_lca_uni','lca']=joints['sh_lca_uni'].jacobian_i(q)
	 jac_df.loc['sh_lca_uni','d1']=joints['sh_lca_uni'].jacobian_j(q)
	 jac_df.loc['tri_uni','l1']=joints['tri_uni'].jacobian_i(q)
	 jac_df.loc['tri_uni','tie']=joints['tri_uni'].jacobian_j(q)
	 jac_df.loc['d_m_cyl','d1']=joints['d_m_cyl'].jacobian_i(q)
	 jac_df.loc['d_m_cyl','d2']=joints['d_m_cyl'].jacobian_j(q)
	 jac_df.loc['wc_rev','wheel']=joints['wc_rev'].jacobian_i(q)
	 jac_df.loc['wc_rev','upright']=joints['wc_rev'].jacobian_j(q)
	 jac_df.loc['ucaf_r_rev','uca_r']=joints['ucaf_r_rev'].jacobian_i(q)
	 jac_df.loc['ucaf_r_rev','chassis']=joints['ucaf_r_rev'].jacobian_j(q)
	 jac_df.loc['lcaf_r_rev','lca_r']=joints['lcaf_r_rev'].jacobian_i(q)
	 jac_df.loc['lcaf_r_rev','chassis']=joints['lcaf_r_rev'].jacobian_j(q)
	 jac_df.loc['ucao_r_sph','uca_r']=joints['ucao_r_sph'].jacobian_i(q)
	 jac_df.loc['ucao_r_sph','upright_r']=joints['ucao_r_sph'].jacobian_j(q)
	 jac_df.loc['lcao_r_sph','lca_r']=joints['lcao_r_sph'].jacobian_i(q)
	 jac_df.loc['lcao_r_sph','upright_r']=joints['lcao_r_sph'].jacobian_j(q)
	 jac_df.loc['tro_r_sph','tie_r']=joints['tro_r_sph'].jacobian_i(q)
	 jac_df.loc['tro_r_sph','upright_r']=joints['tro_r_sph'].jacobian_j(q)
	 jac_df.loc['ch_sh_r_uni','d2_r']=joints['ch_sh_r_uni'].jacobian_i(q)
	 jac_df.loc['ch_sh_r_uni','chassis']=joints['ch_sh_r_uni'].jacobian_j(q)
	 jac_df.loc['sh_lca_r_uni','lca_r']=joints['sh_lca_r_uni'].jacobian_i(q)
	 jac_df.loc['sh_lca_r_uni','d1_r']=joints['sh_lca_r_uni'].jacobian_j(q)
	 jac_df.loc['tri_r_uni','l3']=joints['tri_r_uni'].jacobian_i(q)
	 jac_df.loc['tri_r_uni','tie_r']=joints['tri_r_uni'].jacobian_j(q)
	 jac_df.loc['d_m_r_cyl','d1_r']=joints['d_m_r_cyl'].jacobian_i(q)
	 jac_df.loc['d_m_r_cyl','d2_r']=joints['d_m_r_cyl'].jacobian_j(q)
	 jac_df.loc['wc_r_rev','wheel_r']=joints['wc_r_rev'].jacobian_i(q)
	 jac_df.loc['wc_r_rev','upright_r']=joints['wc_r_rev'].jacobian_j(q)
	 jac_df.loc['origin_br','chassis']=joints['origin_br'].jacobian_i(q)
	 jac_df.loc['origin_br','ground']=joints['origin_br'].jacobian_j(q)
	 jac_df.loc['mount_1_rev','l1']=joints['mount_1_rev'].jacobian_i(q)
	 jac_df.loc['mount_1_rev','chassis']=joints['mount_1_rev'].jacobian_j(q)
	 jac_df.loc['mount_2_rev','l3']=joints['mount_2_rev'].jacobian_i(q)
	 jac_df.loc['mount_2_rev','chassis']=joints['mount_2_rev'].jacobian_j(q)
	 jac_df.loc['C1_uni','l1']=joints['C1_uni'].jacobian_i(q)
	 jac_df.loc['C1_uni','l2']=joints['C1_uni'].jacobian_j(q)
	 jac_df.loc['E_uni','l4']=joints['E_uni'].jacobian_i(q)
	 jac_df.loc['E_uni','chassis']=joints['E_uni'].jacobian_j(q)
	 jac_df.loc['F_uni','l5']=joints['F_uni'].jacobian_i(q)
	 jac_df.loc['F_uni','l3']=joints['F_uni'].jacobian_j(q)
	 jac_df.loc['C2_sph','l2']=joints['C2_sph'].jacobian_i(q)
	 jac_df.loc['C2_sph','l3']=joints['C2_sph'].jacobian_j(q)
	 jac_df.loc['EF_cyl','l4']=joints['EF_cyl'].jacobian_i(q)
	 jac_df.loc['EF_cyl','l5']=joints['EF_cyl'].jacobian_j(q)
	 jac_df.loc['ground','ground']=bodies['ground'].mount_jacobian(q)
	 jac_df.loc['chassis','chassis']=bodies['chassis'].unity_jacobian(q)
	 jac_df.loc['uca','uca']=bodies['uca'].unity_jacobian(q)
	 jac_df.loc['lca','lca']=bodies['lca'].unity_jacobian(q)
	 jac_df.loc['upright','upright']=bodies['upright'].unity_jacobian(q)
	 jac_df.loc['tie','tie']=bodies['tie'].unity_jacobian(q)
	 jac_df.loc['d1','d1']=bodies['d1'].unity_jacobian(q)
	 jac_df.loc['d2','d2']=bodies['d2'].unity_jacobian(q)
	 jac_df.loc['wheel','wheel']=bodies['wheel'].unity_jacobian(q)
	 jac_df.loc['uca_r','uca_r']=bodies['uca_r'].unity_jacobian(q)
	 jac_df.loc['lca_r','lca_r']=bodies['lca_r'].unity_jacobian(q)
	 jac_df.loc['upright_r','upright_r']=bodies['upright_r'].unity_jacobian(q)
	 jac_df.loc['tie_r','tie_r']=bodies['tie_r'].unity_jacobian(q)
	 jac_df.loc['d1_r','d1_r']=bodies['d1_r'].unity_jacobian(q)
	 jac_df.loc['d2_r','d2_r']=bodies['d2_r'].unity_jacobian(q)
	 jac_df.loc['wheel_r','wheel_r']=bodies['wheel_r'].unity_jacobian(q)
	 jac_df.loc['l1','l1']=bodies['l1'].unity_jacobian(q)
	 jac_df.loc['l2','l2']=bodies['l2'].unity_jacobian(q)
	 jac_df.loc['l3','l3']=bodies['l3'].unity_jacobian(q)
	 jac_df.loc['l4','l4']=bodies['l4'].unity_jacobian(q)
	 jac_df.loc['l5','l5']=bodies['l5'].unity_jacobian(q)
	 jac_df.loc['wc_rev_actuator','wheel']=actuators['wc_rev_actuator'].jacobian_i(q)
	 jac_df.loc['wc_rev_actuator','upright']=actuators['wc_rev_actuator'].jacobian_j(q)
	 jac_df.loc['wc_r_rev_actuator','wheel_r']=actuators['wc_r_rev_actuator'].jacobian_i(q)
	 jac_df.loc['wc_r_rev_actuator','upright_r']=actuators['wc_r_rev_actuator'].jacobian_j(q)
	 jac_df.loc['l5.y_actuator','l5']=actuators['l5.y_actuator'].jacobian()
	 jac=sparse.bmat(jac_df,format='csc') 
	 return jac 


eq_s=pd.Series([52 *[None]],index=['ucaf_rev', 'lcaf_rev', 'ucao_sph', 'lcao_sph', 'tro_sph', 'ch_sh_uni', 'sh_lca_uni', 'tri_uni', 'd_m_cyl', 'wc_rev', 'ucaf_r_rev', 'lcaf_r_rev', 'ucao_r_sph', 'lcao_r_sph', 'tro_r_sph', 'ch_sh_r_uni', 'sh_lca_r_uni', 'tri_r_uni', 'd_m_r_cyl', 'wc_r_rev', 'origin_br', 'mount_1_rev', 'mount_2_rev', 'C1_uni', 'E_uni', 'F_uni', 'C2_sph', 'EF_cyl', 'ground', 'chassis', 'uca', 'lca', 'upright', 'tie', 'd1', 'd2', 'wheel', 'uca_r', 'lca_r', 'upright_r', 'tie_r', 'd1_r', 'd2_r', 'wheel_r', 'l1', 'l2', 'l3', 'l4', 'l5', 'wc_rev_actuator', 'wc_r_rev_actuator', 'l5.y_actuator'])
def eq(q,bodies,joints,actuators): 
	 eq_s['ucaf_rev']=joints['ucaf_rev'].equations(q)
	 eq_s['lcaf_rev']=joints['lcaf_rev'].equations(q)
	 eq_s['ucao_sph']=joints['ucao_sph'].equations(q)
	 eq_s['lcao_sph']=joints['lcao_sph'].equations(q)
	 eq_s['tro_sph']=joints['tro_sph'].equations(q)
	 eq_s['ch_sh_uni']=joints['ch_sh_uni'].equations(q)
	 eq_s['sh_lca_uni']=joints['sh_lca_uni'].equations(q)
	 eq_s['tri_uni']=joints['tri_uni'].equations(q)
	 eq_s['d_m_cyl']=joints['d_m_cyl'].equations(q)
	 eq_s['wc_rev']=joints['wc_rev'].equations(q)
	 eq_s['ucaf_r_rev']=joints['ucaf_r_rev'].equations(q)
	 eq_s['lcaf_r_rev']=joints['lcaf_r_rev'].equations(q)
	 eq_s['ucao_r_sph']=joints['ucao_r_sph'].equations(q)
	 eq_s['lcao_r_sph']=joints['lcao_r_sph'].equations(q)
	 eq_s['tro_r_sph']=joints['tro_r_sph'].equations(q)
	 eq_s['ch_sh_r_uni']=joints['ch_sh_r_uni'].equations(q)
	 eq_s['sh_lca_r_uni']=joints['sh_lca_r_uni'].equations(q)
	 eq_s['tri_r_uni']=joints['tri_r_uni'].equations(q)
	 eq_s['d_m_r_cyl']=joints['d_m_r_cyl'].equations(q)
	 eq_s['wc_r_rev']=joints['wc_r_rev'].equations(q)
	 eq_s['origin_br']=joints['origin_br'].equations(q)
	 eq_s['mount_1_rev']=joints['mount_1_rev'].equations(q)
	 eq_s['mount_2_rev']=joints['mount_2_rev'].equations(q)
	 eq_s['C1_uni']=joints['C1_uni'].equations(q)
	 eq_s['E_uni']=joints['E_uni'].equations(q)
	 eq_s['F_uni']=joints['F_uni'].equations(q)
	 eq_s['C2_sph']=joints['C2_sph'].equations(q)
	 eq_s['EF_cyl']=joints['EF_cyl'].equations(q)
	 eq_s['ground']=bodies['ground'].mount_equation(q)
	 eq_s['chassis']=bodies['chassis'].unity_equation(q)
	 eq_s['uca']=bodies['uca'].unity_equation(q)
	 eq_s['lca']=bodies['lca'].unity_equation(q)
	 eq_s['upright']=bodies['upright'].unity_equation(q)
	 eq_s['tie']=bodies['tie'].unity_equation(q)
	 eq_s['d1']=bodies['d1'].unity_equation(q)
	 eq_s['d2']=bodies['d2'].unity_equation(q)
	 eq_s['wheel']=bodies['wheel'].unity_equation(q)
	 eq_s['uca_r']=bodies['uca_r'].unity_equation(q)
	 eq_s['lca_r']=bodies['lca_r'].unity_equation(q)
	 eq_s['upright_r']=bodies['upright_r'].unity_equation(q)
	 eq_s['tie_r']=bodies['tie_r'].unity_equation(q)
	 eq_s['d1_r']=bodies['d1_r'].unity_equation(q)
	 eq_s['d2_r']=bodies['d2_r'].unity_equation(q)
	 eq_s['wheel_r']=bodies['wheel_r'].unity_equation(q)
	 eq_s['l1']=bodies['l1'].unity_equation(q)
	 eq_s['l2']=bodies['l2'].unity_equation(q)
	 eq_s['l3']=bodies['l3'].unity_equation(q)
	 eq_s['l4']=bodies['l4'].unity_equation(q)
	 eq_s['l5']=bodies['l5'].unity_equation(q)
	 eq_s['wc_rev_actuator']=actuators['wc_rev_actuator'].equations(q)
	 eq_s['wc_r_rev_actuator']=actuators['wc_r_rev_actuator'].equations(q)
	 eq_s['l5.y_actuator']=actuators['l5.y_actuator'].equations(q)
	 system=sparse.bmat(eq_s.values.reshape((52,1)),format='csc') 
	 return system.A.reshape((143,)) 


vel_rhs_s=pd.Series([52 *[None]],index=['ucaf_rev', 'lcaf_rev', 'ucao_sph', 'lcao_sph', 'tro_sph', 'ch_sh_uni', 'sh_lca_uni', 'tri_uni', 'd_m_cyl', 'wc_rev', 'ucaf_r_rev', 'lcaf_r_rev', 'ucao_r_sph', 'lcao_r_sph', 'tro_r_sph', 'ch_sh_r_uni', 'sh_lca_r_uni', 'tri_r_uni', 'd_m_r_cyl', 'wc_r_rev', 'origin_br', 'mount_1_rev', 'mount_2_rev', 'C1_uni', 'E_uni', 'F_uni', 'C2_sph', 'EF_cyl', 'ground', 'chassis', 'uca', 'lca', 'upright', 'tie', 'd1', 'd2', 'wheel', 'uca_r', 'lca_r', 'upright_r', 'tie_r', 'd1_r', 'd2_r', 'wheel_r', 'l1', 'l2', 'l3', 'l4', 'l5', 'wc_rev_actuator', 'wc_r_rev_actuator', 'l5.y_actuator'])
def vel_rhs(actuators): 
	 vrhs=np.zeros((140,1))
	 vrhs=np.concatenate([vrhs,actuators['wc_rev_actuator'].vel_rhs()]) 
	 vrhs=np.concatenate([vrhs,actuators['wc_r_rev_actuator'].vel_rhs()]) 
	 vrhs=np.concatenate([vrhs,actuators['l5.y_actuator'].vel_rhs()]) 
	 return vrhs 
acc_rhs_s=pd.Series([52 *[None]],index=['ucaf_rev', 'lcaf_rev', 'ucao_sph', 'lcao_sph', 'tro_sph', 'ch_sh_uni', 'sh_lca_uni', 'tri_uni', 'd_m_cyl', 'wc_rev', 'ucaf_r_rev', 'lcaf_r_rev', 'ucao_r_sph', 'lcao_r_sph', 'tro_r_sph', 'ch_sh_r_uni', 'sh_lca_r_uni', 'tri_r_uni', 'd_m_r_cyl', 'wc_r_rev', 'origin_br', 'mount_1_rev', 'mount_2_rev', 'C1_uni', 'E_uni', 'F_uni', 'C2_sph', 'EF_cyl', 'ground', 'chassis', 'uca', 'lca', 'upright', 'tie', 'd1', 'd2', 'wheel', 'uca_r', 'lca_r', 'upright_r', 'tie_r', 'd1_r', 'd2_r', 'wheel_r', 'l1', 'l2', 'l3', 'l4', 'l5', 'wc_rev_actuator', 'wc_r_rev_actuator', 'l5.y_actuator'])
def acc_rhs(q,qdot,bodies,joints,actuators): 
	 acc_rhs_s['ucaf_rev']=joints['ucaf_rev'].acc_rhs(q,qdot)
	 acc_rhs_s['lcaf_rev']=joints['lcaf_rev'].acc_rhs(q,qdot)
	 acc_rhs_s['ucao_sph']=joints['ucao_sph'].acc_rhs(q,qdot)
	 acc_rhs_s['lcao_sph']=joints['lcao_sph'].acc_rhs(q,qdot)
	 acc_rhs_s['tro_sph']=joints['tro_sph'].acc_rhs(q,qdot)
	 acc_rhs_s['ch_sh_uni']=joints['ch_sh_uni'].acc_rhs(q,qdot)
	 acc_rhs_s['sh_lca_uni']=joints['sh_lca_uni'].acc_rhs(q,qdot)
	 acc_rhs_s['tri_uni']=joints['tri_uni'].acc_rhs(q,qdot)
	 acc_rhs_s['d_m_cyl']=joints['d_m_cyl'].acc_rhs(q,qdot)
	 acc_rhs_s['wc_rev']=joints['wc_rev'].acc_rhs(q,qdot)
	 acc_rhs_s['ucaf_r_rev']=joints['ucaf_r_rev'].acc_rhs(q,qdot)
	 acc_rhs_s['lcaf_r_rev']=joints['lcaf_r_rev'].acc_rhs(q,qdot)
	 acc_rhs_s['ucao_r_sph']=joints['ucao_r_sph'].acc_rhs(q,qdot)
	 acc_rhs_s['lcao_r_sph']=joints['lcao_r_sph'].acc_rhs(q,qdot)
	 acc_rhs_s['tro_r_sph']=joints['tro_r_sph'].acc_rhs(q,qdot)
	 acc_rhs_s['ch_sh_r_uni']=joints['ch_sh_r_uni'].acc_rhs(q,qdot)
	 acc_rhs_s['sh_lca_r_uni']=joints['sh_lca_r_uni'].acc_rhs(q,qdot)
	 acc_rhs_s['tri_r_uni']=joints['tri_r_uni'].acc_rhs(q,qdot)
	 acc_rhs_s['d_m_r_cyl']=joints['d_m_r_cyl'].acc_rhs(q,qdot)
	 acc_rhs_s['wc_r_rev']=joints['wc_r_rev'].acc_rhs(q,qdot)
	 acc_rhs_s['origin_br']=joints['origin_br'].acc_rhs(q,qdot)
	 acc_rhs_s['mount_1_rev']=joints['mount_1_rev'].acc_rhs(q,qdot)
	 acc_rhs_s['mount_2_rev']=joints['mount_2_rev'].acc_rhs(q,qdot)
	 acc_rhs_s['C1_uni']=joints['C1_uni'].acc_rhs(q,qdot)
	 acc_rhs_s['E_uni']=joints['E_uni'].acc_rhs(q,qdot)
	 acc_rhs_s['F_uni']=joints['F_uni'].acc_rhs(q,qdot)
	 acc_rhs_s['C2_sph']=joints['C2_sph'].acc_rhs(q,qdot)
	 acc_rhs_s['EF_cyl']=joints['EF_cyl'].acc_rhs(q,qdot)
	 acc_rhs_s['ground']=bodies['ground'].mount_acc_rhs(qdot)
	 acc_rhs_s['chassis']=bodies['chassis'].acc_rhs(qdot)
	 acc_rhs_s['uca']=bodies['uca'].acc_rhs(qdot)
	 acc_rhs_s['lca']=bodies['lca'].acc_rhs(qdot)
	 acc_rhs_s['upright']=bodies['upright'].acc_rhs(qdot)
	 acc_rhs_s['tie']=bodies['tie'].acc_rhs(qdot)
	 acc_rhs_s['d1']=bodies['d1'].acc_rhs(qdot)
	 acc_rhs_s['d2']=bodies['d2'].acc_rhs(qdot)
	 acc_rhs_s['wheel']=bodies['wheel'].acc_rhs(qdot)
	 acc_rhs_s['uca_r']=bodies['uca_r'].acc_rhs(qdot)
	 acc_rhs_s['lca_r']=bodies['lca_r'].acc_rhs(qdot)
	 acc_rhs_s['upright_r']=bodies['upright_r'].acc_rhs(qdot)
	 acc_rhs_s['tie_r']=bodies['tie_r'].acc_rhs(qdot)
	 acc_rhs_s['d1_r']=bodies['d1_r'].acc_rhs(qdot)
	 acc_rhs_s['d2_r']=bodies['d2_r'].acc_rhs(qdot)
	 acc_rhs_s['wheel_r']=bodies['wheel_r'].acc_rhs(qdot)
	 acc_rhs_s['l1']=bodies['l1'].acc_rhs(qdot)
	 acc_rhs_s['l2']=bodies['l2'].acc_rhs(qdot)
	 acc_rhs_s['l3']=bodies['l3'].acc_rhs(qdot)
	 acc_rhs_s['l4']=bodies['l4'].acc_rhs(qdot)
	 acc_rhs_s['l5']=bodies['l5'].acc_rhs(qdot)
	 acc_rhs_s['wc_rev_actuator']=actuators['wc_rev_actuator'].acc_rhs(q,qdot)
	 acc_rhs_s['wc_r_rev_actuator']=actuators['wc_r_rev_actuator'].acc_rhs(q,qdot)
	 acc_rhs_s['l5.y_actuator']=actuators['l5.y_actuator'].acc_rhs(q,qdot)
	 system=sparse.bmat(acc_rhs_s.values.reshape((52,1)),format='csc') 
	 return system.A.reshape((143,)) 


mass_matrix_df=pd.DataFrame([21 *[None]],columns=['ground', 'chassis', 'uca', 'lca', 'upright', 'tie', 'd1', 'd2', 'wheel', 'uca_r', 'lca_r', 'upright_r', 'tie_r', 'd1_r', 'd2_r', 'wheel_r', 'l1', 'l2', 'l3', 'l4', 'l5'],index=['ground', 'chassis', 'uca', 'lca', 'upright', 'tie', 'd1', 'd2', 'wheel', 'uca_r', 'lca_r', 'upright_r', 'tie_r', 'd1_r', 'd2_r', 'wheel_r', 'l1', 'l2', 'l3', 'l4', 'l5'])
def mass_matrix(q,bodies): 
	 mass_matrix_df.loc['ground','ground']=bodies['ground'].mass_matrix(q)
	 mass_matrix_df.loc['chassis','chassis']=bodies['chassis'].mass_matrix(q)
	 mass_matrix_df.loc['uca','uca']=bodies['uca'].mass_matrix(q)
	 mass_matrix_df.loc['lca','lca']=bodies['lca'].mass_matrix(q)
	 mass_matrix_df.loc['upright','upright']=bodies['upright'].mass_matrix(q)
	 mass_matrix_df.loc['tie','tie']=bodies['tie'].mass_matrix(q)
	 mass_matrix_df.loc['d1','d1']=bodies['d1'].mass_matrix(q)
	 mass_matrix_df.loc['d2','d2']=bodies['d2'].mass_matrix(q)
	 mass_matrix_df.loc['wheel','wheel']=bodies['wheel'].mass_matrix(q)
	 mass_matrix_df.loc['uca_r','uca_r']=bodies['uca_r'].mass_matrix(q)
	 mass_matrix_df.loc['lca_r','lca_r']=bodies['lca_r'].mass_matrix(q)
	 mass_matrix_df.loc['upright_r','upright_r']=bodies['upright_r'].mass_matrix(q)
	 mass_matrix_df.loc['tie_r','tie_r']=bodies['tie_r'].mass_matrix(q)
	 mass_matrix_df.loc['d1_r','d1_r']=bodies['d1_r'].mass_matrix(q)
	 mass_matrix_df.loc['d2_r','d2_r']=bodies['d2_r'].mass_matrix(q)
	 mass_matrix_df.loc['wheel_r','wheel_r']=bodies['wheel_r'].mass_matrix(q)
	 mass_matrix_df.loc['l1','l1']=bodies['l1'].mass_matrix(q)
	 mass_matrix_df.loc['l2','l2']=bodies['l2'].mass_matrix(q)
	 mass_matrix_df.loc['l3','l3']=bodies['l3'].mass_matrix(q)
	 mass_matrix_df.loc['l4','l4']=bodies['l4'].mass_matrix(q)
	 mass_matrix_df.loc['l5','l5']=bodies['l5'].mass_matrix(q)
	 mass_matrix=sparse.bmat(mass_matrix_df,format='csc') 
	 return mass_matrix 


Qg_s=pd.Series([21 *np.zeros((7,1))],index=['ground', 'chassis', 'uca', 'lca', 'upright', 'tie', 'd1', 'd2', 'wheel', 'uca_r', 'lca_r', 'upright_r', 'tie_r', 'd1_r', 'd2_r', 'wheel_r', 'l1', 'l2', 'l3', 'l4', 'l5'])
def Qg(bodies): 
	 Qg_s['ground']=bodies['ground'].gravity()
	 Qg_s['chassis']=bodies['chassis'].gravity()
	 Qg_s['uca']=bodies['uca'].gravity()
	 Qg_s['lca']=bodies['lca'].gravity()
	 Qg_s['upright']=bodies['upright'].gravity()
	 Qg_s['tie']=bodies['tie'].gravity()
	 Qg_s['d1']=bodies['d1'].gravity()
	 Qg_s['d2']=bodies['d2'].gravity()
	 Qg_s['wheel']=bodies['wheel'].gravity()
	 Qg_s['uca_r']=bodies['uca_r'].gravity()
	 Qg_s['lca_r']=bodies['lca_r'].gravity()
	 Qg_s['upright_r']=bodies['upright_r'].gravity()
	 Qg_s['tie_r']=bodies['tie_r'].gravity()
	 Qg_s['d1_r']=bodies['d1_r'].gravity()
	 Qg_s['d2_r']=bodies['d2_r'].gravity()
	 Qg_s['wheel_r']=bodies['wheel_r'].gravity()
	 Qg_s['l1']=bodies['l1'].gravity()
	 Qg_s['l2']=bodies['l2'].gravity()
	 Qg_s['l3']=bodies['l3'].gravity()
	 Qg_s['l4']=bodies['l4'].gravity()
	 Qg_s['l5']=bodies['l5'].gravity()
	 system=sparse.bmat(Qg_s.values.reshape((21,1)),format='csc') 
	 return system.A.reshape((147,)) 


Qv_s=pd.Series([21 *np.zeros((7,1))],index=['ground', 'chassis', 'uca', 'lca', 'upright', 'tie', 'd1', 'd2', 'wheel', 'uca_r', 'lca_r', 'upright_r', 'tie_r', 'd1_r', 'd2_r', 'wheel_r', 'l1', 'l2', 'l3', 'l4', 'l5'])
def Qv(bodies,q,qdot): 
	 Qv_s['ground']=bodies['ground'].centrifugal(q,qdot)
	 Qv_s['chassis']=bodies['chassis'].centrifugal(q,qdot)
	 Qv_s['uca']=bodies['uca'].centrifugal(q,qdot)
	 Qv_s['lca']=bodies['lca'].centrifugal(q,qdot)
	 Qv_s['upright']=bodies['upright'].centrifugal(q,qdot)
	 Qv_s['tie']=bodies['tie'].centrifugal(q,qdot)
	 Qv_s['d1']=bodies['d1'].centrifugal(q,qdot)
	 Qv_s['d2']=bodies['d2'].centrifugal(q,qdot)
	 Qv_s['wheel']=bodies['wheel'].centrifugal(q,qdot)
	 Qv_s['uca_r']=bodies['uca_r'].centrifugal(q,qdot)
	 Qv_s['lca_r']=bodies['lca_r'].centrifugal(q,qdot)
	 Qv_s['upright_r']=bodies['upright_r'].centrifugal(q,qdot)
	 Qv_s['tie_r']=bodies['tie_r'].centrifugal(q,qdot)
	 Qv_s['d1_r']=bodies['d1_r'].centrifugal(q,qdot)
	 Qv_s['d2_r']=bodies['d2_r'].centrifugal(q,qdot)
	 Qv_s['wheel_r']=bodies['wheel_r'].centrifugal(q,qdot)
	 Qv_s['l1']=bodies['l1'].centrifugal(q,qdot)
	 Qv_s['l2']=bodies['l2'].centrifugal(q,qdot)
	 Qv_s['l3']=bodies['l3'].centrifugal(q,qdot)
	 Qv_s['l4']=bodies['l4'].centrifugal(q,qdot)
	 Qv_s['l5']=bodies['l5'].centrifugal(q,qdot)
	 system=sparse.bmat(Qv_s.values.reshape((21,1)),format='csc') 
	 return system.A.reshape((147,)) 


Qa_s=pd.Series([21 *np.zeros((7,1))],index=['ground', 'chassis', 'uca', 'lca', 'upright', 'tie', 'd1', 'd2', 'wheel', 'uca_r', 'lca_r', 'upright_r', 'tie_r', 'd1_r', 'd2_r', 'wheel_r', 'l1', 'l2', 'l3', 'l4', 'l5'])
def Qa(forces,q,qdot): 
	 Qi,Qj=forces['tsda'].equation(q,qdot) 
	 Qa_s['d1']=Qi
	 Qa_s['d2']=Qj
	 Qa_s['wheel']=forces['tvf'].equation(q,qdot)
	 Qi,Qj=forces['tsda_r'].equation(q,qdot) 
	 Qa_s['d1_r']=Qi
	 Qa_s['d2_r']=Qj
	 Qa_s['wheel_r']=forces['tvf_r'].equation(q,qdot)
	 Qa_s['upright_r']=forces['sr'].equation(q,qdot)
	 Qa_s['upright']=forces['sl'].equation(q,qdot)
	 system=sparse.bmat(Qa_s.values.reshape((21,1)),format='csc') 
	 return system.A.reshape((147,)) 


JR_s=pd.Series(np.zeros((168)),index=['ucaf_rev_Fx', 'ucaf_rev_Fy', 'ucaf_rev_Fz', 'ucaf_rev_Mx', 'ucaf_rev_My', 'ucaf_rev_Mz', 'lcaf_rev_Fx', 'lcaf_rev_Fy', 'lcaf_rev_Fz', 'lcaf_rev_Mx', 'lcaf_rev_My', 'lcaf_rev_Mz', 'ucao_sph_Fx', 'ucao_sph_Fy', 'ucao_sph_Fz', 'ucao_sph_Mx', 'ucao_sph_My', 'ucao_sph_Mz', 'lcao_sph_Fx', 'lcao_sph_Fy', 'lcao_sph_Fz', 'lcao_sph_Mx', 'lcao_sph_My', 'lcao_sph_Mz', 'tro_sph_Fx', 'tro_sph_Fy', 'tro_sph_Fz', 'tro_sph_Mx', 'tro_sph_My', 'tro_sph_Mz', 'ch_sh_uni_Fx', 'ch_sh_uni_Fy', 'ch_sh_uni_Fz', 'ch_sh_uni_Mx', 'ch_sh_uni_My', 'ch_sh_uni_Mz', 'sh_lca_uni_Fx', 'sh_lca_uni_Fy', 'sh_lca_uni_Fz', 'sh_lca_uni_Mx', 'sh_lca_uni_My', 'sh_lca_uni_Mz', 'tri_uni_Fx', 'tri_uni_Fy', 'tri_uni_Fz', 'tri_uni_Mx', 'tri_uni_My', 'tri_uni_Mz', 'd_m_cyl_Fx', 'd_m_cyl_Fy', 'd_m_cyl_Fz', 'd_m_cyl_Mx', 'd_m_cyl_My', 'd_m_cyl_Mz', 'wc_rev_Fx', 'wc_rev_Fy', 'wc_rev_Fz', 'wc_rev_Mx', 'wc_rev_My', 'wc_rev_Mz', 'ucaf_r_rev_Fx', 'ucaf_r_rev_Fy', 'ucaf_r_rev_Fz', 'ucaf_r_rev_Mx', 'ucaf_r_rev_My', 'ucaf_r_rev_Mz', 'lcaf_r_rev_Fx', 'lcaf_r_rev_Fy', 'lcaf_r_rev_Fz', 'lcaf_r_rev_Mx', 'lcaf_r_rev_My', 'lcaf_r_rev_Mz', 'ucao_r_sph_Fx', 'ucao_r_sph_Fy', 'ucao_r_sph_Fz', 'ucao_r_sph_Mx', 'ucao_r_sph_My', 'ucao_r_sph_Mz', 'lcao_r_sph_Fx', 'lcao_r_sph_Fy', 'lcao_r_sph_Fz', 'lcao_r_sph_Mx', 'lcao_r_sph_My', 'lcao_r_sph_Mz', 'tro_r_sph_Fx', 'tro_r_sph_Fy', 'tro_r_sph_Fz', 'tro_r_sph_Mx', 'tro_r_sph_My', 'tro_r_sph_Mz', 'ch_sh_r_uni_Fx', 'ch_sh_r_uni_Fy', 'ch_sh_r_uni_Fz', 'ch_sh_r_uni_Mx', 'ch_sh_r_uni_My', 'ch_sh_r_uni_Mz', 'sh_lca_r_uni_Fx', 'sh_lca_r_uni_Fy', 'sh_lca_r_uni_Fz', 'sh_lca_r_uni_Mx', 'sh_lca_r_uni_My', 'sh_lca_r_uni_Mz', 'tri_r_uni_Fx', 'tri_r_uni_Fy', 'tri_r_uni_Fz', 'tri_r_uni_Mx', 'tri_r_uni_My', 'tri_r_uni_Mz', 'd_m_r_cyl_Fx', 'd_m_r_cyl_Fy', 'd_m_r_cyl_Fz', 'd_m_r_cyl_Mx', 'd_m_r_cyl_My', 'd_m_r_cyl_Mz', 'wc_r_rev_Fx', 'wc_r_rev_Fy', 'wc_r_rev_Fz', 'wc_r_rev_Mx', 'wc_r_rev_My', 'wc_r_rev_Mz', 'origin_br_Fx', 'origin_br_Fy', 'origin_br_Fz', 'origin_br_Mx', 'origin_br_My', 'origin_br_Mz', 'mount_1_rev_Fx', 'mount_1_rev_Fy', 'mount_1_rev_Fz', 'mount_1_rev_Mx', 'mount_1_rev_My', 'mount_1_rev_Mz', 'mount_2_rev_Fx', 'mount_2_rev_Fy', 'mount_2_rev_Fz', 'mount_2_rev_Mx', 'mount_2_rev_My', 'mount_2_rev_Mz', 'C1_uni_Fx', 'C1_uni_Fy', 'C1_uni_Fz', 'C1_uni_Mx', 'C1_uni_My', 'C1_uni_Mz', 'E_uni_Fx', 'E_uni_Fy', 'E_uni_Fz', 'E_uni_Mx', 'E_uni_My', 'E_uni_Mz', 'F_uni_Fx', 'F_uni_Fy', 'F_uni_Fz', 'F_uni_Mx', 'F_uni_My', 'F_uni_Mz', 'C2_sph_Fx', 'C2_sph_Fy', 'C2_sph_Fz', 'C2_sph_Mx', 'C2_sph_My', 'C2_sph_Mz', 'EF_cyl_Fx', 'EF_cyl_Fy', 'EF_cyl_Fz', 'EF_cyl_Mx', 'EF_cyl_My', 'EF_cyl_Mz'])
def JR(joints,q,lamda): 
	 JR_s[['ucaf_rev_Fx', 'ucaf_rev_Fy', 'ucaf_rev_Fz', 'ucaf_rev_Mx', 'ucaf_rev_My', 'ucaf_rev_Mz']]=joints['ucaf_rev'].reactions(q,lamda)
	 JR_s[['lcaf_rev_Fx', 'lcaf_rev_Fy', 'lcaf_rev_Fz', 'lcaf_rev_Mx', 'lcaf_rev_My', 'lcaf_rev_Mz']]=joints['lcaf_rev'].reactions(q,lamda)
	 JR_s[['ucao_sph_Fx', 'ucao_sph_Fy', 'ucao_sph_Fz', 'ucao_sph_Mx', 'ucao_sph_My', 'ucao_sph_Mz']]=joints['ucao_sph'].reactions(q,lamda)
	 JR_s[['lcao_sph_Fx', 'lcao_sph_Fy', 'lcao_sph_Fz', 'lcao_sph_Mx', 'lcao_sph_My', 'lcao_sph_Mz']]=joints['lcao_sph'].reactions(q,lamda)
	 JR_s[['tro_sph_Fx', 'tro_sph_Fy', 'tro_sph_Fz', 'tro_sph_Mx', 'tro_sph_My', 'tro_sph_Mz']]=joints['tro_sph'].reactions(q,lamda)
	 JR_s[['ch_sh_uni_Fx', 'ch_sh_uni_Fy', 'ch_sh_uni_Fz', 'ch_sh_uni_Mx', 'ch_sh_uni_My', 'ch_sh_uni_Mz']]=joints['ch_sh_uni'].reactions(q,lamda)
	 JR_s[['sh_lca_uni_Fx', 'sh_lca_uni_Fy', 'sh_lca_uni_Fz', 'sh_lca_uni_Mx', 'sh_lca_uni_My', 'sh_lca_uni_Mz']]=joints['sh_lca_uni'].reactions(q,lamda)
	 JR_s[['tri_uni_Fx', 'tri_uni_Fy', 'tri_uni_Fz', 'tri_uni_Mx', 'tri_uni_My', 'tri_uni_Mz']]=joints['tri_uni'].reactions(q,lamda)
	 JR_s[['d_m_cyl_Fx', 'd_m_cyl_Fy', 'd_m_cyl_Fz', 'd_m_cyl_Mx', 'd_m_cyl_My', 'd_m_cyl_Mz']]=joints['d_m_cyl'].reactions(q,lamda)
	 JR_s[['wc_rev_Fx', 'wc_rev_Fy', 'wc_rev_Fz', 'wc_rev_Mx', 'wc_rev_My', 'wc_rev_Mz']]=joints['wc_rev'].reactions(q,lamda)
	 JR_s[['ucaf_r_rev_Fx', 'ucaf_r_rev_Fy', 'ucaf_r_rev_Fz', 'ucaf_r_rev_Mx', 'ucaf_r_rev_My', 'ucaf_r_rev_Mz']]=joints['ucaf_r_rev'].reactions(q,lamda)
	 JR_s[['lcaf_r_rev_Fx', 'lcaf_r_rev_Fy', 'lcaf_r_rev_Fz', 'lcaf_r_rev_Mx', 'lcaf_r_rev_My', 'lcaf_r_rev_Mz']]=joints['lcaf_r_rev'].reactions(q,lamda)
	 JR_s[['ucao_r_sph_Fx', 'ucao_r_sph_Fy', 'ucao_r_sph_Fz', 'ucao_r_sph_Mx', 'ucao_r_sph_My', 'ucao_r_sph_Mz']]=joints['ucao_r_sph'].reactions(q,lamda)
	 JR_s[['lcao_r_sph_Fx', 'lcao_r_sph_Fy', 'lcao_r_sph_Fz', 'lcao_r_sph_Mx', 'lcao_r_sph_My', 'lcao_r_sph_Mz']]=joints['lcao_r_sph'].reactions(q,lamda)
	 JR_s[['tro_r_sph_Fx', 'tro_r_sph_Fy', 'tro_r_sph_Fz', 'tro_r_sph_Mx', 'tro_r_sph_My', 'tro_r_sph_Mz']]=joints['tro_r_sph'].reactions(q,lamda)
	 JR_s[['ch_sh_r_uni_Fx', 'ch_sh_r_uni_Fy', 'ch_sh_r_uni_Fz', 'ch_sh_r_uni_Mx', 'ch_sh_r_uni_My', 'ch_sh_r_uni_Mz']]=joints['ch_sh_r_uni'].reactions(q,lamda)
	 JR_s[['sh_lca_r_uni_Fx', 'sh_lca_r_uni_Fy', 'sh_lca_r_uni_Fz', 'sh_lca_r_uni_Mx', 'sh_lca_r_uni_My', 'sh_lca_r_uni_Mz']]=joints['sh_lca_r_uni'].reactions(q,lamda)
	 JR_s[['tri_r_uni_Fx', 'tri_r_uni_Fy', 'tri_r_uni_Fz', 'tri_r_uni_Mx', 'tri_r_uni_My', 'tri_r_uni_Mz']]=joints['tri_r_uni'].reactions(q,lamda)
	 JR_s[['d_m_r_cyl_Fx', 'd_m_r_cyl_Fy', 'd_m_r_cyl_Fz', 'd_m_r_cyl_Mx', 'd_m_r_cyl_My', 'd_m_r_cyl_Mz']]=joints['d_m_r_cyl'].reactions(q,lamda)
	 JR_s[['wc_r_rev_Fx', 'wc_r_rev_Fy', 'wc_r_rev_Fz', 'wc_r_rev_Mx', 'wc_r_rev_My', 'wc_r_rev_Mz']]=joints['wc_r_rev'].reactions(q,lamda)
	 JR_s[['origin_br_Fx', 'origin_br_Fy', 'origin_br_Fz', 'origin_br_Mx', 'origin_br_My', 'origin_br_Mz']]=joints['origin_br'].reactions(q,lamda)
	 JR_s[['mount_1_rev_Fx', 'mount_1_rev_Fy', 'mount_1_rev_Fz', 'mount_1_rev_Mx', 'mount_1_rev_My', 'mount_1_rev_Mz']]=joints['mount_1_rev'].reactions(q,lamda)
	 JR_s[['mount_2_rev_Fx', 'mount_2_rev_Fy', 'mount_2_rev_Fz', 'mount_2_rev_Mx', 'mount_2_rev_My', 'mount_2_rev_Mz']]=joints['mount_2_rev'].reactions(q,lamda)
	 JR_s[['C1_uni_Fx', 'C1_uni_Fy', 'C1_uni_Fz', 'C1_uni_Mx', 'C1_uni_My', 'C1_uni_Mz']]=joints['C1_uni'].reactions(q,lamda)
	 JR_s[['E_uni_Fx', 'E_uni_Fy', 'E_uni_Fz', 'E_uni_Mx', 'E_uni_My', 'E_uni_Mz']]=joints['E_uni'].reactions(q,lamda)
	 JR_s[['F_uni_Fx', 'F_uni_Fy', 'F_uni_Fz', 'F_uni_Mx', 'F_uni_My', 'F_uni_Mz']]=joints['F_uni'].reactions(q,lamda)
	 JR_s[['C2_sph_Fx', 'C2_sph_Fy', 'C2_sph_Fz', 'C2_sph_Mx', 'C2_sph_My', 'C2_sph_Mz']]=joints['C2_sph'].reactions(q,lamda)
	 JR_s[['EF_cyl_Fx', 'EF_cyl_Fy', 'EF_cyl_Fz', 'EF_cyl_Mx', 'EF_cyl_My', 'EF_cyl_Mz']]=joints['EF_cyl'].reactions(q,lamda)
	 return JR_s 


