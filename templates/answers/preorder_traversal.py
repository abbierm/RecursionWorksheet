def preorder_traversal(node: dict) -> list[str]: 
    results = []
    results.append(node['name'])
    if len(node['children']) > 0:
        for child in node['children']:
            results.extend(preorder_traversal(child))
    return results