import random 

def BER(message, ber):  # Transmission of the message and CRC through a noisy channel with Bit Error Rate (BER)
    ber_message = message.copy()
    error = 0
    for i in range(len(ber_message)):
        if random.random() < ber:
            error = 1
            ber_message[i] = 1 - ber_message[i]
    return ber_message, error            

def calc_fcs(message, p):  # CRC (FCS) Calculation
    d = message.copy()
    while len(d) >= len(p):
        if d[0] == 1:
            for i in range(len(p)):
                d[i] = d[i] ^ p[i]  # XOR
        d.pop(0) 
    return d    

def random_message(k):  # Generation of a randomly selected k-bit binary message
    message = []
    for i in range(k):
        message.append(random.randint(0, 1))
    return message    
        
# Main program
k = int(input("Enter the number of bits of the binary message: "))
pol = list(input("Enter the binary number P: "))
ber = float(input("Enter the Bit Error Rate (BER): "))
p = []
for i in pol:
    p.append(int(i))
n = len(p) - 1 + k
messagesWithErrorCRC = 0  # Messages detected as erroneous by the CRC
totalMessagesWithError = 0  # Erroneous messages, even those not detected by the CRC
nc = 1000000
for ct in range(nc):
    message = random_message(k)
    print("Random message: ", message)

    message0 = message + [0] * (n - k)
    fcs = calc_fcs(message0, p)
    print("CRC(FCS): ", fcs)

    T = message + fcs
    print("Total sequence T of n bits: ", T)
    ber_t, messageWithError = BER(T, ber)
    print("Transmitted message: ", ber_t)
    
    totalMessagesWithError += messageWithError
        
    # CRC Check at the receiver
    mod = sum(calc_fcs(ber_t, p))
    if mod == 0:
        print("The message contains no errors based on the CRC.")
    else:
        print("The message contains errors based on the CRC.")
        messagesWithErrorCRC += 1

print("\nNumber of messages arriving with an error at the receiver: ", totalMessagesWithError)        
print("Number of messages detected as erroneous by the CRC: ", messagesWithErrorCRC)   
print("Number of messages not detected as erroneous by the CRC: ", totalMessagesWithError - messagesWithErrorCRC) 

totalMessagesRateWithError = '{:.3f}'.format(float(totalMessagesWithError) / nc * 100)
print("\nPercentage of messages arriving with an error at the receiver: ", totalMessagesRateWithError, "%")
messageRateWithErrorCRC = '{:.3f}'.format(float(messagesWithErrorCRC) / nc * 100)
print("Percentage of messages detected as erroneous by the CRC: ", messageRateWithErrorCRC, "%")
print("Percentage of messages not detected as erroneous by the CRC:", '{:.3f}'.format((totalMessagesWithError - messagesWithErrorCRC) / nc * 100), "%")
