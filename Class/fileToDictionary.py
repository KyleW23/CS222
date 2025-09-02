def main():
    try:
        studentList = {}
        fileInput = open("studentsinfo.txt", 'r')
        students = fileInput.readlines()
        fileInput.close()
        for s in students:
            parts = s.split(',')
            studentList[parts[0]] = [parts[1], parts[2], parts[3], parts[4]]

        for k, v in studentList.items():
            print(v)
            if v[2] == "Math":
                print(k + " " + v[0] + ", " + v[1])
    except FileNotFoundError:
        print("File no found")

main()