class Component(object):
    def __init__(self, name=None):
        self.name = name
        self.emoji_str = ":no_entry_sign:"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty or none")
        self._name = value

    @property
    def emoji_str(self):
        return self._emoji_str

    @emoji_str.setter
    def emoji_str(self, value):
        if not value:
            raise ValueError("Emoji string cannot be empty or none")
        self._emoji_str = value
