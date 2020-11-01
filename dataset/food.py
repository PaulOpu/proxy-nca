
from .base import *
import scipy.io
from os import path as pth

class Food(BaseDataset):
    def __init__(self, root, classes, transform = None):
        BaseDataset.__init__(self, root, classes, transform)
        img_dir = pth.join(root,"images")
        category_path = pth.join(root,"categories.txt")
        with open(category_path,"r") as f:
            categories = f.read().split()
        cat2class = {cat:i for i,cat in enumerate(categories)}

        img_paths = [os.path.join(dp, f).replace("._","") for dp, dn, filenames in os.walk(img_dir) for f in filenames if os.path.splitext(f)[1] == '.jpg']
        ys = [cat2class[img_path.split("/")[-2]] for img_path in img_paths]

        index = 0
        for im_path, y in zip(img_paths, ys):
            
            if y in classes: # choose only specified classes
                self.im_paths.append(os.path.join(root, im_path))
                self.ys.append(y)
                self.I += [index]
                index += 1