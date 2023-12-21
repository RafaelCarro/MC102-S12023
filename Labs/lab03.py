Players = int(input())
NumStr = input().split()
Num = [int(x) for x in NumStr]
LimInfSupStr = input().split()
NumInf = [None] * Players
NumSup = [None] * Players
Points = [None] * Players

j = 0
for i in range(Players):
    NumInf[i] = int(LimInfSupStr[j])
    j += 1
    NumSup[i] = int(LimInfSupStr[j])
    j += 1

for i in range(Players):
    if i > (Players)/2 - 1:
        Points[i] = (NumSup[i] - NumInf[i]) + Num[i]
    else:
        Points[i] = (NumSup[i] - NumInf[i]) * Num[i]

Winner = 0
WinnerPoints = 0
NWinners = 0
for i in range(Players):
    if Points[i] > WinnerPoints:
        WinnerPoints = Points[i]
for i in range(Players):
    if Points[i] == WinnerPoints:
        Winner = i
        NWinners += 1

if NWinners > 1:
    print("Rodada de cerveja para todos os jogadores!")
else:
    print("O jogador número", Winner + 1, "vai receber o melhor bolo da cidade pois venceu com", Points[Winner], "ponto(s)!")
