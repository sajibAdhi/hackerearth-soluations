t =int(input())
while(t > 0):
    t -= 1
    n,k = map(int, input().split())
    array =  input().split()
    index = n - (k % n)
    
    for i in range(index, n): print(array[i], end=" ")
    for i in range(index): print(array[i], end=" ")
    print("")