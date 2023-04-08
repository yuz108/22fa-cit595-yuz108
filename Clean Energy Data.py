import csv
filename='INT-Export-03-12-2023_13-35-46.csv'
with open(filename, 'r', newline='') as datafile:
    reader = csv.reader(datafile)
    datalist = list(reader)

fields = ["Country_name", "Year", "Total Consumption (quad Btu)", "Coal (quad Btu)", "Natural Gas (quad Btu)", "Petroleum and other liquid (quad Btu)", "Nuclear, renewables and others (quad Btu)", "Nuclear (quad Btu)", "Renewables and others (quad Btu)"]
outlist=[]
for i in range(1, len(datalist)):
    if datalist[i].count('') == 42 and "Nuclear (quad Btu)" not in datalist[i][0]:
        country_name=datalist[i][0]
        for j in range(0, 42):
            outlist.append([country_name, str(1980+j)])

a=0
k=0
while a < len(datalist):
    if datalist[a].count('') == 42 and "Nuclear (quad Btu)" not in datalist[a][0]:
        if "Consumption" in datalist[a+1][0]:

            for s in range(1,len(datalist[a+1])):
                outlist[k].append(datalist[a+1][s])
                k=k+1
    a=a+1

a=0
k=0
while a < len(datalist):
    if datalist[a].count('') == 42 and "Nuclear (quad Btu)" not in datalist[a][0]:
        if "Coal" in datalist[a+2][0]:

            for s in range(1,len(datalist[a+2])):
                outlist[k].append(datalist[a+2][s])
                k=k+1
    a=a+1

a=0
k=0
while a < len(datalist):
    if datalist[a].count('') == 42 and "Nuclear (quad Btu)" not in datalist[a][0]:
        if "Natural gas" in datalist[a+3][0]:

            for s in range(1,len(datalist[a+3])):
                outlist[k].append(datalist[a+3][s])
                k=k+1
    a=a+1

a=0
k=0
while a < len(datalist):
    if datalist[a].count('') == 42 and "Nuclear (quad Btu)" not in datalist[a][0]:
        if "liquids" in datalist[a+4][0]:

            for s in range(1,len(datalist[a+4])):
                outlist[k].append(datalist[a+4][s])
                k=k+1
    a=a+1

a=0
k=0
while a < len(datalist):
    if datalist[a].count('') == 42 and "Nuclear (quad Btu)" not in datalist[a][0]:
        if "Nuclear" in datalist[a+5][0]:

            for s in range(1,len(datalist[a+5])):
                outlist[k].append(datalist[a+5][s])
                k=k+1
    a=a+1

a=0
k=0
while a < len(datalist):
    if datalist[a].count('') == 42 and "Nuclear (quad Btu)" not in datalist[a][0]:
        if "Nuclear" in datalist[a+6][0]:

            for s in range(1,len(datalist[a+6])):
                outlist[k].append(datalist[a+6][s])
                k=k+1
    a=a+1

a=0
k=0
while a < len(datalist):
    if datalist[a].count('') == 42 and "Nuclear (quad Btu)" not in datalist[a][0]:
        if "Renewables" in datalist[a+7][0]:

            for s in range(1,len(datalist[a+7])):
                outlist[k].append(datalist[a+7][s])
                k=k+1
    a=a+1

with open("Energy data2.csv", 'w', newline='') as writefile:
    write = csv.writer(writefile)
    write.writerow(fields)
    write.writerows(outlist)