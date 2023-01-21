class single:
    def __init__(self, array):
        self.array = array
        
    def printer(self):
        nodes = []
        array = self.array
        for i in array:
            nodes.append(f'[{i}]')
        return '->'.join(nodes)
    
l = single('My Name is buchi')
print(l.printer())
