# ________________________<only Works for odd numbers>________________

numbers = []
Target = 13

for i in range(20):
    numbers.append(i + 1)


def Solve(n):

    if n >= len(numbers) -1:
        return

    if numbers[n] + numbers[n + 1] == Target:
        ans = [numbers[n], numbers[n + 1]]
        print(ans)
    
    Solve(n + 1)

Solve(0)