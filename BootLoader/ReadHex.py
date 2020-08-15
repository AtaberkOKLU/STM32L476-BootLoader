from intelhex import IntelHex

# CONFIGURATIONS
_BUFFER_SIZE     = 256

# IntelHex Object Initiation

intelHex = IntelHex()

# HEX FILE SELECTION

_file_name = str(input("HEX File Name to be uploaded:"))

# Get Data From HEX File
intelHex.fromfile(_file_name+".hex", format='hex')      # Read Hex File
hex_dict = intelHex.todict()                            # Dump into DICT Object

hex_byte_list = list(hex_dict.values())                 # Convert to list
hex_byte_list.pop()                                     # POP: {'EIP': 134218121}
print("FILE-Decimal Bytes:", hex_byte_list)             # All bytes in decimal form

hex_chunk_list = [hex_byte_list[i: i + _BUFFER_SIZE]    # Creating new list: Chunk List
  for i in range(0, len(hex_byte_list), _BUFFER_SIZE)]  # Each containing specified many

print("\nChunks:", hex_chunk_list)                      # See Chunks
print('\n1st Chunk (HEX): [{}]'.format(', '             # See First Chunk in HEX
            .join(hex(x) for x in hex_chunk_list[0])))  # HEX Conversion (CHECKING)

# Some Other Information
print("\nGeneral Code Information:")
print("Total # of Bytes:\t\t", len(hex_byte_list))
print("Buffer Size:\t\t\t", _BUFFER_SIZE)
print("Total # of Chunks:\t\t", len(hex_chunk_list))
print("# of Last Chunk bytes:\t", len(hex_chunk_list[-1]))
