
class CpuSchedule:
	
	def __init__(self, data):
		self.data = data

	def firstComeFirstServed(self):
		turnAround = []
		waitingTime = [0]
		for i in range(len(self.data) - 1):
			waitingTime.append(int(self.data[i]) + int(waitingTime[i]))
		for i in range(len(self.data)):
			turnAround.append(int(self.data[i]) + int(waitingTime[i]))
		
		print(f"\n==============================\n")
		print(f"Total Turnaround Time: {sum(turnAround)}")
		print(f"Average Turnaround Time: {sum(turnAround)/len(turnAround)}")
			
		print(f"Total Waiting Time: {sum(waitingTime)}")
		print(f"Average Waiting Time: {sum(waitingTime)/len(waitingTime)}")
		
		chart_data = list(map(list, zip(waitingTime, self.data)))
		return chart_data

	def shortestJob(self):
		waitingTime = [0]
		turnAround = []
		sorted_data = sorted(self.data)
		
		for i in range(len(sorted_data) - 1):
			waitingTime.append(int(sorted_data[i]) + int(waitingTime[i]))
		
		for i in range(len(sorted_data)):
			turnAround.append(int(sorted_data[i]) + int(waitingTime[i]))
			
		print(f"\n==============================\n")
		print(f"Total Turnaround Time: {sum(turnAround)}")
		print(f"Average Turnaround Time: {sum(turnAround)/len(turnAround)}")
			
		print(f"Total Waiting Time: {sum(waitingTime)}")
		print(f"Average Waiting Time: {sum(waitingTime)/len(waitingTime)}")
		
		chart_data = list(map(list, zip(waitingTime, sorted_data)))
		return chart_data
		
	def priority(self):
		waitingTime = [0]
		turnAround = []
		priority_queue = list(map(int, input("Процессын эрэмбийн дараалалыг оруулна уу.\n").split()))
		
		sorted_data = [x for _,x in sorted(zip(priority_queue, self.data))]
		for i in range(len(sorted_data) - 1):
			waitingTime.append(int(sorted_data[i]) + int(waitingTime[i]))
		
		for i in range(len(sorted_data)):
			turnAround.append(int(sorted_data[i]) + int(waitingTime[i]))
			
		print(f"\n==============================\n")
		print(f"Total Turnaround Time: {sum(turnAround)}")
		print(f"Average Turnaround Time: {sum(turnAround)/len(turnAround)}")
			
		print(f"Total Waiting Time: {sum(waitingTime)}")
		print(f"Average Waiting Time: {sum(waitingTime)/len(waitingTime)}")
		
		chart_data = list(map(list, zip(waitingTime, sorted_data)))
		return chart_data

	def roundRobin(self):
		n = len(self.data)
		wt = [0] * n
		tat = [0] * n
		def findWaitingTime(n, bt,
								wt, quantum):
			rem_bt = [0] * n
			for i in range(n):
				rem_bt[i] = bt[i]
			t = 0 
			while(1):
				done = True
				for i in range(n):
					if (rem_bt[i] > 0) :
						done = False
						if (rem_bt[i] > quantum) :
							t += quantum
							rem_bt[i] -= quantum
						else:
							t = t + rem_bt[i]
							wt[i] = t - bt[i]
							rem_bt[i] = 0
				if (done == True):
					break
		def findTurnAroundTime(n, bt, wt, tat):
			for i in range(n):
				tat[i] = bt[i] + wt[i]
    
		findWaitingTime(len(self.data), self.data, wt, 1)
		findTurnAroundTime(len(self.data), self.data, wt, tat)
  
		print("Processes Service Time	 Waiting",
						"Time Turn-Around Time")
		total_wt = 0
		total_tat = 0
		for i in range(n):
			total_wt = total_wt + wt[i]
			total_tat = total_tat + tat[i]
			print(" ", i + 1, "\t\t", self.data[i],
				"\t\t", wt[i], "\t\t", tat[i])
			
		print(f"\n==============================\n")
		print(f"Total Turnaround Time: {sum(tat)}")
		print(f"Average Turnaround Time: {sum(tat)/n}")
			
		print(f"Total Waiting Time: {sum(wt)}")
		print(f"Average Waiting Time: {sum(wt)/n}")