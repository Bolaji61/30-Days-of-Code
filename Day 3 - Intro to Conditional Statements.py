if __name__ == '__main__':
    N = int(input())
    if N%2==0 and N not in range(6,21):
        print("Not Weird")
    else:
        print("Weird")
