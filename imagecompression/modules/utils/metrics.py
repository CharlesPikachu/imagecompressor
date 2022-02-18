'''
Function:
    define some evaluation metrics
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import numpy as np
from skimage.metrics import structural_similarity as ssim


'''define some evaluation metrics'''
class EvaluationMetrics():
    '''mean squared error'''
    def mse(self, src, target):
        diff = ((target - src) ** 2).mean()
        return diff
    '''peak signal-to-noise ratio'''
    def psnr(self, src, target, num_bits=8):
        mse_value = self.mse(src, target)
        psnr_value = 10 * np.log10((2 ** 8 - 1) ** 2 / mse_value)
        return psnr_value
    '''structural similarity index'''
    def ssim(self, src, target):
        if len(src.shape) == 3:
            ssim_values = []
            for i in range(3):
                ssim_values.append(ssim(src[..., i], target[..., i]))
            return sum(ssim_values) / len(ssim_values)
        else:
            return ssim(src, target)