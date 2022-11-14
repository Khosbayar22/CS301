import string
from tokenize import String


class Lab2:

    def __init__(self):
        self.cpi_table = [
            [
                {
                    'instruction': 'А',
                    'cpi': 3,
                    'cycle_time': 15
                },
                {
                    'instruction': 'Б',
                    'cpi': 4,
                    'cycle_time': 15
                },
                {
                    'instruction': 'В',
                    'cpi': 2,
                    'cycle_time': 15
                },
                {
                    'instruction': 'Г',
                    'cpi': 5,
                    'cycle_time': 15
                }
            ],
            [
                {
                    'instruction': 'А',
                    'cpi': 2,
                    'cycle_time': 10
                },
                {
                    'instruction': 'Б',
                    'cpi': 4,
                    'cycle_time': 10
                },
                {
                    'instruction': 'В',
                    'cpi': 5,
                    'cycle_time': 10
                }
            ]
        ]
    
    def findExecutionTime(self):
        for o in range(1, 3):
            with open(f"execution_time_{o}.txt", encoding="utf8") as file:
                sequence = []
                for line in file:
                    sequence.append(list(map(int, line.strip().split())))
                cpu_cnt = sequence[0]
                time = sequence[1]
                print(f"CPU -ны тоо {cpu_cnt}")
                print(f"Ажиллах хугацаа {time}")
                print(f"Зарцуулсан хугацаа {sum(time) /  (cpu_cnt[0] * cpu_cnt[1])} нано сек\n")
                file.close()

    def totalInstructionTime(self):
        with open('sequence.txt', encoding="utf8") as file:
            index = 0
            sum_cpi = []
            for line in file:
                table = self.cpi_table[index]
                index += 1
                sequence = list(line.strip().split())
                for i in table:
                    cnt = sequence.count(i['instruction'])
                    print(cnt)
                    sum_cpi.append(cnt * i['cpi'] * i['cycle_time'])
                print(f"Зааврыг ажлуулах нийт хугацаа: {sum(sum_cpi)} нано сек\n")
        file.close()

    def findGerts(self):
        with open('gerts.txt') as file:
            for line in file:
                ggts = int(line)
                print(f"Процессын үзүүлэлт: {1 / (ggts * pow(10, 9))} нано сек/заавар \n")
        file.close()


if __name__ == '__main__':
    result = Lab2()
    # result.findExecutionTime()
    result.totalInstructionTime()
    # result.findGerts()
