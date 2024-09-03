

"""
graph = {
        'Node' : [(neighboring_node, multiplier), (""), ("")]
}

(starting_value, starting_unit, target_unit)


"""

#(multiplier, starting_node, neighboring_node)
conversions = [
        (0.3048, 'ft', 'm'),
        (3.28084, 'm', 'ft'),
        (12, 'ft', 'in'),
        (0.08333333, 'in', 'ft'),
        (2.54, 'in', 'cm'),
        (0.3937008, 'cm', 'in'),
]

"""
graph =
{
    'ft': [('m', 0.3048), ('in', 12)]
    'cm': [('in', 0.3937008)]
}
"""
def conversionsToGraph(conversions):
    
        conversionsGraph = {}

        for multiplier, starting_node, neighboring_node in conversions:
                if starting_node not in conversionsGraph:
                        conversionsGraph[starting_node] = [(neighboring_node, multiplier)]
                else:
                        conversionsGraph[starting_node].append((neighboring_node, multiplier))
        
        return conversionsGraph

#dfs/bfs to find the path
#path: ft, in, cm => starting_value * 12 * 2.54 => result
def convert(graph, request):

        def dfs_recursive(graph, starting_node, target_node, units, visited=None, path=None):

                if visited == None:
                        visited = set()
                if path == None:
                        path = []

                visited.add(starting_node)
                path.append(starting_node)

                if starting_node == target_node:
                        return [path, units]
                
                for neighbor, multiplier in graph[starting_node]:
                        if neighbor not in visited:
                                result = dfs_recursive(graph, neighbor, target_node, (units * multiplier), visited, path)
                                if result:
                                        return result
                                
                path.pop()
                visited.remove(starting_node)

        path = dfs_recursive(graph, request[1], request[2], request[0])
        return path


graph = conversionsToGraph(conversions)
starting_unit = 'cm'
starting_units = 560
target_unit = 'ft'
result = convert(graph, (starting_units, starting_unit, target_unit))

print(result[1])

        