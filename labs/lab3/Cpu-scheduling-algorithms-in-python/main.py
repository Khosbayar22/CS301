from app.Schedular import CpuSchedule
from app.Mips import Mips
from app.Chart import Chart

class Main:
    
    def cpu(self):
        input_data = list(map(int, input("Процессын сервис хугацааг оруулна уу.\n").split()))
        
        schedular = CpuSchedule(input_data)
        first_come_first_served = schedular.firstComeFirstServed()
        shorest_job = schedular.shortestJob()
        priority = schedular.priority()
        schedular.roundRobin()
        
        chart = Chart()
        chart.scheduler_chart([first_come_first_served, shorest_job, priority])

    def mips(self):
        time = list(map(float, input("Ажиллах хугацааг оруулна уу.\n").split()))
        frequence = list(map(float, input("Давтамжийг оруулна уу.\n").split()))
        mips = Mips(time, frequence)
        mips.run()
        
if __name__ == "__main__":
    """
        CPU -ны зарцуулсан хугацааг 4 алгоритмаар тооцов. 
        * First come first out
        * Shortest job
        * Priority
        * Robin-round (Графикгүй)
    """
    Main().cpu()
    
    """Компьютерын зааврын хугацааг тооцов. Тооцсон хугацаагаа MIPS -рүү шилжүүлэв."""
    Main().mips()