gross = 0
OT = 0
total_hours = 40

hours = int(input("Enter the amount of hours worked this week:"))
wage = int(input("Enter your hourly wage:"))

if  hours > total_hours:
    OT = 1.5
    gross = (total_hours * wage) + (OT * wage * (hours - total_hours))

else:
    hours = total_hours
    gross = (total_hours * wage) + (OT * wage * (hours - total_hours))

print("Total gross pay for this week is $",gross,)
