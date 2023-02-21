import calendar
from datetime import datetime


class BusinessDays:
    def working_days():
        now = datetime.now()
        current_month = int(now.strftime("%m"))
        current_year = int(now.strftime("%Y"))

        weekday_count = 0
        cal = calendar.Calendar()

        for week in cal.monthdayscalendar(current_year, current_month):
            for i, day in enumerate(week):
                # not this month's day or a weekend
                if day == 0 or i >= 5:
                    continue
                # or some other control if desired...
                weekday_count += 1
        return weekday_count

    def completed_days():
        now = datetime.now()
        current_date = int(now.strftime("%d"))
        current_month = int(now.strftime("%m"))
        current_year = int(now.strftime("%Y"))

        completedBusiDay_count = 0
        cal = calendar.Calendar()

        for week in cal.monthdayscalendar(current_year, current_month):
            for i, day in enumerate(week):
                # not this month's day or a weekend
                if day == 0 or i >= 5 or day >= current_date:
                    continue
                # or some other control if desired...
                completedBusiDay_count += 1
        return completedBusiDay_count
