"""Task 4"""
class CharLenError(Exception):
    """Check len"""
    def __init__(self, character):
        self.character = character
        self.inf = 'Oh, sorry! Length of character must be 1.'
        super().__init__(self.inf)
class CharTypeError(Exception):
    """Check type"""
    def __init__(self, character):
        self.character = character
        self.inf = 'Oh, sorry! Type of character must be string.'
        super().__init__(self.inf)
class HomeError(Exception):
    """Check position"""
    def __init__(self, position):
        self.position = position
        self.inf = "Index is out of range!"
        super().__init__(self.inf)

class Document:
    """Document"""
    def __init__(self):
        """Init args"""
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''
    @property
    def string(self):
        """Str"""
        return "".join((str(c) for c in self.characters))
    def insert(self, character):
        """Insert"""
        if not hasattr(character, 'character'):
            character = Character(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()
    def delete(self):
        """Delete"""
        try:
            del self.characters[self.cursor.position]
        except IndexError:
            print("There is no characters to delete:(") # Не може видалити коли не існує знака
    def save(self):
        """Save"""
        f = open(self.filename, 'w')
        f.write(''.join(self.characters))
        f.close()
class Cursor:
    """Cursor"""
    def __init__(self, document):
        """Init args"""
        self.document = document
        self.position = 0
    def forward(self):
        """Forward"""
        self.position += 1
    def back(self):
        """Back"""
        self.position -= 1
        if self.position < 0:
            raise HomeError(self.position) # Не видає мінусової позиції
    def home(self):
        """Home"""
        while self.document.characters[self.position-1].character != '\n':
            self.position -= 1
            if self.position == 0:
                break
    def end(self):
        """End"""
        while self.position < len(self.document.characters) \
            and self.document.characters[self.position].character != '\n':
            self.position += 1

class Character:
    """Character"""
    def __init__(self, character, bold = False, italic = False, underline = False):
        """Init args"""
        if not isinstance(character, str):
            raise CharTypeError(character) #Збуджує помилку коли тип знака не str
        if len(character) != 1:
            raise CharLenError(character) #Збуджує помилку коли довжина > 1
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline
    def __str__(self):
        """Str"""
        bold = '*' if self.bold else ''
        italic = '/' if self.italic else ''
        underline = '_' if self.underline else ''
        return bold + italic + underline + self.character
# d = Document()
# d.insert('h')
# d.insert('e')
# d.insert(Character('l', bold = True))
# d.insert(Character('l', bold = True))
# d.insert('o')
# d.insert('\n')
# d.insert(Character('w', italic = True))
# d.insert(Character('o', italic = True))
# d.insert(Character('r', underline = True))
# d.insert('l')
# d.insert('d')
# print(d.string)
# d.cursor.home()
# d.delete()
# d.insert("W")
# print(d.string)
# d.characters[0].underline = True
# print(d.string)
# # d_ = Document()
# # d_.insert('W')
# # d_.insert('o')
# # # print(d_.string)
# # d_.cursor.home()
# # print(d_.string)
# # d_.delete()
# # print(d_.string)
# # d_.delete()
# # print(d_.string)
# # d_.delete()
# # # d_.cursor.back()
# # # print(d_.cursor.position)
# # # d_.cursor.back()
# # # print(d_.cursor.position)
# # # d_.cursor.back()
# # # print(d_.cursor.position)
