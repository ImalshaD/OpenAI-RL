import matplotlib.pyplot as plt
import cal
import csv
import RequrimentChecker as r
r.main()
n=10
k=1/n
f=open("coordinates.csv",'w')
writer=csv.writer(f,lineterminator="\n")
array=[]
for i in range(n+1):
    for j in range(n+1):
        x=k*i
        y=k*j
        z=cal.main(x,y,0.0000001)
        ax=plt.axes(projection="3d")
        print(x,y,z)
        array.append([x,y,z])
        ax.plot(i,j,z)
writer.writerows(array)
plt.show()