from helpers import shapes, getParsedData, visualizeGrid
import time


def addShapeToGrid(grid, shape, value="X"):
    grid.update({(x, y): value for x, y in shape})


def startShapeCoords(highest_y, shape):
    return [(2 + x, highest_y + 4 + y) for x, y in shape]


def checkIfHitShape(current_pos, grid):
    nextBlockPos = [(bx, by - 1) for bx, by in current_pos]
    hitShape = any((zx, zy) in grid for zx, zy in nextBlockPos)
    floorCollision = any(y < 1 for _, y in nextBlockPos)
    if hitShape or floorCollision:
        return True, current_pos  # Return current (valid) position
    return False, nextBlockPos


def pushedByGas(grid, dir, current_pos):
    dx, dy = dir
    nextBlockPos = [(sx + dx, sy + dy) for sx, sy in current_pos]
    hitsWall = any(x < 0 or x >= 7 for x, _ in nextBlockPos)
    hitShape = any((zx, zy) in grid for zx, zy in nextBlockPos)
    if hitsWall or hitShape:
        return current_pos
    return nextBlockPos


def runSimulation(grid, operations, raw, limit=2022, visualize=True, waitTime=1):
    highest_y = 0
    opp_idx = 0
    shape_idx = 0

    i = 0
    while i < limit:
        shape_idx = shape_idx % len(shapes)
        shape = shapes[shape_idx]
        current_pos = startShapeCoords(highest_y, shape)
        blocked = False
        copied_grid = grid.copy()
        addShapeToGrid(copied_grid, current_pos)
        visualizeGrid(copied_grid, raw, opp_idx % len(operations) - 1)
        while not blocked:
            current_opp = operations[opp_idx % len(operations)]

            current_pos = pushedByGas(grid, current_opp, current_pos)

            if visualize:
                time.sleep(waitTime)
                copied_grid2 = grid.copy()
                addShapeToGrid(copied_grid2, current_pos)
                visualizeGrid(copied_grid, raw, opp_idx % len(operations) - 1)

            hitShape, nextBlockPos = checkIfHitShape(current_pos, grid)

            if visualize:
                grid_copy_3 = grid.copy()
                time.sleep(waitTime)
                addShapeToGrid(grid_copy_3, nextBlockPos)
                visualizeGrid(copied_grid, raw, opp_idx % len(operations) - 1)

            if hitShape:
                blocked = True
                addShapeToGrid(grid, current_pos, f"{i % 9 + 1}")
                i += 1
                if visualize:
                    time.sleep(waitTime)
                    visualizeGrid(copied_grid, raw, opp_idx % len(operations) - 1)
                highest_y = max(y for _, y in current_pos)
                shape_idx += 1
            else:
                current_pos = nextBlockPos

            opp_idx += 1


def main(input):
    grid = dict()
    operations, raw = getParsedData(input)
    runSimulation(grid, operations, raw, 2022, True, 0.1)

    max_y = max(y for _, y in grid.keys())
    print(f"Highest y: {max_y}")
    # visualizeGrid(grid, list(), 0)


if __name__ == "__main__":
    main("sample")
