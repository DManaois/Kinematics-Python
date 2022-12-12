class Initial:
    def IV(self):
        import os
        os.system('cls')
        FV = float(input("What is the Final Velocity: "))
        AC = float(input("What is the Acceleration: "))
        T= float(input("What is the time: "))
        IV = FV - AC * T
        print("The Initial Velocity is: ", IV)
        aop.AO()

class Final:
    def FV(self):
        import os
        os.system('cls')
        IV = float(input("What is the Initial Velocity: "))
        AC = float(input("What is the Acceleration: "))
        T = float(input("What is the time: "))
        FV = IV + AC * T
        print("The Final Velocity is: ", FV)
        aop.AO()

class Acceleration:
    def ACE1(self):
        import os
        os.system('cls')
        IV = float(input("What is the Initial Velocity: "))
        FV = float(input("What is the Final Velocity: "))
        T = float(input("What is the time: "))
        AC = FV - IV / T
        print("The Acceleration is: ", AC)
        aop.AO()
        
    def ACE2(self):
        import os
        os.system('cls')
        IV = float(input("What is the Initial Velocity: "))
        T = float(input("What is the time: "))
        D = float(input("What is the Distance: "))
        acce = IV * T
        accele = D - acce
        E = T*T
        acceler = accele / E
        acceleration = 2 * acceler
        print("The Acceleration is: ", acceleration)
        aop.AO()

    def ACE3(self):
        import os
        os.system('cls')
        IV = float(input("What is the Initial Velocity: "))
        FV = float(input("What is the Final Velocity: "))
        D = float(input("What is the Distance: "))
        acv1 = IV * IV
        acv2 = FV * FV
        acv3 = acv2 - acv1
        acv4 = acv3 / D
        acceleration = acv4 / 2
        print("The Acceleration is: ", acceleration)
        aop.AO()
        
    def AC(self):
        import os
        os.system('cls')
        print("1. The Distance is not present")
        print("2. The Final Velocity is not present")
        print("3. The Time is not present")
        print("4. Go back to Menu")
        option = int(input("Choose an option: "))
        if option == 1:
            c.ACE1()
        elif option == 2:
            c.ACE2()
        elif option ==3:
            c.ACE3()
        else:
            exit()
class Time:
    def T(self):
        import os
        os.system('cls')
        IV = float(input("What is the Initial Velocity: "))
        FV = float(input("What is the Final Velocity: "))
        DI = float(input("What is the Distance: "))
        t = 2 * DI
        ti = FV + IV
        T = t / ti
        print("The Time is: ", T)
        aop.AO()

class Displacement:
    def DI(self):
        import os
        os.system('cls')
        IV = float(input("What is the Initial Velocity: "))
        FV = float(input("What is the Final Velocity: "))
        T = float(input("What is the time: "))
        di = FV + IV
        Di = di / 2
        DI = Di * T
        print("The Displacement is: ", DI)
        aop.AO()

class Distance:
    def DIS(self):
        import os
        os.system('cls')
        IV = float(input("What is the Initial Velocity: "))
        A = float(input("What is the Acceleration: "))
        T = float(input("What is the time: "))
        d = IV * T
        i = A * T * T
        s = i / 2
        DIS = d + s
        print("The Distance is: ", DIS)
        aop.AO()

class Velocity:
    def V(self):
        import os
        os.system('cls')
        IV = float(input("What is the Initial Velocity: "))
        AC = float(input("What is the Acceleration: "))
        D = float(input("What is the Distance: "))
        v1 = IV * IV
        v2 = AC * D
        v3 = 2 * v2
        v4 = v1 - v3
        import math
        V = math.sqrt(v4)
        print("The Final Velocity is: ", V)
        aop.AO()

class Option:
    def OP(self):
        import os
        os.system('cls')
        print ("Choose what value is determined?")
        print ("1. Initial Velocity")
        print ("2. Final Velocity")
        print ("3. Acceleration")
        print ("4. Time")
        print ("5. Displacement")
        print ("6. Distance")
        print ("7. Velocity")
        print ("8. Exit")
        print (" ")
        option =int(input("Option: "))
        print (" ")
        if option == 1:
            a.IV()
        elif option == 2:
            b.FV()
        elif option == 3:
            c.AC()
        elif option == 4:
            d.T()
        elif option == 5:
            e.DI()
        elif option == 6:
            f.DIS()
        elif option == 7:
            g.V()
        else:
            exit()
            
class Aoption:
    def AO(self):
        input("Press Enter to continue...")
        import os
        os.system('cls')
        print(" ")
        print("Do you want to try new equation?")
        ao=input("Type Y if Yes and N if No: ")
        if ao == 'Y':
            opt.OP()
        else:
            exit()
        
aop = Aoption()
opt = Option()
a=Initial()
b=Final()
c=Acceleration()
d=Time()
e=Displacement()
f=Distance()
g=Velocity()
opt.OP()
