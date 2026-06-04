def greet(language):
   match language:
       case "English":
           print("Hello!")
       case"Spanish":
           print("Hola!")
       case "Japanese":
           print("こんにちは!")
       case _:
           print("Language not recognized")

greet("Japenese")