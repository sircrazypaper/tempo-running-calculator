sprintDistance = 60
sprintTime = 9.04
speedPercentage = 80

def tempoCalculator():
    metersPerSecond = sprintDistance / sprintTime
    tempoTime = sprintDistance / (metersPerSecond * (speedPercentage / 100))
