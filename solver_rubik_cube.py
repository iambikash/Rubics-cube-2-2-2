import rubik_cube
from rubik_cube import *
import time
from collections import deque


from collections import deque

def shortest_path(start, end):
    visited = {}
    visited[start] = (start, -1)
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node == end:
            break

        for move in rubik_cube.quarter_twists:
            next_node = rubik_cube.perm_apply(node, move)

            if next_node not in visited:
                visited[next_node] = (node, rubik_cube.quarter_twists_names[move])
                queue.append(next_node)

    if len(visited) == 1:
        return []

    if end in visited:
        path = []
        node = end

        while node != start:
            prev_node, move = visited[node]
            path.append(move)
            node = prev_node

        return list(reversed(path))

    else:
        return None

def shortest_path_optimized (start, end):
    if start == end:
        return []

    start_parent = {}
    end_parent = {}
    visited_start = set()
    visited_end = set()
    start_q = deque()
    start_q.append(start)
    end_q = deque()
    end_q.append(end)
    start_dist = {start: 0}
    end_dist = {end: 0}
    found = False

    while start_q or end_q:
        if start_q:
            curr = start_q.popleft()

            for move in rubik_cube.quarter_twists:
                neigh = rubik_cube.perm_apply(move, curr)
                if neigh in start_dist.keys():
                    if start_dist[neigh] > start_dist[curr] + 1:
                        start_dist[neigh] = start_dist[curr] + 1
                        start_parent[neigh] = (curr, move)
                        start_q.append(neigh)
                else:
                    start_dist[neigh] = start_dist[curr] + 1
                    start_parent[neigh] = (curr, move)
                    start_q.append(neigh)

            visited_start.add(curr)

        if curr in visited_end and curr in visited_start:
            found = True
            break

        if end_q:
            curr = end_q.popleft()

            for move in rubik_cube.quarter_twists:
                neigh = rubik_cube.perm_apply(move, curr)
                if neigh in end_dist.keys():
                    if end_dist[neigh] > end_dist[curr] + 1:
                        end_dist[neigh] = end_dist[curr] + 1
                        end_parent[neigh] = (curr, move)
                        end_q.append(neigh)
                else:
                    end_dist[neigh] = end_dist[curr] + 1
                    end_parent[neigh] = (curr, move)
                    end_q.append(neigh)

            visited_end.add(curr)

        if curr in visited_start and curr in visited_end:
            found = True
            break

    if found:
        quarter_twists_inverse = {F: Fi, L: Li, U: Ui, Fi: F, Li: L, Ui: U}
        movesto_start = [rubik_cube.quarter_twists_names[start_parent[curr][1]]]
        parent = start_parent[curr][0]

        while parent != start:
            movesto_start.append(rubik_cube.quarter_twists_names[start_parent[parent][1]])
            parent = start_parent[parent][0]

        movesto_end = []

        if curr != end:
            movesto_end = [rubik_cube.quarter_twists_names[quarter_twists_inverse[end_parent[curr][1]]]]
            parent = end_parent[curr][0]

            while parent != end:
                movesto_end.append(rubik_cube.quarter_twists_names[quarter_twists_inverse[end_parent[parent][1]]])
                parent = end_parent[parent][0]

        return movesto_start[::-1] + movesto_end

    else:
        return None


start = time.time()
path = shortest_path(
                     #(6, 7, 8, 20, 18, 19, 3, 4, 5, 16, 17, 15, 0, 1, 2, 14, 12, 13, 10, 11, 9, 21, 22, 23),
                    (23,0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22),
                    #(19, 2, 9, 6, 16, 17, 3, 13, 12, 23, 20, 14, 5, 1, 22, 7, 0, 10, 18, 11, 21, 4, 8, 15), 
                     (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
end = time.time()

print("PATH found by normal bfs:" + str(path))
print("time in secs by normal bfs:" + str(end - start))


start = time.time()
path = shortest_path_optimized(
                     #(3, 4, 5,6, 7, 8, 20, 18, 19,  16, 17, 15, 0, 1, 2, 14, 12, 13, 10, 11, 9, 21, 22, 23),
                     (23,0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22),
                     #(20, 18, 19,6, 7, 8, 3, 4, 5, 16, 17, 15, 0, 1, 2, 14, 12, 13, 10, 11, 9, 21, 22, 23),
                     (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
end = time.time()

print("PATH found by bidirectional bfs:" + str(path))
print("time in secs by bidirectional bfs:" + str(end - start))
