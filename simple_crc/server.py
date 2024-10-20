import socket 
host = '127.0.0.1'
port = 12345

server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind((host,port))

bin_input,client_address = server_socket.recvfrom(1024)
bin_input = bin_input.decode()

div_input,client_address = server_socket.recvfrom(1024)
div_input = div_input.decode()

print(f"Dividend received : {bin_input}")
print(f"Divisor received : {div_input}")

def binary_xor(a, b):
    # Perform XOR between two binary numbers represented as strings
    result = []
    for i in range(len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def crc_division(dividend, divisor):
    # Append (len(divisor) - 1) zeros to the dividend for CRC calculation
    n = len(divisor)
    padded_dividend = dividend 
    remainder = padded_dividend[:n]

    for i in range(n, len(padded_dividend)):
        if remainder[0] == '1':
            # Perform XOR with the divisor
            remainder = binary_xor(remainder, divisor) + padded_dividend[i]
        else:
            # If the first bit is 0, XOR with an equivalent number of 0s (no effect)
            remainder = binary_xor(remainder, '0' * n) + padded_dividend[i]
        
        remainder = remainder[1:]  # Drop the first bit for the next iteration

    # Perform XOR for the last step after the loop
    if remainder[0] == '1':
        remainder = binary_xor(remainder, divisor)
    else:
        remainder = binary_xor(remainder, '0' * n)
    
    return remainder[1:]  # Drop the leading bit

final_crc_code,client_address = server_socket.recvfrom(1024)
final_crc_code = final_crc_code.decode()
print(f"received CRC code  = {final_crc_code}")
r = crc_division(final_crc_code,div_input)
if int(r)==0:
    print("correct CRC received")

server_socket.close()