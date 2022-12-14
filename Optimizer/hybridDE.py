import geatpy as ea
from Optimizer import MyProblem
from Optimizer import templet


def hybridDE_exe(Dim, max_iter, NIND, benchmark, scale_range, VarType):
    obj_trace = []
    problem = MyProblem.Problem(Dim, benchmark, scale_range, obj_trace, VarType)  # 实例化问题对象
    population = ea.Population(Encoding="RI", NIND=NIND)
    """===========================算法参数设置=========================="""
    myAlgorithm = templet.soea_DE_currentToBest_1_L_templet(problem, population)
    myAlgorithm.MAXGEN = max_iter
    myAlgorithm.drawing = 0
    """=====================调用算法模板进行种群进化====================="""
    solution = ea.optimize(myAlgorithm, verbose=False, outputMsg=False, drawLog=False, saveFlag=False)
    return obj_trace, solution["CV"][0]
