testCase = int(input())

for test in range(testCase):
    rows,columns = map(int,input().split())

    maxBlack = 0
    for row in range(rows):
        column = input()
        blackCount = column.count('#')
        if maxBlack < blackCount:
            maxBlack = blackCount
    print(maxBlack)