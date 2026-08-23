# Remember:
# List → keeps order and allows duplicates ✅
# Tuple → keeps order and allows duplicates ✅
# Set → does not guarantee order and removes duplicates ✅
# Dictionary → keeps insertion order (Python 3.7+) ✅
# If you want numbers in exactly the order you enter them, use a list.


# Duplicate Remover
# Ask the user for several numbers and remove duplicates using a set.
set1=set()
while True:
    num=input("Enter only digit to add in set or done to end:")
    if num=="done":
        break
    set1.add(num)
print("The set without duplication is:\n",set1)
    