# attendance = [23, 10, 45, 2, 21, 40]

# sorted does not affect the original list but produces a new one in ascending order

# print(sorted(attendance))
# print()
# print(attendance)

# sort changes the original list

attendance = [23, 10, 45, 2, 21, 40]

attendance.sort(key = lambda x: x * 1.5)

print(attendance)
