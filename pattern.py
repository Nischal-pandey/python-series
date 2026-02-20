# Simple pattern
# n=5
# for i in range (n):
#     for j in range (n):
#         print("*", end=" ")
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# n=5
# for i in range (n, 0, -1):
#     for j in range (i):
#         print("*", end="")
#     print()

# n=5
# for i in range (1,n+1):
#     for j in range (1,i+1):
#         print(j, end=" ")
#     print()

# n=5
# for i in range (1,n+1):
#     for j in range (i):
#         print(i,end=" ")
#     print()


#   SPACES WALE PATTERNS

# n=5
# for i in range (1,n+1):
#     for j in range (n-i): # Pehle space print karo
#         print(" ",end=" ")
#     for j in range (i):   # Phir stars ko print karo
#         print("*",end=" ")
#     print()
#
#
# n=5
# for i in range (n,0,-1):
#     for j in range (n-i):
#         print(" ",end=" ")
#     for j in range (2*i-1):
#         print("*",end=" ")
#     print()

#  Diamond pattern
# n=5
# for i in range(1,n+1):
#     for j in range(n-i):   upper half
#         print(" ",end=" ")
#     for j in range (2*i-1):
#         print("*",end=" ")
#     print()
#
# for i in range (n-1,0,-1):
#     for j in range(n - i):
#         print(" ", end=" ")  Lower half
#     for j in range(2 * i - 1):
#         print("*", end=" ")
#     print()
