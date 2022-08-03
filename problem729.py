class MyCalendar:
    def __init__(self):
        self.times = []
    def book(self, start: int, end: int) -> bool:
        ans = True
        for time in self.times:
            if(start == time[0]):
                ans = False
            elif(start<time[0]):
                if(end>time[0]):
                    ans = False
            else:
                if(start<time[1]):
                    ans = False
        if(ans == True):
            self.times.append([start,end])
        return ans


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)