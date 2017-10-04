from LCDGreekChars import LcdGreek
from RPLCD import CharLCD


if __name__ == '__main__':

    lcd = CharLCD(pin_rs=37, pin_rw=38, pin_e=40, pins_data=[16,18,22,29])
    grlcd = LcdGreek(lcd)

    grlcd.show_text(0,0,"ENGLISH")
    grlcd.show_greek_text(1,0,"EllHNIKA")