from random import uniform



t=[82.0,91.0,100.0,68.0,87.0,73.0,78.0,80.0,65.0,84.0,116.0,76.0,97.0,100.0,105.0,77.0,73.0,78.0]


x=[71.0,64.0,43.0,67.0,56.0,73.0,68.0,56.0,76.0,65.0,45.0,58.0,45.0,53.0,49.0,78.0,73.0,68.0]

alfa=0.000001;
b=0;
w=0

flag=0;
errtotal=0
errant=0
y_in=0
y=0


while flag<9999999:
    flag+=1
    errant=errtotal;
    for k in range(0,len(x)):
         y_in=x[k]*w + b
         y=y_in;                
         errtotal+=0.5*(t[k] - y)*(t[k] - y);                
         w+= alfa*(t[k]-y)*x[k]; 
         b+=alfa*(t[k]-y);
         print(flag)
         

print(w)
print(b)

plt.plot(x[0])


    #w -1.026665294
    #b 148.1969525




