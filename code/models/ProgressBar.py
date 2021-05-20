from progress.bar import Bar


class ProgressBar(Bar):
    def __init__(self, name, max, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = name
        self.fill = '█'
        self.max = max
        self.suffix = '%(index)d/%(max)d(%(percent).1f%%)'
