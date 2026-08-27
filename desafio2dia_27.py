

import numpy as np



arr = np.array (np.random.randint(0,200,(5,5)))
for x  in range(5):
    print(arr[x])
    media  =  np.mean(arr[x])
    print('media', media)  
    print('maior', max(arr[x]))
    print('menor', min(arr[x]))  


