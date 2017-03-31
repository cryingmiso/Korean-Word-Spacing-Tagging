# -*- coding:utf-8 -*-

states = ("B","M","E","S")

test_input = "BBMESBMEBEBESSMEBBME"

observations = [obs for obs in test_input]

#시작확률
start_prob = {"B":0.4,"M":0.2,"E":0.2,"S":0.2}

#전이확률
transit_prob = {"B": {"B": 0.1, "M": 0.4, "E": 0.4, "S": 0.1},
                "M": {"B": 0.1, "M": 0.4, "E": 0.4, "S": 0.1},
                "E": {"B": 0.4, "M": 0.1, "E": 0.1, "S": 0.4},
                "S": {"B": 0.4, "M": 0.1, "E": 0.1, "S": 0.4}}

#출력확률
emission_prob = {'B': {"B": 0.4, "M": 0.2, "E": 0.2, "S": 0.2},
                 "M": {"B": 0.2, "M": 0.4, "E": 0.2, "S": 0.2},
                 "E": {"B": 0.2, "M": 0.2, "E": 0.4, "S": 0.2},
                 "S": {"B": 0.2, "M": 0.2, "E": 0.2, "S": 0.4}}

def viterbi(observs,states,sp,tp,ep):
    T = {} # present state
    for st in states:
        T[st] = (sp[st]*ep[st][observs[0]],[st])
    for ob in observs[1:]:
        T = next_state(ob,states,T,tp,ep)
    prob,labels = max([T[st] for st in T])
    return prob,labels


def next_state(ob,states,T,tp,ep):
    U = {} # next state
    for next_s in states:
        U[next_s] = (0,[])
        for now_s in states:
            p = T[now_s][0] * tp[now_s][next_s] * ep[next_s][ob]
            if p>U[next_s][0]:
                U[next_s] = [p,T[now_s][1]+[next_s]]
    return U

if __name__=="__main__":
    print observations
    per,last = viterbi(observations,states,
                  start_prob,transit_prob,emission_prob)
    print last
    print per