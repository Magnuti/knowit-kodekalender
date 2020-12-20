# counter = 0

# divisor_sum_of_prev = 0
# for n in range(1000000):
#     divisor_sum = divisor_sum_of_prev
#     for d in range(1, n + 1):
#         if(n % d == 0):
#             divisor_sum += d

#     if(divisor_sum > 2*n):
#         print("n: {}, divisor_sum: {}, 2n: {}".format(n, divisor_sum, 2*n))
#         if(divisor_sum**2 == 2*n or (2*n)**2 == divisor_sum):
#             print("--------------------------------------------")
#             counter += 1

# print(counter)

counter = 0
factors = dict()

for n in range(10000):
    for d in range(n // 2, 0, -1):
        if(d)
        if(n % d == 0):
            divisor_sum += d

    if(divisor_sum > 2*n):
        print("n: {}, divisor_sum: {}, 2n: {}".format(n, divisor_sum, 2*n))
        if(divisor_sum**2 == 2*n or (2*n)**2 == divisor_sum):
            print("--------------------------------------------")
            counter += 1

print(counter)
