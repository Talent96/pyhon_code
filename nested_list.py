scores = [[1, 35, 80], [2, 32, 75], [3, 30, 82],[4, 33, 75], [5, 37, 60]]
above_average = 35

new_scores = map(lambda x: x[2]+2 if x[1] >= above_average else x[2] - 2, scores)
print(list(new_scores))