# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 19:00:40 2021

@author: emily giron
"""
#this method will add the loss and gains of jobs and will print them out for each president
def total_jobs(data, party_name, party_years, party):
    tmp_list = []
    total_jobs = []
    
    for i in range(len(data)):
        year = data[i][0] #get the year from data
        r = data[i][1:] #get the rest of the data
        #print (r)
        before = data[i][1] #jan's data
        total = 0
        for d in range(len(party_years)):  
            if year in party_years[d]:
                #print(r)
                for j in r:
                    #print(j)
                    total += j - before
                    before = j
                    #print(total)
                #print(total)
                tmp_list.append(total)
                j =sum(tmp_list) 
                
                #total_sum_list.append(total_list)
                
                #if the last item in party_years at position[d], it will add the item to total_jobs list
                if year == party_years[d][-1]:
                    total_jobs.append(j)
                    #print(total_jobs)          
    print(party)
    for i in range(len(party_name)):
        if i == 0:
            print(party_name[i] ,":", abs(round(total_jobs[i]/1000,1)), "million jobs created")
        if i > 0:
            x = total_jobs[i] - total_jobs[i-1] 
            #since total_jobs calculate all the jobs together, we have to subtract the second value by the previous value after the first value at[0]
            if x < 0 :
                print(party_name[i] ,":",abs(round(x/1000,1)), "million jobs lost")
            else:
                print(party_name[i] ,":",abs(round(x/1000,1)), "million jobs created")
            

    print("Total: Increase of", round(j/1000,1), "jobs under", party, "presidents")
            
file = open("presidents.txt", "r")
data_file = open("BLS_private.csv", "r")

republicans = [] #where all republican president names will be
democrats = [] #where all democratic president name will be
dem_years = [] #where the years served for democratic presidents will be stored
rep_years = [] #where the years served for republican presidents wiil be stored
#reading presidents.txt file
for aline in file:
    aline = aline.strip()
    value = aline.split(',')
#Depending what party the president's in, they will be added in different lists  
    if value[1] == "Democrats":
        democrats.append(value[0]) 
        dem_years.append(value[2:])
    else:
        republicans.append(value[0])
        rep_years.append(value[2:])

#putting in the data from BLS_private.csv in a list
data = []
line_num = 1 
for line in data_file:
    #start to add in the data after line 13 in the csv file because that is where it starts
    if line_num > 13:
        line = line.strip()
        value2 = line.split(',')
        #converting number of jobs in each month to an int
        #if we don't do this the values will still be a string
        year = str(value2[0])
        jan = int(value2[1])
        feb = int(value2[2])
        mar = int(value2[3])
        april = int(value2[4])
        may = int(value2[5])
        june = int(value2[6])
        july = int(value2[7])
        aug = int(value2[8])
        sept = int(value2[9])
        octob = int(value2[10])
        nov = int(value2[11])
        dec = int(value2[12])
        #adding the variables in a list
        data.append([year, jan, feb, mar, april, may, june, july, aug, sept, octob, nov, dec])
              
    line_num += 1 
    
print("Let's cut to the chase. According to the Bureau of Labor Statistics, here are the net increases in private-sector employment under each president, chronologically by party:")
print("")

#Calling the method 
rep_total_amount = total_jobs(data, republicans, rep_years, 'Republican')
print(" ")
dem_total_amount = total_jobs(data, democrats, dem_years, 'Democrats')

file.close()
data_file.close()