attendance = [23, 10, 45, 2, 21, 40]
above_average_attendance = filter(lambda x: x >= 35, attendance)
print(list(above_average_attendance))

countries = ["Nigeria", "US", "UK", "Canada", "Germany"]
letter_greaterThan_three = filter(lambda x: len(x) > 3, countries)
print(list(letter_greaterThan_three))
