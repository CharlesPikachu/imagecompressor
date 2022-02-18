'''
Function:
    Implementation of "RAISR: Rapid and Accurate Image Super Resolution"
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import os
import cv2
import numpy as np
from .base import BaseCompressor
from scipy.sparse.linalg import cg


'''hash table'''
def hashTable(patch, Qangle, Qstrenth, Qcoherence, eps=0.0001):
    [gx, gy] = np.gradient(patch)
    G = np.matrix((gx.ravel(), gy.ravel())).T
    x = G.T * G
    [eigenvalues, eigenvectors] = np.linalg.eig(x)
    # for angle
    angle = np.math.atan2(eigenvectors[0, 1], eigenvectors[0, 0])
    if angle < 0: angle += np.pi
    # for strength
    strength = eigenvalues.max() / (eigenvalues.sum() + eps)
    # for coherence
    lamda1 = np.math.sqrt(eigenvalues.max())
    lamda2 = np.math.sqrt(eigenvalues.min())
    coherence = np.abs((lamda1 - lamda2) / (lamda1 + lamda2 + eps))
    # quantization
    angle = np.floor(angle / (np.pi / Qangle) - 1)
    strength = np.floor(strength / (1.0 / Qstrenth) - 1)
    coherence = np.floor(coherence / (1.0 / Qcoherence) - 1)
    return int(angle), int(strength), int(coherence)


'''RAISR compressor'''
class RAISRCompressor(BaseCompressor):
    def __init__(self, **kwargs):
        self.train_cfg = {
            'rate': 3,
            'patch_size': 11, 
            'Qangle': 24,
            'Qstrength': 3,
            'Qcoherence': 3,
        }
        kwargs['read_img_method'] = 'cv2'
        super(RAISRCompressor, self).__init__(**kwargs)
        self.rootdir = os.path.split(os.path.abspath(__file__))[0]
    '''process'''
    def process(self, image, imagepath=None, modelpath=None):
        self.train(imagepaths=[imagepath])
        if modelpath is None: modelpath = os.path.join(self.rootdir, 'filter.npy')
        H = np.load(modelpath)
        Qangle, Qstrength, Qcoherence = self.train_cfg['Qangle'], self.train_cfg['Qstrength'], self.train_cfg['Qcoherence']
        patch_size, rate = self.train_cfg['patch_size'], self.train_cfg['rate']
        image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
        image_y = image[..., 2]
        LR = cv2.resize(image_y, (0, 0), fx=1./rate, fy=1./rate)
        LRDirect = np.zeros((LR.shape[0], LR.shape[1]))
        for x in range(patch_size // 2, LR.shape[0] - patch_size + patch_size // 2):
            for y in range(patch_size // 2, LR.shape[1] - patch_size + patch_size // 2):
                img_patch = LR[
                    x - patch_size // 2: x + patch_size - patch_size // 2, 
                    y - patch_size // 2: y + patch_size - patch_size // 2,
                ]
                [angle, strength, coherence] = hashTable(img_patch, Qangle, Qstrength, Qcoherence)
                t = x % rate * rate + y % rate
                A = img_patch.reshape(1, -1)
                LRDirect[x][y] = np.matrix(H[angle, strength, coherence, t]) * A.T
        image_scaled = cv2.resize(image, (0, 0), fx=1./rate, fy=1./rate)
        image_scaled[..., 2] = LRDirect
        image = cv2.cvtColor(image_scaled, cv2.COLOR_YCrCb2BGR)
        image = cv2.resize(image, (0, 0), fx=rate, fy=rate)
        return image
    '''train'''
    def train(self, imagepaths=None, savename='filter.npy'):
        # 初始化
        Qangle, Qstrength, Qcoherence = self.train_cfg['Qangle'], self.train_cfg['Qstrength'], self.train_cfg['Qcoherence']
        patch_size, rate = self.train_cfg['patch_size'], self.train_cfg['rate']
        Q = np.zeros((Qangle, Qstrength, Qcoherence, rate * rate, patch_size * patch_size, patch_size * patch_size))
        V = np.zeros((Qangle, Qstrength, Qcoherence, rate * rate, patch_size * patch_size, 1))
        H = np.zeros((Qangle, Qstrength, Qcoherence, rate * rate, patch_size * patch_size))
        # 训练
        from tqdm import tqdm
        for imagepath in tqdm(imagepaths):
            image = cv2.imread(imagepath)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
            image_y = cv2.normalize(image[..., 2].astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)
            HR = image_y
            LR = cv2.GaussianBlur(HR, (rate, rate), 2)
            for x in range(patch_size // 2, LR.shape[0] - patch_size + patch_size // 2):
                for y in range(patch_size // 2, LR.shape[1] - patch_size + patch_size // 2):
                    img_patch = LR[
                        x - patch_size // 2: x + patch_size - patch_size // 2, 
                        y - patch_size // 2: y + patch_size - patch_size // 2,
                    ]
                    [angle, strength, coherence] = hashTable(img_patch, Qangle, Qstrength, Qcoherence)
                    t = x % rate * rate + y % rate
                    A = img_patch.reshape(1, -1)
                    Q[angle, strength, coherence, t] += A * A.T
                    V[angle, strength, coherence, t] += A.T * HR[x, y]
            for pixeltype in range(0, rate * rate):
                for angle in range(0, Qangle):
                    for strength in range(0, Qstrength):
                        for coherence in range(0, Qcoherence):
                            H[angle, strength, coherence, pixeltype] = cg(Q[angle, strength, coherence, pixeltype], V[angle, strength, coherence, pixeltype])[0]
        np.save(os.path.join(self.rootdir, savename), H)