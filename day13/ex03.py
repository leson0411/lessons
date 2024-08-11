def return_a_dictionary():
    name, nationality, age = ("Tom Hardy", "English", 42)  # name, nationality, age
    k1, k2, k3 = ("name", "nationality", "age")

    return {
        k1.title(): name,
        k2.title(): nationality,
        k3.title(): age
    }

print(return_a_dictionary())
