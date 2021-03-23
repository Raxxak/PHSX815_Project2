#This is the DECAY SIMULATOR (The second code will involve analysis and hypothesis testing) This simulates a radioactive decay

from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt


###DEFINE VARIABLES###########
lambda_null_naught=50
lambda_alter_naught=85#Average counts per hour
NumberofEvents=100000
####################################

#CREATES THE DISTRIBUTION
lambda_null=np.random.poisson(lambda_null_naught,NumberofEvents)
lambda_alter=np.random.poisson(lambda_alter_naught,NumberofEvents)
datanull = np.random.poisson(lambda_null, NumberofEvents)
dataalter = np.random.poisson(lambda_alter, NumberofEvents)


#WRITES THE OUTPUT IN A TEXTFILE

np.savetxt("output_null.txt", datanull,fmt='%u')
np.savetxt("output_alter.txt",  dataalter,fmt='%u')



#PLOTS THE DISTRIBUTION

plt.hist(datanull,alpha=0.6, bins=lambda_null_naught,label='H0, μ_0= '+str(lambda_null_naught), density=True)
plt.hist(dataalter,alpha=0.6, bins=lambda_alter_naught,label='H1, μ_1= '+str(lambda_alter_naught), density=True)

plt.title('Distribution of the Count')
plt.ylabel('Probability')
plt.xlabel('Counts in  seconds')
plt.grid()
plt.legend(loc='upper right')
plt.savefig('Normalized_Distribution.pdf')

plt.show()


