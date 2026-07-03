def greet(language):
   match language:
       case "English":
           print("Hello!")
       case _:
           print("Language not recognized")

greet("English")