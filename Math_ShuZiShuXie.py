import math
import random

class Math_ShuZiShuXie():

    def __init__(self):
        self.upper_limit=100
        self.count_limit=200
        self.paper_size = "A4"
        
        
    def create_homework(self):
        if self.paper_size == "A4":
            self.num_perline = 20
        else:
            self.num_perline = 15

        print("create Math_ShuZiShuXie")
        f=open("Math_ShuZiShuXie_HOMEWORK.txt","w")
        line_return = 0
        for i in range(0,self.count_limit):
            for j in range(0,self.num_perline):
                f.write(str(random.randint(0,self.upper_limit-1)))
                f.write("  ")
            f.write("\n\n")
            
        f.close()
        
    
