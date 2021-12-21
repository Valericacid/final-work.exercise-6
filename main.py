import csv


def read_gc():
    filename = input("Введите название файла: ")
   
    n = int(input("Введите количесвто нуклеотидов в для одного участка: "))
    with open(filename) as f:
        name = f.readline().replace("\n", "")[1:]
        lines = f.read()

    with open("DNA.csv", "w",  newline='') as f_csv:
        writer = csv.writer(f_csv, delimiter=";")
        lines = lines.replace("\n", "")
        writer.writerow(["Идентификатор хромосомы", "Номер участка", "gc-content [%]"])

        count = 0
        area = 1
        gc_count = 0
        for x in lines:
            if count == n:
                percent = (gc_count / n) * 100

                writer.writerow([name, area, "{:.4f}%".format(percent)])
                count = 0
                area += 1
                gc_count = 0
            if x.upper() == "G" or x.upper() == "C":
                gc_count += 1
            count += 1


if __name__ == '__main__':
    read_gc()
