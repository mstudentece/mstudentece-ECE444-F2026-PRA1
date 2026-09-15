class utils:
    def reversed(self, number: int) -> int:
        if type(number) is not int:
            raise TypeError("input must be int")
        if number < 0:
            return -int(str(abs(number))[::-1])
        return int(str(number)[::-1])

    def formatter(self, number: int):
        if type(number) is not int:
            raise TypeError("input must be int")
        return bin(number), oct(number)