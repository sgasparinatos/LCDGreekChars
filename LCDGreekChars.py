
class LcdGreek:

    GREEK_CHARS = {'gamma': (0b11111, 0b10000, 0b10000, 0b10000, 0b10000, 0b10000, 0b10000, 0b00000),
                        'delta': (0b00100,	0b01010, 0b10001, 0b10001, 0b10001, 0b10001, 0b11111, 0b00000),
                        'lamda': (0b00100, 0b01010, 0b10001, 0b10001, 0b10001, 0b10001, 0b10001, 0b00000),
                        'ksi': (0b11111, 0b00000, 0b00000, 0b01110, 0b00000, 0b00000, 0b11111, 0b00000),
                        'pi': (0b11111, 0b10001, 0b10001, 0b10001, 0b10001, 0b10001, 0b10001, 0b00000),
                        'phi': (0b01110, 0b10101, 0b10101, 0b10101, 0b01110, 0b00100, 0b00100, 0b00000),
                        'psi': (0b10101, 0b10101, 0b10101, 0b10101, 0b01110, 0b00100, 0b00100, 0b00000),
                        'omega': (0b01110, 0b10001, 0b10001, 0b10001, 0b01110, 0b00000, 0b11111, 0b00000)}

    CHARS_DICT = {'g': 0 , 'd': 1 , 'l': 2, 'j': 3, 'p': 4, 'f': 5 , 'c': 6 , 'v': 7 , 's': 0b11110110,
                   'u' : 0b11110010}

    def __init__(self, rpilcd):
        self.lcd = rpilcd
        self.lcd.clear()
        self.add_greek_chars()

    def convert_to_greek(self, text):
        out_str = ""
        for c in text:
            if c in self.CHARS_DICT:
                out_str += unichr(self.CHARS_DICT[c])
            else:
                out_str += c

        return out_str

    def add_greek_chars(self):
        self.lcd.create_char(0, self.GREEK_CHARS['gamma'])
        self.lcd.create_char(1, self.GREEK_CHARS['delta'])
        self.lcd.create_char(2, self.GREEK_CHARS['lamda'])
        self.lcd.create_char(3, self.GREEK_CHARS['ksi'])
        self.lcd.create_char(4, self.GREEK_CHARS['pi'])
        self.lcd.create_char(5, self.GREEK_CHARS['phi'])
        self.lcd.create_char(6, self.GREEK_CHARS['psi'])
        self.lcd.create_char(7, self.GREEK_CHARS['omega'])

    def show_text(self, line, column, text):
        self.lcd.cursor_pos = (line, column)
        self.lcd.write_string(text)

    def show_greek_text(self, line, column, text):
        self.lcd.cursor_pos = (line, column)
        self.lcd.write_string(self.convert_to_greek(text))
