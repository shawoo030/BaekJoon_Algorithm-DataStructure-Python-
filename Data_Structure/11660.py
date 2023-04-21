import sys
input = sys.stdin.readline
N,M= map(int, input().split())
num_arr = [[0]*(N+1)]
sum_arr = [[0]*(N+1) for _ in range(N+1)]
#print(num_arr)

for i in range(N):
    row = [0]+[int(x) for x in input().split()]
    num_arr.append(row)
#print(num_arr)

# sum_array 채우기
for i in range(1,N+1):
    for j in range(1,N+1):
        sum_arr[i][j] = sum_arr[i-1][j]\
                        +sum_arr[i][j-1]\
                        -sum_arr[i-1][j-1]\
                        +num_arr[i][j]


#print(sum_arr)

# 구간 합 구하기
def answer(x1,y1,x2,y2):
    return sum_arr[x2][y2]\
        -sum_arr[x1-1][y2]\
        -sum_arr[x2][y1-1]\
        +sum_arr[x1-1][y1-1]

for i in range(M):
    x1, y1, x2, y2 = map(int,input().split())
    print(answer(x1,y1,x2,y2))


