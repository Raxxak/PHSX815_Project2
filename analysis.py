#analyzes the output from simulation
import numpy as np
import matplotlib.pyplot as plt

alpha=0.05    
Lambda_null_naught=50
Lambda_alter_naught=85



#open the output files
f1 = open("output_null.txt", "r")
f2 = open("output_alter.txt", "r")


array_null=[]
array_alter=[]
for line in f1:
    array_null.append(int(line))
for line in f2:
    array_alter.append(int(line))    

#sort the arrays
array_null.sort()
array_alter.sort()


#Make bins of one element
i=0
j=min(min(array_null),min(array_alter))
bins=[]
while j<max(max(array_null),max(array_alter)) :
    bins.append(j)
    j=j+1


#Convert to array
bins=np.array(bins)

 
###########Arrange data into bin##################

#null hypothesis data
i=0
null_distribution=[]
for i in bins:
    j=0
    temp=[]
    for j in range(0,len(array_null)):
        if array_null[j]==i:
            temp.append(j)
    null_distribution.append(len(temp))
null_distribution=np.array(null_distribution)

null_distribution=null_distribution/sum(null_distribution)

#for alternative hypothesis
i=0
alter_distribution=[]
for i in bins:
    j=0
    temp=[]
    for j in range(0,len(array_alter)):
        if array_alter[j]==i:
            temp.append(j)
    alter_distribution.append(len(temp))
alter_distribution=np.array(alter_distribution)    

alter_distribution=alter_distribution/sum(alter_distribution)    
    

    
#sort the arrays
array_alter.sort()
array_null.sort()

#list has to be converted to an array to work with it
array_alter=np.array(array_alter)



lambda_crit = array_null[min(int((1-alpha)*len(array_null)), len(array_null)-1)]
first_leftover = np.where( array_alter > lambda_crit )[0][0]
beta = first_leftover/len(array_alter)




#Plotting Likelyhood Ratio


fig,ax=plt.subplots()

ax.plot(bins,null_distribution, label='L(H0)')
ax.plot(bins,alter_distribution,label='L(H1)')
plt.axvline(lambda_crit, color='k')

plt.title("Likelihood plots for Null and Alternative Hypothesis")
plt.xlabel("Parameter(Lambda)")
plt.ylabel("Likelihood ")
plt.grid(True)
plt.plot([],[], '', label='$\lambda_{crit} = $' + '${:.3f}$'.format(lambda_crit))
plt.plot([],[], '', label='$\\alpha = {:.3f}$'.format(alpha))
plt.plot([],[], '', label='$\\beta = {:.3f}$'.format(beta))
ax.fill_between(bins,0,null_distribution, alpha=0.5)
ax.fill_between(bins,0,alter_distribution, alpha=0.5)
plt.grid()
plt.legend()
plt.savefig('Likelihood_plot.pdf')



plt.show()    
    
