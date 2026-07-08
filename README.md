# py-qrcode-generator 📱

命令行二维码生成器，支持自定义颜色、尺寸、Logo 嵌入。

## 快速开始

### 安装依赖

> ⚠️ **注意**：不要用 `pip3 install`，必须用 `python3 -m pip install` 确保装到正确的 Python 环境。

```bash
# 安装 qrcode
python3 -m pip install qrcode

# 安装 Pillow（二维码图片处理）
python3 -m pip install Pillow
```

验证安装：
```bash
python3 -c "import qrcode; print('✅ qrcode 已安装')"
python3 -c "from PIL import Image; print('✅ Pillow 已安装')"
```

如果上面两个都不报错，说明依赖安装成功。

## 用法

```bash
# 生成基础二维码
python3 gen_qr.py "https://github.com/jingjing737"

# 自定义颜色和尺寸
python3 gen_qr.py "Hello" -o hello.png -s 15 --fill "#4CAF50" --back "#000000"

# 嵌入 Logo（纠错级别需用 H）
python3 gen_qr.py "https://example.com" --logo logo.png --ec H
```

## 参数说明

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `data` | 二维码内容 | — |
| `-o / --output` | 输出路径 | `qrcode.png` |
| `-s / --size` | 每个模块像素数 | `10` |
| `--border` | 边框模块数 | `4` |
| `--fill` | 前景色 | `black` |
| `--back` | 背景色 | `white` |
| `--ec` | 纠错级别 (L/M/Q/H) | `M` |
| `--logo` | 嵌入Logo图片路径 | 无 |

## 纠错级别

| 级别 | 可恢复数据比例 |
|------|----------------|
| L | ~7% |
| M | ~15% |
| Q | ~25% |
| H | ~30% |

> ⚠️ 嵌入 Logo 时建议用 `--ec H`，避免扫码失败。

## License

MIT
