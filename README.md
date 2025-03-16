# Hamming Code Implementation in Python

## Overview

This repository contains a Python implementation of Hamming Code for error detection and correction. The Hamming Code is a widely used error-correcting code that can detect and correct single-bit errors in transmitted data. This implementation uses the (7,4) Hamming Code, which encodes 4 data bits into a 7-bit codeword by adding 3 parity bits.

## Features

. Encoding: Converts 4 data bits into a 7-bit encoded message with redundant parity bits.

. Error Detection: Identifies single-bit errors in the encoded message.

. Error Correction: Corrects the error by flipping the erroneous bit.

. Decoding: Extracts the original data bits from the corrected message.

## How It Works

1. Encoding
   The input data (4 bits) is encoded into a 7-bit message using redundant parity bits. Parity bits are placed at positions that are powers of 2 (e.g., 1, 2, 4).

```
Example:
Input Data: 1011
Encoded Message: 0b1011011
```

2. Error Detection
   The receiver calculates parity checks using the redundant bits to detect errors. If an error is detected, its position is identified using a "syndrome."

```
Example:
Message with Error: 0b1011111
Error Position: 3
```

3. Error Correction
   Once the error position is identified, the erroneous bit is flipped to correct it.

```
Example:
Corrected Message: 0b1011011
```

4. Decoding
   After correcting errors, redundant bits are removed to retrieve the original data.

```
Example:
Decoded Data: 1011
```

Encoding Process:
Below is an example of how Hamming Code places and calculates parity bits:

```
Data Bits (D): D3 D5 D6 D7
Parity Bits (P): P1 P2 P4
Encoded Message: P1 P2 D3 P4 D5 D6 D7
```

Parity bits are calculated based on even parity rules for specific groups of bits.

### Error Detection and Correction:

When an error occurs, the "syndrome" (calculated from parity checks) identifies the position of the error. For example:

```
Original Message:   0b1011011
Message with Error: 0b1011111
Syndrome:           011 (binary) = Position 3
Corrected Message:  0b1011011
```

### Code Structure

### Functions:

1. calculate_redundant_bits(m): Calculates the number of redundant bits required for m data bits.

2. position_redundant_bits(data): Inserts redundant bits at positions that are powers of 2.

3. calculate_parity_bits(encoded_data, r): Computes parity values for redundant bits.

4. hamming_encode(data): Encodes input data using Hamming Code.

5. detect_and_correct_error(encoded_data): Detects and corrects single-bit errors in encoded data.

6. hamming_decode(encoded_data): Decodes the corrected message to retrieve original data.

###Usage
Prerequisites
. Python 3.x installed on your system.

Running the Code

1. Clone this repository:

```
git clone git@github.com:bharathkreddy/information_theory.git
cd information_theory
```

2. Run the code

```
python hamming_code.py
```

3. Input your data (4-bit binary string) when prompted.
   Example output

```
Original data: 1011
Encoded message: [0, 1, 0, 1, 0, 1, 1]
Message with error: [0, 1, 1, 1, 0, 1, 1]
Error detected at position: 3
Error corrected.
Decoded message: 1011
```

## Contribution

Feel free to contribute by submitting issues or pull requests! If you have suggestions for improving this implementation or adding features like multi-bit error detection, let me know!

## Future additions

1. Reed Solomon codes
2. Turbo codes
3. LDPC codes.

## Author

Bharath k. Reddy
