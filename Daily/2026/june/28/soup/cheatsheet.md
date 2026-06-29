# PRETTIFY() #

from bs4 import BeautifulSoup

html = "<html><body><p>Hello, Friday!</p></body></html>"
soup = BeautifulSoup(html, "html.parser")

print(soup.prettify())

# SELECT BY TAG #

from bs4 import BeautifulSoup

html = "<html><body><p>Hello Friday</p><p>How are you?</p></body></html>"
soup = BeautifulSoup(html, "html.parser")

# First <p> Tag
print(soup.p)

# Same Result
print(soup.find("p"))

# All <p> tags as a list
print(soup.find_all("p"))


# SELECT BY CLASS OR ID #

from bs4 import BeautifulSoup

html = <div class="note">Hi</div><div id="msg>Yo</div>"
soup = BeautifulSoup(html, "html.parser")

print(soup.find("div", class_="note"))
print(soup.find("div", id="msg"))