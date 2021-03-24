import os
''' 
Accepts string of shifted unshifted characters
shifts alphabet list by #, and returns corrected string.
'''

class Caesar:
    """
    Ceasar Attempt class.
    """
    def __init__(self):
        """
        Here we set up the letter matrix. Odd string length = upper, even = lower
        """

        self.abc_list = list('abcdefghijklmnopqrstuvwxyz')
        self.clear = lambda: os.system('cls')

    def print_error(self, error_to_print: str) -> bool:
        """
        Print's out string prefixed with 'Error: '

        Return
        ------
        :return bool: 
        """
        print('Error: {}\n'.format(error_to_print))
        return True

    def print_cipher(self) -> bool:
        """
        Everything should be ready to print our output text. The inverse
        switch acts as the "random" selection of upper vs lower case.

        Return
        ------
        :return bool: default true
        """
        
        self.cipher_out = list()

        for key in self.abc_key:
            self.cipher_out.append(self.abc_list[key])

        for space in self.space_pointers:
            self.cipher_out.insert(space, ' ')

        print(''.join(self.cipher_out))

        return True

    def set_keys(self, from_words: list) -> bool:
        """
        Here we convert the from_words to their index value, we will use this 
        value for the shift (ie the negative impliciation) to 'shift' the 
        indicy value? (hopefully)

        Parameters
        ----------
        :from_words list: list of word(s)

        Return
        ------
        :return bool: for error? :)
        """

        self.abc_key = list()
        self.space_pointers = list()
        from_words = list((' '.join(from_words)).lower())

        for i in range(len(from_words)):
            if from_words[i] == ' ':
                self.space_pointers.append((i*-1))
                continue 
            if not from_words[i].isalpha():
                continue 
            self.abc_key.append(
                    (
                    self.abc_list.index(
                        from_words[i]
                        ) 
                        + self.shift_value
                    ) % 26
                )
        return len(self.abc_key) >= 1 

    def set_shift(self, output_shift: list) -> bool:
        """
        A T/F for completion. Left assumes negative for list index later
        
        Parameters
        ----------
        :output_shift list: this is the 'l/r 1-26' "list" asserts value for
        index value of cipher text output.

        Return
        ------
        :return bool: we shifted output or errored.
        """
        if not output_shift[1].isnumeric():
            return False

        self.shift_value = int(output_shift[1])

        if output_shift[0] in ['l','left']:
            self.shift_value = self.shift_value * -1

        return True

    def handle_input(self, user_input: str) -> bool:
        """
        This assumes they follow input 'l/r 1-26 lorem ipsmu'
        This is probably bad habit... bool is to save space? Who knows.

        Paramaters
        ----------
        :user_input str: assumes string from input, splits to list.

        Return
        ------
        :return bool:    true is success, false is error? 
        """
        user_input = user_input.split()

        if len(user_input) < 3:
            return False

        if not user_input[1].isnumeric():
            return False

        if not self.set_shift([user_input[0],user_input[1]]):
            return False

        if not self.set_keys(user_input[2:]):
            return False

        if not self.print_cipher():
            return False

        return True


        

if __name__ == "__main__":
    c = Caesar()
    c.clear()
    print('Follows a "left/right 1-26 string_to_shift" format.\n\n')
    while True:
        cipher = input()
        if cipher == 'break' or cipher == 'exit':
            break
        elif cipher == 'clear':
            c.clear()
        elif cipher == 'help':
            print(
                'break/exit will exit program.',
                'help displays this.',
                'clear clears display screen.',
                sep='\n')
        
        if not c.handle_input(cipher):
            c.print_error('left/right 1-26 something to cipher')
        
        
