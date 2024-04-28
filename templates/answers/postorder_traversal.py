root = {'name': 'A', 'children': [
                {'name': 'B', 'children': [
                    {'name': 'D', 'children':[
                        {'name': 'H', 'children':[]},
                        {'name': 'I', 'children': [
                            {'name': 'M', 'children': []}
                        ]}
                    ]}, 
                    {'name': 'E', 'children': [
                        {'name': 'J', 'children': []}
                    ]},
                {'name': 'C', 'children': [
                    {'name': 'F', 'children': [
                        {'name': 'K', 'children': []},
                        {'name': 'L', 'children': []}
                    ]},
                    {'name': 'G','children': []}
                ]}]}]}


def postorder_traversal(node: dict) -> list:
    results = []
    for child in node['children']:
        results.extend(postorder_traversal(child))
    results.append(node['name'])
    return results



# print(postorder_traversal(root))