class Mips:

    def __init__(self, time, frequence):
        self.time = time
        self.frequence = frequence
    
    def run(self):
        result = []
        for i in range(len(self.time)):
            result.append(self.time[i] * self.frequence[i] / 100)
        print(f"{sum(result)} микросекунд")
        print(f"{int(1/sum(result))} MIPS")