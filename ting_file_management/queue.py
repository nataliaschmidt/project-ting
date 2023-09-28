from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    def search(self, index):
        if index < 0 or index > len(self.queue) - 1:
            raise IndexError("Índice Inválido ou Inexistente")
        return self.queue[index]

    def __str__(self):
        return f"""
            Os arquivos a serem lidos são: {self.queue}
        """


# new_queue = Queue()
# new_queue.queue(1)
# print(new_queue)
