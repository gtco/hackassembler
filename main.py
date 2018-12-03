import sys
from instruction import Instruction

instructions = []


def parse(line):
    i = None
    line = line.strip(' \r\n')
    if len(line) > 0 and not line.startswith('//'):
        if line.startswith('('):
            # Todo Implement symbol table
            print("Label " + line)
        else:
            i = Instruction(line)
    return i


with open(sys.argv[1]) as f:
    for line in f:
        i = parse(line)
        if i is not None:
            instructions.append(i)

idx = sys.argv[1].find('.asm')
if idx >= 0:
    hack_file = sys.argv[1][:idx] + ".hack"
    with open(hack_file, mode='w') as f:
        for i in instructions:
            f.write(i.emit())
