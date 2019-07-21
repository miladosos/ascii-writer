import os


class Config:
    def __init__(self, font="standard", env=True):
        """
        check font_list.py for supported fonts
        """
        self._font = font
        self.read_from_env = env

    @property
    def font(self):
        if self.read_from_env:
            return os.environ.get('ASCII_ART_FONT', self._font)

        return self._font
