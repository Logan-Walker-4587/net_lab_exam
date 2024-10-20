import socket 
host = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bin_input = input("Enter a binary number (dividend): ")
div_input = input("Enter the divisor in binary: ")

client_socket.sendto(bin_input.encode(), (host, port))
client_socket.sendto(div_input.encode(), (host, port))

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
    padded_dividend = dividend + '0' * (n - 1)
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

r = crc_division(bin_input, div_input)
final_crc_code = bin_input + r
print(f"Sent CRC code = {final_crc_code}")
client_socket.sendto(final_crc_code.encode(), (host, port))

client_socket.close()
