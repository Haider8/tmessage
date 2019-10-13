from html.parser import HTMLParser
from simple_chalk import chalk


class MessageParser(HTMLParser):
    method_call_list = []
    message_to_show = ""
    wrong_tag_stack = []

    @staticmethod
    def validate_tag(self, tag):
        return hasattr(chalk, tag)

    def add_tag_from_method_call_list(self, tag):
        if self.validate_tag(self, tag):
            self.method_call_list.append(tag)

    def remove_tag_from_method_call_list(self, tag):
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
        if len(self.method_call_list):
            method_to_call = "chalk." + ".".join(self.method_call_list)
            self.message_to_show += eval(method_to_call + '("' + data + '")')
        else:
            self.message_to_show += data


def get_formatted_message(raw_message):
    parser = MessageParser()
    parser.feed(raw_message)
    return parser.message_to_show
