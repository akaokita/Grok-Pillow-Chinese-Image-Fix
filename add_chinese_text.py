from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

def add_chinese_text(
    image_path: str,
    output_path: str,
    texts: list,
    font_path: str = None,
    font_size: int = 48,
    stroke_width: int = 2,
    shadow: bool = True
):
    """
    精准叠加中文文字到图片上
    texts 示例格式:
    [("文字内容", (x坐标, y坐标), (R, G, B)), ...]
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"❌ 图片不存在: {image_path}")

    # 自动使用 Windows 自带微软雅黑字体
    if font_path is None:
        font_path = "C:\\Windows\\Fonts\\msyh.ttc"   # 微软雅黑
        if not os.path.exists(font_path):
            font_path = "C:\\Windows\\Fonts\\simhei.ttf"  # 黑体备用

    img = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)

    for text, position, color in texts:
        x, y = position
        
        # 描边（让文字更清晰）
        if stroke_width > 0:
            for dx in [-stroke_width, 0, stroke_width]:
                for dy in [-stroke_width, 0, stroke_width]:
                    if dx == 0 and dy == 0:
                        continue
                    draw.text((x + dx, y + dy), text, font=font, fill=(0, 0, 0))
        
        # 轻微阴影
        if shadow:
            draw.text((x + 3, y + 3), text, font=font, fill=(0, 0, 0, 160))
        
        # 真正文字
        draw.text(position, text, font=font, fill=color)

    img.save(output_path, quality=95)
    print(f"✅ 文字叠加完成！保存为 → {output_path}")

# ==================== 使用示例 ====================
if __name__ == "__main__":
    add_chinese_text(
        image_path="底图.png",           # ← 改成你从 Grok 下载的无中文底图文件名
        output_path="最终中文版.png",
        texts=[
            ("远紫外背景（FUV）", (150, 200), (255, 255, 255)),
            ("高银河纬度", (180, 380), (0, 255, 100)),
            ("非尘埃成分", (800, 550), (255, 220, 0)),
            ("来自河外星系 + 银河系内部过程", (120, 720), (200, 200, 255)),
        ],
        font_size=56,
        stroke_width=3
    )
