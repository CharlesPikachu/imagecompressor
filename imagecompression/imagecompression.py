'''
Function:
    imagecompression
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
if __name__ == '__main__':
    from modules import *
else:
    from .modules import *


'''Image Compressor'''
class ImageCompressor():
    def __init__(self, compressor_type=None, logfilepath='imagecompression.log', **kwargs):
        self.logger_handle = Logger(logfilepath)
        self.supported_compressors = {
            'dct': DCTCompressor,
            'pil': PILCompressor,
            'raisr': RAISRCompressor,
        }
        assert compressor_type in self.supported_compressors
        kwargs['logger_handle'] = self.logger_handle
        self.compressor = self.supported_compressors[compressor_type](**kwargs)
    '''call'''
    def __call__(self, imagepath, **kwargs):
        return self.compressor(imagepath, **kwargs)
    '''repr'''
    def __repr__(self):
        return 'imagecompression, author: charles, 微信公众号: Charles的皮卡丘'


'''test'''
if __name__ == '__main__':
    compressor = ImageCompressor('dct')
    image, eavl_result = compressor('input.jpg')
    print(eavl_result)