plain_text = input("Enter a plain text : ")
depth  = int(input("enter the depth : "))

count = 0
i = 0
fence = []
for i in range(depth):
    fence.append([])
up = 0
for i in range(len(plain_text)):
    fence[count].append(plain_text[i])  # Append the character to the correct depth
    if up == 0:
        count += 1
        if count == depth:  # Change direction when reaching the bottom
            count = depth - 1
            up = 1
    else:
        count -= 1
        if count == -1:  # Change direction when reaching the top
            count = 0
            up = 0
print(fence)
cipher = []       
ciphertext = "".join(["".join(row) for row in fence])
print(f"ciphertext = {ciphertext}")


