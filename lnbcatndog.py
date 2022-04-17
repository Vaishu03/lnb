inp_str = input()
inp_str = inp_str.lower()
cat_count = inp_str.count('cat')
dog_count = inp_str.count('dog')
if cat_count == dog_count:
    print(True)
else:
    print(False)