class HomeworkFactory():

    def __init__(self):        
        self.print_format = ""
        self._creators = {}
    
    def register_homework(self,type,creator):
        self._creators[type] = creator
        
    def get_homework(self,type):
        creator = self._creators.get(type)
        if not creator:
            raise ValueError(type)
        return creator()
        
    def is_homework_exist(self,type):
        if type in self._creators:
            return True
        else:
            return False

factory = HomeworkFactory()
