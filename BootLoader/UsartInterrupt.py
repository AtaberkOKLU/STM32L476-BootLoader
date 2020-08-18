import serial
from time import sleep


# CONFIGURATIONS
_BAUD_RATE       = 115200
_PORT            = "COM5"
_SERIAL_TIMEOUT  = 10
_BYTE_SIZE       = 8
_STOP_BITS       = serial.STOPBITS_ONE
_PARITY          = serial.PARITY_EVEN

# COMM CONSTANTS
_ACK        = b'\x79'

_UART_SELEC = b'\x7F'


# Serial Object Init with proper parameters


serialPort = serial.Serial(port=_PORT,
                           baudrate=_BAUD_RATE,
                           timeout=_SERIAL_TIMEOUT, #DISABLE READ TIMEOUT
                           stopbits=_STOP_BITS,
                           bytesize=_BYTE_SIZE,
                           parity=_PARITY)

# serialPort.open()
serialPort.write(_UART_SELEC)
# serialPort.close()
