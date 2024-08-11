with open("hello_world.txt", "a") as f:
    f.write("Hello, World!")
    f.write("/nHow are you")

with open("iris.csv", "r") as iris_file:
    iris_data = iris_file.readlines()

irises = []

for row in iris_data[1:]:
    sepal_length, sepal_width, petal_length, petal_width, species = row.strip().split(",")

    iris_dict = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
        "species": species
    }

    irises.append(iris_dict)

with open("iris_02.csv", "w") as iris_file02:
    header = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
    iris_file02.write(",".join(header) + "\n")
    for iris in irises:
        iris_file02.write(",".join(iris.values()) + "\n")
