# # # for i in range(2, 11):
# # #     print(i)
# # from linecache import cache
# #
# #
# # def fibonacci(n):
# #
# #     if n == 1:
# #         return 1
# #     elif n == 2:
# #         return 1
# #     elif n > 2:
# #         return fibonacci(n-1) + fibonacci(n-2)
# #
# # for i in range (1,5):
# #     print(i, ":", fibonacci(i))
#
#
# cache = {}
#
# value = 0
#
#
# def fib2(n):  #different n from the one used above | once the code runs it'll be terminated
#
#     if n in cache:
#         return cache[n]
#
#     if n == 1 or n == 2:
#         value = 1
#     elif n > 2:
#         value = fib2(n-1) + fib2(n-2)
#
#     cache[n] = value
#
#     return value
# #
# # for i in range (1, 500):
# #     print(f"{i} Term: {fib2(i)}")
#
# from functools import lru_cache
#
# # L -> LAST, R -> RECENTLY, C -> CACHE
# @lru_cache(maxsize=1000) #assign 1000 more bytes to the main function.(Compiler assigns 100 bytes by default)
# def fib3(n):
#
#     if n == 1 or n == 2:
#         return 1
#     elif n > 2:
#         return fib3(n-1) + fib3(n-2)
# for i in range (1, 10000):
#     print(i, ":", fib3(i))


def TowerOfHanoi(n,source, destination_rod, auxiliary_rod):

    if n == 1:
        print("Move disc 1 from source", source, "to destination", destination_rod)
        return
    TowerOfHanoi(n-1, source, auxiliary_rod, destination_rod)
    print("Move disc ", n, "from source", source, "to destination", destination_rod)
    TowerOfHanoi(n-1, auxiliary_rod, destination_rod, source)


n = 5
TowerOfHanoi(n, 'A', 'B', 'C')
TowerOfHanoi(n, 'A', 'B', 'C')