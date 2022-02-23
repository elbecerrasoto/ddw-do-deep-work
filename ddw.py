import datetime as dt


class Interval:
    def __init__(self, tag: str, duration: int = 25, comment: str = "", sep: str = ","):

        self.sep = sep

        self.tag = tag
        self.start = dt.datetime.now()
        self.end = self.start + dt.timedelta(minutes=duration)
        self.comment = comment

        def get_fields():
            # For Computers
            start_stamp = self.start.timestamp()
            end_stamp = self.start.timestamp()

            # For Humans
            # It could be ambiguos, day focused
            start_date = self.start.strftime("%F") # iso date
            start_time = self.start.strftime("%R") # 24-hour
            start_week = self.start.strftime("%V-%u") # week (1..53) and day (monday is 1)

            end_time = self.end.strftime("%R")

            return [str(i) for i in (self.tag, start_time, end_time, start_week, start_date, self.comment, start_stamp, end_stamp)]

        self.fields = get_fields()

    def __repr__(self):
        return self.sep.join(self.fields)

    def write(self, ofile):
        with open(ofile, "a") as f:
            f.write(str(self) + "\n")
