# Finds the depth of a binary tree
# Binary tree is a dictionary where 'children': [{More children}]


root = {'data': 'A', 'children': [{'data': 'B', 'children':
[{'data': 'D', 'children': []}]}, {'data': 'C', 'children':
[{'data': 'E', 'children': [{'data': 'G', 'children': []},
{'data': 'H', 'children': []}]}, {'data': 'F', 'children': []}]}]}

def max_depth(node):
    if len(node['children']) == 0:
        return 0
    depth = 0
    for child in node['children']:
        child_depth = max_depth(child)
        if child_depth > depth:
            depth = child_depth
    return depth + 1
