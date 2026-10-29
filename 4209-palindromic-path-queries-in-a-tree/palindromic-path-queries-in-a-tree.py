
class Solution:
    def palindromePath(self, n, edges, s, queries):
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        prefix = [0] * n
        timer = 0

        # Iterative DFS: Euler tour and root-prefix masks
        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                tin[u] = timer
                timer += 1

                prefix[u] = (
                    (prefix[p] if p != -1 else 0)
                    ^ (1 << (ord(s[u]) - ord('a')))
                )

                stack.append((u, p, 1))

                for v in reversed(graph[u]):
                    if v != p:
                        parent[v] = u
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        # Binary lifting table
        LOG = n.bit_length()
        up = [parent[:]]

        for k in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[v]] for v in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            for k in range(LOG):
                if diff & (1 << k):
                    u = up[k][u]

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]

            return parent[u]

        # Fenwick tree supporting range XOR updates
        # and point queries
        bit = [0] * (n + 1)

        def add(i, val):
            i += 1
            while i <= n:
                bit[i] ^= val
                i += i & -i

        def point(i):
            result = 0
            i += 1

            while i > 0:
                result ^= bit[i]
                i -= i & -i

            return result

        def update_subtree(u, delta):
            add(tin[u], delta)

            if tout[u] < n:
                add(tout[u], delta)

        chars = list(s)
        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                old_mask = 1 << (ord(chars[u]) - ord('a'))
                new_mask = 1 << (ord(c) - ord('a'))
                delta = old_mask ^ new_mask

                if delta:
                    update_subtree(u, delta)
                    chars[u] = c

            else:
                u = int(parts[1])
                v = int(parts[2])

                w = lca(u, v)

                pu = prefix[u] ^ point(tin[u])
                pv = prefix[v] ^ point(tin[v])

                mask = (
                    pu ^ pv
                    ^ (1 << (ord(chars[w]) - ord('a')))
                )

                # True if at most one bit is set
                answer.append((mask & (mask - 1)) == 0)

        return answer
