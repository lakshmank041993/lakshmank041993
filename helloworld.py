class Hello_world:
    def __init__(self,name : str) -> None:
        self.name =name

    def hello_world_def(self):
        print("hello world"+self.name)

a=Hello_world("lakshman")

a.hello_world_def()


