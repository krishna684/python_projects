# Caesar Cipher

Implements the Caesar cipher encryption and decryption algorithm.

## Files
- `caesar.py` - Caesar cipher implementation

## Description
This program implements the classic Caesar cipher, which:
- Shifts letters by a fixed number of positions (key)
- Supports both encryption and decryption
- Preserves non-alphabetic characters
- Works with any shift value (uses modulo for wrapping)
- Handles multiple messages in one session

## How to Run
```bash
python caesar.py
```

## Usage
```
Enter a message: hello world
Enter a shift key: 3
Encrypt (e) or decrypt (d): e
Encrypted message: khoor zruog

Enter a message: khoor zruog
Encrypt (e) or decrypt (d): d
Decrypted message: hello world
```

## Features
- Case-insensitive processing (output in lowercase)
- Non-letter characters preserved
- Input validation
- Modular function design
- Support for multiple operations in one session

## How It Works
- **Encryption**: Shift each letter forward by key positions
- **Decryption**: Shift each letter backward by key positions
- Example with shift 3: a→d, b→e, c→f, etc.
