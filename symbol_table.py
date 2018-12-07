class SymbolTable:
        def __init__(self):
            self.last_variable = 0x0010
            self.table = {}
            self.table['SP'] = 0x00
            self.table['LCL'] = 0x01
            self.table['ARG'] = 0x02
            self.table['THIS'] = 0x03
            self.table['THAT'] = 0x04
            self.table['SCREEN'] = 0x4000
            self.table['KBD'] = 0x6000                        
            for i in range(0,16):
                register = 'R{0}'.format(i)
                self.table[register] = i
        
        def add_label(self, symbol, address):
            self.table[symbol] = address

        def contains(self, symbol):
            return symbol in self.table

        def get_address(self, symbol):
            return self.table[symbol]

        def add_variable(self, symbol):
            address = self.last_variable
            self.table[symbol] = address            
            self.last_variable += 1
            return address
