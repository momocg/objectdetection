import os



files = os.listdir('./traindata')

for i,file in enumerate(files):
    os.mkdir('./traindata/'+str(i))
    os.system('mv '+'./traindata/'+file+' '+'./traindata/'+str(i))