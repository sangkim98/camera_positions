import open3d as o3d
import numpy as np

PYRAMID_VERTICES = np.asarray([[1, 1, 2.5],
                               [1, -1, 2.5],
                               [-1, 1, 2.5],
                               [-1, -1, 2.5],
                               [0, 0, 0]])

TRIANGULAR_FACES = np.asarray([[1,0,4],
                               [0,2,4],
                               [3,1,4],
                               [2,3,4],
                               [0,1,2],
                               [2,1,3]])

def create_base_pyramid(color):
    
    pyramid_base = o3d.geometry.TriangleMesh()
    
    pyramid_base.vertices = o3d.utility.Vector3dVector(PYRAMID_VERTICES)
    pyramid_base.triangles = o3d.utility.Vector3iVector(TRIANGULAR_FACES)
    
    colored_pyramid = pyramid_base.paint_uniform_color(np.asarray(color))
    
    colored_pyramid.vertex_colors[4] = np.asarray([1,0,0])
    
    return colored_pyramid

