def make_data(student_id):
  from random import seed
  from random import random
  seed(student_id)
  import numpy as np
  samples = 24*60*7
  height = 500;
  step = 10
  n = samples*(height/step)
  n = np.int(n);
  number = np.zeros((n,1))
  data = np.zeros((samples,np.int(height/step)))
  r = (np.linspace(0.0001,1,np.int(height/step))**0.143)
  s = np.linspace(0.1,1,np.int(height/step))
  base = 25;

  for i in range(0,np.int(height/step)):
    a = np.zeros((samples,40))
    for j in range(0,40):
      tmp = random()
      if tmp < 0.2: 
        tmp = 1;
      add = np.int((200-base) + base*tmp);
      add = np.int(base*tmp)
      # print(add)
      a[:,j] =  np.sin(np.resize(np.linspace(0,2*np.pi,add),samples));
    base = base + 5 
    x = np.sum(a[:,:],1) ;
    data[:,i] = r[i] + x*s[i]
  data = data + 3 + (10*random())/2

