<div align="center">
  <img src="./docs/logo.png" width="600"/>
</div>
<br />

[![docs](https://img.shields.io/badge/docs-latest-blue)](http://imagecompressor.readthedocs.io/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyimagecompressor)](https://pypi.org/project/pyimagecompressor/)
[![PyPI](https://img.shields.io/pypi/v/pyimagecompressor)](https://pypi.org/project/pyimagecompressor)
[![license](https://img.shields.io/github/license/CharlesPikachu/imagecompressor.svg)](https://github.com/CharlesPikachu/imagecompressor/blob/master/LICENSE)
[![PyPI - Downloads](https://pepy.tech/badge/pyimagecompressor)](https://pypi.org/project/pyimagecompressor/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pyimagecompressor?style=flat-square)](https://pypi.org/project/pyimagecompressor/)
[![issue resolution](https://isitmaintained.com/badge/resolution/CharlesPikachu/imagecompressor.svg)](https://github.com/CharlesPikachu/imagecompressor/issues)
[![open issues](https://isitmaintained.com/badge/open/CharlesPikachu/imagecompressor.svg)](https://github.com/CharlesPikachu/imagecompressor/issues)

Documents: http://imagecompressor.readthedocs.io/


# ImageCompressor
```
Image compressors written by pure python.
You can star this repository to keep track of the project if it's helpful for you, thank you for your support.
```


# Support List
|   Compressor         |      Paper                                          | Introduction                                                  | Core Code                                               | In Chinese                    |
|   :----:             |      :----:                                         | :----:                                                        | :----:                                                  | :----:                        |
|   pil                |      N/A                                            | [click](https://mp.weixin.qq.com/s/hkUqyCO4lC_zLo0II_NUgA)    | [click](./imagecompressor/modules/compressors/pil.py)   | PIL自带压缩算法               |
|   raisr              |      [click](https://arxiv.org/pdf/1606.01299.pdf)  | [click](https://mp.weixin.qq.com/s/hkUqyCO4lC_zLo0II_NUgA)    | [click](./imagecompressor/modules/compressors/raisr.py) | 谷歌RAISR算法                 |
|   dct                |      N/A                                            | [click](https://mp.weixin.qq.com/s/hkUqyCO4lC_zLo0II_NUgA)    | [click](./imagecompressor/modules/compressors/dct.py)   | 基于离散余弦变换的图像压缩    |
|   svd                |      N/A                                            | [click](https://mp.weixin.qq.com/s/hkUqyCO4lC_zLo0II_NUgA)    | [click](./imagecompressor/modules/compressors/svd.py)   | 基于奇异值分解的图像压缩      |


# Install

#### Pip install
```
run "pip install pyimagecompressor"
```

#### Source code install
```sh
(1) Offline
Step1: git clone https://github.com/CharlesPikachu/imagecompressor.git
Step2: cd imagecompressor -> run "python setup.py install"
(2) Online
run "pip install git+https://github.com/CharlesPikachu/imagecompressor.git@master"
```


# Quick Start
```python
from imagecompressor import imagecompressor

compressor = imagecompressor.ImageCompressor('dct')
image, eavl_result = compressor('input.jpg')
```


# Screenshot
![img](./docs/screenshot.png)


# Projects in Charles_pikachu
- [Games](https://github.com/CharlesPikachu/Games): Create interesting games by pure python.
- [DecryptLogin](https://github.com/CharlesPikachu/DecryptLogin): APIs for loginning some websites by using requests.
- [Musicdl](https://github.com/CharlesPikachu/musicdl): A lightweight music downloader written by pure python.
- [Videodl](https://github.com/CharlesPikachu/videodl): A lightweight video downloader written by pure python.
- [Pytools](https://github.com/CharlesPikachu/pytools): Some useful tools written by pure python.
- [PikachuWeChat](https://github.com/CharlesPikachu/pikachuwechat): Play WeChat with itchat-uos.
- [Pydrawing](https://github.com/CharlesPikachu/pydrawing): Beautify your image or video.
- [ImageCompressor](https://github.com/CharlesPikachu/imagecompressor): Image compressors written by pure python.
- [FreeProxy](https://github.com/CharlesPikachu/freeproxy): Collecting free proxies from internet.
- [Paperdl](https://github.com/CharlesPikachu/paperdl): Search and download paper from specific websites.
- [Sciogovterminal](https://github.com/CharlesPikachu/sciogovterminal): Browse "The State Council Information Office of the People's Republic of China" in the terminal.
- [CodeFree](https://github.com/CharlesPikachu/codefree): Make no code a reality.
- [DeepLearningToys](https://github.com/CharlesPikachu/deeplearningtoys): Some deep learning toys implemented in pytorch.
- [DataAnalysis](https://github.com/CharlesPikachu/dataanalysis): Some data analysis projects in charles_pikachu.
- [Imagedl](https://github.com/CharlesPikachu/imagedl): Search and download images from specific websites.
- [Pytoydl](https://github.com/CharlesPikachu/pytoydl): A toy deep learning framework built upon numpy.


# More
#### WeChat Official Accounts
*Charles_pikachu*  
![img](./docs/pikachu.jpg)