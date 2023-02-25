# Scenario
# Imagine that you receive a task description of an application that
# monitors the process of apple packaging before the apples are sent
# to a shop.
#
# A shop owner has asked for 1000 apples, but the total weight limitation
# cannot exceed 300 units.
#
# Write a code that creates objects representing apples as long as both
# limitations are met. When any limitation is exceeded, than the packaging
# process is stopped, and your application should print the number of
# apple class objects created, and the total weight.
#
import random


class Apples:
    tot_apples = 0
    tot_weight = 0

    def __init__(self, weight):
        self.weight = weight

    def boxing(self, weight):
        boxed = Apples.tot_weight
        if boxed + weight < 300:
            Apples.tot_weight += weight
            Apples.tot_apples += 1
        elif boxed + weight == 300:
            print("Closing box with {} apples weighting {}".format(Apples.tot_apples, Apples.tot_weight))
        elif boxed + weight > 300:
            print("Closing box with {} apples weighting {}".format(Apples.tot_apples, Apples.tot_weight))
            Apples.tot_weight = weight
            Apples.tot_apples = 1


lower = 0.2
upper = 0.5
for x in range(1, 1001):
    size = random.uniform(lower, upper)
    apple = Apples(size)
    apple.boxing(size)

# # Their solution... is so simple
#
# import random
#
#
# class Apple:
#     counter = 0
#     total_weight = 0
#
#     def __init__(self, weight):
#         self.weight = weight
#         Apple.total_weight += weight
#         Apple.counter += 1
#
#
# # the while loop has access to the class instance to check that parameters are meet, it is simpler than my code
# while Apple.counter < 1000 and Apple.total_weight < 300:
#     apple = Apple(random.uniform(0.2, 0.5))
#
# print('A limit has been reached. The order details:')
# print('# of apples:', Apple.counter)
# # smart use of round function ;)
# print('total weight:', round(Apple.total_weight, 2))
