import numpy as np


def algo(graph, no_bug, with_bug, N):
    bug_free   = np.zeros(N+1, dtype=np.bool)
    que = no_bug
    while(True):
        current = que.pop() if len(que) else None
        if current == None:
            break
        if bug_free[current]:
            continue
        bug_free[current] = True
        parents = list(np.where(graph[:,current])[0])
        que.extend(parents)

    bug_prohibit = np.zeros(N+1, dtype=np.bool)
    que = []
    for current in with_bug:
        childs = list(np.where(graph[current,:])[0])
        que.extend(childs)
    while(True):
        current = que.pop() if len(que) else None
        if current == None:
            break
        if bug_prohibit[current]:
            continue
        bug_prohibit[current] = True
        childs = list(np.where(graph[current,:])[0])
        que.extend(childs)



    bug_candidate = np.zeros(N+1, dtype=np.bool)
    origin = [set([]) for i in range(N+1)]
    que = []
    for current in with_bug:
        if not bug_prohibit[current]:
            que.append(current)
            origin[current] = origin[current] | set([current])
    origin_que = [i for i in que]


    del_que = []
    while(True):

        print(que)
        print(origin_que)

        current = que.pop() if len(que) else None
        current_origin = origin_que.pop() if len(origin_que) else None

        # print(f'current {current}')
        # print(f'origin[current] {origin[current]}')
        # print(f'current_origin {current_origin}')
        # print(f'origin[current_origin] {origin[current_origin]}')
        print(origin)
        print(current)
        print(current_origin)
        

        if current == None:
            break
        if bug_free[current]:
            continue
        if bug_candidate[current] and origin[current] and origin[current].isdisjoint(origin[current_origin]):
            childs = list(np.where(graph[current,:])[0])
            del_que.extend(childs)
            origin[current] = origin[current] | origin[current_origin]
            parents = list(np.where(graph[:,current])[0])
            que.extend(parents)
            origin_que.extend([current for i in range(len(parents))])
            print('yajuuuuuuu')
            continue
        if bug_candidate[current] and origin[current] > origin[current_origin]:
            del_que.append(current_origin)
            continue
        bug_candidate[current] = True
        origin[current] = origin[current] | origin[current_origin]
        parents = list(np.where(graph[:,current])[0])
        que.extend(parents)
        origin_que.extend([current for i in range(len(parents))])
    print(del_que)
    
    while(True):
        current = del_que.pop() if len(del_que) else None
        if current == None:
            break
        bug_candidate[current] = False
        childs = list(np.where(graph[current,:])[0])
        del_que.extend(childs)

    print(bug_candidate)
    print(bug_prohibit)
    print(bug_free)

    return np.sum(bug_candidate)


if __name__ == '__main__':
    N, A, B = map(int,input().split(' '))
    graph   = np.zeros((N+1,N+1),dtype=np.bool)
    for i in range(1, N+1):
        command, *parents = input().split(' ')
        parents = list(map(int, parents))
        assert np.max(parents) < i
        graph[parents, i] = True
    no_bug      = list(map(int, input().split(' ')))
    with_bug    = list(map(int, input().split(' ')))
    result = algo(graph, no_bug, with_bug, N)
    print(result)
