if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    students.sort(key=lambda x: x[1])
    second_lowest = sorted(list(set([x[1] for x in students])))[1]
    for name, score in sorted(students):
        if score == second_lowest:
            print(name)
