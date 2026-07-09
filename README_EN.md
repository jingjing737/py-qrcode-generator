# py-qrcode-generator 📱

Command-line QR code generator with custom colors, sizes, and logo embedding.

## Quick Start

### Install Dependencies

> ⚠️ Use `python3 -m pip install` to ensure correct Python environment.

```bash
python3 -m pip install qrcode
python3 -m pip install Pillow
```

### Usage

```bash
# Generate basic QR code
python3 gen_qr.py "https://github.com/jingjing737"

# Custom colors and size
python3 gen_qr.py "Hello" -o hello.png -s 15 --fill "#4CAF50" --back "#000000"

# Embed logo (use error correction level H)
python3 gen_qr.py "https://example.com" -o logo.png --logo logo.png
```

## License

MIT
