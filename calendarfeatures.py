from dateutil.rrule import rrule, YEARLY
from datetime import datetime, timedelta
from collections.abc import MutableMapping
from itertools import chain


class Holiday:
    def __init__(self, name, month=None, day=None, nth=None, weekday=None):
        self.name = name
        self.month = month
        self.day = day
        self.nth = nth  # -1 can be used for last
        self.weekday = weekday

    def __repr__(self):
        first = f'name="{self.name}", '
        args = ", ".join([f"{k}={v}" for (k, v) in vars(self).items() if k != "name"])
        return "Holiday(" + first + args + ")"

    @staticmethod
    def _get_observed_date(holiday_date):
        if holiday_date.weekday() == 5:
            return holiday_date - timedelta(days=1)
        elif holiday_date.weekday() == 6:
            return holiday_date + timedelta(days=1)
        else:
            return holiday_date

    def get_dates(self, start, stop, observed=False):
        if all([self.day, self.month]):
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

        if observed:
            return {self._get_observed_date(d) for d in dates}
        else:
            return list(dates)

    # US Holidays

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
    def VeteransDay(cls):
        return cls("Veterans's Day", month=11, day=11)

    @classmethod
    def Thanksgiving(cls):
        return cls("Thanksgivng", month=11, nth=4, weekday=3)

    @classmethod
    def Christmas(cls):
        return cls("Christmas", month=12, day=25)

    # Other Holidays

    @classmethod
    def ColumbusDay(cls):
        return cls("Columbus Day", month=10, nth=2, weekday=0)

    # Pseudo Holidays

    @classmethod
    def BlackFriday(cls):
        return cls("Black Friday", month=11, nth=4, weekday=4)

    @classmethod
    def ChristmasEve(cls):
        return cls("Christmas Eve", month=12, day=24)


class Holidays(MutableMapping):
    def __init__(self, holidays):
        if all([isinstance(h, Holiday) for h in holidays]):
            self.holidays = holidays
            self.store = {h.name: h for h in self.holidays}
        else:
            raise TypeError("Holidays only accepts Holiday objects.")

    def __repr__(self):
        return f"Holidays({self.holidays})"

    def __getitem__(self, key):
        return self.store[key]

    def __setitem__(self, key, value):
        self.store[key] = value

    def __delitem__(self, key):
        self.store.pop(key, None)

    def keys(self):
        return self.store.keys()

    def items(self):
        return self.store.items()

    def values(self):
        return self.store.values()

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def get_dates(self, start, stop, observed=False):
        return [d for h in self.holidays for d in h.get_dates(start, stop)]

    # Predefined holiday lists


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

NERCHolidays = [
    Holiday.NewYearsDay(),
    Holiday.MemorialDay(),
    Holiday.IndependenceDay(),
    Holiday.LaborDay(),
    Holiday.Thanksgiving(),
    Holiday.Christmas(),
]
