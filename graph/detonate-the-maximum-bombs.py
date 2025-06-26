class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        adj_list = defaultdict(list)

        def former_explodes_latter(bomb_one, bomb_two):
            one_x, one_y, one_radius = bomb_one
            two_x, two_y, two_radius = bomb_two

            distance = (((one_x - two_x) ** 2) + ((one_y - two_y) ** 2)) ** 0.5 ## Pythagorean theorem to get distance between two points 

            if distance <= one_radius:
                return True
            
            return False

        def dfs(node, visited):
            visited.add(node)
            count = 1

            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    count += dfs(neighbor, visited)

            return count

        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                if former_explodes_latter(bombs[i], bombs[j]):
                    adj_list[i].append(j)
                
                if former_explodes_latter(bombs[j], bombs[i]):
                    adj_list[j].append(i)
        
        return max(dfs(bomb, set()) for bomb in range(len(bombs)))