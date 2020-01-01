from fastai.vision import *
from fastai.imports import *
import numpy as np
import os

path = Path('downloads')


dirname = os.path.dirname(os.path.realpath(__file__)) + "\downloads" 

#for name in os.listdir(dirname):
#    print(path/name)
#    verify_images(path/name, delete=True, max_size=100)


np.random.seed(42)
data = ImageDataBunch.from_folder(path, train=".", valid_pct=0.2,
        ds_tfms=get_transforms(), size=224, num_workers=4,bs=4).normalize(imagenet_stats)