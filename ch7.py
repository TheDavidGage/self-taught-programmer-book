name = "David"
for character in name:
    print(character)

shows = ["GOT",
         "Narcos",
         "Vice"]
for show in shows:
    print(show)

coms = ("A. Development",
        "Friends",
        "Always Sunny")
for show in coms:
    print(show)

people = {"G. Bluth II":
          "A. Development",
          "Barney":
          "HIMYM",
          "Dennis":
          "Always Sunny"}

for character in people:
    print(character)

tv = ["GOT",
      "Narcos",
      "Vice"]
i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1

print(tv)
