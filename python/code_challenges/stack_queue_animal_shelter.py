from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.dog_queue = Queue()
        self.cat_queue = Queue()

    def enqueue(self, animal):
        if animal.value == 'dog':
            self.dog_queue.enqueue(animal)
        if animal.value == 'cat':
            self.cat_queue.enqueue(animal)

    def dequeue(self, pref):
        if pref == "dog" and not self.dog_queue.is_empty():
            return self.dog_queue.dequeue()
        if pref == "cat" and not self.cat_queue.is_empty():
            return self.cat_queue.dequeue()
        else:
            return None


class Dog:
    def __init__(self):
        self.value = "dog"


class Cat:
    def __init__(self):
        self.value = "cat"
