import pandas as pd
import numpy as np
import random as ran
import math as m

class Fiber_num_distribution():
    def __init__(self,Fib_num_set,Fib_zone):
        self.Fib_num_set = Fib_num_set
        self.Fib_zone = Fib_zone
    
    ### The following code outputs the fiber number distribution corresponding to each fiber diameter
    def fib_num_dis(self):
        fib_num_dis = []
        fib_dia = []
        fib_dia_fra = []
        fib_dia = [465, 435, 405, 375, 345, 315, 285, 255, 225, 195, 165, 135, 105, 75, 45, 15]
        if Fib_zone == 2:
            fib_dia_fra = [0.0033, 0.0000, 0.0000, 0.0000, 0.0000, 0.0033, 0.0016, 0.0341, 0.0927, 0.2813, 0.3545, 0.0927, 0.0146, 0.0293, 0.0846, 0.0081]   #张鑫的全部数据
        leng = len(fib_dia)
        l = 0
        while l < leng:
            fib_dia_number = [fib_dia[l], round(self.Fib_num_set * fib_dia_fra[l])]
            fib_num_dis.append(fib_dia_number)
            l += 1
            continue
        return fib_num_dis
    
    ### The following code outputs the fiber SVF distribution corresponding to each fiber diameter
    def fib_svf_dis(self):
        fib_svf_dis = []
        fib_dia = []
        fib_dia_svf = []
        fib_dia = [465, 435, 405, 375, 345, 315, 285, 255, 225, 195, 165, 135, 105, 75, 45, 15]
        if Fib_zone == 2:
            fib_dia_svf = [0.0230, 0.0000, 0.0000, 0.0000, 0.0000, 0.0105, 0.0043, 0.0725, 0.1533, 0.3495, 0.3153, 0.0552, 0.0053, 0.0054, 0.0056, 0.0001]
        leng = len(fib_dia)
        l = 0
        while l < leng:
            fib_dia_fraction = [fib_dia[l], fib_dia_svf[l]]
            fib_svf_dis.append(fib_dia_fraction)
            l += 1
            continue
        return fib_svf_dis

class Bead_num_distribution():
    def __init__(self,Bead_num_set,Bead_zone):
        self.Bead_num_set = Bead_num_set
        self.Bead_zone = Bead_zone
    
    ### The following code outputs the bead number distribution corresponding to each fiber diameter
    def Bead_num_dis(self):
        Bead_num_dis = []
        Bead_dia = []
        Bead_dia_fra = []
        Bead_dia = [465, 435, 405, 375, 345, 315, 285, 255, 225, 195, 165, 135, 105, 75, 45, 15]
        if Bead_zone == 2:
            Bead_dia_fra = [0.0033, 0.0000, 0.0000, 0.0000, 0.0000, 0.0033, 0.0016, 0.0341, 0.0927, 0.2813, 0.3545, 0.0927, 0.0146, 0.0293, 0.0846, 0.0081]
        leng = len(Bead_dia)
        l = 0
        while l < leng:
            Bead_dia_number = [Bead_dia[l], round(self.Bead_num_set * Bead_dia_fra[l])]
            Bead_num_dis.append(Bead_dia_number)
            l += 1
            continue
        return Bead_num_dis
    
    ### The following code outputs the bead SVF distribution corresponding to each fiber diameter
    def Bead_svf_dis(self):
        Bead_svf_dis = []
        Bead_dia = []
        Bead_dia_svf = []
        Bead_dia = [465, 435, 405, 375, 345, 315, 285, 255, 225, 195, 165, 135, 105, 75, 45, 15]
        if Bead_zone == 2:
            Bead_dia_svf = [0.0230, 0.0000, 0.0000, 0.0000, 0.0000, 0.0105, 0.0043, 0.0725, 0.1533, 0.3495, 0.3153, 0.0552, 0.0053, 0.0054, 0.0056, 0.0001]
        leng = len(Bead_dia)
        l = 0
        while l < leng:
            Bead_dia_fraction = [Bead_dia[l], Bead_dia_svf[l]]
            Bead_svf_dis.append(Bead_dia_fraction)
            l += 1
            continue
        return Bead_svf_dis


### The following code set the initial value for the variables
coordinate_all = []
bead_all = []
SV_all = 0
SVF_all = 0
SV_bd_all = 0
SVF_bd_all = 0
windAngle_all = 0
windAngle_ave_all = 0
Fiber_num_all = 0
Bead_num_all = 0
zone_volume = 9000*9000*9000
Fiber_SVF_Original = 0.0184
Bead_Fraction = 0.2
SVF_control_all = Fiber_SVF_Original * (1-Bead_Fraction)
SVF_bead_all = Fiber_SVF_Original * Bead_Fraction
bead_lh_ratio = 2
bead_hf_ratio = 2
SVF_control_factor_Fiber = 0.05
SVF_control_factor_Bead = 0.05
Fib_num_set = 58
Bead_num_set = 92
Fib_zone = 2
Bead_zone = 2
angle_control = 85
SVF_control_all_down = (1 - SVF_control_factor_Fiber)*SVF_control_all
SVF_control_all_up   = (1 + SVF_control_factor_Fiber)*SVF_control_all
SVF_bead_all_down = (1 - SVF_control_factor_Bead)*SVF_bead_all
SVF_bead_all_up   = (1 + SVF_control_factor_Bead)*SVF_bead_all

### The following code outputs the fiber number distribution and SVF distribution
Fiber_num_distribution_temp = Fiber_num_distribution(Fib_num_set,Fib_zone)
Fiber_num_dis = Fiber_num_distribution_temp.fib_num_dis()
Fiber_svf_dis = Fiber_num_distribution_temp.fib_svf_dis()
fib_dia_length = len(Fiber_num_dis)
Bead_num_distribution_temp = Bead_num_distribution(Bead_num_set,Bead_zone)
Bead_num_dis = Bead_num_distribution_temp.Bead_num_dis()
Bead_svf_dis = Bead_num_distribution_temp.Bead_svf_dis()
Bead_dia_length = len(Bead_num_dis)
dia_l = 0
bead_l = 0
layer_gap = 0

### The following code outputs all the fibers' and beads' coordinates
if SVF_all < SVF_control_all:
    ### The following loop outputs all the coordinates for each fiber diameter
    while dia_l < fib_dia_length:
        ### The following code defined the control paramenters for the current fiber and bead diameter
        SVF_control = 0
        SVF_control_Bead = 0
        fiber_dia = Fiber_num_dis[dia_l][0]
        bead_height = bead_hf_ratio * Bead_num_dis[bead_l][0]
        bead_length = bead_lh_ratio * bead_height
        layer_gap = int(2 * fiber_dia / 2 / 2**0.5)
        fiber_dia_num = int(Fiber_num_dis[dia_l][1])
        bead_dia_num  = int(Bead_num_dis[bead_l][1])
        fiber_dia_svf = float(Fiber_svf_dis[dia_l][1]*SVF_control_all)
        Bead_dia_svf = float(Bead_svf_dis[bead_l][1]*SVF_bead_all)
        SVF_control_factor_F = 0.1
        SVF_control_factor_B = 2
        SVF_control = fiber_dia_svf
        SVF_down = (1 - SVF_control_factor_F)*SVF_control
        SVF_up = (1 + SVF_control_factor_F)*SVF_control
        SVF_control_Bead = Bead_dia_svf
        SVF_down_Bead = (1 - SVF_control_factor_B)*SVF_control_Bead
        SVF_up_Bead = (1 + SVF_control_factor_B)*SVF_control_Bead
    
        ### Initial value of the paramenters for the current diameter
        SV = 0
        SVF = 0
        SV_bd = 0
        SVF_bd = 0
        coordinate = []
        bead = []
        windAngle = 0
        windAngle_ave = 0
        fiber_gen_way = [0,1,2,3,4,5]
        i = 0
        Fiber_num = 0
        Bead_num = 0
        Fiber_num_01a = 0
        Fiber_num_02a = 0
        Fiber_num_03a = 0
        Fiber_num_12a = 0
        Fiber_num_13a = 0
        Fiber_num_23a = 0
        Fiber_num_all = len(coordinate_all)
        Fiber_num_all_b = Fiber_num_all
        Bead_num_all = len(bead_all)
        Bead_num_all_b = Bead_num_all
        SVF_judge = SV / zone_volume
        
        ### The following code outputs the fibers' and beads' coordinates for current diameter
        if SVF_judge <= SVF_control:

            ### If the current diameter has no fibers to generate, then jump to next diameter
            if SVF_control == 0 or fiber_dia_num == 0:
                print("Current diameter: ", str(fiber_dia), "nm. No fibers are needed to generate!")
                dia_l += 1
                bead_l += 1
            
            ### The following code generate all the fibers' coordinates for current diameter, each loop generate one fiber's coornates
            fiber_dia_num_temp = fiber_dia_num
            bead_dia_num_temp = bead_dia_num
            while i < fiber_dia_num:

                ### Initial value of the paramenters for current fiber
                angle = 0
                codi1 = []
                codi2 = []
                Fiber_num = len(coordinate)
                Fiber_num_all = len(coordinate_all)
                Bead_num = len(bead)
                Bead_num_all = len(bead_all)

                ### The following code outputs a randomly selected fiber generation method without repetition.
                ### Once fewer than one method remains, all methods will be reset.
                if len(fiber_gen_way) == 0:
                    fiber_gen_way = [0,1,2,3,4,5]
                    fib_gen_way = ran.choice(fiber_gen_way)
                else:
                    fib_gen_way = ran.choice(fiber_gen_way)

                ### The following code outputs the coordinates of a fiber using the previously randomly selected method.
                if fib_gen_way == 0:
                    coordinate1 = []
                    x1 = int(ran.uniform(18000,    18000 + 9000))
                    y1 = int(ran.uniform(layer_gap,9000-layer_gap))
                    z1 = int(ran.uniform(layer_gap,layer_gap))
                    coordinate1 = [x1,y1,z1]
                    coordinate2 = []
                    x2 = int(ran.uniform(18000,    18000 + 9000))
                    y2 = int(ran.uniform(layer_gap,9000-layer_gap))
                    z2 = int(ran.uniform(9000-layer_gap,9000-layer_gap))
                    coordinate2 = [x2,y2,z2]
                    codi1 = [coordinate1,coordinate2,fiber_dia]
                elif fib_gen_way == 1:
                    coordinate1 = []
                    x3 = int(ran.uniform(18000,    18000 + 9000))
                    y3 = int(ran.uniform(layer_gap,layer_gap))
                    z3 = int(ran.uniform(layer_gap,9000-layer_gap))
                    coordinate1 = [x3,y3,z3]
                    coordinate2 = []
                    x4 = int(ran.uniform(18000,    18000 + 9000))
                    y4 = int(ran.uniform(9000-layer_gap,9000-layer_gap))
                    z4 = int(ran.uniform(layer_gap,9000-layer_gap))
                    coordinate2 = [x4,y4,z4]
                    codi1 = [coordinate1,coordinate2,fiber_dia]
                elif fib_gen_way == 2:
                    coordinate1 = []
                    x1 = int(ran.uniform(18000,    18000 + 9000))
                    y1 = int(ran.uniform(layer_gap,9000-layer_gap))
                    z1 = int(ran.uniform(layer_gap,layer_gap))
                    coordinate1 = [x1,y1,z1]
                    coordinate2 = []
                    x4 = int(ran.uniform(18000,    18000 + 9000))
                    y4 = int(ran.uniform(layer_gap,layer_gap))
                    z4 = int(ran.uniform(layer_gap,9000-layer_gap))
                    coordinate2 = [x4,y4,z4]
                    codi1 = [coordinate1,coordinate2,fiber_dia]
                elif fib_gen_way == 3:
                    coordinate1 = []
                    x2 = int(ran.uniform(18000,    18000 + 9000))
                    y2 = int(ran.uniform(layer_gap,9000-layer_gap))
                    z2 = int(ran.uniform(9000-layer_gap,9000-layer_gap))
                    coordinate1 = [x2,y2,z2]
                    coordinate2 = []
                    x3 = int(ran.uniform(18000,    18000 + 9000))
                    y3 = int(ran.uniform(9000-layer_gap,9000-layer_gap))
                    z3 = int(ran.uniform(layer_gap,9000-layer_gap))
                    coordinate2 = [x3,y3,z3]
                    codi1 = [coordinate1,coordinate2,fiber_dia]
                elif fib_gen_way == 4:
                    coordinate1 = []
                    x2 = int(ran.uniform(18000,    18000 + 9000))
                    y2 = int(ran.uniform(layer_gap,9000-layer_gap))
                    z2 = int(ran.uniform(9000-layer_gap,9000-layer_gap))
                    coordinate1 = [x2,y2,z2]
                    coordinate2 = []
                    x4 = int(ran.uniform(18000,    18000 + 9000))
                    y4 = int(ran.uniform(layer_gap,layer_gap))
                    z4 = int(ran.uniform(layer_gap,9000-layer_gap))
                    coordinate2 = [x4,y4,z4]
                    codi1 = [coordinate1,coordinate2,fiber_dia]
                else:
                    coordinate1 = []
                    x1 = int(ran.uniform(18000,    18000 + 9000))
                    y1 = int(ran.uniform(layer_gap,9000-layer_gap))
                    z1 = int(ran.uniform(layer_gap,layer_gap))
                    coordinate1 = [x1,y1,z1]
                    coordinate2 = []
                    x3 = int(ran.uniform(18000,    18000 + 9000))
                    y3 = int(ran.uniform(9000-layer_gap,9000-layer_gap))
                    z3 = int(ran.uniform(layer_gap,9000-layer_gap))
                    coordinate2 = [x3,y3,z3]
                    codi1 = [coordinate1,coordinate2,fiber_dia]
                
                ### The following code outputs the wind angle of current fiber
                if fib_gen_way == 0:
                    a = abs(z1 - z2)
                    b = abs(x1 - x2)
                elif fib_gen_way == 1:
                    a = abs(z3 - z4)
                    b = abs(x3 - x4)
                elif fib_gen_way == 2:
                    a = abs(z1 - z4)
                    b = abs(x1 - x4)
                elif fib_gen_way == 3:
                    a = abs(z2 - z3)
                    b = abs(x2 - x3)
                elif fib_gen_way == 4:
                    a = abs(z2 - z4)
                    b = abs(x2 - x4)
                else:
                    a = abs(z1 - z3)
                    b = abs(x1 - x3)
                if b == 0:
                    angle = 90
                else:
                    angle = m.atan(a/b)/m.pi*180
                
                ### The following code checks whether the fiber coordinates meet the requirements based on wind angle and fiber distance.
                ### If the coordinates do not meet the requirements, a new pair will be generated.
                if angle_control + 5 > angle > angle_control - 5:
                    fib_dis_ok = 0
                    beadf_dis_ok = 0
                    bead_dis_ok = 0
                    
                    ### The first fiber was added to the coordinates list without judgement
                    if Fiber_num_all == 0:
                        coordinate.append(codi1)
                        fiber_dia_num_temp -= 1
                        coordinate_all.append(codi1)
                        fiber_gen_way.remove(fib_gen_way)
                        if fib_gen_way == 0:
                            Fiber_num_01a += 1
                            SV += ((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**(0.5)*m.pi*fiber_dia**2/4
                        elif fib_gen_way == 1:
                            Fiber_num_23a += 1
                            SV += ((x4-x3)**2+(y4-y3)**2+(z4-z3)**2)**(0.5)*m.pi*fiber_dia**2/4
                        elif fib_gen_way == 2:
                            Fiber_num_03a += 1
                            SV += ((x4-x1)**2+(y4-y1)**2+(z4-z1)**2)**(0.5)*m.pi*fiber_dia**2/4
                        elif fib_gen_way == 3:
                            Fiber_num_12a += 1
                            SV += ((x2-x3)**2+(y2-y3)**2+(z2-z3)**2)**(0.5)*m.pi*fiber_dia**2/4
                        elif fib_gen_way == 4:
                            Fiber_num_13a += 1
                            SV += ((x2-x4)**2+(y2-y4)**2+(z2-z4)**2)**(0.5)*m.pi*fiber_dia**2/4
                        else:
                            Fiber_num_02a += 1
                            SV += ((x3-x1)**2+(y3-y1)**2+(z3-z1)**2)**(0.5)*m.pi*fiber_dia**2/4
                        fib_dis_ok += 1
                        windAngle += angle
                        print("Fiber_number_all_last=",str(Fiber_num_all_b), \
                                "  Fiber_number_all_temp=",str(Fiber_num_all), \
                                "  Fiber_number_dia=",str(fiber_dia_num), \
                                "  Fiber_number_now=",str(Fiber_num), \
                                "  Fiber_distance_judge=",str(0), \
                                "  Fiber_distance_ok=",str(fib_dis_ok))
                        
                        ### The other fibers were judged before being added to the coordinates list.
                        ### The judgement primarily focuses on the fiber distance to ensure mesh quality.
                        if bead_dia_num > 0:
                            bead1 = [[0, 0, 0]]
                            bead1[0][0] = (codi1[0][0] + codi1[1][0]) / 2
                            bead1[0][1] = (codi1[0][1] + codi1[1][1]) / 2
                            bead1[0][2] = (codi1[0][2] + codi1[1][2]) / 2
                            bead1 = [bead1[0], bead_height, bead_length]
                            bead.append(bead1)
                            bead_all.append(bead1)
                            SV_bd += 4/3*m.pi*(bead1[1]/2)**2*bead1[2]/2 - m.pi*fiber_dia**2/4*bead_length
                            beadf_dis_ok += 1
                            bead_dis_ok += 1
                            print("Fiber_number_all_last = ",str(Fiber_num_all_b), \
                                "  Fiber_number_all_temp = ",str(Fiber_num_all), \
                                "  Bead_number_dia = ",str(bead_dia_num), \
                                "  Fiber_number_now = ",str(Bead_num), \
                                "  Fiber_distance_judge = ",str(0), \
                                "  Fiber_distance_ok = ",str(fib_dis_ok))
                    else:
                        Points = int(bead_dia_num / fiber_dia_num)
                        Fiber_length = np.sqrt((codi1[0][0] - codi1[1][0])**2+(codi1[0][1] - codi1[1][1])**2+(codi1[0][2] - codi1[1][2])**2)
                        if bead_dia_num == 0 or bead_dia_num_temp == 0:
                            jud = 0                            
                            while jud < Fiber_num_all:
                                codi2 = coordinate_all[jud]
                                coordinate1_temp = np.array(coordinate_all[jud][0])
                                coordinate2_temp = np.array(coordinate_all[jud][1])
                                fiber_dia_temp = coordinate_all[jud][2]
                                r = coordinate1_temp
                                e = coordinate2_temp - coordinate1_temp
                                d_all = []
                                t = 0
                                while t <= 1000:
                                    P = r + t/1000 * e
                                    l = coordinate1 - P
                                    s = np.array(coordinate2) - np.array(coordinate1)
                                    S = np.linalg.norm(s)
                                    d = abs(np.linalg.norm(np.cross(l,s)) / S)
                                    d_all.append(d)
                                    t += 1
                                d_min = min(d_all)
                                fib_dis_control = (fiber_dia/2 + fiber_dia_temp/2)*1.5
                                if d_min < fib_dis_control:
                                    fib_dis_ok += 0
                                else:
                                    fib_dis_ok += 1
                                print("Fiber_number_all_last=",str(Fiber_num_all_b), \
                                    "  Fiber_number_all_temp=",str(Fiber_num_all), \
                                    "  Fiber_number_dia=",str(fiber_dia_num), \
                                    "  Fiber_number_now=",str(Fiber_num), \
                                    "  Fiber_distance_judge=",str(jud), \
                                    "  Fiber_distance_ok=",str(fib_dis_ok))
                                jud += 1
                                continue
                            if fib_dis_ok >= Fiber_num_all:                                
                                coordinate.append(codi1)
                                fiber_dia_num_temp -= 1
                                coordinate_all.append(codi1)
                                fiber_gen_way.remove(fib_gen_way)
                                windAngle += angle
                                if fib_gen_way == 0:
                                    Fiber_num_01a += 1
                                    SV += ((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**(0.5)*m.pi*fiber_dia**2/4
                                elif fib_gen_way == 1:
                                    Fiber_num_23a += 1
                                    SV += ((x4-x3)**2+(y4-y3)**2+(z4-z3)**2)**(0.5)*m.pi*fiber_dia**2/4
                                elif fib_gen_way == 2:
                                    Fiber_num_03a += 1
                                    SV += ((x4-x1)**2+(y4-y1)**2+(z4-z1)**2)**(0.5)*m.pi*fiber_dia**2/4
                                elif fib_gen_way == 3:
                                    Fiber_num_12a += 1
                                    SV += ((x2-x3)**2+(y2-y3)**2+(z2-z3)**2)**(0.5)*m.pi*fiber_dia**2/4
                                elif fib_gen_way == 4:
                                    Fiber_num_13a += 1
                                    SV += ((x2-x4)**2+(y2-y4)**2+(z2-z4)**2)**(0.5)*m.pi*fiber_dia**2/4
                                else:
                                    Fiber_num_02a += 1
                                    SV += ((x3-x1)**2+(y3-y1)**2+(z3-z1)**2)**(0.5)*m.pi*fiber_dia**2/4  
                            else:
                                i-= 1
                        elif fiber_dia_num >= bead_dia_num > 0 and fiber_dia_num >= bead_dia_num_temp > 0:
                            bead1 = [[0, 0, 0]]
                            bead1[0][0] = (codi1[0][0] + codi1[1][0]) / 2
                            bead1[0][1] = (codi1[0][1] + codi1[1][1]) / 2
                            bead1[0][2] = (codi1[0][2] + codi1[1][2]) / 2
                            bead1 = [bead1[0], bead_height, bead_length]
                            jud_ff = 0                            
                            while jud_ff < Fiber_num_all:
                                codi2 = coordinate_all[jud_ff]
                                coordinate1_temp = np.array(coordinate_all[jud_ff][0])
                                coordinate2_temp = np.array(coordinate_all[jud_ff][1])
                                fiber_dia_temp = coordinate_all[jud_ff][2]
                                r = coordinate1_temp
                                e = coordinate2_temp - coordinate1_temp
                                d_all = []
                                t = 0
                                while t <= 1000:
                                    P = r + t/1000 * e
                                    l = coordinate1 - P
                                    s = np.array(coordinate2) - np.array(coordinate1)
                                    S = np.linalg.norm(s)
                                    d = abs(np.linalg.norm(np.cross(l,s)) / S)
                                    d_all.append(d)
                                    t += 1
                                d_min = min(d_all)
                                fib_dis_control = (fiber_dia/2 + fiber_dia_temp/2)*1.5
                                if d_min < fib_dis_control:
                                    fib_dis_ok += 0
                                else:
                                    fib_dis_ok += 1
                                print("Fiber_number_all_last=",str(Fiber_num_all_b), \
                                    "  Fiber_number_all_temp=",str(Fiber_num_all), \
                                    "  Fiber_number_dia=",str(fiber_dia_num), \
                                    "  Fiber_number_now=",str(Fiber_num), \
                                    "  Fiber_distance_judge=",str(jud_ff), \
                                    "  Fiber_distance_ok=",str(fib_dis_ok))
                                jud_ff += 1
                                continue
                            jud_bf = 0
                            while jud_bf < Fiber_num_all:
                                codi2 = coordinate_all[jud_bf]
                                coordinate1_temp = np.array(coordinate_all[jud_bf][0])
                                coordinate2_temp = np.array(coordinate_all[jud_bf][1])
                                fiber_dia_temp = coordinate_all[jud_bf][2]
                                r = coordinate1_temp
                                e = coordinate2_temp - coordinate1_temp
                                d_all = []
                                t = 0
                                while t <= 1000:
                                    P = r + t/1000 * e
                                    d = m.dist(bead1[0],P)
                                    d_all.append(d)
                                    t += 1
                                d_bf_min = min(d_all)
                                beadf_dis_control = (bead1[1]/2 + fiber_dia_temp/2)*1.5
                                if d_bf_min < beadf_dis_control:
                                    beadf_dis_ok += 0
                                else:
                                    beadf_dis_ok += 1
                                print("Bead_number_all_last=",str(Bead_num_all_b), \
                                    "  Bead_number_all_temp=",str(Bead_num_all), \
                                    "  Bead_number_dia=",str(bead_dia_num), \
                                    "  Bead_number_now=",str(Bead_num), \
                                    "  Beadf_distance_judge=",str(jud_bf), \
                                    "  Beadf_distance_ok=",str(beadf_dis_ok))
                                jud_bf += 1
                                continue
                            jud_Bead = 0
                            while jud_Bead < Bead_num_all:
                                codi2 = bead_all[jud_Bead]
                                coordinate1_temp = np.array(bead_all[jud_Bead][0])
                                bead_height_temp = bead_all[jud_Bead][1]
                                bead_length_temp = bead_all[jud_Bead][2]
                                d_b_min = m.dist(bead1[0],coordinate1_temp)
                                bead_dis_control = (bead1[1] + bead_height_temp)/2 * 1.5
                                if d_b_min < bead_dis_control:
                                    bead_dis_ok += 0
                                else:
                                    bead_dis_ok += 1
                                print("Bead_number_all_last=",str(Bead_num_all_b), \
                                    "  Bead_number_all_temp=",str(Bead_num_all), \
                                    "  Bead_number_dia=",str(bead_dia_num), \
                                    "  Bead_number_now=",str(Bead_num), \
                                    "  Beadf_distance_judge=",str(jud_bf), \
                                    "  Beadf_distance_ok=",str(beadf_dis_ok))
                                jud_Bead += 1
                                continue
                            if fib_dis_ok >= Fiber_num_all and beadf_dis_ok >= Fiber_num_all and bead_dis_ok >= Bead_num_all:                                
                                coordinate.append(codi1)
                                fiber_dia_num_temp -= 1
                                coordinate_all.append(codi1)
                                fiber_gen_way.remove(fib_gen_way)
                                windAngle += angle
                                if fib_gen_way == 0:
                                    Fiber_num_01a += 1
                                    SV += ((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**(0.5)*m.pi*fiber_dia**2/4
                                elif fib_gen_way == 1:
                                    Fiber_num_23a += 1
                                    SV += ((x4-x3)**2+(y4-y3)**2+(z4-z3)**2)**(0.5)*m.pi*fiber_dia**2/4
                                elif fib_gen_way == 2:
                                    Fiber_num_03a += 1
                                    SV += ((x4-x1)**2+(y4-y1)**2+(z4-z1)**2)**(0.5)*m.pi*fiber_dia**2/4
                                elif fib_gen_way == 3:
                                    Fiber_num_12a += 1
                                    SV += ((x2-x3)**2+(y2-y3)**2+(z2-z3)**2)**(0.5)*m.pi*fiber_dia**2/4
                                elif fib_gen_way == 4:
                                    Fiber_num_13a += 1
                                    SV += ((x2-x4)**2+(y2-y4)**2+(z2-z4)**2)**(0.5)*m.pi*fiber_dia**2/4
                                else:
                                    Fiber_num_02a += 1
                                    SV += ((x3-x1)**2+(y3-y1)**2+(z3-z1)**2)**(0.5)*m.pi*fiber_dia**2/4  
                                bead.append(bead1)
                                bead_all.append(bead1)
                                bead_dia_num_temp -= 1
                                SV_bd += 4/3*m.pi*(bead1[1]/2)**2*bead1[2]/2 - m.pi*fiber_dia**2/4*bead_length
                            else:
                                i-= 1   
                        elif fiber_dia_num < bead_dia_num and bead_dia_num_temp > 0 and bead1[2]*Points <= Fiber_length:
                            bead_ok = 0
                            Points_jud = float(bead_dia_num / fiber_dia_num)
                            Er = (Points_jud - Points) * fiber_dia_num
                            Points_plus = np.round(Er)
                            if Er > 0 and (fiber_dia_num - fiber_dia_num_temp) < Points_plus:
                                Points += 1
                            point = 0
                            bead_temp = []
                            SV_bd_temp = 0
                            while point < Points:
                                bead1 = [[0, 0, 0]]
                                bead1[0][0] = codi1[1][0] + (codi1[0][0] - codi1[1][0]) / (2 * Points ) * (2 * point + 1)
                                bead1[0][1] = codi1[1][1] + (codi1[0][1] - codi1[1][1]) / (2 * Points ) * (2 * point + 1)
                                bead1[0][2] = codi1[1][2] + (codi1[0][2] - codi1[1][2]) / (2 * Points ) * (2 * point + 1)
                                bead1 = [bead1[0], bead_height, bead_length]
                                jud_bf = 0
                                while jud_bf < Fiber_num_all:
                                    codi2 = coordinate_all[jud_bf]
                                    coordinate1_temp = np.array(coordinate_all[jud_bf][0])
                                    coordinate2_temp = np.array(coordinate_all[jud_bf][1])
                                    fiber_dia_temp = coordinate_all[jud_bf][2]
                                    r = coordinate1_temp
                                    e = coordinate2_temp - coordinate1_temp
                                    d_all = []
                                    t = 0
                                    while t <= 1000:
                                        P = r + t/1000 * e
                                        d = m.dist(bead1[0],P)
                                        d_all.append(d)
                                        t += 1
                                    d_bf_min = min(d_all)
                                    beadf_dis_control = (bead1[1]/2 + fiber_dia_temp/2)*1.5
                                    if d_bf_min < beadf_dis_control:
                                        beadf_dis_ok += 0
                                    else:
                                        beadf_dis_ok += 1
                                    print("Bead_number_all_last=",str(Bead_num_all_b), \
                                        "  Bead_number_all_temp=",str(Bead_num_all), \
                                        "  Bead_number_dia=",str(bead_dia_num), \
                                        "  Bead_number_now=",str(Bead_num), \
                                        "  Beadf_distance_judge=",str(jud_bf), \
                                        "  Beadf_distance_ok=",str(beadf_dis_ok))
                                    jud_bf += 1
                                    continue
                                jud_Bead = 0
                                while jud_Bead < Bead_num_all:
                                    codi2 = bead_all[jud_Bead]
                                    coordinate1_temp = np.array(bead_all[jud_Bead][0])
                                    bead_height_temp = bead_all[jud_Bead][1]
                                    bead_length_temp = bead_all[jud_Bead][2]
                                    d_b_min = m.dist(bead1[0],coordinate1_temp)
                                    bead_dis_control = (bead1[1] + bead_height_temp)/2 * 1.5
                                    if d_b_min < bead_dis_control:
                                        bead_dis_ok += 0
                                    else:
                                        bead_dis_ok += 1
                                    print("Bead_number_all_last=",str(Bead_num_all_b), \
                                        "  Bead_number_all_temp=",str(Bead_num_all), \
                                        "  Bead_number_dia=",str(bead_dia_num), \
                                        "  Bead_number_now=",str(Bead_num), \
                                        "  Beadf_distance_judge=",str(jud_bf), \
                                        "  Beadf_distance_ok=",str(beadf_dis_ok))
                                    jud_Bead += 1
                                    continue
                                if beadf_dis_ok >= Fiber_num_all and bead_dis_ok >= Bead_num_all:
                                    bead_temp.append(bead1)
                                    bead_dia_num_temp -= 1
                                    SV_bd_temp += 4/3*m.pi*(bead1[1]/2)**2*bead1[2]/2 - m.pi*fiber_dia**2/4*bead_length
                                    bead_ok += 1
                                else:
                                    bead_ok += 0
                                point += 1
                                continue
                            jud_ff = 0                            
                            while jud_ff < Fiber_num_all:
                                codi2 = coordinate_all[jud_ff]
                                coordinate1_temp = np.array(coordinate_all[jud_ff][0])
                                coordinate2_temp = np.array(coordinate_all[jud_ff][1])
                                fiber_dia_temp = coordinate_all[jud_ff][2]
                                r = coordinate1_temp
                                e = coordinate2_temp - coordinate1_temp
                                d_all = []
                                t = 0
                                while t <= 1000:
                                    P = r + t/1000 * e
                                    l = coordinate1 - P
                                    s = np.array(coordinate2) - np.array(coordinate1)
                                    S = np.linalg.norm(s)
                                    d = abs(np.linalg.norm(np.cross(l,s)) / S)
                                    d_all.append(d)
                                    t += 1
                                d_min = min(d_all)
                                fib_dis_control = (fiber_dia/2 + fiber_dia_temp/2)*1.5
                                if d_min < fib_dis_control:
                                    fib_dis_ok += 0
                                else:
                                    fib_dis_ok += 1
                                print("Fiber_number_all_last=",str(Fiber_num_all_b), \
                                    "  Fiber_number_all_temp=",str(Fiber_num_all), \
                                    "  Fiber_number_dia=",str(fiber_dia_num), \
                                    "  Fiber_number_now=",str(Fiber_num), \
                                    "  Fiber_distance_judge=",str(jud_ff), \
                                    "  Fiber_distance_ok=",str(fib_dis_ok))
                                jud_ff += 1
                                continue
                            if fib_dis_ok >= Fiber_num_all and bead_ok >= Points:
                                bead += bead_temp
                                bead_all += bead_temp
                                SV_bd += SV_bd_temp
                                coordinate.append(codi1)
                                coordinate_all.append(codi1)
                                fiber_dia_num_temp -= 1
                                fiber_gen_way.remove(fib_gen_way)
                                windAngle += angle
                                if fib_gen_way == 0:
                                    Fiber_num_01a += 1
                                    SV += ((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**(0.5)*m.pi*fiber_dia**2/4
                                elif fib_gen_way == 1:
                                    Fiber_num_23a += 1
                                    SV += ((x4-x3)**2+(y4-y3)**2+(z4-z3)**2)**(0.5)*m.pi*fiber_dia**2/4
                                elif fib_gen_way == 2:
                                    Fiber_num_03a += 1
                                    SV += ((x4-x1)**2+(y4-y1)**2+(z4-z1)**2)**(0.5)*m.pi*fiber_dia**2/4
                                elif fib_gen_way == 3:
                                    Fiber_num_12a += 1
                                    SV += ((x2-x3)**2+(y2-y3)**2+(z2-z3)**2)**(0.5)*m.pi*fiber_dia**2/4
                                elif fib_gen_way == 4:
                                    Fiber_num_13a += 1
                                    SV += ((x2-x4)**2+(y2-y4)**2+(z2-z4)**2)**(0.5)*m.pi*fiber_dia**2/4
                                else:
                                    Fiber_num_02a += 1
                                    SV += ((x3-x1)**2+(y3-y1)**2+(z3-z1)**2)**(0.5)*m.pi*fiber_dia**2/4
                            else:
                                bead_dia_num_temp += Points
                                i -= 1
                else:
                    i -= 1
                i += 1
                continue
        SVF_judge = SV / zone_volume
        SVFB_judge = SV_bd / zone_volume
        if SVF_down <= SVF_judge <= SVF_up and SVF_down_Bead <= SVFB_judge <= SVF_up_Bead:
            Fiber_num = len(coordinate)
            Bead_num = len(bead)
            SVF = SV / zone_volume
            SVF_bd = SV_bd / zone_volume
            SV_all += SV
            SVF_all = SV_all / zone_volume
            SV_bd_all += SV_bd
            SVF_bd_all = SV_bd_all / zone_volume
            windAngle_all += windAngle
            if Fiber_num == 0:
                windAngle_ave = 0
            else:
                windAngle_ave = str(windAngle / Fiber_num)
            print("SVF_all",round(SVF_all,4),"  Fiber_num_all",Fiber_num_all,"  SVF=",round(SVF,4),"  Fiber_generate=",i,"  Fiber_number=",Fiber_num,"  Bead_number=",Bead_num,"  Bead_num_all",Bead_num_all)
            print(*coordinate)
            print(*bead)
            if fiber_dia_num > 0:
                SVF = str(SVF)
                coordinate_str = '\n'.join(map(str,coordinate))
                file_name = str(str(fiber_dia) + 'nm.txt')
                f = open(file_name,'w')
                f.write("SVF = " + SVF + '\n' + \
                        "WindAngle = " + str(windAngle_ave) + '\n' + \
                        "Fiber_number = " + str(Fiber_num) + '\n' + \
                        "Fiber_number_01 = " + str(Fiber_num_01a) + '\n' + \
                        "Fiber_number_02 = " + str(Fiber_num_02a) + '\n' + \
                        "Fiber_number_03 = " + str(Fiber_num_03a) + '\n' + \
                        "Fiber_number_12 = " + str(Fiber_num_12a) + '\n' + \
                        "Fiber_number_13 = " + str(Fiber_num_13a) + '\n' + \
                        "Fiber_number_23 = " + str(Fiber_num_23a) + '\n' + \
                        coordinate_str)
                f.close()
            if bead_dia_num > 0:
                SVF_bd = str(SVF_bd)
                bead_str = '\n'.join(map(str,bead))
                file_name = str(str(bead_height/2) + 'nm_bd.txt')
                f = open(file_name,'w')
                f.write("SVF_bd = " + SVF_bd + '\n' + \
                        "Bead_number = " + str(Bead_num) + '\n' + \
                        bead_str)
                f.close()
        else:
            j = 0
            Fiber_num_all = len(coordinate_all)
            while j < fiber_dia_num:
                if Fiber_num_all > 0 and Fiber_num_all - j - 1 >= 0:
                    coordinate_all.pop(Fiber_num_all - j - 1)
                j += 1
                continue
            k = 0
            Bead_num_all = len(bead_all)
            while k < bead_dia_num:
                if Bead_num_all > 0 and Bead_num_all - k - 1 >= 0:
                    bead_all.pop(Bead_num_all - k - 1)
                k += 1
                continue
            dia_l -= 1
            bead_l -= 1
            coordinate = []
            bead = []
            windAngle = 0
            windAngle_ave = 0
            fiber_gen_way = [0,1,2,3,4,5]
            i = 0
            Fiber_num = 0
            Fiber_num_01a = 0
            Fiber_num_02a = 0
            Fiber_num_03a = 0
            Fiber_num_12a = 0
            Fiber_num_13a = 0
            Fiber_num_23a = 0
            Bead_num = 0
        dia_l += 1
        bead_l += 1
        continue
Fiber_num_all = len(coordinate_all)
SVF_all = SV_all / zone_volume
Bead_num_all = len(bead_all)
SVF_bd_all = SV_bd_all / zone_volume
if Fiber_num_all == 0:
    windAngle_ave_all = 0
else:
    windAngle_ave_all = int(windAngle_all / Fiber_num_all)
if SVF_control_all_down <= SVF_all <= SVF_control_all_up and SVF_bead_all_down <= SVF_bd_all <= SVF_bead_all_up:
    print("SVF_all=",SVF_all,"  Fiber_number_all=",Fiber_num_all,"  SVF_bd_all=",SVF_bd_all,"  Bead_number_all=",Bead_num_all)
    print(*coordinate_all)
    print(*bead_all)
    print("Congratulations! All the coordinates were generated successfully!")
    SVF_all = str(SVF_all)
    SVF_bd_all = str(SVF_bd_all)
    coordinate_all_str = '\n'.join(map(str,coordinate_all))
    bead_all_str = '\n'.join(map(str,bead_all))
    file_name = str('All.txt')
    f = open(file_name,'w')
    f.write("SVF_all = " + SVF_all + '\n' + \
            "WindAngle = " + str(windAngle_ave_all) + '\n' + \
            "Fiber_number = " + str(Fiber_num_all) + '\n' + \
            coordinate_all_str)
    f.close()
    file_name = str('All_bd.txt')
    f = open(file_name,'w')
    f.write("SVF_bd_all = " + SVF_bd_all + '\n' + \
            "Bead_number = " + str(Bead_num_all) + '\n' + \
            bead_all_str)
    f.close()
else:
    print("SVF_all=",SVF_all," Fiber_number_all=",Fiber_num_all," SVF_bd_all=",SVF_bd_all," Bead_number_all=",Bead_num_all)
    print(*coordinate_all)
    print(*bead_all)
    print("Oops! The current coordinate SVF does not meet the requirements!")
    SVF_all = str(SVF_all)
    SVF_bd_all = str(SVF_bd_all)
    coordinate_all_str = '\n'.join(map(str,coordinate_all))
    bead_all_str = '\n'.join(map(str,bead_all))
    file_name = str('All.txt')
    f = open(file_name,'w')
    f.write("SVF_all = " + SVF_all + '\n' + \
            "WindAngle = " + str(windAngle_ave_all) + '\n' + \
            "Fiber_number = " + str(Fiber_num_all) + '\n' + \
            coordinate_all_str)
    f.close()
    file_name = str('All_bd.txt')
    f = open(file_name,'w')
    f.write("SVF_bd_all = " + SVF_bd_all + '\n' + \
            "Bead_number = " + str(Bead_num_all) + '\n' + \
            bead_all_str)
    f.close()