import csv
filename='API_SP.POP.TOTL_DS2_en_csv_v2_5349253.csv'
with open(filename, 'r', newline='') as datafile:
    reader = csv.reader(datafile)
    datalist = list(reader)

fields = ["Country_name", "Country_code", "Year", "Population"]
outlist=[]
for i in range(1, len(datalist)):
    country_name = datalist[i][0]
    country_code=datalist[i][1]
    for j in range(0, 62):
        outlist.append([country_name, country_code, str(1960 + j)])

a=1
k=0
while a < len(datalist):
    for s in range(2,len(datalist[a])):
        outlist[k].append(datalist[a][s])
        k=k+1
    a=a+1

with open("Population data.csv", 'w', newline='') as writefile:
    write = csv.writer(writefile)
    write.writerow(fields)
    write.writerows(outlist)
