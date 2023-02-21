from datetime import datetime
import time
from library.businessDays import BusinessDays


class Session:
    _session = ("Scripting Languages", "Softskill Session",
                "DevOps Training", "Discussion Session")
    _sessionstart = ("09:00:00", "11:00:00", "14:00:00", "12:00:00")
    _sessionend = ("10:00:00", "12:00:00", "15:00:00", "17:30:00")

    def schedule(self, dname):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("")
        print("     -_"*2, "Scheduled Sessions", "_-"*2)
        print("")
        try:
            choice = int(input(
                "You can view:\n1. Completed Sessions\n2. On-Going Sessions\n3. Upcoming Sessions\n4. All Sessions\nEnter your choice: "))
        except:
            choice = 0
            print("Choice must be a positive integer within 1 to 5")

        match choice:
            case 1:
                print("")
                print("-_"*2, "Completed Session", "_-"*2)
                print("")
                for i in range(len(Session._session)):
                    if (current_time) > (Session._sessionend[i]):
                        print(
                            f"{Session._session[i]:>20} => Completed At: {Session._sessionend[i]}")
                    else:
                        if i <= 0:
                            print("Your Day has started....")
                            time.sleep(2)
                            print("-->You have sessions planned upcoming\3<--")
                            break
                        else:
                            print("Value of i:", i)
                            # print("-->You have no plan for this day<--")
            case 2:
                print("")
                print("-_"*2, "On-Going Sessions", "_-"*2)
                print("")
                print("S.No   Session Title\t   Start Time  End Time")
                count = 0
                for i in range(len(Session._session)):
                    if ((current_time) > (Session._sessionstart[i])) and ((current_time) < (Session._sessionend[i])):
                        count += 1
                        print(
                            f" {count:<3}  {Session._session[i]:<20}  {Session._sessionstart[i]:<8}   {Session._sessionend[i]}")
                    elif count > 1:
                        if ((current_time) > (Session._sessionend[i])):
                            print("-->Day Ended!<--")
                        elif ((current_time) < (Session._sessionstart[i])):
                            print("-->Day Started!<--")
                        else:
                            print("-->No Sessions now!<--")
                print()

            case 3:
                print("")
                print("     -_"*2, "Upcoming Sessions", "_-"*2)
                print("")
                print("S.No   Session Title\t   Start Time  End Time")
                count = 0
                for i in range(len(Session._session)):
                    if ((current_time) < (Session._sessionstart[i])):
                        count += 1
                        print(
                            f" {count:<3}  {Session._session[i]:<20}  {Session._sessionstart[i]:<8}   {Session._sessionend[i]}")
                    else:
                        print("--> Your Sessions are over! <--")
                        break
                print()

            case 4:
                print("")
                print("     _-"*2, "Your Sessions", "_-"*2)
                print("")
                print("S.No\t  Session Title\t    Start Time  End Time")
                for i in range(len(Session._session)):
                    print(
                        f"  {i+1:<4} {Session._session[i]:<20}  {Session._sessionstart[i]:<8}   {Session._sessionend[i]}")
                print("")

            case 5:
                print()

    def attendance(self, dname):
        print("")
        print("-_"*2, "Welcome", dname,"_-"*2)
        print("")
        print("\n", " -_", "Current Attendance Status", "_-")
        print("Total Number of Working Days:", BusinessDays.working_days())
        print("Total Number of Working Days Completed:",
              BusinessDays.completed_days())
        res = (((BusinessDays.completed_days()) /
               (BusinessDays.working_days()))*100)
        print("Your Attendance Percentage is:", "%.2f" % res, "%")
