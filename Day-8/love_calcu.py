print("Welcome to the Love Calculator score check!!")
def calculator_love_score(name1, name2):
    combine_name = (name1+name2).lower()
    t = combine_name.count("t")
    r = combine_name.count("r")
    u = combine_name.count("u")
    e = combine_name.count("e")
    score1 = t+r+u+e
    l = combine_name.count("l")
    o = combine_name.count("o")
    v = combine_name.count("v")
    e = combine_name.count("e")
    score2 = l+o+v+e
    score = str(score1)+str(score2)
    print(score)
calculator_love_score(name1="love",name2="kesh")
