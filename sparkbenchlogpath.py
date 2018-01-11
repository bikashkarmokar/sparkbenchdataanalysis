import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


file = open("cluster1522.path", 'r')

jobTasks={}
count = {}
jobruntime = {}


with file:
    for line in file:
        jid = int(line.strip().split()[0])        
        task = int(line.strip().split()[2])
        runtime = int(line.strip().split()[9])
        #print(str(jid)+" "+str(task) +" "+str(runtime))
        

        
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
    
listjobnumtask = sorted(jobnumtask.items()) # sorted by key, return a list of tuples

x1, y1 = zip(*listjobnumtask) # unpack a list of pairs into two tuples

plt.plot(x1, y1)
plt.show()


listjobtotruntime = sorted(jobtotruntime.items()) # sorted by key, return a list of tuples

x2, y2 = zip(*listjobtotruntime) # unpack a list of pairs into two tuples

plt.plot(x2, y2)
plt.show()
    
#for key, values in jobTasks.items():
 #   items[key] = sum(values)
            
#for key, values in jobTasks.items():
 #       count[key] = len(values) 
    
#for x in count:
 #       print(x)
  #      print(count[x])
   #     print("----------------------------------------")
            
            
            
            
