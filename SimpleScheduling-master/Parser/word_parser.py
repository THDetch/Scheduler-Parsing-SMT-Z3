class WordParser:
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.buffer = False

    def next_word(self):
        """
        >>> w = WordParser("../Examples/simplest")
        >>> w.next_word()
        'Task'
        >>> w.next_word()
        'takes'
        >>> w.next_word()
        '1'
        >>> w.next_word()
        'needs'
        >>> w.next_word()
        'none'
        """
        word = ""

        # If the buffer attribute is set, return a right parenthesis
        if self.buffer:
            self.buffer = False
            return ")"

        # Read characters from the file until a word is formed
        while True:
            # Read a single character from the file
            c = self.file.read(1)

            # Return the word or None if the end of the file has been reached
            if not c:
                return word or None

            # Skip spaces, newlines, and tabs unless a word has already been formed
            if c in " \n\t":
                if word:
                    break
            # Add left parentheses to the word and break the loop to return the parentheses
            elif c == "(":
                word += c
                break
            # Return right parentheses immediately or add them to the word if no word has already been formed
            elif c == ")":
                if not word:
                    return ")"
                self.buffer = True
                break
            # Add any other character to the word
            else:
                word += c

        return word

# if __name__ == '__main__':
#     doctest.testmod()
