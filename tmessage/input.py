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
        whitespaces = "                                                                         "
        while True:
            keypress = readkey()
            if keypress == key.ENTER:
                print('\n', end='')
                break
            if keypress == key.CR:
                continue
            if keypress == key.BACKSPACE:
                self.buffer = self.buffer[:-1]
            else:
                self.buffer = self.buffer + keypress
            print("\r" + self.buffer + whitespaces + f'\033[{len(whitespaces)}D', end='')
        result = str(self.buffer)
        self.buffer = ""
        return result
