# Enter your code here. Read input from STDIN. Print output to STDOUT
actual = str(input()).split(" ")
actual_day = int(actual[0])
actual_month = int(actual[1])
actual_year = int(actual[2])

due = str(input()).split(" ")
due_day = int(due[0])
due_month = int(due[1])
due_year = int(due[2])

fine = 0

if actual_year > due_year:
    fine = 10000
elif actual_year == due_year:
    if actual_month > due_month:
        fine = (actual_month - due_month) * 500
    elif actual_month == due_month and actual_day > due_day:
        fine = (actual_day - due_day) * 15

print(fine)
