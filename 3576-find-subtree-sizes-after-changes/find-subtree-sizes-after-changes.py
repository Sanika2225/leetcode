
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = {}

        def dfs(node):
            ch = s[node]

            old = last.get(ch, -1)
            last[ch] = node

            for child in children[node]:
                dfs(child)

            # Restore previous ancestor of this character
            if old == -1:
                del last[ch]
            else:
                last[ch] = old

            # Update parent of node
            if old != -1:
                new_parent[node] = old

        dfs(0)

        # Build the modified tree
        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        # Calculate subtree sizes
        ans = [0] * n

        def calculate(node):
            ans[node] = 1

            for child in new_children[node]:
                ans[node] += calculate(child)

            return ans[node]

        calculate(0)

        return ans
