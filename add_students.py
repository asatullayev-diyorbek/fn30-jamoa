with open("students.txt", "a") as f:
    id = input("ID: ")
    ism = input("Ism: ")
    f.write(f"{id},{ism}\n")
    print("✅ Ma'lumot saqlandi!")