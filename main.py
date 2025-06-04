import matplotlib.pyplot as plt
from utils import read_las_file

def visualize_point_cloud(points):
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=points[:, 2], cmap='viridis', s=1)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    plt.title("3D Lidar Point Cloud Visualization")
    plt.show()

if __name__ == "__main__":
    file_path = "your_file.las"  # Replace with your actual path
    print("Reading .las file...")
    points = read_las_file(file_path)
    print("Rendering 3D plot...")
    visualize_point_cloud(points)
