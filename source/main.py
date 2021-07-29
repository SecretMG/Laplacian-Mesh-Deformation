import numpy as np

from S3DGLPy.PolyMesh import PolyMesh
from utlis.loader import load_obj, load_pkl
from LMP import LMP




if __name__ == '__main__':
    in_file = 'blender/in.obj'
    mid_file = 'blender/mid.obj'
    anchor_file = 'blender/anchor.pkl'

    print('get vertex_ls')
    vertex_ls = load_obj(mid_file)
    vertex_ls = np.array(vertex_ls)

    print('get anchor_ls & id')
    anchor_id_ls = load_pkl(anchor_file)
    anchor_id_ls = np.array(anchor_id_ls)
    anchor_ls = vertex_ls[anchor_id_ls]     # 从index转换到coord
    # 注意：如果点选了Keep Vert Order，这里的anchor坐标应当和文件中的相应行一致，如果不一致，无法正确实验


    poly = PolyMesh()
    poly.loadObjFile(in_file)
    solver = LMP(poly)  # poly.mesh是原来的
    print('solving matrix (mean weight)...')
    solver.forward(anchor_ls, anchor_id_ls, mode='mean')    # anchor是改变后的
    solver.mesh.saveObjFile('blender/out_mean.obj')