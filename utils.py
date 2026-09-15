class utils:
    def reverse(self, number: int) -> int:
        if number < 0:
            return -int(str(abs(number))[::-1])
        return int(str(number)[::-1])

    def formatter(self, number: int):
        return bin(number), oct(number)
        
