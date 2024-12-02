left_list=[]
right_list=[]
with open('day1input.txt', 'r') as f:
    for x in f:
        #kek
        left_list.append(int(x[0:5]))
        right_list.append(int(x[8:13]))
    f.close()
    left_list.sort()
    right_list.sort()

total=0
for element_r,element_l in zip(right_list,left_list):
    distance=abs(int(element_r)-int(element_l))
    #print(f"left element : {element_l} right element: {element_r}")
    #print(f"added distance : {distance} to total : {total}")
    total+=distance
    #print(f"New total : {total}")
    
print("total_distance (p1) is : ",total)

simosaliraty_score=0
for el in left_list:
    simosaliraty_score+=right_list.count(el)*el

print("simosaliraty_score (p2) is : ",simosaliraty_score)

