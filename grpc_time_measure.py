import datetime
import dateutil.relativedelta

start_input=int(input("Enter start time in epoch format: \n"))
end_input=int(input("Enter end time in epoch format : \n"))

start = datetime.datetime.fromtimestamp(start_input)
end = datetime.datetime.fromtimestamp(end_input)
rd = dateutil.relativedelta.relativedelta (end, start)

print ("{} years, {} months, {} days, {} hours, {} minutes and {} seconds".format(rd.years, rd.months, rd.days, rd.hours, rd.minutes, rd.seconds))
