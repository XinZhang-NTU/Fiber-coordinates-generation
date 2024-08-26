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
        ## Fiber diameters
        fib_dia = [465, 435, 405, 375, 345, 315, 285, 255, 225, 195, 165, 135, 105, 75, 45, 15]
        if Fib_zone == 2:
            ## Fiber diameter number distribution
            fib_dia_fra = [0.0033, 0.0000, 0.0000, 0.0000, 0.0000, 0.0033, 0.0016, 0.0341, 0.0927, 0.2813, 0.3545, 0.0927, 0.0146, 0.0293, 0.0846, 0.0081]
        leng = len(fib_dia) # Number of fiber diameters
        l = 0
        while l < leng:
            fib_dia_number = [fib_dia[l], round(self.Fib_num_set * fib_dia_fra[l])] # Number of fibers generated for this diameter
            fib_num_dis.append(fib_dia_number) # Fiber number corresponding to each diameter
            l += 1
            continue
        return fib_num_dis
    
    ### The following code outputs the fiber SVF distribution corresponding to each fiber diameter
    def fib_svf_dis(self):
        fib_svf_dis = []
        fib_dia = []
        fib_dia_svf = []        
        ## Fiber diameters
        fib_dia = [465, 435, 405, 375, 345, 315, 285, 255, 225, 195, 165, 135, 105, 75, 45, 15]
        if Fib_zone == 2:
            ## Fiber diameter SVF distribution
            fib_dia_svf = [0.0230, 0.0000, 0.0000, 0.0000, 0.0000, 0.0105, 0.0043, 0.0725, 0.1533, 0.3495, 0.3153, 0.0552, 0.0053, 0.0054, 0.0056, 0.0001]
        leng = len(fib_dia) # Number of fiber diameters
        l = 0
        while l < leng:
            fib_dia_fraction = [fib_dia[l], fib_dia_svf[l]] # SVF for this diameter
            fib_svf_dis.append(fib_dia_fraction) # Fiber SVF distribution corresponding to each diameter
            l += 1
            continue
        return fib_svf_dis













































### The following code set the initial value for the variables
coordinate_all = []            # All the coordinates including fibers and beads
SV_all = 0                     # All the solid part volume including fibers and beads
SVF_all = 0                    # Total SVF including fibers and beads
windAngle_all = 0              # Summary of all the fibers wind angles
windAngle_ave_all = 0          # Average of all the fibers wind angles
Fiber_num_all = 0              # Number of all the fibers
zone_volume = 9000*9000*9000   # Fiber zone volume with unit of nm

### The following code set the values of structure control parameters
SVF_control_all = 0.0184       # Total SVF of the filter media including fibers and beads, this value can not be zero
SVF_control_factor = 0.05      # Control precision of the total SVF
Fib_num_set = 72               # Estimated total fiber numbers to generate
Fib_zone = 2                   # Fiber generation zone, don't have specific meaning for this case, keep it as 2
angle_control = 85             # Control value of wind angle for each fiber
SVF_control_all_down = (1 - SVF_control_factor)*SVF_control_all # Control range of the total SVF
SVF_control_all_up   = (1 + SVF_control_factor)*SVF_control_all # Control range of the total SVF

### The following code outputs the fiber number distribution and SVF distribution
Fiber_num_distribution_temp = Fiber_num_distribution(Fib_num_set,Fib_zone)
Fiber_num_dis = Fiber_num_distribution_temp.fib_num_dis()
Fiber_svf_dis = Fiber_num_distribution_temp.fib_svf_dis()
dia_length = len(Fiber_num_dis)  # Total number of diameters
dia_l = 0                        # Control value of the diamenter numbers
layer_gap = 0                    # Control value of the distance between fibers and the simulation zone boundary

### The following code outputs all the fibers' and beads' coordinates
if SVF_all < SVF_control_all:
    ### The following loop outputs all the coordinates for each fiber diameter
    while dia_l < dia_length:  # dia_l means the current number of fiber diameters
        ### The following code defined the control paramenters for the current fiber diameter
        SVF_control = 0                                                 # SVF control value for the current diameter
        fiber_dia = Fiber_num_dis[dia_l][0]                             # Current fiber diameter
        layer_gap = int(2 * fiber_dia / 2 / 2**0.5)                     # Gap control value for the current diameter
        fiber_dia_num = int(Fiber_num_dis[dia_l][1])                    # Number of fibers to generate for current diameter
        fiber_dia_svf = float(Fiber_svf_dis[dia_l][1]*SVF_control_all)  # SVF of the fibers for current diameter
        SVF_control = fiber_dia_svf
        SVF_down = 0.8*SVF_control                                      # SVF control range for current diameter
        SVF_up = 1.2*SVF_control
        
        ### Initial value of the paramenters for the current diameter
        SV = 0
        SVF = 0
        coordinate = []
        windAngle = 0
        windAngle_ave = 0
        fiber_gen_way = [0,1,2,3,4,5] # Fiber generate methods
        i = 0
        Fiber_num = 0                 # Number of fibers generated for the current diameter
        Fiber_num_01a = 0             # Number of fibers generated for the current diameter with method 0
        Fiber_num_02a = 0             # Number of fibers generated for the current diameter with method 1
        Fiber_num_03a = 0             # Number of fibers generated for the current diameter with method 2
        Fiber_num_12a = 0             # Number of fibers generated for the current diameter with method 3
        Fiber_num_13a = 0             # Number of fibers generated for the current diameter with method 4
        Fiber_num_23a = 0             # Number of fibers generated for the current diameter with method 5
        Fiber_num_all = len(coordinate_all)
        Fiber_num_all_b = Fiber_num_all       # Backup of the number of fibers generated until last diameter
        SVF_judge = SV / zone_volume

        ### The following code outputs the fibers' and beads' coordinates for current diameter
        if SVF_judge <= SVF_control:

            ### If the current diameter has no fibers to generate, then jump to next diameter
            if SVF_control == 0 or fiber_dia_num == 0:
                print("Current diameter: ", str(fiber_dia), "nm. No fibers are needed to generate!")
                dia_l += 1
            
            ### The following code generate all the fibers' coordinates for current diameter, each loop generate one fiber's coornates
            while i < fiber_dia_num:
                
                ### Initial value of the paramenters for current fiber
                angle = 0
                codi1 = []
                codi2 = []
                Fiber_num = len(coordinate)                             # Number of fibers generated of the current diameter
                Fiber_num_all = len(coordinate_all)                     # Total number of fibers generated
                
                ### The following code outputs a randomly selected fiber generation method without repetition.
                ### Once fewer than one method remains, all methods will be reset.
                if len(fiber_gen_way) == 0 or len(fiber_gen_way) == 1:
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
                    fib_dis_ok = 0  # The number of fibers meet the requirements
                    
                    ### The first fiber was added to the coordinates list without judgement
                    if Fiber_num_all == 0:
                        coordinate.append(codi1)           # Add the generated coordinates to the list of this diameter
                        coordinate_all.append(codi1)       # Add the generated coordinates to the list of all fibers
                        fiber_gen_way.remove(fib_gen_way)  # If one generate method was used, it will be removed from the methods list
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
                        print("Fiber_number_all_last = ",str(Fiber_num_all_b), \
                                "  fiber_number_all_temp = ",str(Fiber_num_all), \
                                "  fiber_number_dia = ",str(fiber_dia_num), \
                                "  fiber_number_now = ",str(Fiber_num), \
                                "  fiber_distance_judge = ",str(0), \
                                "  fiber_distance_ok = ",str(fib_dis_ok))
                        
                    ### The other fibers were judged before being added to the coordinates list.
                    ### The judgement primarily focuses on the fiber distance to ensure mesh quality.
                    else:
                        jud = 0
                        while jud < Fiber_num_all:
                            codi2 = coordinate_all[jud]
                            coordinate1_temp = np.array(coordinate_all[jud][0])
                            coordinate2_temp = np.array(coordinate_all[jud][1])
                            fiber_dia_temp = coordinate_all[jud][2]
                            
                            ### The following code outputs the fiber distance
                            r = coordinate1_temp
                            e = coordinate2_temp - coordinate1_temp
                            d_all = []
                            t = 0
                            while t <= 1000:          # The calculation resolution of the fiber distance
                                P = r + t/1000 * e
                                l = coordinate1 - P
                                s = np.array(coordinate2) - np.array(coordinate1)
                                S = np.linalg.norm(s)
                                d = abs(np.linalg.norm(np.cross(l,s)) / S)
                                d_all.append(d)
                                t += 1
                            d_min = min(d_all)        # Fiber distance

                            ### The following code set the ccontrol range, judge the fiber distance and pint the information of the current fiber
                            fib_dis_control = (fiber_dia/2 + fiber_dia_temp/2)*1.5
                            if d_min < fib_dis_control:
                                fib_dis_ok += 0
                            else:
                                fib_dis_ok += 1                            
                            print("fiber_number_all_last=",str(Fiber_num_all_b), \
                                "  fiber_number_all_temp=",str(Fiber_num_all), \
                                "  fiber_number_dia=",str(fiber_dia_num), \
                                "  fiber_number_now=",str(Fiber_num), \
                                "  fiber_distance_judge=",str(jud), \
                                "  fiber_distance_ok=",str(fib_dis_ok))
                            jud += 1
                            continue
                        
                        ### The following code adds suitable fiber coordinates to the list
                        ### If they don't meet the criteria, the code generates the next set of fiber coordinates.
                        if fib_dis_ok >= Fiber_num_all:                                
                            coordinate.append(codi1)
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
                else:
                    i-= 1
                i+=1
                continue
        
        ### The following code judge the fiber SVF of current diameter
        ### If the SVF meet the control range, jump to next diameter
        ### If the SVF don't meet the control range, restart the fiber generation of current diameter
        SVF_judge = SV / zone_volume
        if SVF_down <= SVF_judge <= SVF_up:
            Fiber_num = len(coordinate)
            SVF = SV / zone_volume
            SV_all += SV
            SVF_all = SV_all / zone_volume           
            windAngle_all += windAngle
            if Fiber_num == 0:
                windAngle_ave = 0
            else:
                windAngle_ave = str(windAngle / Fiber_num)
            print("SVF_all = ",round(SVF_all,4),"  Fiber_num_all = ",Fiber_num_all," SVF = ",round(SVF,4),"  Fiber_generate = ",i,"  Fiber_number = ",Fiber_num)
            print(*coordinate)
            
            ### The following code outputs the coordinates of current diameter to a .txt file
            SVF = str(SVF)
            coordinate_str = '\n'.join(map(str,coordinate))
            file_name = str(str(fiber_dia) + 'nm.txt')
            f = open(file_name,'w')
            f.write("SVF = " + SVF + '\n' + \
                    "windAngle = " + str(windAngle_ave) + '\n' + \
                    "Fiber_number = " + str(Fiber_num) + '\n' + \
                    "Fiber_number_01 = " + str(Fiber_num_01a) + '\n' + \
                    "Fiber_number_02 = " + str(Fiber_num_02a) + '\n' + \
                    "Fiber_number_03 = " + str(Fiber_num_03a) + '\n' + \
                    "Fiber_number_12 = " + str(Fiber_num_12a) + '\n' + \
                    "Fiber_number_13 = " + str(Fiber_num_13a) + '\n' + \
                    "Fiber_number_23 = " + str(Fiber_num_23a) + '\n' + \
                    coordinate_str)
            f.close()                
        else:

            ### The following code initializes the parameters used for generating new fibers
            j = 0
            Fiber_num_all = len(coordinate_all)
            while j < fiber_dia_num:
                coordinate_all.pop(Fiber_num_all - j - 1)
                j += 1
                continue
            dia_l -= 1
            coordinate = []
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
        dia_l += 1
        continue

### The following code checks all the generated fibers
### If they meet the requirements, all the coordinates will be output to a .txt file
### If they do not meet the requirements, the fiber generation process will stop, and a manual restart will be needed to initiate a new generation process
Fiber_num_all = len(coordinate_all)
SVF_all = SV_all / zone_volume
if Fiber_num_all == 0:
    windAngle_ave_all = 0
else:
    windAngle_ave_all = int(windAngle_all / Fiber_num_all)
if SVF_control_all_down <= SVF_all <= SVF_control_all_up:
    print(" SVF_all=",SVF_all," fiber_number_all=",Fiber_num_all)
    print(*coordinate_all)
    print("Congratulations! All the coordinates were generated successfully!")
    SVF_all = str(SVF_all)
    coordinate_all_str = '\n'.join(map(str,coordinate_all))
    file_name = str('All.txt')
    f = open(file_name,'w')
    f.write("SVF_all = " + SVF_all + '\n' + \
            "windAngle = " + str(windAngle_ave_all) + '\n' + \
            "Fiber_number = " + str(Fiber_num_all) + '\n' + \
            coordinate_all_str)
    f.close()
else:
    print(" SVF_all=",SVF_all," fiber_number_all=",Fiber_num_all)
    print(*coordinate_all)
    print("Oops! The current coordinate SVF does not meet the requirements!")
    SVF_all = str(SVF_all)
    coordinate_all_str = '\n'.join(map(str,coordinate_all))
    file_name = str('All.txt')
    f = open(file_name,'w')
    f.write("SVF_all = " + SVF_all + '\n' + \
            "windAngle = " + str(windAngle_ave_all) + '\n' + \
            "Fiber_number = " + str(Fiber_num_all) + '\n' + \
            coordinate_all_str)
    f.close()