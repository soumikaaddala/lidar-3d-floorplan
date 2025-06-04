import laspy
import numpy as np

def read_las_file(file_path):
    las = laspy.read(file_path)
    x = las.x
    y = las.y
    z = las.z
    return np.vstack((x, y, z)).T
