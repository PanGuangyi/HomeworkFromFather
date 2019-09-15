import random

class Math_TuiWeiJianFa():

    def __init__(self):
        self.upper_limit=100
        self.count = 20
        
        
    def create_homework(self):
        print("create Math_TuiWeiJianFa")
        tuiwei = []
        f=open("Math_TuiWeiJianFa_HOMEWORK.txt","w")
        max_len = 0
        #遍历
        for i in range(11,self.upper_limit):
            for j in range(2,i):
                #如果被减数个位数小于减数个位
                if i%10<j%10:
                    tuiwei.append("%d-%d="%(i,j))
                    if(len(tuiwei[-1])>max_len):
                        max_len = len(tuiwei[-1])
                    
        sample_tuiwei=random.sample(range(0,len(tuiwei)+1),self.count);
        line_return = 0
        for idx in sample_tuiwei:
            write_item = tuiwei[idx].ljust(max_len," ")
            f.write(write_item)
            if line_return == 3:
                f.write("\n")
                line_return = 0
            else:
                f.write("    ")
                line_return = line_return+1
        f.close()
                
                
                    
                    
    
    