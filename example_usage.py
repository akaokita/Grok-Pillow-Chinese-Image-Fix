from add_chinese_text import add_chinese_text

# ==================== 使用示例 ====================
if __name__ == "__main__":
    add_chinese_text(
        image_path="底图.png",           # ← 把这行改成你从 Grok 下载的无中文底图文件名
        output_path="最终中文版.png",     # 输出文件名
        texts=[
            ("远紫外背景（FUV）", (150, 200), (255, 255, 255)),
            ("高银河纬度", (180, 380), (0, 255, 100)),
            ("非尘埃成分", (800, 550), (255, 220, 0)),
            ("来自河外星系 + 银河系内部过程", (120, 720), (200, 200, 255)),
        ],
        font_size=56,
        stroke_width=3
    )
