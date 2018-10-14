import pylab
import numpy as np 

def get_columns(data_lst,cols_lst):
    selected_lst = []
    selected_cols = []
    index = 0
    for key_word in cols_lst:
        for word in data_lst[0]:
            if word == key_word:
                index = data_lst[0].index(word)
                for i in range(1,len(data_lst)):
                    for j in range(0,len(data_lst[i])):
                        if j == index:
                            selected_lst.append(data_lst[i][j])
                selected_cols.append(selected_lst)
                selected_lst = []
    return selected_cols
        
def get_csv_data(f,string_pos_lst,sep):
    bb_sub_lst = []
    bb_lst = []
    
    lines = [line.strip('\n,ï»¿,"') for line in f]

    for line in lines:
        words = line.split(sep)
        for i in range(0,len(words)):
            if i not in string_pos_lst:
                try:
                    bb_sub_lst.append(float(words[i]))
                except ValueError:
                    bb_sub_lst.append(words[i])
            else:
                bb_sub_lst.append(words[i])
            
            
        bb_lst.append(bb_sub_lst)
        bb_sub_lst = []
    return bb_lst
    
bb_file = open('lb-james.csv', 'r')
james_lst = get_csv_data(bb_file, [0, 2, 3, 4], ',')
#print(james_lst[len(james_lst)-1])
s_lst = get_columns(james_lst,["Season"])
seasons = s_lst[0]

three_percentage = get_columns(james_lst,["3P%"])
three = three_percentage[0]

two_percentage = get_columns(james_lst,["2P%"])
two = two_percentage[0]

free_percentage = three_p = get_columns(james_lst,["FT%"])
free = free_percentage[0]

x_length = len(s_lst[0])
x_lst = []
for i in range(0, x_length-1):
    x_lst.append(i)

xs = np.array(x_lst)
ys_1 = np.array(three)
ys_2 = np.array(two)
ys_3 = np.array(free)

pylab.xticks(x_lst, seasons, rotation=90)
pylab.plot(xs, ys_1, marker='o', linestyle='-', color='blue', label='3-point field goal percentage')

pylab.plot(xs,ys_2, marker='o', linestyle='-', color='red', label='2-point field goal percentage')

pylab.plot(xs, ys_3, marker='o', linestyle='-', color='green', label='free-throw percentage')

pylab.legend(loc='lower right')

pylab.show()



    

