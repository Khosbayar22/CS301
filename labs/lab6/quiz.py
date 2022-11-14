import string


class Quiz:
    def __init__(self):
        self.total = 0
        self.quiz = [
            {
                "question": "Түргэн хаяглалтын аргыг ашиглаж байх үед санах ойн . . . шаардлагагүй. Цэгийн оронд нөхөж бичнэ үү",
                "answers": [
                    ('Регистрийн дугаар', False),
                    ('Заавар', True),
                    ('Програмын тооллуур', False),
                ],
            },
            {
                "question": "Хамгийн энгийн хаяглалтын арга нь эдгээрээс аль нь вэ ?",
                "answers": [
                    ('Шууд хаяглалтын арга', False),
                    ('Түргэн хаяглалтын арга', True),
                    ('Индексэн хаяглалтын арга', False),
                ],
            },
            {
                "question": "Индексэн хаяглалтын арга ашиглаж байх үед зааврын хаяг нь санах ойн өгөгдлийн дараалалд юуг нь тодорхойлдог вэ ?",
                "answers": [
                    ('Эхлэх хаяг', True),
                    ('Төгсөх хаяг ', False),
                    ('Ямар ч хамааралгүй', False),
                ],
            },
            {
                "question": "Регистрийн хаяглалтын арга нь . . . хоорондын дамжуулалтыг хэрэгжүүлэхэд ашиглагддаг. Цэгийн оронд нөхөж бичнэ үү.",
                "answers": [
                    ('Сегмент', True),
                    ('Заавар ', False),
                    ('Регистрийн дугаар', False),
                ],
            },
            {
                "question": "Харьцангуй хаяглалтын арга нь зааврын хаяглалтанд . . . нэмнэ. Цэгийн оронд нөхөж бичнэ үү.",
                "answers": [
                    ('Програмын тоолуур', True),
                    ('Регистрийн дугаар ', False),
                    ('Сегмент', False),
                ],
            }
        ]

    def main(self):
        for item in self.quiz:
            print(item["question"])
            for (index, answer) in enumerate(item['answers']):
                alp = string.ascii_lowercase[index]
                print(f"{alp}. {answer[0]}")

            flag = True
            while flag:
                inp = input('Хариултаа оруулна уу.')
                for (index, answer) in enumerate(item['answers']):
                    alp = string.ascii_lowercase[index]
                    if alp == inp:
                        flag = False
                        if answer[1]:
                            print('============= Та зөв хариуллаа')
                            self.total += 1
                        else:
                            print('============= Та буруу хариуллаа')
                        break
                if flag:
                    print('!!!!!!!!!!!!! Та a, b, c гэсэн хувилбараас сонгоно уу')
                else:
                    break

        print('\nНийт буруу хариулт: \t', len(self.quiz) - self.total)
        print('Нийт зөв харилт:\t', self.total)


if __name__ == '__main__':
    quiz = Quiz()
    quiz.main()
