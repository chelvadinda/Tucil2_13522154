import matplotlib.pyplot as plt
import numpy as np
import time  

curve_points = []
control_points = []
mid_points = []

def get_input():
    while True:
        try:
            p0 = tuple(map(float, input("Koordinat titik p0 (x y): ").split()))
            p1 = tuple(map(float, input("Koordinat titik p1 (x y): ").split()))
            p2 = tuple(map(float, input("Koordinat titik p2 (x y): ").split()))
            iteration = int(input("Banyak iterasi yang dilakukan: "))
            if iteration <= 0:
                print("Banyak iterasi harus lebih besar dari 0. Silakan coba lagi.")
                continue
            return p0, p1, p2, iteration
        except ValueError:
            print("Input tidak valid. Pastikan Anda memasukkan angka.")
        except KeyboardInterrupt:
            print("\nProgram berhenti.")
            exit()
        return p0, p1, p2, iteration

# divide and conquer #
def result(p0, p1, p2, iteration):
    curve_points.append(p0)
    divide_conquer(p0, p1, p2, 0, iteration)
    curve_points.append(p2)

def divide_conquer(p0, p1, p2, current_Iteration, iteration):
    if current_Iteration < iteration:
        mid1 = [(p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2]
        mid2 = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
        mid = [(mid1[0] + mid2[0]) / 2, (mid1[1] + mid2[1]) / 2]
        mid_points.append(mid1)
        mid_points.append(mid2)
        mid_points.append(mid)

        current_Iteration += 1
        # kiri
        divide_conquer(p0, mid1, mid, current_Iteration, iteration)
        curve_points.append(mid)
        # kanan
        divide_conquer(mid, mid2, p2, current_Iteration, iteration)

def plot_curve(curve_points, title, color, label):
    x = [curvePoint[0] for curvePoint in curve_points]
    y = [curvePoint[1] for curvePoint in curve_points]
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
    p0, p1, p2, iteration = get_input()
    # Start time
    start_time = time.time()
    points = [p0,p1,p2]
    
    # Devide Conquer
    result(p0, p1, p2, iteration)
    end_time = time.time() # end time setelah dnc #
    
    # Plot Bezier Curves
    plot_curve(curve_points, 'Bezier Curves', 'orange', 'Divide and Conquer')
    
    # Plot Control Polygon
    plot_control_polygon(points, 'black')

    # Plot Control Points
    plot_control_points(points, 'red')
    plt.legend()
    plt.show()
    
    # waktu eksekusi
    execution_time = (end_time - start_time) * 1000
    print("Execution time:", execution_time, "ms")

if __name__ == "__main__":
    main()
