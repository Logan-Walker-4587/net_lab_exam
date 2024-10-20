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

def main():

    bin_input = input("Enter a binary number (dividend): ")
    div_input = input("Enter the divisor in binary: ")


    remainder = crc_division(bin_input, div_input)


    final_crc_code = bin_input + remainder


    print(f"Dividend (binary): {bin_input}")
    print(f"Remainder (last {len(div_input)-1} bits): {remainder}")
    print(f"CRC code: {final_crc_code}")

if __name__ == "__main__":
    main()
