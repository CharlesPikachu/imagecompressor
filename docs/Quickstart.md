# 快速开始


## 已经支持的算法

#### PIL自带压缩算法

1.相关论文

暂无

2.公众号文章介绍

[Introduction]()

3.调用示例

```python
from imagecompressor import imagecompressor

compressor = imagecompressor.ImageCompressor('pil')
image, eavl_result = compressor('input.jpg')
```

#### 谷歌RAISR算法

1.相关论文

[paper](https://arxiv.org/pdf/1606.01299.pdf)

2.公众号文章介绍

[Introduction]()

3.调用示例

```python
from imagecompressor import imagecompressor

compressor = imagecompressor.ImageCompressor('raisr')
image, eavl_result = compressor('input.jpg')
```

#### 基于离散余弦变换的图像压缩

1.相关论文

暂无

2.公众号文章介绍

[Introduction]()

3.调用示例

```python
from imagecompressor import imagecompressor

compressor = imagecompressor.ImageCompressor('dct')
image, eavl_result = compressor('input.jpg')
```

#### 基于奇异值分解的图像压缩

1.相关论文

暂无

2.公众号文章介绍

[Introduction]()

3.调用示例

```python
from imagecompressor import imagecompressor

compressor = imagecompressor.ImageCompressor('svd')
image, eavl_result = compressor('input.jpg')
```