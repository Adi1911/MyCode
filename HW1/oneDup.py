size = int(input().strip())
ref = int(input().strip())
count = 1

while count < size + 2:
    try:
        num = int(input().strip())
    except:
        exit()
    if num < 0 or num > size or num < ref:
        exit()
    if ref == num:
        ref = num
        print(ref)
        exit()
    else:
        ref = num
    count += 1


