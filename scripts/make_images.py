from PIL import Image, ImageDraw


def apple():
    img = Image.new("RGBA", (200, 224), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # ground shadow
    d.ellipse((35, 198, 165, 216), fill=(0, 0, 0, 30))
    # body: two overlapping circles make the classic dip at the top
    d.ellipse((20, 60, 120, 205), fill="#d8363c")
    d.ellipse((80, 60, 180, 205), fill="#d8363c")
    d.ellipse((35, 72, 165, 198), fill="#e64a50")          # inner tone
    # highlight
    d.ellipse((55, 85, 88, 125), fill="#f28b8e")
    # stem
    d.line((100, 68, 106, 30), fill="#6b4a2b", width=8)
    # leaf, pointed, swooping right
    d.polygon([(106, 38), (145, 20), (172, 30), (142, 46), (108, 46)], fill="#5a9e3d")
    img.save("apple.png")


def blueberry():
    img = Image.new("RGBA", (200, 224), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # ground shadow
    d.ellipse((35, 198, 165, 216), fill=(0, 0, 0, 30))

    def berry(x, y, r):
        d.ellipse((x - r, y - r, x + r, y + r), fill="#3f5a9e")
        d.ellipse((x - r + 8, y - r + 8, x + r - 6, y + r - 6), fill="#4c6cb8")
        # highlight
        d.ellipse((x - r + 12, y - r + 12, x - r + 30, y - r + 32), fill="#7d92cf")
        # star crown: 4 short lines
        for dx, dy in [(-8, -3), (8, -3), (-3, -8), (-3, 8)]:
            d.line((x + dx, y + dy, x + dx * 2, y + dy * 2), fill="#2b3f73", width=4)

    # back berries first, front berry last so it overlaps
    berry(62, 105, 44)
    berry(140, 112, 40)
    berry(100, 160, 48)
    img.save("blueberry.png")


apple()
blueberry()
print("Made: apple.png, blueberry.png")