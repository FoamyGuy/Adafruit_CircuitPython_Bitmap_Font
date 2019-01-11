import displayio

class GlyphCache:
    def __init__(self):
        self._glyphs = {}

    def get_glyph(self, code_point):
        if code_point in self._glyphs:
            return self._glyphs[code_point]
        info = self._get_glyph(code_point)
        if info:
            b = bytearray(4)
            x, y, dx, dy = info["bounds"]
            bmp = displayio.Bitmap(x, y, 2)
            for y in range(y):
                b[0] = info["bitmap"][y]

                bmp._load_row(y, b)
            info["bitmap"] = bmp
        self._glyphs[code_point] = info
        return info
