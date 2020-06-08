if __name__ == '__main__':
    N = int(input())

arr = []
for N_itr in range(N):
    firstNameEmailID = input().split()
    firstName = firstNameEmailID[0]
    emailID = firstNameEmailID[1]

    if re.findall(r'.+@gmail\.com', emailID):
        arr.append(firstName)

arr.sort()
for firstname in arr:
    print(firstname)
