class DES:
    key = None

    #initail permutation
    initialTable = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]

    pc1_table = [
        57, 49, 41, 33, 25, 17, 9, 1,
        58, 50, 42, 34, 26, 18, 10, 2,
        59, 51, 43, 35, 27, 19, 11, 3,
        60, 52, 44, 36, 63, 55, 47, 39,
        31, 23, 15, 7, 62, 54, 46, 38,
        30, 22, 14, 6, 61, 53, 45, 37,
        29, 21, 13, 5, 28, 20, 12, 4
    ]

    pc2_table = [
        14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32
    ]

    s_boxes = [
        # S1
        [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        ],
        # S2
        [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
        ],
        # S3
        [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
        ],
        # S4
        [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
        ],
        # S5
        [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
        ],
        # S6
        [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
        ],
        # S7
        [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
        ],
        # S8
        [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
        ]
    ]

    # Define the left shift schedule for each round
    shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


    #expansion box table
    e_box_table = [ 32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]


    p_box_table = [
        16, 7, 20, 21, 29, 12, 28, 17,
        1, 15, 23, 26, 5, 18, 31, 10,
        2, 8, 24, 14, 32, 27, 3, 9,
        19, 13, 30, 6, 22, 11, 4, 25
    ]
    inverse_table = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25
    ]
    
    def __init__(self, key):
        self.key = self.key_to_binary(key)


    def bin_to_hex(self, bin_string):

        decimal_value = int(bin_string, 2)  # Convertendo o inteiro para hexadecimal, removendo o prefixo '0x'
        hexa = hex(decimal_value)[2:] # Garantindo que a saída seja em letras minúsculas e sem o prefixo '0x'
        return hexa.zfill(len(bin_string) // 4)  # Cada 4 bits são 1 dígito hexadecimal
    
    def hex_to_bin(self, hex_str):
        
        decimal_value = int(hex_str, 16) # Convertendo a string hexadecimal para inteiro
        binvalue = bin(decimal_value)[2:] # Convertendo o inteiro para binário, removendo o prefixo '0b'
        return binvalue.zfill(len(hex_str) * 4) # Garantindo que o número de bits seja múltiplo de 4 (ou seja, 1 dígito hexadecimal = 4 bits)



    def get_subkeys(self):
        if self.key is None:
            raise ValueError("Chave não definida")
    
        permuted_key = ''.join(self.key[i-1] for i in self.pc1_table) # PC1 permuta a chave inicial
        
        c, d = permuted_key[:28], permuted_key[28:] # Divida a chave permutada em duas metades
        
        subkeys = []
        for round_num in range(16): # Gerar 16 subchaves

            c = c[self.shift[round_num]:] + c[:self.shift[round_num]]
            d = d[self.shift[round_num]:] + d[:self.shift[round_num]]

            # Aplicar PC2
            cd = c + d
            subkey = ''.join(cd[i-1] for i in self.pc2_table)
            subkeys.append(subkey)        
        return subkeys
         
            
    def to_binary(self, input):
        return ''.join(f'{ord(c):08b}' for c in input)

    def padding(self, input_bin) :
        if len(input_bin) < 64: #se tamanho < 64 bits
            padded_bits = input_bin.ljust(64, '0') #adiciona 0s até completar 64 bits	
        return padded_bits    

    def msg_to_binary(self, msg):
        msg_bin = self.to_binary(msg)        

        blocks = [msg_bin[i:i+64] for i in range(0, len(msg_bin), 64)] # Divide a mensagem em blocos de 64 bits
        
        if len(blocks[-1]) < 64: # Adiciona padding ao último bloco, se necessário
            blocks[-1] = self.padding(blocks[-1]) # Adiciona 0s até completar 64 bits
        return blocks
     
    def key_to_binary(self, key_str):
        key_bin = self.to_binary(key_str)

        if len(key_bin) < 64: #adicona padding se tamanho da key binaria < 64 bits
            key_bin = self.padding(key_bin)
        
        key_bin = key_bin[:64] # Garante que a chave terá 64 bits
        return key_bin

    def bin_to_ascii(self, bin_string):
        ascii_str = ''.join([chr(int(bin_string[i:i+8], 2)) for i in range(0, len(bin_string), 8)])
        return ascii_str

    
    def initial_permutation(self, block):
        permuted_block = ''.join(block[i-1] for i in self.initialTable)
        return permuted_block
    
    def split(self, block):
        left = block[:32]
        right = block[32:]
        return left, right
    
    def expand_half(self, half_block):
        expanded_half = ''.join(half_block[i-1] for i in self.e_box_table)
        return expanded_half
    
    def substitute(self, block):
        substituted = ''
        for i in range(8):
            segment = block[i*6:(i+1)*6]
            row = int(segment[0] + segment[-1], 2)
            col = int(segment[1:5], 2)
            substituted += f'{self.s_boxes[i][row][col]:04b}'
        return substituted

    def round(self, left, right, subkey):
        
        expanded_right = self.expand_half(right) # Expande a metade direita
        xored = ''.join('1' if expanded_right[i] != subkey[i] else '0' for i in range(48)) # XOR com a subchave
        substituted = self.substitute(xored) # Substituição com as S-boxes
        permuted = ''.join(substituted[i-1] for i in self.p_box_table)  # Permutação P
        new_right = ''.join('1' if permuted[i] != left[i] else '0' for i in range(32))# XOR com a metade esquerda
        return right, new_right
    
    def inverse_initial_permutation(self, block):
        permuted_block = ''.join(block[i-1] for i in self.inverse_table)
        return permuted_block 
    



    #encriptar
    def encrypt(self, plaintext):
        blocks = self.msg_to_binary(plaintext)
        subkeys = self.get_subkeys()
        ciphertext = ''
        for block in blocks:
            block = self.initial_permutation(block)
            left, right = self.split(block)
            for subkey in subkeys:
                left, right = self.round(left, right, subkey)
            combined_block = right + left
            ciphertext += self.inverse_initial_permutation(combined_block)
        cipherhex = self.bin_to_hex(ciphertext)      
        return cipherhex


    #decriptar
    def decrypt(self, hex): 
        blocks = self.hex_to_bin(hex)
        blocks = [blocks[i:i+64] for i in range(0, len(blocks), 64)]
        subkeys = self.get_subkeys()[::-1]
        decrypted_bin = ''
        for block in blocks:
            block = self.initial_permutation(block)
            left, right = self.split(block)
            for subkey in subkeys:
                left, right = self.round(left, right, subkey)
            combined_block = right + left
            decrypted_bin += self.inverse_initial_permutation(combined_block)
        decrypted_text = self.bin_to_ascii(decrypted_bin)      
        return decrypted_text
        
