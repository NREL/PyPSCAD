#!/usr/bin/env python3

import mhi.pscad
import numpy as np

class PSCAD_RUN:
    def __init__(self,run_num,p1_p,p1_q,p2_p,p2_q,p2_ph):
        self.run_num = run_num
        self.p1_p = p1_p
        self.p1_q = p1_q
        self.p2_p = p2_p
        self.p2_q = p2_q
        self.p2_ph = p2_ph

cases = []
case_data = np.loadtxt(r'C:\Users\matti\Source\Droop-e - Copy\matlab\ThreeBusPF_Sweep.csv',delimiter=',')

for i in range(0,len(case_data)-1):
    cases.append(PSCAD_RUN(i+1,case_data[i,1],case_data[i,2],case_data[i,3],case_data[i,4],case_data[i,5]))

# for case in cases:
#     with mhi.pscad.application() as pscad:

#         three_bus = pscad.project("Three_Bus")
#         kw_p1_p = {"Value": str(case.p1_p)}
#         gen_1_p_setpoint = three_bus.component(603507007)
#         gen_1_p_setpoint.parameters(**kw_p1_p)

#         gen_1_q_setpoint = three_bus.component(2014534646)
#         kw_p1_q = {"Value": str(case.p1_q)}
#         gen_1_q_setpoint.parameters(**kw_p1_q)

#         gen_2_p_setpoint = three_bus.component(949654747)
#         kw_p2_p = {"Value": str(case.p2_p)}
#         gen_2_p_setpoint.parameters(**kw_p2_p)

#         gen_2_q_setpoint = three_bus.component(200636900)
#         kw_p2_q = {"Value": str(case.p2_q)}
#         gen_2_q_setpoint.parameters(**kw_p2_q)

#         gen_2_ph_setpoint = three_bus.component(830299848)
#         kw_p2_ph = {"Value": str(case.p2_ph)}
#         gen_2_ph_setpoint.parameters(**kw_p2_ph)

#         data_txt = np.loadtxt(r'C:\Users\matti\Source\Droop-e - Copy\pscad\3_bus\Three_Bus.gf81\Three_Bus_01.out')
#         case.data = data_txt

#         three_bus.run()


                                              
# data_txt = np.loadtxt('Three_Bus.gf81/Three_Bus_01.out')