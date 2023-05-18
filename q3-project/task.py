class Task:
    def __init__(self, duration, _task):
        self.duration = duration
        self.task = _task
    
    def complete(task, person):
        if task == "get wood":
            person.backpack.append("wood")
        if task == "get stone":
            person.backpack.append("stone")
        if task == "get food":
            person.backpack.append("food")
        if task == "build":
            pass # figure out how to build things first