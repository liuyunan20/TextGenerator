full_name = input().split(' ')
try:
    assert len(full_name) == 2
except AssertionError:
    print("You need to enter exactly 2 words. Try again!")
else:
    print(f"Welcome to our party, {full_name[0]} {full_name[1]}")
