'''
Function:
    The compression algorithm implemented by svd transform
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import numpy as np
from .base import BaseCompressor


'''svd compressor'''
class SVDCompressor(BaseCompressor):
    def __init__(self, stride=1024, reserved_start_idx=50, **kwargs):
        self.stride = stride
        self.reserved_start_idx = int(stride * 0.1) if reserved_start_idx is None else reserved_start_idx
        kwargs['read_img_method'] = 'cv2'
        super(SVDCompressor, self).__init__(**kwargs)
    '''process'''
    def process(self, image, imagepath=None):
        image = image.astype('float')
        image_processed = image.copy()
        for c in range(image.shape[2]):
            for y in range(0, image.shape[1] // self.stride):
                for x in range(0, image.shape[0] // self.stride):
                    img_patch = image[x * self.stride: x * self.stride + self.stride, y * self.stride: y * self.stride + self.stride, c]
                    # svd
                    U, sigma, VT = np.linalg.svd(img_patch)
                    # recover
                    dig = np.mat(np.eye(self.reserved_start_idx) * sigma[:self.reserved_start_idx])
                    img_patch = U[:, :self.reserved_start_idx] * dig * VT[:self.reserved_start_idx, :]
                    # copy
                    image_processed[x * self.stride: x * self.stride + self.stride, y * self.stride: y * self.stride + self.stride, c] = img_patch
        return image_processed