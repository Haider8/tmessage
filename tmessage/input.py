""" Handle input/keystroke for outgoing message """
from readchar import readkey, key


class Input:
    """ Custom Input class buffering every typed characters """
    buffer = ""

    def get_buffer(self):
        """ Get buffered content as a string """
        return str(self.buffer)

    def get_input(self):
        """ Retrieve input from user with every keystroke buffered """
        while True:
            keypress = readkey()
            if keypress == key.CTRL_C:
                raise KeyboardInterrupt('Ctrl + C combination detected')
            if keypress in (key.ENTER, key.CR):
                print('\n\r', end='')
                break
            if keypress in (key.UP, key.DOWN, key.LEFT, key.RIGHT):
                continue
            if keypress == key.BACKSPACE:
                self.buffer = self.buffer[:-1]
            else:
                self.buffer = self.buffer + keypress
            print("\r\033[K" + self.buffer, end='', flush=True)
        result = str(self.buffer)
        self.buffer = ""
        return result
