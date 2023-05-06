def calc_dist(index1, index2):
    dist = (abs(index1 - index2) // 3)
    if abs(index1 - index2) % 3 > dist:
        dist += (abs(index1 - index2) % 3) - (abs(index1 - index2) // 3)
    return dist

code = str(input("Please enter the security code: "))
keypad = str(input("Please enter the keypad sequence: "))
keys = [int(keypad[i]) for i in range(9)]

adjMat = [[0 for x in range(9)] for y in range(9)]
for i in range(9):
    for k in range(i, 9):
        dist = calc_dist(i, k)
        adjMat[keys[i] - 1][keys[k] - 1] = dist
        adjMat[keys[k] - 1][keys[i] - 1] = dist

total_cost = 0
current_elem = int(code[0])
for elem in code:
    total_cost += adjMat[current_elem - 1][int(elem) - 1]
    current_elem = int(elem)

print(total_cost)