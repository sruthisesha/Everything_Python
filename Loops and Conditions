print("'continue-statement:' we can skip current iteration and send it to next iteration")
print("-"*20)
# ---------------

# Value perl is not required to process, so we can skip iteration if value is 'Perl'

my_list = ["Java", "perl", "python", "perl", "C", "perl", "C++"]
print("my_list", my_list, end="\n\n")

index_no = 0
while index_no < len(my_list):
    j = my_list[index_no]
    index_no += 1
    if j == "perl":
        print("\nGot Value 'Perl', so skipping current iteration and sending it to next iteration using 'continue-statement'\n")
        continue
    print("Each Value is:", j)

# USING for-loop

# for j in my_list:
#     if j == "perl":
#         print("\nGot Value 'Perl', so skipping current iteration and sending it to next iteration using 'continue-statement'\n")
#         continue
#     print("Each Value is:", j)

print("#"*40, end="\n\n")
############################

print("USING 'while-else' block")
print("-"*20)
# ---------------

my_list = ["Java", "perl", "python-1", "perl", "python-2", "C", "python-3", "perl", "C++"]
print("my_list", my_list, end="\n\n")

# Requirement,
# - check are there any python course
# - print 'found' or 'not-found'.
# - if one value found then it is found. so no need to verify value

index_no = 0
while index_no < len(my_list):
    j = my_list[index_no]
    index_no += 1
    if j.startswith("python"):
        print("course FOUND")
        break
else:
    print("course NOT FOUND")

# USING for-loop

# for j in my_list:
#     if j.startswith("python"):
#         print("course FOUND")
#         break
# else:
#     print("course NOT FOUND")

# after completing the while-loop, 'while-else' block will execute

print("#"*40, end="\n\n")
############################
