import numpy as np
import matplotlib.pyplot as plt
import scipy.io
from stack import *
import time


data = scipy.io.loadmat('SASA_example_data.mat')

lambda_FMM = np.linspace(0.6, 1.62, 64)

n_vac = np.ones((1, np.size(lambda_FMM)))
n_SiO2 = data["n_SiO2"]
# First Meta-Layer parameters
H1_ind = 0  # height [50, 55] nm
W1_ind = 0  # width 75:5:90 nm
L1_ind = 3  # length 220:5:240 nm

# Second Meta-Layer parameters
H2_ind = 2  # height [55 65 75] nm
RAD_ind = 2  # corner radius [20 22.5 25] nm
W2_ind = 3  # width 60:5:80 nm
L2_ind = 0  # length 220:5:250 nm

subs_h = 910 / 1000

H_Sp = 350 / 1000


SMAT_1 = data["SMAT_1"]
SMAT_1 = np.squeeze(SMAT_1[H1_ind, W1_ind, L1_ind, :, :, :])

SMAT_2 = data["SMAT_2"]
SMAT_2 = np.squeeze(SMAT_2[H2_ind, RAD_ind, W2_ind, L2_ind, :, :, :])
#print("SMAT_2", SMAT_2[0])
# Build Stack
#layer1 = NonMetaLayer(subs_h,n_SiO2)
layer1 = MetaLayer(SMAT_1, n_SiO2, n_SiO2)
layer2 = NonMetaLayer(np.ones(100)*H_Sp, n_SiO2)

layer3 = MetaLayer(SMAT_2, n_SiO2, n_SiO2)
layer3.rotate(35)

layer4 = NonMetaLayer(subs_h, n_SiO2)
layer_list = [layer1, layer2, layer3, layer4]
stack1 = Stack(layer_list, lambda_FMM, n_SiO2, n_vac)
t1 = time.perf_counter()
s_out = stack1.build()
#s_out2 = stack1.order_up_to(5)
t2 = time.perf_counter()
print("Ausgabe", s_out[0, 0, :, :])
#print("Up_to", s_out2[-1][0,0,:,:])
print("Time in s", t2-t1)
"""
#intensity plot
index_1 = 2
index_2 = 2

intensity = np.abs( s_out[0,:, index_1, index_2] )**2 / n_SiO2
plt.plot(lambda_FMM, np.squeeze(intensity))
plt.show()


#print(SMAT_2)
"""
