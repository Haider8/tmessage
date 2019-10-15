"""Utils : Methods and Class which are used for tmessage."""
from html.parser import HTMLParser
from simple_chalk import chalk


# pylint: disable=W0223
class MessageParser(HTMLParser):
    """Message Parser class which is a HTMLParser for the message."""
    method_call_list = []
    message_to_show = ""

    @staticmethod
    def validate_tag(tag):
        """Validate the tag given is valid for text styling / colouring."""
        return hasattr(chalk, tag)

    def add_tag_from_method_call_list(self, tag):
        """Add the given tag in method_call_list if it is a valid tag."""
        if self.validate_tag(tag):
            self.method_call_list.append(tag)

    def remove_tag_from_method_call_list(self, tag):
        """Remove the given tag from list. Removal will happen in LIFO."""
        self.method_call_list.reverse()
        try:
            self.method_call_list.remove(tag)
        except ValueError:
            pass
        self.method_call_list.reverse()

    def handle_starttag(self, tag, attrs):
        self.add_tag_from_method_call_list(tag)

    def handle_endtag(self, tag):
        self.remove_tag_from_method_call_list(tag)

    def handle_data(self, data):
        if self.method_call_list:
            method_to_call = "chalk." + ".".join(self.method_call_list)
            self.message_to_show += eval(method_to_call + '("' + data + '")')  # pylint: disable=eval-used
        else:
            self.message_to_show += data


def get_formatted_message(raw_message):
    """Get the formatted message by parsing the given message."""
    parser = MessageParser()
    parser.feed(raw_message)
    return parser.message_to_show
