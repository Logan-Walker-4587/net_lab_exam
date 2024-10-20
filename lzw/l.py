text = input("Enter a string to encode : ")
code = 0
eo = []
entry = {}
counter = 1

for char in text:
     if char not in entry :
          entry[char] = counter 
          counter += 1

code = len(entry)+1
current_text = ""

for char in text :
     combined_text = current_text + char 
     if combined_text not in entry:
          entry[combined_text] = code 
          code+=1 
          eo.append(entry[current_text]) 
          current_text = char
     else:
          current_text = combined_text
if current_text:
     eo.append(entry[current_text]) 
    
print(entry)

print(f"Encoded text = {eo}")
     


