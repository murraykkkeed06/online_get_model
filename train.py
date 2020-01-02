from fastai.vision import *
from fastai.imports import *
import numpy as np
import asyncio






def my_function():

        loop = asyncio.get_event_loop()

        path = Path('downloads')

        np.random.seed(42)

        data = ImageDataBunch.from_folder(path, train=".", valid_pct=0.2, ds_tfms=get_transforms(), size=224, num_workers=4,bs=4).normalize(imagenet_stats)

        print(data.classes)


        learn = cnn_learner(data, models.resnet34, metrics=error_rate)

        learn.fit_one_cycle(4)

        learn.save('stage-1')

        learn.unfreeze()

        learn.lr_find()

        learn.fit_one_cycle(2, max_lr=slice(3e-8,3e-6))

        learn.save('stage-2')

        learn.export()


        




if __name__ == '__main__':
        my_function()
 

"""
learn.save('stage-1')

learn.unfreeze()

learn.lr_find()

learn.fit_one_cycle(2, max_lr=slice(3e-8,3e-6))

learn.save('stage-2')

learn.export()

"""

