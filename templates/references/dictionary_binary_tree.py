# Used for references for pre-order/ post-order / and inorder searches
# This is the format the algorithms should be able to 


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


root2 = {'name': 'A', 'children': [{'name': 'B', 'children':
[{'name': 'D', 'children': []}]}, {'name': 'C', 'children':
[{'name': 'E', 'children': [{'name': 'G', 'children': []},
{'name': 'H', 'children': []}]}, {'name': 'F', 'children': []}]}]}



m = {'name': 'M', 'children': []} # 13
l = {'name': 'L', 'children': []} # 12
k = {'name': 'K', 'children': []} # 11
j = {'name': 'J', 'children': []} # 10
i = {'name': 'I', 'children': [m]} # 9
h = {'name': 'H', 'children': []} # 8
g = {'name': 'G', 'children': []} # 7
f = {'name': 'F', 'children': [k, l]} # 6
e = {'name': 'E', 'children': [j]} # 5
d = {'name': 'D', 'children': [h, i]} # 4
c = {'name': 'C', 'children': [f, g]} # 3
b = {'name': 'B', 'children': [d, e]} # 2
a = {'name': 'A', 'children': [b, c]} # 1