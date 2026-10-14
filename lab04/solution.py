def winner(names, scores):
    c = 0
    mx = -1000000
    for i in range(len(scores)):
        if scores[i] > mx:
            mx = scores[i]
            c = i
    return names[c]

def average(scores):
    if scores:
        return round(sum(scores)/len(scores), 2)
    else:
        return 0.0

def ranking(names, scores):
    rank = []
    names1 = []
    scores1 = []
    for i in range(len(names)):
        names1.append(names[i])
    for i in range(len(scores)):
        scores1.append(scores[i])
    for i in range(len(names1)):
        mx = -10000
        imx = 0
        for j in range(len(scores1)):
            if scores1[j] > mx:
                mx = scores1[j]
                imx = j
        rank.append(names1[imx])
        names1.pop(imx)
        scores1.pop(imx)
    return rank

def above_average(names, scores):
    sr = sum(scores)/len(scores)
    Legends = []
    for i in range(len(names)):
        if scores[i] > sr:
            Legends.append(names[i])
    return Legends
