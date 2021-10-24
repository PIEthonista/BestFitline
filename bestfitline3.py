def best_fit_line():
    word = ""
    path = "Entered by hand."

    def lines():
        print("------------------------------------------------")

    def linel():
        print("--------------------------------------------------------------------------")

    def end():
        print("")

    def emp1():
        print(" ", end="", flush=True)

    def blank():
        end()
        linel()
        end()

    def heading():
        print("The analysed data are as below:")
        linel()

    def bell():
        print("\a")

    print("-------------------------------------------------------------------------------------------------------------")
    print("This calculator can generate the equation of the linear trend line for multiple coordinates (x,y) entered.")
    print("Please input coordinates directly from a local text file (.txt). ")
    print("")
    print("1. The text file should only contain coordinates in the form below.")
    print("   --> (X,Y) or [X,Y] or {X,Y} or X,Y ")
    print("2. To predict values using the input data, replace EITHER ONE of X or Y with any of the below.")
    print("   --> \"unknown\" or any alphabetical text, but not alphanumerical.")
    print("3. Any other text not included in the above forms will be omitted.")
    print("")
    print("Press any key to start.")
    option = input("")

    xval = []
    yval = []
    xuk = []
    yuk = []

    print("----------------------------------------------------------------------------")
    print("Enter the path and file name of the text file below:")
    print("")
    while True:
        path = input(">>> ")
        oldpath = path
        try:
            file = open(path,"r")
            break
        except:
            bell()
            print("Error: Couldn't find path or invalid file name. Please re-enter.")
            print("----------------------------------------------------------------")
            continue

    import re
    import matplotlib.pyplot as plt
    import numpy as np            #code for plot at tag: mpl

    for line in file:
        line = line.strip()
        match = re.findall("\[?\{?\(?\s*(-?\+?[a-zA-Z0-9]+\.?[a-zA-Z0-9]*\s*,+\s*-?\+?[a-zA-Z0-9]+\.?[a-zA-Z0-9]*)\s*\)?\[?\{?", line)
        if len(match) > 0:
            for item in match:
                comma = item.find(",")
                vx = item[:comma].strip().lower()
                vy = item[comma+1:].strip().lower()
                try:
                    fx = float(vx)
                except:
                    fx = "uk"
                try:
                    fy = float(vy)
                except:
                    fy = "uk"
                if fx != "uk" and fy != "uk":
                    xval.append(fx)
                    yval.append(fy)
                elif fx == "uk" and fy != "uk":
                    yuk.append(fy)
                elif fx != "uk" and fy == "uk":
                    xuk.append(fx)
                elif fx == "uk" and fy == "uk":
                    continue


    if len(xval) == len(yval):
        xuk = sorted(xuk)
        yuk = sorted(yuk)
        srt = list(zip(*sorted(zip(xval, yval))))
        for i in srt[0]:
            xval.remove(i)
        for i in srt[1]:
            yval.remove(i)

        for i in srt[0]:
            xval.append(i)
        for i in srt[1]:
            yval.append(i)

        mx = sum(xval) / len(xval)
        my = sum(yval) / len(yval)
        A = []
        B = []
        C = []
        AS = []
        YCAL = []
        YDIF = []
        YPER = []
        total = 0
        equal = 0
        bigger = 0
        smaller = 0
        for i in xval:
            A.append(i - mx)
        for i in yval:
            B.append(i - my)
        for i in range(len(A)):
            C.append(A[i]*B[i])
        for i in A:
            AS.append(i*i)
        grad = sum(C) / sum(AS)
        yint = my - grad*mx
        xint = -(yint / grad)

        def eqn(x):
            return grad*x + yint

        for i in xval:
            YCAL.append(eqn(i))

        for i in range(len(YCAL)):
            YDIF.append(yval[i] - YCAL[i])

        for i in range(len(YDIF)):
            YPER.append(abs((yval[i] - YCAL[i])/YCAL[i])*100)

        heading()
        word = word + "The analysed data are as below:\n----------------------------------------------------------------------------------------\n"
        end()
        word = word + "\n"

        cw_x = max(len(str(item)) for item in xval) + 1
        cw_y = max(len(str(item)) for item in yval) + 1
        cw_yc = max(len(str(item)) for item in YCAL) + 1
        cw_ydif = max(len(str(item)) for item in YDIF)
        if cw_ydif > 15:
            cw_yd = cw_ydif
        elif cw_ydif <= 15:
            cw_yd = 15

        print("  Input (I)", end="", flush=True)
        word = word + "  Input (I)"
        xygap1 = cw_x + cw_y - 2
        xynum1 = 0
        while xynum1 < xygap1:
            emp1()
            word = word + " "
            xynum1 = xynum1 + 1
        print("  Fitted (F)", end="", flush=True)
        word = word + "  Fitted (F)"
        xygap2 = cw_x + cw_yc - 7
        xynum2 = 0
        while xynum2 < xygap2:
            emp1()
            word = word + " "
            xynum2 = xynum2 + 1
        print("    Comparison   Error (IY - FY)", end="", flush=True)
        word = word + "    Comparison   Error (IY - FY)"
        ydgap = cw_yd - 13
        for i in range(ydgap):
            emp1()
            word = word + " "
        print("  Percentage Error (%)")
        word = word + "  Percentage Error (%)\n"

        print("  X", end="", flush=True)
        word = word + "  X"
        xgap1 = cw_x + 1
        xnum1 = 0
        while xnum1 < xgap1:
            emp1()
            word = word + " "
            xnum1 = xnum1 + 1
        print("Y", end="", flush=True)
        word = word + "Y"
        ygap1 = cw_y + 4
        ynum1 = 0
        while ynum1 < ygap1:
            emp1()
            word = word + " "
            ynum1 = ynum1 + 1
        print("  X", end="", flush=True)
        word = word + "  X"
        xgap2 = cw_x + 1
        xnum2 = 0
        while xnum2 < xgap2:
            emp1()
            word = word + " "
            xnum2 = xnum2 + 1
        print("Y", end="", flush=True)
        word = word + "Y"
        ygap1 = cw_y + 4
        ynum1 = 0
        while ynum1 < ygap1:
            emp1()
            word = word + " "
            ynum1 = ynum1 + 1
        print("")
        word = word + "\n"

        num = 0
        while num < len(xval):
            print("( " + str(xval[num]), end="", flush=True)
            word = word + "( " + str(xval[num])
            xgap = cw_x - len(str(xval[num]))
            xnum = 0
            while xnum < xgap:
                emp1()
                word = word + " "
                xnum = xnum + 1
            print(", " + str(yval[num]), end="", flush=True)
            word = word + ", " + str(yval[num])
            ygap = cw_y - len(str(yval[num]))
            ynum = 0
            while ynum < ygap:
                emp1()
                word = word + " "
                ynum = ynum + 1
            print(")    ( " + str(xval[num]), end="", flush=True)
            word = word + ")    ( " + str(xval[num])
            x2gap = cw_x - len(str(xval[num]))
            x2num = 0
            while x2num < x2gap:
                emp1()
                word = word + " "
                x2num = x2num + 1
            print(", " + str(YCAL[num]), end="", flush=True)
            word = word + ", " + str(YCAL[num])
            ycgap = cw_yc - len(str(YCAL[num]))
            ycnum = 0
            while ycnum < ycgap:
                emp1()
                word = word + " "
                ycnum = ycnum + 1
            print(")    [IY ", end="", flush=True)
            word = word + ")    [IY "
            if yval[num] > YCAL[num]:
                print("> FY]    ", end="", flush=True)
                word = word + "> FY]    "
                bigger = bigger + 1
            elif yval[num] == YCAL[num]:
                print("= FY]*   ", end="", flush=True)
                word = word + "= FY]*   "
                equal = equal + 1
            elif yval[num] < YCAL[num]:
                print("< FY]    ", end="", flush=True)
                word = word + "< FY]    "
                smaller = smaller + 1
            print(str(YDIF[num]), end="", flush=True)
            word = word + str(YDIF[num])
            ydgap = cw_yd - len(str(YDIF[num]))
            for i in range(ydgap):
                emp1()
                word = word + " "
            print("    " + str(YPER[num]))
            word = word + "    " + str(YPER[num]) + "\n"
            total = total + 1
            num = num + 1
        end()
        word = word + "\n"

        if smaller == 0:
            print("[IY < FY]  : 0/" + str(total) + " (0%)")
            word = word + "[IY < FY]  : 0/" + str(total) + " (0%)\n"
        elif smaller != 0:
            print("[IY < FY]  : " + str(smaller) + "/" + str(total) + " (" + str((smaller/total)*100) + "%)")
            word = word + "[IY < FY]  : " + str(smaller) + "/" + str(total) + " (" + str((smaller/total)*100) + "%)\n"

        if bigger == 0:
            print("[IY > FY]  : 0/" + str(total) + " (0%)")
            word = word + "[IY > FY]  : 0/" + str(total) + " (0%)\n"
        elif bigger != 0:
            print("[IY > FY]  : " + str(bigger) + "/" + str(total) + " (" + str((bigger/total)*100) + "%)")
            word = word + "[IY > FY]  : " + str(bigger) + "/" + str(total) + " (" + str((bigger/total)*100) + "%)\n"

        if equal == 0:
            print("[IY = FY]* : 0/" + str(total) + " (0%)", end="", flush=True)
            word = word + "[IY = FY]* : 0/" + str(total) + " (0%)\n"
        elif equal != 0:
            print("[IY = FY]* : " + str(equal) + "/" + str(total) + " (" + str((equal/total)*100) + "%)", end="", flush=True)
            word = word + "[IY = FY]* : " + str(equal) + "/" + str(total) + " (" + str((equal/total)*100) + "%)\n"

        blank()
        word = word + "----------------------------------------------------------------------------------------" + "\n" + "\n"
        if len(xuk) != 0 or len(yuk) != 0:
            xcaluk = []
            ycaluk = []
            for i in xuk:
                ycaluk.append((grad*i) + yint)
            for i in yuk:
                xcaluk.append((i - yint)/grad)

            if len(xuk) == 1:
                cw_xuk = len(str(xuk[0])) + 1
            elif len(xuk) != 1 and len(xuk) != 0:
                cw_xuk = max(len(str(item)) for item in xuk) + 1

            if len(yuk) == 1:
                cw_yuk = len(str(yuk[0])) + 1
            elif len(yuk) != 1 and len(yuk) != 0:
                cw_yuk = max(len(str(item)) for item in yuk) + 1

            if len(xcaluk) == 1:
                cw_xcaluk = len(str(xcaluk[0])) + 1
            elif len(xcaluk) != 1 and len(xcaluk) != 0:
                cw_xcaluk = max(len(str(item)) for item in xcaluk) + 1

            if len(ycaluk) == 1:
                cw_ycaluk = len(str(ycaluk[0])) + 1
            elif len(ycaluk) != 1 and len(ycaluk) != 0:
                cw_ycaluk = max(len(str(item)) for item in ycaluk) + 1

            if len(yuk) != 0:       #~!yuk -> xcaluk
                num = 0
                print("Calculated X Unknowns:")
                word = word + "Calculated X Unknowns:\n"
                while num < len(yuk):
                    print("( " + str(xcaluk[num]), end="", flush=True)
                    word = word + "( " + str(xcaluk[num])
                    xcalukgap = cw_xcaluk - len(str(xcaluk[num]))
                    xnum = 0
                    while xnum < xcalukgap:
                        emp1()
                        word = word + " "
                        xnum = xnum + 1
                    print(", " + str(yuk[num]), end="", flush=True)
                    word = word + ", " + str(yuk[num])
                    yukgap = cw_yuk - len(str(yuk[num]))
                    ynum = 0
                    while ynum < yukgap:
                        emp1()
                        word = word + " "
                        ynum = ynum + 1
                    print(")")
                    word = word + ")\n"
                    num = num + 1
                end()
                word = word + "\n"
            if len(xuk) != 0:            #~!xuk -> ycaluk
                print("Calculated Y Unknowns:")
                word = word + "Calculated Y Unknowns:\n"
                num = 0
                while num < len(xuk):
                    print("( " + str(xuk[num]), end="", flush=True)
                    word = word + "( " + str(xuk[num])
                    xukgap = cw_xuk - len(str(xuk[num]))
                    xnum = 0
                    while xnum < xukgap:
                        emp1()
                        word = word + " "
                        xnum = xnum + 1
                    print(", " + str(ycaluk[num]), end="", flush=True)
                    word = word + ", " + str(ycaluk[num])
                    ycalukgap = cw_ycaluk - len(str(ycaluk[num]))
                    ynum = 0
                    while ynum < ycalukgap:
                        emp1()
                        word = word + " "
                        ynum = ynum + 1
                    print(")")
                    word = word + ")\n"
                    num = num + 1
                end()
                word = word + "\n"
            linel()
            word = word + "----------------------------------------------------------------------------------------\n"
            end()
            word = word + "\n"
        if yint > 0:
            print("Trend Line Equation: Y = (" + str(grad) + ")X + (" + str(yint) + ")")
            word = word + "Trend Line Equation: Y = (" + str(grad) + ")X + (" + str(yint) + ")\n"
        elif yint == 0:
            print("Trend Line Equation: Y = (" + str(grad) + ")X")
            word = word + "Trend Line Equation: Y = (" + str(grad) + ")X\n"
        elif yint < 0:
            print("Trend Line Equation: Y = (" + str(grad) + ")X - (" + str(abs(yint)) + ")")
            word = word + "Trend Line Equation: Y = (" + str(grad) + ")X - (" + str(abs(yint)) + ")\n"
        end()
        word = word + "\n"
        print("Gradient: " + str(grad))
        word = word + "Gradient: " + str(grad) + "\n"
        print("Y-intercept: " + str(yint))
        word = word + "Y-intercept: " + str(yint) + "\n"
        print("X-intercept: " + str(xint))
        word = word + "X-intercept: " + str(xint) + "\n"
        end()
        word = word + "\n"
        print("From Data Input:")
        word = word + "From Data Input:" + "\n"
        print("X mean: " + str(mx))
        word = word + "X mean: " + str(mx) + "\n"
        print("Y mean: " + str(my))
        word = word + "Y mean: " + str(my) + "\n"
        print("SUM[(x@ - Xmean)*(y@ - Ymean)]: " + str(sum(C)))
        word = word + "SUM[(x@ - Xmean)*(y@ - Ymean)]: " + str(sum(C)) + "\n"
        print("SUM[(x@ - Xmean)^2]: " + str(sum(AS)))
        word = word + "SUM[(x@ - Xmean)^2]: " + str(sum(AS)) + "\n"

        end()
        word = word + "\n"
        print("Close plot to continue.")
        linel()

        # cd Documents/pyprojects/bestfitline2
        plt.xlabel("X-values")
        plt.ylabel("Y-values")
        plt.title("Visualisation for: "+path, size=15, loc="left")
        plt.grid()

        inx = np.array([x for x in xval])       #input x  & y ~!mpl
        iny = np.array([y for y in yval])
        siz0 = np.array([5 for x in range(len(xval))])

        cay = np.array([y for y in YCAL])       #calc-ed y vals, same x as input here
        plt.scatter(inx, iny, siz0, color='orange', label='Entries')      # input here
        plt.plot(inx, cay, '-', label='Fits')        # calc-ed    To add marker paste: , marker='.', ms=5

        if len(xuk) != 0:                            # calc-ed unknowns here
            ukx1 = np.array([x for x in xuk])
            uky1 = np.array([y for y in ycaluk])
            siz1 = np.array([5 for x in range(len(xuk))])
            plt.scatter(ukx1, uky1, siz1, color='red', zorder=3, label='Unknowns')
        if len(yuk) != 0:
            ukx2 = np.array([x for x in xcaluk])
            uky2 = np.array([y for y in yuk])
            siz2 = np.array([5 for x in range(len(yuk))])
            plt.scatter(ukx2, uky2, siz2, color='red', zorder=3)

        plt.legend()
        plt.show()
        plt.close()
        # to add save visual.png option: plt. savefig('plot.png', dpi=300, bbox_inches='tight')

        word = word + "----------------------------------------------------------------------------------------\n"
        word = word + "Generated using Trend Line Calculator V1.3.0. (c)2020 XProductions. All rights reserved.\n"
        print("All Done!")
        print("Press \"Enter\" anytime if you wish to run the program again.")
        end()
        print("Type \"1\" to add the above data to an existing local text file (.txt).")
        print("Type \"2\" to overwrite the above data to an existing local text file (.txt).")
        print("Type \"3\" to create and write the above data into a new file in a desired directory.")
        print("Type \"4\" to create and write the above data into a new file in the same directory as the data source.")
        print("")
        run = input(">>> ")

        if run == "":
            best_fit_line()

        elif run == "1" or run == "\"1\"":
            linel()
            print("Enter the path and file name of the text file below:")
            while True:
                run1 = input(">>> ")
                if run1 != "":
                    try:
                        file1 = open(run1, "a")
                    except:
                        bell()
                        print("Error: Couldn't find path or invalid file name. Please re-enter.")
                        print("----------------------------------------------------------------")
                        continue
                    try:
                        file1.write("\n\nData Source: " + path + "\n\n" + word)
                        file1.close()
                        if option == "2" or option == "\"2\"":
                            file.close()
                        break
                    except:
                        bell()
                        print("Error: Couldn't add data into file. Please try another file.")
                        print("------------------------------------------------------------")
                        continue
                elif run1 == "":
                    best_fit_line()
            print("")
            linel()
            print("Data succesfully added to the desired file!")
            restart = input("End of task. Press \"Enter\" if you wish to run the program again. ")
            if restart == "":
                best_fit_line()
            else:
                exit()

        elif run == "2" or run == "\"2\"":
            linel()
            print("Enter the path and file name of the text file below:")
            while True:
                run2 = input(">>> ")
                if run2 != "":
                    try:
                        file2 = open(run2, "w")
                    except:
                        bell()
                        print("Error: Couldn't find path or invalid file name. Please re-enter.")
                        print("----------------------------------------------------------------")
                        continue
                    try:
                        file2.write("Data Source: " + path + "\n\n" + word)
                        file2.close()
                        if option == "2" or option == "\"2\"":
                            file.close()
                        break
                    except:
                        bell()
                        print("Error: Couldn't overwrite data into file. Please try another file.")
                        print("------------------------------------------------------------------")
                        continue
                elif run2 == "":
                    best_fit_line()
            print("")
            linel()
            print("Data succesfully overwritten to the desired file!")
            restart = input("End of task. Press \"Enter\" if you wish to run the program again. ")
            if restart == "":
                best_fit_line()
            else:
                exit()

        elif run == "3" or run == "\"3\"":
            linel()
            print("Enter the desired path and file name below:")
            while True:
                run3 = input(">>> ")
                if run3 != "":
                    try:
                        file3 = open(run3, "w+")
                    except:
                        bell()
                        print("Error: Couldn't create file or current file in path already existed. Please re-enter.")
                        print("-------------------------------------------------------------------------------------")
                        continue
                    try:
                        file3.write("Data Source: " + path + "\n\n" + word)
                        file3.close()
                        if option == "2" or option == "\"2\"":
                            file.close()
                        break
                    except:
                        bell()
                        print("Error: File created but couldn't write data into file. Please try another path.")
                        print("-------------------------------------------------------------------------------")
                        continue
                elif run3 == "":
                    best_fit_line()
            print("")
            linel()
            print("File succesfully created and data succesfully written into file!")
            restart = input("End of task. Press \"Enter\" if you wish to run the program again. ")
            if restart == "":
                best_fit_line()
            else:
                exit()

        elif run == "4" or run == "\"4\"":
            while path[-1] != "/":          #<--------------for win: \\, mac: /       Ques: why? or error?
                path = path[:-1]
            linel()
            print("Enter the file name below:")
            while True:
                newpath = input(path)
                run4 = path + newpath
                if run4 != "":
                    try:
                        file4 = open(run4, "w+")
                    except:
                        bell()
                        print("Error: Couldn't create file or current file in path already existed. Please re-enter.")
                        print("-------------------------------------------------------------------------------------")
                        continue
                    try:
                        file4.write("Data Source: " + oldpath + "\n\n" + word)
                        file4.close()
                        if option == "2" or option == "\"2\"":
                            file.close()
                        break
                    except:
                        bell()
                        print("Error: File created but couldn't write data into file. Please try another path.")
                        print("-------------------------------------------------------------------------------")
                        continue
                elif run4 == "":
                    best_fit_line()
            print("")
            linel()
            print("File succesfully created and data succesfully written into file!")
            restart = input("End of task. Press \"Enter\" if you wish to run the program again. ")
            if restart == "":
                best_fit_line()
            else:
                exit()


        else:
            exit()

    elif len(xval) != len(yval):
        bell()
        linel()
        print("Error: Number of values of X and Y do not add up.")
        restart = input("Press \"Enter\" if you wish to run the program again. ")
        if restart == "":
            best_fit_line()
        else:
            exit()
best_fit_line()
