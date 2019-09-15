import math
import random

class Math_FuHaoShiBie():

    def __init__(self):
        self.upper_limit=100
        self.count = 160
        
        
    def create_homework(self):
        print("create Math_FuHaoShiBie")
        max_len = 2* math.ceil(math.log(self.upper_limit,10))+2
        f=open("Math_FuHaoShiBie_HOMEWORK.txt","w")
        line_return = 0
        for idx in range(0,self.count):
            lvalue = str(random.randint(0,self.upper_limit-1))
            if random.randint(0,self.upper_limit)%2==0:
                _operator = "+"
            else:
                _operator = "-"
            rvalue = str(random.randint(0,self.upper_limit-1))
            
            equation = lvalue+_operator+rvalue+"="
            write_item = equation.ljust(max_len," ")
            f.write(write_item)
            if line_return == 3:
                f.write("\n")
                line_return = 0
            else:
                f.write("    ")
                line_return = line_return+1
        f.close()
    
    