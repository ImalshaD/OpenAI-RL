import matplotlib.pyplot as plt
import cal
import csv
import os

# put your preferred location to "saveLocation" to save graphs
saveLocation="D:\Gimhan Sandeeptha\Gimhan\Semester 03\Introduction to artificial intelligence\RL100"
saveDir=""
title=""
xlabal=""
ylabal="Number of Episodes to converge"
num_of_iter=10
n=100
k=1/n
x_avg = [k*i for i in range(1,n+1)]
y_avg = [0 for i in range (n)]

f=open("coordinates2d.csv",'w')
writer=csv.writer(f,lineterminator="\n")
learning_rate=1
discount_rate=1
m = int(input("Select the fix variable  \n 1) Learning Rate \n 2) Discount Rate\n "))
if m==1:
    learning_rate= float(input("Enter the fixed learning rate (0-1): "))
    saveDir="\LR-"+str(learning_rate)
    title="Learning Rate = "+str(learning_rate)
    xlabal="Discount Rate"

elif m==2:
    discount_rate=float(input("Enter the fixed discount rate (0,1): "))
    saveDir="\DR-"+str(discount_rate)
    title="Discount Rate = "+str(discount_rate)
    xlabal="Learning Rate"

saveLocation=saveLocation+saveDir
os.mkdir(saveLocation)

for j in range(num_of_iter):
    array=[]
    x_lst=[]
    y_lst=[]
    for i in range(1,n+1):
        x=k*i
        if m==1:
            y=cal.main(learning_rate,x)
        elif m==2:
            y=cal.main(x,discount_rate)

        x_lst.append(x)
        y_lst.append(y)
        y_avg[i-1]=y_avg[i-1]+y

        print(x,y)
        array.append([x,y])
    writer.writerows(array)
    plt.figure(j+1)
    plt.plot(x_lst,y_lst)
    plt.title(title)
    plt.xlabel(xlabal)
    plt.ylabel(ylabal)
        
    plt.savefig(saveLocation+"\Iteration"+str(j+1),dpi=200)
    plt.close()
    

for k in range (len(y_avg)):
    y_avg[k]=y_avg[k]/num_of_iter

plt.figure(num_of_iter+1)
plt.plot(x_avg,y_avg)
plt.title(title)
plt.xlabel(xlabal)
plt.ylabel(ylabal)

plt.savefig(saveLocation+"\Average ",dpi=200)
plt.close()

print(y_avg)

# plt.show()
