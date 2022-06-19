class Equatable:

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Equatable):
            return False

        if len(obj.get_list()) != len(self.get_list()):
            return False

        current_list = self.get_list()
        new_list = obj.get_list()
        for index, i in enumerate(new_list):
            if current_list[index] != i:
                return False

        if isinstance(obj, self.__class__):
            return obj.__dict__ == self.__dict__
        return False

    def get_list(self) -> list:
        return None
