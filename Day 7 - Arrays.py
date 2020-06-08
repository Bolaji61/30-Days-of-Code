if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    reverse = arr[::-1]
    print(*reverse)
