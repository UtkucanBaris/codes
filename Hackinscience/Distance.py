def dist(points):
    x = abs(max(points))
    y = abs(min(points))
    if max(points) and min(points) > 0:
        points= x-y
        return points
    if max(points) < 0 and min(points) < 0: 
        points=abs(x-y)
        return points
    if max(points) > 0 and min(points) < 0 or max(points) < 0 and min(points) > 0:
        points=x+y
        return points
if __name__ == "__main__":
    assert dist([1,-9]) ==10
    assert dist([-1,-2,-3]) ==2 
    assert dist([1,0.01]) ==0.99 
    assert dist([1, 2, 3]) == 2
    assert dist([1, 2, 3, 2.5]) == 2
    assert dist([1, 2, 3, 2.5, 3.5]) == 2.5
    assert dist([1, 2, 3, 2.5, 3.5, 120]) == 119
    assert dist([1, 2, 3, 2.5, 3.5, 120, -1000]) == 1120