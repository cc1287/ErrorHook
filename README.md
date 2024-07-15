# ErrorHook

自动全局捕捉错误，并
- 输出错误到控制台
- 输出错误到文件（可选，默认开启）
- 显示错误窗口（可选，默认开启）
Code by: cc1287

### 示例

```python
import ErrorHook
# 然后...就什么都不用做了，会自动捕捉错误

# 下面有一个错误
raise BaseException('I am a Error.')
```

![错误窗口样式](https://gitee.com/cc1287/error-hook/raw/master/assets/image-20240715103626507.png)

### 安装

```bash
pip install ErrorHook
```

### License

```
MIT License

Copyright (c) 2024 cc1287

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

#### 更新日志
- 1.2~1.6
> 让导入更便捷，更改导入名称从`ErrorHook`为`errorhook`
- 1.1
> 更新界面-退出按钮
- 1.0
> update