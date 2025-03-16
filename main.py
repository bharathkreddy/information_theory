def binary_format(number, length = 8):
    return '0b'+bin(number)[2:].zfill(length)

def xor_function(a, b):
    print(f'{"binary of":<12} {a:02d}: {binary_format(a)}\n{"binary of":<12} {b:02d}: {binary_format(b)}')
    print(f'{"xor":<13}{a ^ b:02d}: {binary_format(a ^ b)}')
    return a ^ b

def calculate_redundant_bits(m):
    """Calculate the number of redundant bits (r) required for m data bits."""
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1
    return r

def position_redundant_bits(data):
    """Insert redundant bits at positions that are powers of 2."""
    m = len(data)
    r = calculate_redundant_bits(m)
    j = 0
    k = 0
    result = []

    # Total length of the encoded message is m + r
    for i in range(1, m + r + 1):
        if i == 2 ** j:  # Position of redundant bits (powers of 2)
            result.append(0)  # Placeholder for parity bit
            j += 1
        else:
            result.append(int(data[k]))
            k += 1

    return result

def calculate_parity_bits(encoded_data, r):
    """Calculate the values of the parity bits."""
    n = len(encoded_data)

    for i in range(r):
        parity_position = 2 ** i
        parity_value = 0

        # Check all bits covered by this parity bit
        for j in range(1, n + 1):
            if j & parity_position:  # Check if the bit is included in this parity group
                parity_value ^= encoded_data[j - 1]

        encoded_data[parity_position - 1] = parity_value

    return encoded_data

def hamming_encode(data):
    """Encode the input data using Hamming Code."""
    print(f"Original data: {data}")
    
    # Step 1: Insert redundant bits at appropriate positions
    encoded_data = position_redundant_bits(data)
    
    # Step 2: Calculate and set the values of the redundant (parity) bits
    r = calculate_redundant_bits(len(data))
    encoded_data = calculate_parity_bits(encoded_data, r)
    
    return encoded_data

def detect_and_correct_error(encoded_data):
    """Detect and correct a single-bit error in the encoded data."""
    n = len(encoded_data)
    r = calculate_redundant_bits(n - calculate_redundant_bits(n))
    
    error_position = 0

    # Calculate the syndrome to detect errors
    for i in range(r):
        parity_position = 2 ** i
        parity_value = 0

        for j in range(1, n + 1):
            if j & parity_position:  # Check if the bit is included in this parity group
                parity_value ^= encoded_data[j - 1]

        error_position += parity_value * parity_position

    if error_position == 0:
        print("No errors detected.")
        return encoded_data
    else:
        print(f"Error detected at position: {error_position}")
        
        # Correct the error by flipping the bit at the error position
        encoded_data[error_position - 1] ^= 1
        
        print("Error corrected.")
        return encoded_data

def hamming_decode(encoded_data):
    """Decode the Hamming Code by removing redundant bits."""
    n = len(encoded_data)
    r = calculate_redundant_bits(n - calculate_redundant_bits(n))
    
    decoded_data = []
    
    for i in range(1, n + 1):
        if not (i & (i - 1)) == 0:  # Skip positions that are powers of two (redundant bits)
            decoded_data.append(encoded_data[i - 1])
    
    return decoded_data

# Example usage:
if __name__ == "__main__":
    # Input data to encode (4 data bits)
    data = "1011"
    
    # Encoding process
    encoded_message = hamming_encode(data)
    print(f"Encoded message: {encoded_message}")
    
    # Introduce an error at position 3 (for demonstration purposes)
    encoded_message[2] ^= 1
    print(f"Message with error: {encoded_message}")
    
    # Error detection and correction process
    corrected_message = detect_and_correct_error(encoded_message)
    
    # Decoding process to retrieve original data
    decoded_message = hamming_decode(corrected_message)
    print(f"Decoded message: {''.join(map(str, decoded_message))}")



