with open("students.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        id, ism = line.split(",")
        print(f"ID: {id} - {ism}")

    print(f"Jami o'quvchilar: {len(lines)}")