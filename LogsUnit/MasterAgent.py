from LogsUnit.CollectorAgent import CollectorAgent

class MasterAgent:
    def __init__(self):
        self.collectorAgents = []

    def addCollectorAgent(self, agent):
        if isinstance(agent, CollectorAgent):
            self.collectorAgents.append(agent)
        return

    def saveNewLog(self, log):
        print("saving new log ...\n"+log)

    pass