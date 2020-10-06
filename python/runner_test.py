import math
import python.simulator.test_configurator as tc
import python.simulator.test_result as tr
import python.simulator.tester as ts
import python.simulator.simulation_configurator as sc
import python.simulator.graph_generator as gg

# simple main that performs a test by running multiple simulation on a fixed config.
ITERATIONS = 10

n = 4096
p = math.log(n, 2)/n

graph = gg.generateERGraph(n, p)


simulationConfigurator = sc.SimulationConfigurator(
    graph_desc="Erdos–Renyi n=" + str(n) + ", p = " + str(p),
    graph=graph,
    bias=0.25,
    opinion_update_rule=sc.OpinionUpdateRule.MAJORITY_DYNAMIC)


testConfigurator = tc.TestConfigurator(simulationConfigurator=simulationConfigurator, iterations=ITERATIONS)

# returns a list of dicts containing simulations id and rounds
results = ts.runTest(testConfigurator=testConfigurator)

testResult = tr.TestResult(testConfigurator=testConfigurator, results=results)
testResult.saveTest(draw=True)
