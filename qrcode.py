#!/usr/bin/env python3
"""
py-qrcode-generator — 命令行二维码生成器
支持：自定义尺寸、颜色、纠错级别、Logo嵌入
"""
import argparse
import os
import sys
from pathlib import Path

try:
    import qrcode
    from qrcode.image.styledpil import StyledPilImage
    from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
    from PIL import Image
except ImportError:
    print("❌ 缺少依赖，请运行：pip3 install qrcode[pil]")
    sys.exit(1)


def generate(data: str, output: str = "qrcode.png",
             size: int = 10, border: int = 4,
             fill_color: str = "black", back_color: str = "white",
             error_correction: str = "M", logo: str = None) -> str:
    """生成二维码图片"""

    ec_map = {"L": qrcode.constants.ERROR_CORRECT_L,
              "M": qrcode.constants.ERROR_CORRECT_M,
              "Q": qrcode.constants.ERROR_CORRECT_Q,
              "H": qrcode.constants.ERROR_CORRECT_H}
    ec = ec_map.get(error_correction.upper(), qrcode.constants.ERROR_CORRECT_M)

    qr = qrcode.QRCode(version=1, error_correction=ec,
                       box_size=size, border=border)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color,
                        image_factory=StyledPilImage,
                        module_drawer=RoundedModuleDrawer())
    img = img.convert("RGB")

    # 嵌入 Logo
    if logo and os.path.isfile(logo):
        logo_img = Image.open(logo).convert("RGBA")
        qr_w, qr_h = img.size
        logo_size = int(min(qr_w, qr_h) * 0.22)
        logo_img = logo_img.resize((logo_size, logo_size), Image.LANCZOS)
        pos = ((qr_w - logo_size) // 2, (qr_h - logo_size) // 2)
        img.paste(logo_img, pos, logo_img)

    out_path = Path(output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path)
    return str(out_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="命令行二维码生成器")
    parser.add_argument("data", help="二维码内容（URL/文本）")
    parser.add_argument("-o", "--output", default="qrcode.png", help="输出路径")
    parser.add_argument("-s", "--size", type=int, default=10, help="每个模块像素数")
    parser.add_argument("--border", type=int, default=4, help="边框模块数")
    parser.add_argument("--fill", default="black", help="前景色")
    parser.add_argument("--back", default="white", help="背景色")
    parser.add_argument("--ec", default="M", choices=["L", "M", "Q", "H"],
                        help="纠错级别 (L/M/Q/H)")
    parser.add_argument("--logo", help="嵌入Logo图片路径")
    args = parser.parse_args()

    path = generate(args.data, args.output, args.size, args.border,
                    args.fill, args.back, args.ec, args.logo)
    print(f"✅ 二维码已生成：{path}")
