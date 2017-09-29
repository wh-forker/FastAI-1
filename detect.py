import  os,json
from glob import glob
import numpy as np
np.set_printoptions(precision=4,linewidth=100)
import matplotlib.pyplot as plt
import utils
import imp
imp.reload(utils)
path = 'sample/'
batch_size = 64
from vgg16 import Vgg16
vgg = Vgg16()
batches = vgg.get_batches(path+'train',batch_size=batch_size)
val_batches = vgg.get_batches(path+'valid',batch_size=batch_size*2)
vgg.finetune(batches)
vgg.fit(batches,val_batches,epochs=1)
