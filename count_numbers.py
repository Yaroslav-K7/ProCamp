nums = []
with open('numbers2.txt', 'r') as file:
    # numbers2.txt is a file in the same directory; or need to specify the path to the file
    for x in file:
        try:
            nums.append(float(x))
        except ValueError:
            pass

print(sum(nums))


# # 2nd method
# def to_float(value):
#     try:
#         float(value)
#         return True
#     except ValueError:
#         return False
#
#
# all_numbers = []
# with open('numbers2.txt', 'r') as file:
#     # numbers2.txt is a file in the same directory; or need to specify the path to the file
#     for s in file:
#         if to_float(s):
#             all_numbers.append(s)
#
# print(sum([float(x) for x in all_numbers]))
