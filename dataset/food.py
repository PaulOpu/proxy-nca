
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
        """ 
        annos_fn = 'cars_annos.mat'
        cars = scipy.io.loadmat(os.path.join(root, annos_fn))
        ys = [int(a[5][0] - 1) for a in cars['annotations'][0]]
        im_paths = [a[0][0] for a in cars['annotations'][0]]
        index = 0
        for im_path, y in zip(im_paths, ys):
            if y in classes: # choose only specified classes
                self.im_paths.append(os.path.join(root, im_path))
                self.ys.append(y)
                self.I += [index]
                index += 1 """