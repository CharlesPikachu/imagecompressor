'''
Function:
    The compression algorithm implemented by dct transform
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import cv2
from .base import BaseCompressor


'''dct compressor'''
class DCTCompressor(BaseCompressor):
    def __init__(self, stride=8, reserved_start_idx=1, **kwargs):
        self.stride = stride
        self.reserved_start_idx = reserved_start_idx
        kwargs['read_img_method'] = 'cv2'
        super(DCTCompressor, self).__init__(**kwargs)
    '''process'''
    def process(self, image, imagepath=None):
        image = image.astype('float')
        image_processed = image.copy()
        for c in range(image.shape[2]):
            for y in range(0, image.shape[1] // self.stride):
                for x in range(0, image.shape[0] // self.stride):
                    img_patch = image[x * self.stride: x * self.stride + self.stride, y * self.stride: y * self.stride + self.stride, c]
                    # dct 
                    img_patch_dct = cv2.dct(img_patch)
                    img_patch_dct[self.reserved_start_idx:, self.reserved_start_idx:] = 0.0
                    # idct
                    img_patch = cv2.idct(img_patch_dct)
                    # copy
                    image_processed[x * self.stride: x * self.stride + self.stride, y * self.stride: y * self.stride + self.stride, c] = img_patch
        return image_processed