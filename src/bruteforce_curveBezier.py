import matplotlib.pyplot as plt
import numpy as np
import time  

def get_input():
    p0 = tuple(map(float, input("Koordinat titik p0 (x y): ").split()))
    p1 = tuple(map(float, input("Koordinat titik p1 (x y): ").split()))
    p2 = tuple(map(float, input("Koordinat titik p2 (x y): ").split()))
    iterasi = int(input("Banyak iterasi yang dilakukan: "))
    
    n = iterasi
    for i in range(n):
        if i == 0:
            iterasi = 3
        else:
            iterasi = iterasi * 2 - 1
    
    return p0, p1, p2, iterasi

# BRUTE FORCE #
def brute_force_bezier(points, iterasi):
    result = []
    curvepoints = []
    if iterasi > 1:
        for i in range(iterasi):
            t = i / (iterasi-1)
            x = (1 - t) ** 2 * points[0][0] + 2 * (1 - t) * t * points[1][0] + t ** 2 * points[2][0]
            y = (1 - t) ** 2 * points[0][1] + 2 * (1 - t) * t * points[1][1] + t ** 2 * points[2][1]
            result.append([x, y])
            curvepoints.append([x, y])
    else:
        result.extend(points)
        curvepoints.extend(points)
    return result, curvepoints

def plot_curve(result, title, color, label):
    x = [result[0] for result in result]
    y = [result[1] for result in result]
    plt.plot(x, y, color, label=label)
    plt.scatter(x, y, c=color, s=10, alpha=0.5)

def plot_control_polygon(points, color):
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    plt.plot(x ,y, linestyle='--', color=color, label='Control Polygon')

def plot_control_points(points, color):
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    plt.scatter(x, y, c=color, label='Control Points', s=50)

def main():
    p0, p1, p2, iterasi = get_input()
    # Start time
    start_time = time.time()
    
    # Brute Force
    points = [p0,p1,p2]
    t = np.linspace(0, 1)
    result, curvepoints = brute_force_bezier(points, iterasi)
    
    # End time
    end_time = time.time()
    
    # Plot Bezier Curve
    plot_curve(result, 'Bezier Curves', 'green', 'Brute Force')
    
    # Plot Control Polygon
    plot_control_polygon(points, 'black')

    # Plot Control Points
    plot_control_points(points, 'red')
    plt.legend()
    plt.show()
    
   # Execution time
    execution_time = (end_time - start_time) * 1000
    print("Execution time:", execution_time, "ms")

if __name__ == "__main__":
    main()
