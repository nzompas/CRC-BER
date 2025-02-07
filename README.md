# Bit Error Rate (BER) Simulation with CRC (FCS) Detection

This repository contains a Python implementation that simulates the transmission of a binary message through a noisy channel, applying a Cyclic Redundancy Check (CRC) for error detection. The simulation computes the Bit Error Rate (BER), calculates the Frame Check Sequence (FCS), and assesses the error detection performance of the CRC algorithm.

## Features

- **Bit Error Rate (BER) Simulation**: Introduces noise to the binary message based on a given BER value.
- **CRC Calculation**: Implements the Cyclic Redundancy Check (CRC) algorithm to detect errors in the transmitted message.
- **Simulation of Errors**: Simulates message transmission over a noisy channel and checks if errors are detected by CRC.
- **Statistical Reporting**: Outputs statistics regarding the error detection capabilities of the CRC and the overall reliability of the transmission.

## How it Works

1. **Input Parameters**:
    - The number of bits in the binary message.
    - The binary polynomial `P` used for CRC calculation.
    - The Bit Error Rate (BER) value that determines how often a bit flips during transmission.

2. **Transmission Simulation**:
    - A random binary message is generated.
    - The message is appended with CRC (FCS) bits calculated using the polynomial `P`.
    - The message is then transmitted over a noisy channel, where each bit has a chance to flip according to the given BER.

3. **Error Detection**:
    - At the receiver side, the CRC is recalculated and compared with the received CRC. If the values don't match, an error is detected.
    - A count of the total errors and the errors detected by the CRC is provided.

4. **Statistics**:
    - The total percentage of messages that experience errors.
    - The percentage of messages where errors are detected by the CRC.
    - The percentage of messages where errors go undetected by the CRC.
