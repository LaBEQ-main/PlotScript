import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline
from scipy.signal import savgol_filter

def plot_overlay(plist, excurr, resmeas):

    for data in plist:
        file = data[0]
        vars = data[1]
        lbl = data[2]

        xcol = vars[0]
        ycol = vars[1]

        data = pd.read_csv(file, sep = '\t')
        # cleandata = data.drop_duplicates(subset=[xcol])
        x = data[xcol]
        y = data[ycol]

        #set up overlay plot
        # plt.style.use('fivethirtyeight')
        plt.tight_layout()
        plt.xlabel(str(xcol))
        plt.ylabel(str(ycol))
        plt.title(f"Live Overlay")

        if resmeas == True:
            plt.plot(x, y * excurr * np.log(2), linestyle = "None", marker = 'o', markersize = 2.0)
            plt.xlabel("T (K)", fontsize = 18)
            plt.xticks(fontsize = 14)
            plt.ylabel("R (Ω/□)", fontsize = 18)
            plt.yticks(fontsize = 14)
            plt.title(f"{lbl} R vs T", fontsize = 20)
        else:
            plt.plot(x, y, linestyle = "None", marker = 'o', label = lbl)
            plt.legend(loc='best')
    
    plt.tight_layout()
    plt.show()

def plot_overlay_bf(plist):

    for data in plist:
        file = data[0]
        vars = data[1]
        lbl = data[2]
        data = pd.read_csv(file, sep = '\t')
        xcol = vars[0]
        ycol = vars[1]
        x = data[xcol]
        y = data[ycol]

        # Calculating parameters (theta0, theta1 and theta2)
        # of the 2nd degree curve using the numpy.polyfit() function
        theta = np.polyfit(x, y, 4)

        print(f'The parameters of the curve: {theta}')

        # Now, calculating the y-axis values against x-values according to
        # the parameters theta0, theta1 and theta2
        y_line = theta[4] + theta[3] * pow(x, 1) + theta[2] * pow(x, 2) + theta[1] * pow(x, 3) + theta[0] * pow(x, 4)

        #set up overlay plot
        plt.style.use('fivethirtyeight')
        plt.tight_layout()
        plt.xlabel(str(xcol))
        plt.ylabel(str(ycol))
        plt.title(f"Live Overlay")
        plt.plot(x, y_line, label = lbl, )
        plt.legend(loc='best')
    plt.show()

def plot_overlay_savgol(plist, excurr):
    #plot data using Savitzky Golay filter

    for data in plist:
        file = data[0]
        vars = data[1]
        lbl = data[2]
        xcol = vars[0]
        ycol = vars[1]

        #get data from file, drop duplicates and sort i.e. clean the data
        data = pd.read_csv(file, sep = '\t')
        x = data[xcol].to_numpy()
        y = data[ycol].to_numpy()
        cleandata = data.drop_duplicates(subset=[xcol]).sort_values(by=[xcol])
        cx = cleandata[xcol].to_numpy()
        cy = cleandata[ycol].to_numpy()

        # #test if x is 1D and sorted with no duplicates
        # print(cx.ndim)
        # print(np.any(cx[1:] <= x[:-1]))
        
        #calculate savgol filtered yaxis data
        yhat = savgol_filter(cy, 151, 3) # window size 51, polynomial order 3

        #set up overlay plot
        # plt.style.use('fivethirtyeight')
        plt.tight_layout()
        plt.xlabel('T (K)', fontsize=18)
        plt.ylabel('R (Ω)', fontsize=18)
        # plt.title(f"Normalized R vs T")
        # plt.plot(x,y, label = lbl, marker = 'o', linestyle = 'None')
        plt.plot(cx, yhat * excurr * np.log(2), linewidth = 3.0) #,label = lbl)
        # plt.legend(loc='best')

        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)

    plt.show()

def plot_overlay_polyfit(plist):
    #plot data using Savitzky Golay filter

    for data in plist:
        file = data[0]
        vars = data[1]
        lbl = data[2]
        xcol = vars[0]
        ycol = vars[1]

        #get data from file, drop duplicates and sort i.e. clean the data
        data = pd.read_csv(file, sep = '\t')
        x = data[xcol].to_numpy()
        y = data[ycol].to_numpy()
        cleandata = data.drop_duplicates(subset=[xcol]).sort_values(by=[xcol])
        cx = cleandata[xcol].to_numpy()
        cy = cleandata[ycol].to_numpy()

        poly = np.polyfit(cx,cy,9)
        poly_y = np.poly1d(poly)(cx)

        #set up overlay plot
        # plt.style.use('fivethirtyeight')
        plt.tight_layout()
        plt.xlabel(str(xcol))
        plt.ylabel(str(ycol))
        plt.title(f"Overlay")
        plt.plot(x,y, label = lbl, marker = 'o', linestyle = 'None')
        plt.plot(cx,poly_y, label = lbl)
        plt.legend(loc='best')
    plt.show()



plotlist = [
                # ['C:\\Users\\2administrator\\exopy\\measurement\\saved_measurements\\06292022_A025_A026_CoolDown\\CoolDownData_2.txt',('vti temp (K)', 'res'), "A025"],
                # ['C:\\Users\\2administrator\\exopy\\measurement\\saved_measurements\\06302022_A025_A026_ProbeHeating\\probeheat_data.txt',('vti temp (K)', 'res'), "A025"],
                # ['C:\\Users\\2administrator\\exopy\measurement\\saved_measurements\\06302022_A026_A027_ProbeHeating\\probeheat_data.txt', ('vti temp (K)', 'NF res'), "A026"],
                # ['C:\\Users\\2administrator\\exopy\measurement\\saved_measurements\\09212022_A027\\003 -Warm Up 5K to 10K\\5Kto10K_data.txt', ('he3 pot temp (K)', 'NF R (uV)'), "NF"],
                # ['C:\\Users\\2administrator\\exopy\measurement\\saved_measurements\\09212022_A027\\001\\Heliox_cooldown_data_3.txt', ('time (s)', 'he3 pot temp (K)'), "pot"],
                # ['C:\\Users\\2administrator\\exopy\measurement\\saved_measurements\\09212022_A027\\001\\Heliox_cooldown_data_3.txt', ('time (s)', 'he3 sorb temp (K)'), "sorb"],
                # ['C:\\Users\\2administrator\\exopy\measurement\\saved_measurements\\09212022_A027\\001\\Heliox_cooldown_data_3.txt', ('time (s)', 'vti temp (K)'), "vti"],
                # ['C:\\Users\\2administrator\\exopy\measurement\\saved_measurements\\09212022_A027\\003\\5Kto10K_data.txt', ('time (s)', 'he3 pot temp (K)'), "pot"],
                # ['C:\\Users\\2administrator\\exopy\measurement\\saved_measurements\\09292022_NbSnWire_AuWire_AuOnGlass_Ta\\001\\data_cooldown_2.txt', ('time (s)', 'he3 pot temp (K)'), "pot"],
                # ['C:\\Users\\2administrator\\exopy\measurement\\saved_measurements\\09292022_NbSnWire_AuWire_AuOnGlass_Ta\\001\\data_cooldown_2.txt', ('time (s)', 'he3 sorb temp (K)'), "sorb"],
                # ['C:\\Users\\2administrator\\exopy\measurement\\saved_measurements\\09292022_NbSnWire_AuWire_AuOnGlass_Ta\\001\\data_cooldown_2.txt', ('time (s)', 'vti temp (K)'), "vti"],
                # ['C:\\Users\\2administrator\\exopy\measurement\\saved_measurements\\09292022_NbSnWire_AuWire_AuOnGlass_Ta\\001\\data_cooldown.txt', ('time (s)', 'he3 pot temp (K)'), "pot"],
                # ['C:\\Users\\2administrator\\exopy\measurement\\saved_measurements\\09292022_NbSnWire_AuWire_AuOnGlass_Ta\\001\\data_cooldown.txt', ('time (s)', 'he3 sorb temp (K)'), "sorb"],
                # ['C:\\Users\\2administrator\\exopy\\measurement\\saved_measurements\\HelioxTesting\\10052022 base temp and hold time testing - VTI pumped and -0.9mbar to VTI\\2nd regen\\data_regen_10052022_0200PM.txt', ('time (s)', 'he3 pot temp (K)'), "pot"],
                # ['C:\\Users\\2administrator\\exopy\\measurement\\saved_measurements\\HelioxTesting\\10052022 base temp and hold time testing - VTI pumped and -0.9mbar to VTI\\2nd regen\\data_regen_10052022_0200PM.txt', ('time (s)', 'he3 sorb temp (K)'), "sorb"],
                # ['C:\\Users\\2administrator\\exopy\\measurement\\saved_measurements\\HelioxTesting\\10052022 base temp and hold time testing - VTI pumped and -0.9mbar to VTI\\2nd regen\\data_regen_10052022_0200PM.txt', ('time (s)', 'vti temp (K)'), "vti"],
                # ['C:\\Users\\2administrator\\exopy\\measurement\\saved_measurements\HelioxTesting\\100720022 no PCB or copper rods\\Regeneration vti at -900mbar\\data_regen_10082022_1230PM.txt', ('time (s)', 'he3 pot temp (K)'), "pot"],
                # ['C:\\Users\\2administrator\\exopy\\measurement\\saved_measurements\HelioxTesting\\100720022 no PCB or copper rods\\Regeneration vti at -900mbar\\data_regen_10082022_1230PM.txt', ('time (s)', 'he3 sorb temp (K)'), "sorb"],
                # ['C:\\Users\\2administrator\\exopy\\measurement\\saved_measurements\HelioxTesting\\100720022 no PCB or copper rods\\Regeneration vti at -900mbar\\data_regen_10082022_1230PM.txt', ('time (s)', 'vti temp (K)'), "vti"],
                # ['C:\\Users\\2administrator\\exopy\\measurement\\saved_measurements\HelioxTesting\\100720022 no PCB or copper rods\\6th Regen\\data_regen_10102022_0530PM.txt', ('time (s)', 'he3 pot temp (K)'), "pot"],
                # ['C:\\Users\\2administrator\\exopy\\measurement\\saved_measurements\HelioxTesting\\100720022 no PCB or copper rods\\6th Regen\\data_regen_10102022_0530PM.txt', ('time (s)', 'he3 sorb temp (K)'), "sorb"],
                # ['C:\\Users\\2administrator\\exopy\\measurement\\saved_measurements\HelioxTesting\\100720022 no PCB or copper rods\\6th Regen\\data_regen_10102022_0530PM.txt', ('time (s)', 'vti temp (K)'), "vti"],
                # ['C:\\Users\\2administrator\\exopy\\measurement\\saved_measurements\HelioxTesting\\100720022 no PCB or copper rods\\6th Regen\\data_regen_10102022_0530PM.txt', ('time (s)', 'vti pres (mbar)'), "vti pres"],
                # ['C:\\Users\\2administrator\\exopy\\measurement\\saved_measurements\HelioxTesting\\10132022 Heliox removed, STD probe loaded\\data_10132022_test1.txt', ('time (s)', 'vti perc (%)'), "test1 %"],
                # ['C:\\Users\\2administrator\\exopy\\measurement\\saved_measurements\HelioxTesting\\10132022 Heliox removed, STD probe loaded\\data_10132022_test1.txt', ('time (s)', 'vti pres (mbar)'), "test1 mbar"],
                # ['C:\\Users\\2administrator\\exopy\\measurement\\saved_measurements\HelioxTesting\\10132022 Heliox removed, STD probe loaded\\data_10132022_test2.txt', ('time (s)', 'vti perc (%)'), "test2 %"],
                # ['C:\\Users\\2administrator\\exopy\\measurement\\saved_measurements\HelioxTesting\\10132022 Heliox removed, STD probe loaded\\data_10132022_test2.txt', ('time (s)', 'vti pres (mbar)'), "test2 mbar"],
                # ['C:\\Users\\2administrator\\exopy\\measurement\\saved_measurements\HelioxTesting\\10132022 Heliox removed, STD probe loaded\\data_10132022_test3.txt', ('time (s)', 'vti perc (%)'), "test3 %"],
                # ['C:\\Users\\2administrator\\exopy\\measurement\\saved_measurements\HelioxTesting\\10132022 Heliox removed, STD probe loaded\\data_10132022_test3.txt', ('time (s)', 'vti pres (mbar)'), "test3 mbar"],
                # ['C:\\Users\\2administrator\\exopy\\measurement\\saved_measurements\HelioxTesting\\10132022 Heliox removed, STD probe loaded\\data_10132022_test4.txt', ('time (s)', 'vti perc (%)'), "test4 %"],
                # ['C:\\Users\\2administrator\\exopy\\measurement\\saved_measurements\HelioxTesting\\10132022 Heliox removed, STD probe loaded\\data_10132022_test4.txt', ('time (s)', 'vti pres (mbar)'), "test4 mbar"],
                ['C:\\Users\\2administrator\\exopy\\measurement\\saved_measurements\\2022_10_20_NCSTATE_A049_A050_A092\\003 - Controlled Warm\\2022_10_28_0200PM_cwarm.txt', ('probe temp (K)', 'PG1 res'), "A092"],
                # ['C:\\Users\\2administrator\\exopy\\measurement\\saved_measurements\\2022_11_11_NCSU_A093_A069_A081\\002\\002_Data.txt', ('probe temp (K)', 'NF res'), "A093"],
            ]

excurr = 0.001
resmeas = True
plot_overlay(plotlist, excurr, resmeas)
# plot_overlay_bf(plotlist)
# plot_overlay_savgol(plotlist, excurr)
# plot_overlay_polyfit(plotlist)