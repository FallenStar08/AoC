data=[]
with open('day2input.txt', 'r') as f:
    data=[list(map(int,line.split())) for line in f if line.strip()]

#p1
valid_sets=0
for set in data:
    is_increasing=all(i < j and abs(i-j)<=3 for i, j in zip(set, set[1:]))
    is_decreasing=all(i > j and abs(i-j)<=3 for i, j in zip(set, set[1:]))
    is_valid=is_increasing or is_decreasing
    print(f"Set: {set} is {'increasing' if is_increasing else 'decreasing' if is_decreasing else 'invalid'}")
    if is_valid:
        valid_sets+=1
print(f" p1 valid set : {valid_sets}") #341

#p2 doot
def is_set_valid(set):
    return all(i < j and abs(i-j)<=3 for i, j in zip(set, set[1:])) or all(i > j and abs(i-j)<=3 for i, j in zip(set, set[1:]))

def couldbe(seq):
    if is_set_valid(seq):
        return True
    #this is SHIT
    for i in range(len(seq)):
        new_seq = seq[:i] + seq[i+1:]
        if is_set_valid(new_seq):
            return True
    return False

valid_sets=0
for set in data:
    is_valid=couldbe(set)
    if is_valid:
        valid_sets+=1
print(f" p2 valid set : {valid_sets}")

