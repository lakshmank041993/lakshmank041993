# problem1
print("Hello world") #-> c1 > O(c) > O(1)

#problem 2
print(1) # - c1
print(2) # -c2
print(3) # c3
# c1+c2+c3 > O(c) > O(1) when we doing constant amout of work


n = 10
for i in range (n):
    print("hello")  # > n*c3


# c1+c2+n*c3  > O(n*c3) > O(n)


