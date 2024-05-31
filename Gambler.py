import random

# taking input
stake = int(input("Enter the starting Stake : "))
goal = int(input("Enter the Final goal: "))
N = int(input("Enter the Number of chances : "))

def gambler_simulation(stake, goal, N):
    wins = 0
    total_bets = 0

    for i in range(N):
        cash = stake                            # stake = starting money
        bets = 0

        while cash > 0 and cash < goal:         #  0 < cash <goal
            bets += 1
            if random.random() < 0.5:          # Assuming 50/50 chance as random.random has range 0.0-0.9
                cash += 1
            else:
                cash -= 1

        total_bets += bets
        if cash == goal:
            wins += 1

    win_percentage = (wins / N) * 100
    loss_percentage = 100 - win_percentage

    print("Number of Wins:", wins)
    print("Win Percentage:", win_percentage, "%")
    print("Loss Percentage:", loss_percentage, "%")
    
    
# calling method
gambler_simulation(stake, goal, N)