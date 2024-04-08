

start = int(input())
end = int(input())

if start > end:
    print('Second integer can\'t be less than the first.')
else:
    while start <= end:
        print(start, end=" ")
        start += 5
    print()



    
