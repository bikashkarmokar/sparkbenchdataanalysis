import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


file = open("local0009.path", 'r')

jobTasks={}
count = {}
jobruntime = {}


with file:
    for line in file:
        jid = int(line.strip().split()[0])        
        task = int(line.strip().split()[2])
        runtime = int(line.strip().split()[9])
        print(str(jid)+" "+str(task) +" "+str(runtime))
        

        
        if jid in jobTasks:                          
            jobTasks[jid].append(task)
        else:
            jobTasks.setdefault(jid,[])                                                
            jobTasks[jid].append(task)
            
            
        if jid in jobruntime:                          
            jobruntime[jid].append(runtime)
        else:
            jobruntime.setdefault(jid,[])                                                
            jobruntime[jid].append(runtime)
            

jobnumtask={}
jobtotruntime={}
            
for x in jobTasks:
        #print(x)
        #print(jobTasks[x])
        #print(len(jobTasks[x]))
        jobnumtask[x]= len(jobTasks[x])
        #print(jobruntime[x])
        #print(sum(jobruntime[x]))
        jobtotruntime[x] = sum(jobruntime[x])
        
        #print("----------------------------------------")

        
#for x in jobTasks:
 #   print(jobnumtask[x])
  #  print(jobtotruntime[x])
   # print("----------------------------------------")
    
for x in jobTasks:
    print(jobnumtask[x])
    print(jobruntime[x])
    print("----------------------------------------")
    
listjobnumtask = sorted(jobnumtask.items()) # sorted by key, return a list of tuples

x1, y1 = zip(*listjobnumtask) # unpack a list of pairs into two tuples

plt.plot(x1, y1)
plt.xlabel("JobId")
plt.ylabel("NumberOfTask")
plt.show()


listjobtotruntime = sorted(jobtotruntime.items()) # sorted by key, return a list of tuples

x2, y2 = zip(*listjobtotruntime) # unpack a list of pairs into two tuples

plt.plot(x2, y2)
plt.xlabel("JobId")
plt.ylabel("RunTime")
plt.show()
    
#plotting task and runtime
plt.plot()

    
#for key, values in jobTasks.items():
 #   items[key] = sum(values)
            
#for key, values in jobTasks.items():
 #       count[key] = len(values) 
    
#for x in count:
 #       print(x)
  #      print(count[x])
   #     print("----------------------------------------")
            
            
            
            

#run time of each task of a job 
runtimes=[]
for x in jobTasks:    
    print(jobruntime[x])    
    print("----------------------------------------")
    
    
    
#plotting run time of each task of a job 

dictionary={}
y=0;
for x in jobTasks:  
    if(len(jobTasks[x])>10):
        print("Total tasks:")
        print(len(jobTasks[x]))
        print("Run times:")
        print(jobruntime[x])    
        for i in jobruntime[x]:
            dictionary[y]=i
            y=y+1    
        plt.bar(list(dictionary.keys()), dictionary.values(), color='g')
        plt.xlabel("Tasks")
        plt.ylabel("RunTime")
        plt.show()  
        dictionary={}
        print("----------------------------------------")
