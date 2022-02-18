'''
Function:
    the base module of compressor
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import os
import numpy as np
from ..utils import touchdir, EvaluationMetrics


'''base compressor'''
class BaseCompressor():
    def __init__(self, savedir='outputs', logger_handle=None, read_img_method='pil', **kwargs):
        assert read_img_method in ['pil', 'cv2']
        touchdir(savedir)
        self.savedir = savedir
        self.logger_handle = logger_handle
        self.read_img_method = read_img_method
        for key, value in kwargs.items(): setattr(self, key, value)
    '''call'''
    def __call__(self, imagepath=None, **kwargs):
        # process
        if self.read_img_method == 'pil':
            from PIL import Image
            image = Image.open(imagepath)
        else:
            import cv2
            image = cv2.imread(imagepath)
        image_processed = self.process(image, imagepath, **kwargs)
        savepath = os.path.join(self.savedir, os.path.split(imagepath)[-1])
        if self.logger_handle is not None:
            self.logger_handle.info(f'Processed {imagepath} successfully, and the result is saved into {savepath}')
        if self.read_img_method == 'pil':
            image_processed.save(savepath)
        else:
            cv2.imwrite(savepath, image_processed)
        # evaluate
        if self.read_img_method == 'pil':
            eavl_result = self.evaluate(np.array(image), np.array(image_processed))
        else:
            eavl_result = self.evaluate(image, image_processed)
        # return
        return image_processed, eavl_result
    '''process'''
    def process(self, image, imagepath, **kwargs):
        raise NotImplementedError('not to be implemented')
    '''evaluate'''
    def evaluate(self, src, target):
        client = EvaluationMetrics()
        result = {
            'mse': client.mse(src, target),
            'psnr': client.psnr(src, target),
            'ssim': client.ssim(src, target),
        }
        return result