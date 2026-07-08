# py-qrcode-generator 📱

命令行二维码生成器，支持自定义颜色、尺寸、Logo 嵌入。

## 快速开始

```bash
# 安装依赖
pip3 install qrcode[pil]

# 生成基础二维码
python3 qrcode.py "https://github.com/jingjing737"

# 自定义颜色和尺寸
python3 qrcode.py "Hello" -o hello.png -s 15 --fill "#4CAF50" --back "#000000"

# 嵌入 Logo（纠错级别需用 H）
python3 qrcode.py "https://example.com" --logo logo.png --ec H
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
