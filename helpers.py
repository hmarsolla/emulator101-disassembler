def get_registers(source, offset, position, address):
    """This function will retrieve the memory register argument present in the hexdump"""
    registers = ''

    for x in range(1, offset+1):
        next_byte = source[position + x * 2] + source[position + x*2 +1]
        registers = next_byte + registers

    registers = address + registers
    return registers

#This dictionary has the opcodes as keys and the tuple in the value has the instruction, size and memory register arguments if any:
opcodes8080 = {
    '00' : ('NOP', 1, None),
    '01' : ('LXI', 3, 'B,$'),
    '02' : ('STAX', 1, 'B'),
    '03' : ('INX', 1, 'B'),
    '04' : ('INR', 1, 'B'),
    '05' : ('DCR', 1, 'B'),
    '06' : ('MVI', 2, 'B,$'),
    '07' : ('RLC', 1, None),
    '08' : (None, None, None),
    '09' : ('DAD', 1, 'B'),
    '0a' : ('LDAX', 1, 'B'),
    '0b' : ('DCX', 1, 'B'),
    '0c' : ('INR', 1, 'C'),
    '0d' : ('DCR', 1, 'C'),
    '0e' : ('MVI', 2, 'C,$'),
    '0f' : ('RRC', 1, None),
    '10' : (None, None, None),
    '11' : ('LXI', 3, 'D,$'),
    '12' : ('STAX', 1, 'D'),
    '13' : ('INX', 1, 'D'),
    '14' : ('INR', 1, 'D'),
    '15' : ('DCR', 1, 'D'),
    '16' : ('MVI', 2, 'D,$'),
    '17' : ('RAL', 1, None),
    '18' : (None, None, None),
    '19' : ('DAD', 1, 'D'),
    '1a' : ('LDAX', 1, 'D'),
    '1b' : ('DCX', 1, 'D'),
    '1c' : ('INR', 1, 'E'),
    '1d' : ('DCR', 1, 'E'),
    '1e' : ('MVI', 2, 'E,$'),
    '1f' : ('RAR', 1, None),
    '20' : ('RIM', 1, None),
    '21' : ('LXI', 3, 'H,$'),
    '22' : ('SHLD', 1, '$'),
    '23' : ('INX', 1, 'H'),
    '24' : ('INR', 1, 'H'),
    '25' : ('DCR', 1, 'H'),
    '26' : ('MVI', 2, 'H,$'),
    '27' : ('DAA', 1, None),
    '28' : (None, None, None),
    '29' : ('DAD', 1, 'H'),
    '2a' : ('LHLD', 3, '$'),
    '2b' : ('DCX', 1, 'H'),
    '2c' : ('INR', 1, 'L'),
    '2d' : ('DCR', 1, 'L'),
    '2e' : ('MVI', 2, 'L,$'),
    '2f' : ('CMA', 1, None),
    '30' : ('SIM', 1, None),
    '31' : ('LXI', 3, 'SP,$'),
    '32' : ('STA', 3, '$'),
    '33' : ('INX', 1, 'SP'),
    '34' : ('INR', 1, 'M'),
    '35' : ('DCR', 1, 'M'),
    '36' : ('MVI', 2, 'M,$'),
    '37' : ('STC', 1, None),
    '38' : (None, None, None),
    '39' : ('DAD', 1, 'SP'),
    '3a' : ('LDA', 3, '$'),
    '3b' : ('DCX', 1, 'SP'),
    '3c' : ('INR', 1, 'A'),
    '3d' : ('DCR', 1, 'A'),
    '3e' : ('MVI', 2, 'A,$'),
    '3f' : ('CMC', 1, None),
    '40' : ('MOV', 1, 'B,B'),
    '41' : ('MOV', 1, 'B,C'),
    '42' : ('MOV', 1, 'B,D'),
    '43' : ('MOV', 1, 'B,E'),
    '44' : ('MOV', 1, 'B,H'),
    '45' : ('MOV', 1, 'B,L'),
    '46' : ('MOV', 1, 'B,M'),
    '47' : ('MOV', 1, 'B,A'),
    '48' : ('MOV', 1, 'C,B'),
    '49' : ('MOV', 1, 'C,C'),
    '4a' : ('MOV', 1, 'C,D'),
    '4b' : ('MOV', 1, 'C,E'),
    '4c' : ('MOV', 1, 'C,H'),
    '4d' : ('MOV', 1, 'C,L'),
    '4e' : ('MOV', 1, 'C,M'),
    '4f' : ('MOV', 1, 'C,A'),
    '50' : ('MOV', 1, 'D,B'),
    '51' : ('MOV', 1, 'D,C'),
    '52' : ('MOV', 1, 'D,D'),
    '53' : ('MOV', 1, 'D,E'),
    '54' : ('MOV', 1, 'D,H'),
    '55' : ('MOV', 1, 'D,L'),
    '56' : ('MOV', 1, 'D,M'),
    '57' : ('MOV', 1, 'D,A'),
    '58' : ('MOV', 1, 'E,B'),
    '59' : ('MOV', 1, 'E,C'),
    '5a' : ('MOV', 1, 'E,D'),
    '5b' : ('MOV', 1, 'E,E'),
    '5c' : ('MOV', 1, 'E,H'),
    '5d' : ('MOV', 1, 'E,L'),
    '5e' : ('MOV', 1, 'E,M'),
    '5f' : ('MOV', 1, 'E,A'),
    '60' : ('MOV', 1, 'H,B'),
    '61' : ('MOV', 1, 'H,C'),
    '62' : ('MOV', 1, 'H,D'),
    '63' : ('MOV', 1, 'H,E'),
    '64' : ('MOV', 1, 'H,H'),
    '65' : ('MOV', 1, 'H,L'),
    '66' : ('MOV', 1, 'H,M'),
    '67' : ('MOV', 1, 'H,A'),
    '68' : ('MOV', 1, 'L,B'),
    '69' : ('MOV', 1, 'L,C'),
    '6a' : ('MOV', 1, 'L,D'),
    '6b' : ('MOV', 1, 'L,E'),
    '6c' : ('MOV', 1, 'L,H'),
    '6d' : ('MOV', 1, 'L,L'),
    '6e' : ('MOV', 1, 'L,M'),
    '6f' : ('MOV', 1, 'L,A'),
    '70' : ('MOV', 1, 'M,B'),
    '71' : ('MOV', 1, 'M,C'),
    '72' : ('MOV', 1, 'M,D'),
    '73' : ('MOV', 1, 'M,E'),
    '74' : ('MOV', 1, 'M,H'),
    '75' : ('MOV', 1, 'M,L'),
    '76' : ('HLT', 1, None),
    '77' : ('MOV', 1, 'M,A'),
    '78' : ('MOV', 1, 'A,B'),
    '79' : ('MOV', 1, 'A,C'),
    '7a' : ('MOV', 1, 'A,D'),
    '7b' : ('MOV', 1, 'A,E'),
    '7c' : ('MOV', 1, 'A,H'),
    '7d' : ('MOV', 1, 'A,L'),
    '7e' : ('MOV', 1, 'A,M'),
    '7f' : ('MOV', 1, 'A,A'),
    '80' : ('ADD', 1, 'B'),
    '81' : ('ADD', 1, 'C'),
    '82' : ('ADD', 1, 'D'),
    '83' : ('ADD', 1, 'E'),
    '84' : ('ADD', 1, 'H'),
    '85' : ('ADD', 1, 'L'),
    '86' : ('ADD', 1, 'M'),
    '87' : ('ADD', 1, 'A'),
    '88' : ('ADC', 1, 'B'),
    '89' : ('ADC', 1, 'C'),
    '8a' : ('ADC', 1, 'D'),
    '8b' : ('ADC', 1, 'E'),
    '8c' : ('ADC', 1, 'H'),
    '8d' : ('ADC', 1, 'L'),
    '8e' : ('ADC', 1, 'M'),
    '8f' : ('ADC', 1, 'A'),
    '90' : ('SUB', 1, 'B'),
    '91' : ('SUB', 1, 'C'),
    '92' : ('SUB', 1, 'D'),
    '93' : ('SUB', 1, 'E'),
    '94' : ('SUB', 1, 'H'),
    '95' : ('SUB', 1, 'L'),
    '96' : ('SUB', 1, 'M'),
    '97' : ('SUB', 1, 'A'),
    '98' : ('SBB', 1, 'B'),
    '99' : ('SBB', 1, 'C'),
    '9a' : ('SBB', 1, 'D'),
    '9b' : ('SBB', 1, 'E'),
    '9c' : ('SBB', 1, 'H'),
    '9d' : ('SBB', 1, 'L'),
    '9e' : ('SBB', 1, 'M'),
    '9f' : ('SBB', 1, 'A'),
    'a0' : ('ANA', 1, 'B'),
    'a1' : ('ANA', 1, 'C'),
    'a2' : ('ANA', 1, 'D'),
    'a3' : ('ANA', 1, 'E'),
    'a4' : ('ANA', 1, 'H'),
    'a5' : ('ANA', 1, 'L'),
    'a6' : ('ANA', 1, 'M'),
    'a7' : ('ANA', 1, 'A'),
    'a8' : ('XNA', 1, 'B'),
    'a9' : ('XNA', 1, 'C'),
    'aa' : ('XNA', 1, 'D'),
    'ab' : ('XNA', 1, 'E'),
    'ac' : ('XNA', 1, 'H'),
    'ad' : ('XNA', 1, 'L'),
    'ae' : ('XNA', 1, 'M'),
    'af' : ('XNA', 1, 'A'),
    'b0' : ('ORA', 1, 'B'),
    'b1' : ('ORA', 1, 'C'),
    'b2' : ('ORA', 1, 'D'),
    'b3' : ('ORA', 1, 'E'),
    'b4' : ('ORA', 1, 'H'),
    'b5' : ('ORA', 1, 'L'),
    'b6' : ('ORA', 1, 'M'),
    'b7' : ('ORA', 1, 'A'),
    'b8' : ('CMP', 1, 'B'),
    'b9' : ('CMP', 1, 'C'),
    'ba' : ('CMP', 1, 'D'),
    'bb' : ('CMP', 1, 'E'),
    'bc' : ('CMP', 1, 'H'),
    'bd' : ('CMP', 1, 'L'),
    'be' : ('CMP', 1, 'M'),
    'bf' : ('CMP', 1, 'A'),
    'c0' : ('RNZ', 1, None),
    'c1' : ('POP', 1, 'B'),
    'c2' : ('JNZ', 3, '$'),
    'c3' : ('JMP', 3, '$'),
    'c4' : ('CNZ', 3, '$'),
    'c5' : ('PUSH', 1, 'B'),
    'c6' : ('ADI', 2, '$'),
    'c7' : ('RST', 1, '0'),
    'c8' : ('RZ', 1, None),
    'c9' : ('RET', 1, None),
    'ca' : ('JZ', 3, '$'),
    'cb' : (None, None, None),
    'cc' : ('CZ', 3, '$'),
    'cd' : ('CALL', 3, '$'),
    'ce' : ('ACI', 2, '$'),
    'cf' : ('RST', 1, '1'),
    'd0' : ('RNC', 1, None),
    'd1' : ('POP', 1, 'D'),
    'd2' : ('JNC', 3, '$'),
    'd3' : ('OUT', 2, '$'),
    'd4' : ('CNC', 3, '$'),
    'd5' : ('PUSH', 1, 'D'),
    'd6' : ('SUI', 2, '$'),
    'd7' : ('RST', 1, '2'),
    'd8' : ('RC', 1, None),
    'd9' : (None, None, None),
    'da' : ('JC', 3, '$'),
    'db' : ('IN', 2, '$'),
    'dc' : ('CC', 3, '$'),
    'dd' : (None, None, None),
    'de' : ('SBI', 2, '$'),
    'df' : ('RST', 1, '3'),
    'e0' : ('RPO', 1, None),
    'e1' : ('POP', 1, 'H'),
    'e2' : ('JPO', 3, '$'),
    'e3' : ('XTHL', 1, None),
    'e4' : ('CPO', 3, '$'),
    'e5' : ('PUSH', 1, 'H'),
    'e6' : ('ANI', 2, '$'),
    'e7' : ('RST', 1, '4'),
    'e8' : ('RPE', 1, None),
    'e9' : ('PCHL', 1, None),
    'ea' : ('JPE', 3, '$'),
    'eb' : ('XCHG', 1, None),
    'ec' : ('CPE', 3, '$'),
    'ed' : (None, None, None),
    'ee' : ('XRI', 2, '$'),
    'ef' : ('RST', 1, '5'),
    'f0' : ('RP', 1, None),
    'f1' : ('POP', 1, 'PSW'),
    'f2' : ('JP', 3, '$'),
    'f3' : ('DI', 1, None),
    'f4' : ('CP', 3, '$'),
    'f5' : ('PUSH', 1, 'PSW'),
    'f6' : ('ORI', 2, '$'),
    'f7' : ('RST', 1, '6'),
    'f8' : ('RM', 1, None),
    'f9' : ('SPHL', 1, None),
    'fa' : ('JM', 3, '$'),
    'fb' : ('EI', 1, None),
    'fc' : ('CM', 3, '$'),
    'fd' : (None, None, None),
    'fe' : ('CPI', 2, '$'),
    'ff' : ('RST', 1, '7')
}

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	