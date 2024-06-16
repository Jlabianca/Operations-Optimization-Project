from pulp import LpMaximize, LpProblem, LpVariable

def optimize_example():
    model = LpProblem(name="optimization-problem", sense=LpMaximize)
    x = LpVariable(name="x", lowBound=0)
    y = LpVariable(name="y", lowBound=0)
    model += 2 * x + 3 * y
    model += (4 * x + 2 * y <= 8, "constraint_1")
    model += (3 * x + y <= 6, "constraint_2")
    model.solve()
    for var in model.variables():
        print(f"{var.name}: {var.value()}")
    print(f"Objective: {model.objective.value()}")

if __name__ == "__main__":
    optimize_example()
