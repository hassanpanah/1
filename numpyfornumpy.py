import numpy as np
import datetime
import pytz

ar1=np.array([1,2,5,6])
ar2=np.array([5,3,6,9])
j=np.stack((ar1,ar2),axis=0)
timeodexec=datetime.datetime.now()
tz=pytz.timezone('+02:00')
print('--- new execution ---')
print('Moment of Execution',timeodexec)
print(ar1)
print(ar2)
print('---     result    ---')
print(j)



print('---      END      ---')