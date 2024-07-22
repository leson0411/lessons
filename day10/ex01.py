album = (
    "The Dark Side of the Moon",
    "Pink Floyd",
    1973,
    (
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    )
)

keys = ("album name", "artist name", "release year", "track list")

dic = dict(zip(keys, album))
print(dic)

for key, value in dic.items():
    print(f"{key}: {value}")

del dic["release year"]
del dic["track list"]
dic["date of release"] = "March 1st, 1973"
print(dic)

# print(dic["release year"])
print(dic.get("release year"))
