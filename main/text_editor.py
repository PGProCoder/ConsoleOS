import os

class Editor:
    def __init__(self):
        self.start = True
        self.text = []
        self.line = 1 

    def editor_on(self):
        while self.start:
            text = input(f"{self.line}:  ")
            if text == "SAVE":
                self.start = False
                self.save_text()
            else:
                self.text.append(text)
                self.line += 1 #Switches per line 

    def save_text(self):
        filename = input("Save as: ")
        fileextension = input("Save as .txt or .docx? ")  #Adds file extension
        with open(f"{filename}.{fileextension}", 'w') as f:
            for line in self.text:
                f.write(line + '\n')
        print("Text saved successfully!")
        print("Saved in: ", os.path.abspath(filename))

# instance of the Editor class
editor = Editor()
editor.editor_on()
