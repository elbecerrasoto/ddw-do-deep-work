class Interval:
    def __init__(self, tag: str, duration: int = 0, comment: str = "", sep: str = "\t"):

        self.sep = sep

        self.tag = tag
        self.start = 0
        self.end = self.start + duration
        self.comment = comment

        self.fields = [str(i) for i in (self.tag, self.start, self.end, self.comment)]

    def __repr__(self):
        return self.sep.join(self.fields)

    def write(self, ofile):
        with open(ofile, "a") as f:
            f.write(str(self) + "\n")
