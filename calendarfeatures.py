from dateutil.rrule import rrule, YEARLY
from datetime import datetime


class Holiday:
    def __init__(self, name, month=None, day=None, nth=None, weekday=None):
        self.name = name
        self.month = month
        self.day = day
        self.nth = nth  # -1 can be used for last
        self.weekday = weekday

    def __repr__(self):
        return f"Holiday({vars(self)})"

    def get_dates(self, start, stop):
        if self.day:
            dates = rrule(
                YEARLY,
                bymonth=self.month,
                bymonthday=self.day,
                dtstart=start,
                until=stop,
            )
        else:
            dates = rrule(
                YEARLY,
                bymonth=self.month,
                byweekday=self.weekday,
                bysetpos=self.nth,
                dtstart=start,
                until=stop,
            )

        return [d.date() for d in dates]

    @classmethod
    def NewYearsDay(cls):
        return cls("New Year's Day", month=1, day=1)

    @classmethod
    def MartinLutherKingDay(cls):
        return cls("Martin Luther King Jr. Day", month=1, nth=3, weekday=0)

    @classmethod
    def PresidentsDay(cls):
        return cls("President's Day", month=2, nth=3, weekday=0)

    @classmethod
    def MemorialDay(cls):
        return cls("Memorial Day", month=5, nth=-1, weekday=0)

    @classmethod
    def IndependenceDay(cls):
        return cls("Independence Day", month=7, day=4)

    @classmethod
    def LaborDay(cls):
        return cls("Labor Day", month=9, nth=1, weekday=0)

    @classmethod
    def ColumbusDay(cls):
        return cls("Columbus Day", month=10, nth=2, weekday=0)

    @classmethod
    def VeteransDay(cls):
        return cls("Veterans's Day", month=11, day=11)

    @classmethod
    def Thanksgiving(cls):
        return cls("Thanksgivng", month=11, nth=4, weekday=3)

    @classmethod
    def Christmas(cls):
        return cls("Christmas", month=12, day=25)


USHolidays = [
    Holiday.NewYearsDay(),
    Holiday.MartinLutherKingDay(),
    Holiday.PresidentsDay(),
    Holiday.MemorialDay(),
    Holiday.IndependenceDay(),
    Holiday.LaborDay(),
    Holiday.VeteransDay(),
    Holiday.Thanksgiving(),
    Holiday.Christmas(),
]


if __name__ == "__main__":

    for i in USHolidays:
        print(i)
    # START = datetime(2021, 1, 1)
    # STOP = datetime(2029, 1, 1)

    # thg = Holiday(month=11, nth=4, weekday=3)
    # print(thg)

    # print(Holiday.memorialday().get_dates(START, STOP))
