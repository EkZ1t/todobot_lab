
class TodoElement:
    def __init__(self, text: str):
        self.text = text 

class ToDoList:
    def __init__(self):
        self.items = []
        
    def create(self, text: str):
        item = TodoElement(text)
        self.items.append(item)
        
    def update(self, pk: int, new_text: str):
        if 0 <= int(pk) < len(self.items):
            self.items[int(pk)].text = new_text  
        
    def delete(self, pk: int):
        if 0 <= int(pk) < len(self.items):
            self.items.pop(pk)
        
    def read(self):
        return [item.text for item in self.items]
    
    def retrieve(self, pk: int):
        if 0 <= int(pk) < len(self.items):
            return self.items[pk].text 