'''
Function:
    The compression algorithm in PIL library
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
from PIL import Image
from .base import BaseCompressor


'''PIL compressor'''
class PILCompressor(BaseCompressor):
    def __init__(self, **kwargs):
        super(PILCompressor, self).__init__(**kwargs)
    '''process'''
    def process(self, image, imagepath=None, quality=20):
        ext = imagepath.split('.')[-1]
        image = image.save(f'tmp.{ext}', quality=quality)
        image = Image.open(f'tmp.{ext}')
        return image