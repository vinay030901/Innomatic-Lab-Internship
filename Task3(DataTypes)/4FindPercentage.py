if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    ans=[i for i in student_marks[query_name]]
    s=sum(ans)/3
    format_float = "{:.2f}".format(s)
    print(format_float)
