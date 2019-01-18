# Vigenere_Cipher

The Vigenere Cipher, once considered the unbreakable cihper, was created in the 16th century. The Vigenere Cipher uses a polyalphabetic algorithm to encrypt a message based on the key, which should be a difficult to predict and preferrably lengthy word.

The core algorithm of this cipher iterates over each letter of the message simutaneously with the key. If the key is shorter than the message, the iterator will continue to wrap around the key index value until the entire message is encrypted. The letters selected are converted to integers for addition (encryption) or subtraction (decryption), then they are converted back to letters.

A message "hello world" encrypted with a key "abcd" will return "hfnoo xqule".
Note that the third and fourth letters of the message are "ll" but the third and fourth letters of the cipher text are "no". This means repeating plain text letters may not be repeating in the cipher text, thwarting mono-alphabetic substitution cipher attack vectors.

Attack vectors for the Vigenere Cipher include a modified monographic phi test, statistical key length tests, dictionary attacks, and brute force attacks on key lengths shorter than 9 letters (depending on cryptanalytic resources).

A key that is equivalent in length to the message is called a "One-Time Pad" and is hypothetically unbreakable if the key is selected entirely at random (NO computer PRNG). The "One-Time Pad" is the grandfather to modern bitwise stream ciphers such as ARC-4, Salsa-20, Two-fish, Blowfish, etc.

#TODO include attack vectors
