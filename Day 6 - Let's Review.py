# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(0, n):
    word = str(input())
    even_index = [word[index_e] for index_e in range(len(word)) if index_e%2==0]
    join_even_index = ''.join(even_index)
    odd_index = [word[index_o] for index_o in range(len(word)) if index_o%2!=0]
    join_odd_index = ''.join(odd_index)
    print("%s %s" % (join_even_index, join_odd_index))
