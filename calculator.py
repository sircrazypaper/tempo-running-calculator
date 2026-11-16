def tempoCalculator(sprintDistance, sprintTime):
    metersPerSecond = sprintDistance / sprintTime
    tempoTimes = []
    for i in range(65, 100):
        tempoTime = sprintDistance / (metersPerSecond * (i / 100))
        tempoTimes.append(tempoTime)
    return tempoTimes
