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
    def AC(self):
        import os
        os.system('cls')
        IV = float(input("What is the Initial Velocity: "))
        FV = float(input("What is the Final Velocity: "))
        T = float(input("What is the time: "))
        AC = FV - IV / T
        print("The Acceleration is: ", AC)
        aop.AO()

class Time:
    def T(self):
        import os
        os.system('cls')
        IV = float(input("What is the Initial Velocity: "))
        FV = float(input("What is the Final Velocity: "))
        AC = float(input("What is the Acceleration: "))
        T = FV - IV / AC
        print("The Time is: ", T)
        aop.AO()

class Displacement:
    def DI(self):
        import os
        os.system('cls')
        IV = float(input("What is the Initial Velocity: "))
        AC = float(input("What is the Acceleration: "))
        T = float(input("What is the time: "))
        DI = IV * T + 1/2 * AC * T **2
        print("The Displacement is: ", DI)
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
        print ("6. Exit")
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
        else:
            exit()
            
class Aoption:
    def AO(self):
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

opt.OP()
