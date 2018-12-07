import sys
from instruction import Instruction
from symbol_table import SymbolTable

instructions = []
symbol_table = SymbolTable()

def strip_line(line):
    line = line.strip(' \r\n')
    if len(line) > 0:
        comment = line.rfind('//')
        if comment >= 0:
            line = line[:comment].strip(' \r\n')
    return line

def first_pass(line, address):
    line = strip_line(line)
    if len(line) > 0:    
        if line.startswith('('):
            rparen = line.rfind(')')
            label = line[1:rparen]
            symbol_table.add_label(label, address)
        else:
            address += 1
    return address

def second_pass(line):
    i = None
    line = strip_line(line)
    if len(line) > 0:
        if line.startswith('('):
            pass
        else:
            i = Instruction(line, symbol_table)
    return i

def emit(filename):
    line_count = 0
    with open(filename, mode='w') as f:
        for i in instructions:
            f.write(i.emit())
            line_count += 1
    print("Wrote (" + str(line_count) + ") lines to " + filename)

def main(argv):
    address = 0
    with open(argv[1]) as f:
        for line in f:
            address = first_pass(line, address)
        f.seek(0)
        for line in f:
            i = second_pass(line)
            if i is not None:
                instructions.append(i)
    idx = argv[1].find('.asm')
    if idx >= 0:
        hack_file = argv[1][:idx] + ".hack"
        emit(hack_file)

if __name__ == "__main__":
    main(sys.argv)
