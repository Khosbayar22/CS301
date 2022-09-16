class Lab1:

    def __init__(self):
        self.times = [
            {
                "time": 2,
                "name": "Cache",
                "length": 1
            },
            {
                "time": 10,
                "name": "Main memory",
                "length": 1
            },
            {
                "time": pow(10, 6),
                "name": "Magnetic disk",
                "length": 1024
            },
            {
                "time": pow(10, 9),
                "name": "Magnetic tape",
                "length": 1
            },
        ]

    def findRamSize(self):
        with open('ram.txt') as file:
            for line in file:
                row, column, color = list(map(int, line.strip().split()))
                cnt = 0
                while color / 2 >= 1:
                    color /= 2
                    cnt += 1
                ram_size = (row * column) / cnt
                print(f"Ram size: {ram_size}\nBit size: {ram_size / 8}\n")
        file.close()

    def findExecutingTime(self):
        with open('book.txt') as file:
            for line in file:
                page, row, column = list(map(int, line.strip().split()))
                size = page * row * column
                print(f"total: {size}\n")
                for i in self.times:
                    print(f"{i['name']}: {size * i['time'] / i['length']}")

                print(f"\n================================\n")
        file.close()


if __name__ == '__main__':
    result = Lab1()
    result.findRamSize()
    result.findExecutingTime()
