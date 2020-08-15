import serial
from time import sleep


# Color Class
class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# CONFIGURATIONS
_BAUD_RATE       = 115200
_PORT            = "COM5"
_SERIAL_TIMEOUT  = 10
_BYTE_SIZE       = 8
_STOP_BITS       = serial.STOPBITS_ONE
_PARITY          = serial.PARITY_EVEN

# COMM CONSTANTS
_ACK        = b'\x79'
_NACK       = b'\x1F'
_GET_CMD    = b'\x00\xFF'
_GV_CMD     = b'\x01\xFE'
_GED_ID_CMD = b'\x02\xFD'
_WRITE_CMD  = b'\x31\xCE'
_READ_CMD   = b'\x11\xEE'
_GO_CMD     = b'\x21\xDE'
_ERASE_CMD  = b'\x43\xBC'

_UART_SELEC = b'\x7F'
ACK_counter = 0

# Serial Object Init with proper parameters


serialPort = serial.Serial(port=_PORT,
                           baudrate=_BAUD_RATE,
                           timeout=_SERIAL_TIMEOUT, #DISABLE READ TIMEOUT
                           stopbits=_STOP_BITS,
                           bytesize=_BYTE_SIZE,
                           parity=_PARITY)

# serialPort.open()
print(f"{Bcolors.OKBLUE}UARTx SELECTION CMD:", _UART_SELEC, f"{Bcolors.ENDC}")
serialPort.write(_UART_SELEC)
sleep(1)
char = serialPort.read()
if char == _ACK:
    print(f"{Bcolors.OKGREEN}Received ACK | UARTx SUCCESS{Bcolors.ENDC}")
elif char == _NACK:
    print(f"{Bcolors.FAIL}Received NACK | UARTx FAILED{Bcolors.ENDC}")
sleep(1)
print(f"{Bcolors.OKBLUE}Sending GET CMD:{Bcolors.ENDC}", _GV_CMD)
serialPort.write(_GV_CMD)
sleep(1)
while True:
    char = serialPort.read()
    if char == _NACK:
        print(f"{Bcolors.FAIL}Received NACK | CMD FAILED{Bcolors.ENDC}")
        break
    elif char == _ACK and ACK_counter == 0:
        print(f"{Bcolors.OKGREEN}Received ACK | CMD STARTED{Bcolors.ENDC}")
        ACK_counter += 1
    elif char == _ACK and ACK_counter:
        print(f"{Bcolors.OKGREEN}Received ACK | CMD SUCCESS{Bcolors.ENDC}")
        break
    else:
        print(f"{Bcolors.HEADER}Response:", char, f"{Bcolors.ENDC}")

serialPort.close()
