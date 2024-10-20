plain_text = input("Enter plain text : ")
key = input("Enter your key : ")
plain_text = plain_text.replace(" ","x")
print(f"added x to plain text : {plain_text}")


if (len(plain_text)%2==1):
    plain_text += "z"
    print(f"appended z = {plain_text}")

digraph = []
for i in range (0,len(plain_text),2):
    digraph.append(plain_text[i]+plain_text[i+1])

print(f"digraph = {digraph}")

key_letters = []
for i in range (0,len(key)):
        if key[i] not in key_letters:
             key_letters.append(key[i])


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
count = 0
row_list = []
matrix = []
for letter in key_letters:
     if count<5:
          row_list.append(letter)
          count += 1
     if count == 5:
          matrix.append(row_list)
          row_list = []
          count = 0
for letter in letters:
     if letter not in key_letters:
       if count<5:
            row_list.append(letter)
            count += 1
       if count == 5:
            matrix.append(row_list)
            row_list = []
            count = 0

print(f"matrix is")
for row in matrix:
    print(" ".join(row))

for i in range(0,len(plain_text)):
     if (plain_text[i]=="j"):
          plain_text[i] = "i"

def search(mat,letter):
     for i in range(0,5):
          for j in range(0,5):
               if mat[i][j]==letter:
                    return i,j 
               
cipher_text = ""

for i in range(len(digraph)):
      row1,col1 = search(matrix,digraph[i][0])
      row2,col2 = search(matrix,digraph[i][1])
      if row1==row2 :
            #print(f"{digraph[i][0]} and {digraph[i][1]} are in same row")
            if col1!=4  and col2 != 4:
                cipher_text += matrix[row1][col1+1]
                cipher_text += matrix[row2][col2+1]
            else :
                if col1==4:
                     cipher_text += matrix[row1][0]
                     cipher_text += matrix[row2][col2+1]
                else:
                     cipher_text += matrix[row1][col1+1]
                     cipher_text += matrix[row2][0]                   
      elif col1==col2 :
            #print(f"{digraph[i][0]} and {digraph[i][1]} are in same col")
            if row1!=4  and row2 != 4:
                cipher_text += matrix[row1+1][col1]
                cipher_text += matrix[row2+1][col2]
            else :
                if row1==4:
                     cipher_text += matrix[0][col1]
                     cipher_text += matrix[row2+1][col2]
                else:
                     cipher_text += matrix[0][col2]
                     cipher_text += matrix[row1+1][col1]
      else:
               #print(f"{digraph[i][0]} and {digraph[i][1]} are diagonals")
               cipher_text += matrix[row1][col2]
               cipher_text += matrix[row2][col1]
               
          
print(f"Cipher text = {cipher_text}")