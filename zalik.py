# Басенюк Артем КІ-1 Залік

class Text:
    def __init__(self):
        self.file = ''
        self.menu()
    
    def menu(self):
        while True:
            choice = int(input('Enter the number of the thing that you want to choose:' + '\n' +
                           '1. Enter the file' + '\n' +
                           '2. Search the paragraph with the word' + '\n' +
                           '3. Exit' + '\n' +
                           'Enter the number: '))
            match(choice):
                case(1):
                    self.file = self.read_file()
                case(2):
                    self.inputWord()
                case(3):
                    break
    
    def inputWord(self):
        word = input('Enter the word that you want to search: ')

        self.paragraphsWordFind(self.divideIntoParagraphs(self.file), word)

    def read_file(self):
        file_location = input("Please enter the file location: ")
        with open(file_location, 'r') as file:
            file_content = file.read()
        return file_content
    
    def divideIntoParagraphs(self, text):
        lines = text.split('\n')

        paragraphs = []
        current_paragraph = ''

        for line in lines:
            if line.strip():
                current_paragraph += line.strip() + ' '
            else:
                if current_paragraph.strip():
                    paragraphs.append(current_paragraph.strip())
                    current_paragraph = ''

        if current_paragraph.strip():
            paragraphs.append(current_paragraph.strip())

        return paragraphs
    
    def paragraphsWordFind(self, paragraphs, word):
        for paragraph in paragraphs:
            if word.lower() in paragraph.lower():
                print(paragraph)
        
the = Text
the()
