import numpy as np
import kmeans
import common
import naive_em
import em

X = np.loadtxt("toy_data.txt")

# TODO: Your code here
for K in range(1,5):
  print('K:',K)
  for seed in range(5):
    print('Seed:',seed)
    title = "K:" + str(K) + ", Seed:" + str(seed)
    (mixture,post)=common.init(X, K, seed)
    common.plot(X,mixture,post,title)

