import binascii
import sys
from helpers import get_registers, opcodes8080

#File Reading
source_file = str(sys.argv[1])
output_file_name = source_file.split('.')[0] + "_disassembled.txt"

with open(source_file, 'rb') as f:
    source_code = f.read()

hex_dump = binascii.hexlify(source_code).decode()
bit_size = int(len(hex_dump) / 2)

output = ""
opcode = 0
data_address_bytes = 0

for x in range(bit_size):

    if data_address_bytes > 0:
        data_address_bytes -= 1
        opcode += 1
        continue
    
    position = (x * 2)

    byte = hex_dump[position] + hex_dump[position + 1]

    opcode_tuple = opcodes8080[byte]
    instruction = opcode_tuple[0]
    if not instruction:
        continue
    
    offset = opcode_tuple[1] - 1
    op_register = opcode_tuple[2] if opcode_tuple[2] else ""

    if offset > 0:
        arguments = get_registers(hex_dump, offset, position, op_register)
    else:
        arguments = op_register

    output += hex(opcode) + "\t" + instruction + "\t" + arguments + "\n"
    opcode += 1

with open(output_file_name, "w") as f:
    f.write(output)