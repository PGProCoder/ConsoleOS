def google_search(): #implementation of search function here, to run the main function
    from googlesearch import search
    query = input("What do you want to search? ")
    if query == "EXIT CONSOLEOS BROWSER":
           print("Exit succesful")
           main()
    else:
           pass
    for url in search(query):
        print(f"URL: {url}")
        print("------------------------")

    url =input("Paste the url by copying it from above: ")
    if url == "EXIT CONSOLEOS BROWSER":
           print("Exit succesful")
           main()
    else:
           pass       
    import webview as w
    w.create_window("ConsoleOS Browser", f"{url}")
    w.start()

#variable containig "documentation". See https://prathamghaywat.github.io/ConsoleOS/documentation.md
help = """ 
Open Apps with command = open [appname]
Apps to choose:
text editor
calculator
games
browser


Check about ConsoleOS: check [command]
Commands to choose:
version
help

Use the "dwld" function to download or get stuff from diffrent online Platforms or services like this:
dwld 
Types to choose:
youtube --> download youtube videos
img --> download images from the internet
html --> get html code of a wbsite
console source --> get source code zipfile

View ConsoleOS App source codes:
view [appname]
'Check out apps above'

For more view https://prathamghaywat.github.io/ConsoleOS/documentation.md
"""
def unknown_command():
       print("Unknown command")
       print("Type 'close' or 'stop' to stop ConsoleOS")

def main():
       option = input("> ")
       option == option.lower()
       option == option.strip(" ") #TODO: Fix implementation of striping whitspace
       if option == "open text editor" or option == "open editor" or option == "editor" or option == "text editor" : #Text editor
              from text_editor import editor
              editor.editor_on()
       elif option == "open calculator": #simple calculator
              from calculator import calc
              calc.calculate()
       elif option == "open browser" or option == "browser": #browser using pywebview
                google_search()  
       elif option == "open games":
              choices = """
                            1. Guess the Word
                            2. Tic Tac Toe
                            3. Guess the number
                            """
              print(choices)
              choices = input("What do you want to play? ")
              choices = choices.lower() #TODO: Fix implementation of lowering the input
              choices = choices.strip() #TODO: Fix implementation of striping whitspace
              if choices == "guess the word":
                     import games.guess_the_word
                     games.guess_the_word.hangman()
              elif choices == "tic tac toe":
                     pass #TODO: tictactoe.py
              elif choices.lower == "guess the number":
                     pass #TODO: guess_the_number.py
       elif option == "check version": #V.1.0.0
              print("ConsoleOS Version 1.0.0")
              print("Higlight: First version of consoleos")
       elif option == "dwld console source":
              import dwld.getsource
              dwld.getsource.get()
       elif option == "dwld html":
              url = input("Website URL: ")
              import dwld.get_html
              dwld.get_html.get_html_code(url)
       elif option == "dev-python":
              import devloper_mode.python_dev
              devloper_mode.python_dev.exec_python_code()
       elif option == "close" or option == "stop":
              quit() #quits programm
       elif option == "dwld youtube":
              url = input("Video URL: ")
              from dwld.get_yt_vid import download_yt_video
              download_yt_video(url)
       elif option == "dwld img":
              url = input("Image URL: ")
              from dwld.get_img import download_image
              download_image(url)
       else: #detect unknown command##
              unknown_command()           
while True: #run forever till loop is broken           
        main()