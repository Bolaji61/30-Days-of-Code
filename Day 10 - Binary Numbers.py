if __name__ == '__main__':
    n = int(input())
    binary = bin(n)   #convert to bin
    binary = binary.split('b')[1]  #remove the b part of the result
    print(len(max(binary.split('0'))))
