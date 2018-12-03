class Instruction:

    jump_keywords = {'JGT': 0b001,
                     'JEQ': 0b010,
                     'JGE': 0b011,
                     'JLT': 0b100,
                     'JNE': 0b101,
                     'JLE': 0b110,
                     'JMP': 0b111}

    dest_keywords = {'M': 0b1000,
                     'D': 0b10000,
                     'MD': 0b11000,
                     'A': 0b100000,
                     'AM': 0b101000,
                     'AD': 0b110000,
                     'AMD': 0b111000}

    comp_keywords = {'0':  0b0101010000000, '1':  0b0111111000000,
                     '-1':  0b0111010000000, 'D':  0b0001100000000,
                     'A':  0b0110000000000, '!D':  0b0001101000000,
                     '!A':  0b0110001000000, '-D':  0b0001111000000,
                     '-A':  0b0110011000000, 'D+1':  0b0011111000000,
                     'A+1':  0b0110111000000, 'D-1':  0b0001110000000,
                     'A-1':  0b0110010000000, 'D+A':  0b0000010000000,
                     'D-A':  0b0010011000000, 'A-D':  0b0000111000000,
                     'D&A':  0b0000000000000, 'D|A':  0b0010101000000,
                     'M':  0b1110000000000, '!M':  0b1110001000000,
                     '-M':  0b1110011000000, 'M+1':  0b1110111000000,
                     'M-1':  0b1110010000000, 'D+M':  0b1000010000000,
                     'D-M':  0b1010011000000, 'M-D':  0b1000111000000,
                     'D&M':  0b1000000000000, 'D|M':  0b1010101000000}

    def __init__(self, text):
        self.text = text
        if self.text.startswith('@'):
            self.instruction_type = "A"
            self.address = self.text[1:]
            if self.address.isdigit():
                self.value = int(self.address)
            else:
                raise ValueError("Expected an integer value " + self.text)
        else:
            self.instruction_type = "C"
            self.value = 0b1110000000000000
            ci = self.text.find('=')
            ji = self.text.find(';')
            dest, dest, jump = '', '', ''
            if ci > 0 and ji > 0:
                # dest=comp;jump
                dest = self.text[:ci]
                comp = self.text[ci+1:ji]
                jump = self.text[ji+1:]
            elif ci < 0 and ji > 0:
                # comp;jump
                comp = self.text[:ji]
                jump = self.text[ji+1:]
            elif ci > 0 and ji < 0:
                # dest=comp
                dest = self.text[:ci]
                comp = self.text[ci+1:]
            elif ci < 0 and ji < 0:
                # comp
                comp = self.text
            if len(dest) > 0:
                self.value += self.dest_keywords[dest]
            if len(comp) > 0:
                self.value += self.comp_keywords[comp]
            if len(jump) > 0:
                self.value += self.jump_keywords[jump]

    def emit(self):
        return format(int(self.value), 'b').zfill(16) + '\n'
