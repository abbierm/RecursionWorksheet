root = {'data': 'A', 'children': [{'data': 'B', 'children':
[{'data': 'D', 'children': []}]}, {'data': 'C', 'children':
[{'data': 'E', 'children': [{'data': 'G', 'children': []},
{'data': 'H', 'children': []}]}, {'data': 'F', 'children': []}]}]}

def inorder_traversal(node: dict):
    results = []
    if len(node['children']) >= 1:
        results.extend(inorder_traversal(node['children'][0]))
    results.append(node['data'])
    if len(node['children']) >= 2:
        results.extend(inorder_traversal(node['children'][1]))
    return results