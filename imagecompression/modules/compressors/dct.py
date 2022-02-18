'''
Function:
    The compression algorithm implemented by dct transform
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
from .base import BaseCompressor


'''dct compressor'''
class DCTCompressor():
    def __init__(self, kernel_size=8, **kwargs):
        kwargs['read_img_method'] = 'cv2'
        super(DCTCompressor, self).__init__(**kwargs)
    '''process'''
    def process(self, image, imagepath=None):
        pass