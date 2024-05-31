import time

class Stopwatch:
    def _init_(self):
        self.start_time = 0
        self.end_time = 0
        
    def start(self):
        self.start_time = time.time()
        print("Stopwatch started !")
        
    def stop(self):
        self.end_time = time.time()
        print("Stopwatch stopped !")
        
    def recorded_time(self):
        if self.start_time == 0:
            print("Please start the stopwatch first.")
        elif self.end_time == 0:
            print("Please stop the stopwatch to get the elapsed time.")
        else:
            recorded = self.end_time - self.start_time
            print(f"Recorded time: {recorded} seconds")
            
def main():
    stopwatch = Stopwatch()
    
    input("Press Enter to start the stopwatch !")
    stopwatch.start()
    
    input("Press Enter to stop the stopwatch !")
    stopwatch.stop()
    
    stopwatch.recorded_time()
    
if __name__ == "__main__":
    main()