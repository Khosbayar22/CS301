from matplotlib import pyplot as plt


class Chart:
    def scheduler_chart(self, datas):
        label_list = ['First Come First Served', 'Shortes Job', 'Priority', 'Round-Robin']
        label_cnt = 0
        for data in datas:
            y_axis = [15, 25, 35, 45]
            
            fig, gnt = plt.subplots(figsize=(6, 4))
            
            gnt.set_ylim(0, 50)
            gnt.set_xlim(0, 30)
            gnt.set_title(label_list[label_cnt])
            gnt.set_xlabel('Хугацаа')
            gnt.set_ylabel('Процесс')
            gnt.set_yticks(y_axis)
            gnt.set_yticklabels([1, 2, 3, 4])
            
            gnt.grid(True)
            
            label_cnt += 1
            
            for i in range(len(data)):
                gnt.broken_barh([data[i]], ((i + 1) * 10, 9), facecolors =('tab:gray'))
                for x1, x2 in [data[i]]:
                    gnt.text(x=x1 + x2/2, 
                            y=y_axis[i],
                            s=x2, 
                            ha='center', 
                            va='center',
                            color='black',
                        )
        
        plt.show()