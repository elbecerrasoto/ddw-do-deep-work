import datetime as dt

INTERVAL = 25


class Interval:
    def __init__(self, tag: str, duration: int = INTERVAL, comment: str = "", sep: str = ","):

        self.sep = sep

        self.tag = tag
        self.start = dt.datetime.now()
        self.end = self.start + dt.timedelta(minutes=25)
        self.comment = comment

        self.fields = [str(i) for i in (self.tag, self.start.isoformat(), self.end.isoformat(), self.comment)]

    def __repr__(self):
        return self.sep.join(self.fields)

    def write(self, ofile):
        with open(ofile, "a") as f:
            f.write(str(self) + "\n")
