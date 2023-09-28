# How it works

def cipher(message, key, skey):
    message = str(message)
    key = str(key)
    skey = str(skey)
    # Needed lists
    messageCIPHER = []
    keyCIPHER = []
    keyASCII2 = []
    skeyASCII = []

    # Divide string in two parts (avoiding generating more than two parts)
    keyPARTS = []
    n = len(key) // 2
    for partnumber, i in enumerate(range(0, len(key), n), start=1):
        if partnumber <= 2:
            keyPARTS.append(key[i: i + n])
        else:
            keyPARTS[1] = keyPARTS[1] + key[i: i + n]

    messageASCII = [ord(char) for char in message]
    keyASCII1 = [ord(char) for char in keyPARTS[0]]
    for char in keyPARTS[1]:
        keyASCII2.append(ord(char))
    keyASCII = [ord(char) for char in key]
    for char in skey:
        skeyASCII.append(ord(char))

    # Cipher
    counterEven = 0
    counterOdd = 0
    for i in range(0, len(messageASCII)):
        if (i % 2) == 0:
            # Use the first part of the key
            counterEven += 1
            if counterEven > len(keyASCII1) - 1:
                counterEven = 0
            cipherResult = int(messageASCII[i]) + int(keyASCII1[counterEven])
        else:
            # Use the second part of the key
            counterOdd += 1
            if counterOdd > len(keyASCII2) - 1:
                counterOdd = 0
            cipherResult = int(messageASCII[i]) + int(keyASCII2[counterOdd])
        while (cipherResult > 125) or (cipherResult < 32):
            if cipherResult > 125:
                cipherResult = 31 + (cipherResult - 125)
            if cipherResult < 32:
                cipherResult = 126 - (32 - cipherResult)
        messageCIPHER.append(cipherResult)
    messageCIPHERAscii = [chr(char) for char in messageCIPHER]
    # Cipher the key
    counterSkey = 0
    for i in range(0, len(keyASCII)):
        counterSkey += 1
        if counterSkey > len(skeyASCII) - 1:
            counterSkey = 0
        cipherResult = int(keyASCII[i]) + int(skeyASCII[counterSkey])
        while (cipherResult > 125) or (cipherResult < 32):
            if cipherResult > 125:
                cipherResult = 31 + (cipherResult - 125)
            if cipherResult < 32:
                cipherResult = 126 - (32 - cipherResult)
        keyCIPHER.append(cipherResult)

    keyCIPHERAscii = [chr(char) for char in keyCIPHER]
    # Return a string
    messageCIPHERstr = ""
    for i in messageCIPHERAscii:
        messageCIPHERstr = messageCIPHERstr + i
    keyCIPHERstr = ""
    for i in keyCIPHERAscii:
        keyCIPHERstr = keyCIPHERstr + i

    return messageCIPHERstr, keyCIPHERstr


def decipher(message, key, securekey):
    message = str(message)
    key = str(key)
    securekey = str(securekey)
    keyDECIPHER = []
    keyDECIPHERParts = []
    messageDECIPHERAscii = []
    messageDECIPHERchar = []

    messageCIPHERAscii = [ord(char) for char in message]
    keyCIPHER = [ord(char) for char in key]
    skeyASCII = [ord(char) for char in securekey]
    # Decipher the key
    counterSkey = 0
    for i in range(0, len(keyCIPHER)):
        counterSkey += 1
        if counterSkey > len(skeyASCII) - 1:
            counterSkey = 0
        cipherResult = int(keyCIPHER[i]) - int(skeyASCII[counterSkey])
        while (cipherResult > 125) or (cipherResult < 32):
            if cipherResult > 125:
                cipherResult = 31 + (cipherResult - 125)
            if cipherResult < 32:
                cipherResult = 126 - (32 - cipherResult)
        keyDECIPHER.append(cipherResult)

    keyDECIPHERChar = [chr(char) for char in keyDECIPHER]
    # Divide the key deciphered
    n = len(key) // 2
    for partnumber, i in enumerate(range(0, len(keyDECIPHERChar), n), start=1):
        if partnumber <= 2:
            keyDECIPHERParts.append(keyDECIPHERChar[i: i + n])
        else:
            keyDECIPHERParts[1] = keyDECIPHERParts[1] + keyDECIPHERChar[i: i + n]
    keyDECIPHERParts1 = [ord(char) for char in keyDECIPHERParts[0]]
    keyDECIPHERParts2 = [ord(char) for char in keyDECIPHERParts[1]]
    # Copy the functions to cipher but to decipher
    counterEven = 0
    counterOdd = 0
    for i in range(0, len(messageCIPHERAscii)):
        if (i % 2) == 0:
            # Use the first part of the key
            counterEven += 1
            if counterEven > len(keyDECIPHERParts1) - 1:
                counterEven = 0
            cipherResult = int(messageCIPHERAscii[i]) - int(keyDECIPHERParts1[counterEven])
        else:
            # Use the second part of the key
            counterOdd += 1
            if counterOdd > len(keyDECIPHERParts2) - 1:
                counterOdd = 0
            cipherResult = int(messageCIPHERAscii[i]) - int(keyDECIPHERParts2[counterOdd])
        while (cipherResult > 125) or (cipherResult < 32):
            if cipherResult > 125:
                cipherResult = 31 + (cipherResult - 125)
            if cipherResult < 32:
                cipherResult = 126 - (32 - cipherResult)
        messageDECIPHERAscii.append(cipherResult)
    for char in messageDECIPHERAscii:
        messageDECIPHERchar.append(chr(char))

    # Return a string
    messageDECIPHERAsciistr = ""
    for i in messageDECIPHERchar:
        messageDECIPHERAsciistr = messageDECIPHERAsciistr + i
    keyDECIPHERstr = ""
    for i in keyDECIPHERChar:
        keyDECIPHERstr = keyDECIPHERstr + i

    return messageDECIPHERAsciistr, keyDECIPHERstr


if __name__ == "__main__":
    message = "a simple message"
    key = "casualkeytouse"
    skey = "evenbetter"

    print("==TESTING MODE==")
    print("=====")
    print("Testing '" + message + "' encoded with '" + key + "' secured by '" + skey + "'")
    print("=====")
    messaggio_cifrato, chiave_cifrata = cipher(message, key, skey)
    print(messaggio_cifrato)
    print(chiave_cifrata)
    print("=====")
    print("Decoding '" + message + "' encoded with '" + key + "' secured by '" + skey + "'")
    print("=====")
    messaggio_decifrato, chiave_decifrata = decipher(messaggio_cifrato, chiave_cifrata, "evenbetter")
    print(messaggio_decifrato)
    print(chiave_decifrata)
