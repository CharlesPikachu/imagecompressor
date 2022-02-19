# 快速开始


## 已经支持的算法

#### PIL自带压缩算法

1.相关论文

暂无

2.公众号文章介绍

[Introduction](https://mp.weixin.qq.com/s/hkUqyCO4lC_zLo0II_NUgA)

3.调用示例

```python
from imagecompressor import imagecompressor

compressor = imagecompressor.ImageCompressor('pil')
image, eavl_result = compressor('input.jpg', quality=20)
```

4.参数含义

- quality: 图像质量, 默认值为20。

#### 谷歌RAISR算法

1.相关论文

[paper](https://arxiv.org/pdf/1606.01299.pdf)

2.公众号文章介绍

[Introduction](https://mp.weixin.qq.com/s/hkUqyCO4lC_zLo0II_NUgA)

3.调用示例

```python
from imagecompressor import imagecompressor

train_cfg = {
	'rate': 3,
	'patch_size': 11, 
	'Qangle': 24,
	'Qstrength': 3,
	'Qcoherence': 3,
}
compressor = imagecompressor.ImageCompressor('raisr', train_cfg=train_cfg)
image, eavl_result = compressor('input.jpg')
```

4.参数含义

- train_cfg: 训练配置文件。

#### 基于离散余弦变换的图像压缩

1.相关论文

暂无

2.公众号文章介绍

[Introduction](https://mp.weixin.qq.com/s/hkUqyCO4lC_zLo0II_NUgA)

3.调用示例

```python
from imagecompressor import imagecompressor

compressor = imagecompressor.ImageCompressor('dct', stride=8, reserved_start_idx=1)
image, eavl_result = compressor('input.jpg')
```

4.参数含义

- stride: 窗口步长, 默认值为8;
- reserved_start_idx: 保留的高系数能量值数量, 默认值为1。

#### 基于奇异值分解的图像压缩

1.相关论文

暂无

2.公众号文章介绍

[Introduction](https://mp.weixin.qq.com/s/hkUqyCO4lC_zLo0II_NUgA)

3.调用示例

```python
from imagecompressor import imagecompressor

compressor = imagecompressor.ImageCompressor('svd', stride=1024, reserved_start_idx=50)
image, eavl_result = compressor('input.jpg')
```

4.参数含义

- stride: 窗口步长, 默认值为1024;
- reserved_start_idx: 保留的特征值数量, 默认值为50。