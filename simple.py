# -*- coding: utf-8 -*-

import pandas as pd
#make data 
wholedata=[]
x_columns=[]

f = open("Colon.arff", 'r')
print("--start--")
while(1):
    line = f.readline()
    if("class" in line):
        print("--end--")
        break
    line_list = line.split(" ")
    if(len(line_list) == 3 ):
        x_columns.append(line_list[1])
        
x_columns.append("class")
wholedata.append(x_columns)
f.close()

f = open("Colon.arff",'r')


print("datastart")

while(1):
    line = f.readline()
    line_list = line.split(",")
    if(len(line_list)>10):
        if("Tumor" in line_list[2000]):
            line_list[2000] = int(1)
        elif("Normal" in line_list[2000]):
            line_list[2000] = int(0)
        wholedata.append(line_list)
#Tumor는 비정상 1로 표시 Normal은 정상 0으로 표시
    if not line:
        break
print("dataend")

f.close()


#make csv file

my_df = pd.DataFrame(wholedata)
my_df.to_csv('colon.csv', index = False, header = False)

