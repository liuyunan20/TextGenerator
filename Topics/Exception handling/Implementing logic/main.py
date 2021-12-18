full_name = input().split(' ')
try:
    l = len(full_name)
    assert l == 2
except AssertionError as error:
    print("You need to enter exactly 2 words. Try again!")
else:
    print(f"Welcome to our party, {full_name[0]} {full_name[1]}")
