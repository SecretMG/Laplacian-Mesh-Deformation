import numpy as np
from scipy.sparse import coo_matrix, block_diag
from scipy.sparse.linalg import lsqr

from S3DGLPy.PolyMesh import getEdgeInCommon


class LMP:
    def __init__(self, mesh):
        self.mesh = mesh
        self.N, self.K = None, None
        self.anchor_ls, self.anchor_id_ls = None, None
        self.mode = None
        self.Ls, self.delta = None, None

    def forward(self, anchor_ls, anchor_id_ls, mode='mean'):
        self.N = self.mesh.VPos.shape[0]     # 总点数
        self.K = anchor_ls.shape[0]          # 锚点数
        self.anchor_ls, self.anchor_id_ls = anchor_ls, anchor_id_ls
        self.mode = mode

        self.calc_Ls()
        self.delta = self.Ls.dot(self.mesh.VPos)    # Ls * 原坐标
        for i in range(self.K):
            self.delta[self.N + i] = self.anchor_ls[i]  # 将delta中的锚点部分改成新坐标

        A = block_diag((self.Ls, self.Ls, self.Ls))
        b = np.hstack((self.delta[:, 0], self.delta[:, 1], self.delta[:, 2]))
        x = lsqr(A, b)[0]
        x = x.reshape((3, -1)).T

        self.mesh.VPos = x



    def calc_Ls(self):
        # D-A
        data = []
        row, col = [], []
        if self.mode == 'mean':
            for i in range(self.N):
                vertex = self.mesh.vertices[i]  # 注意这里是vertex类，而非ids
                neighbors = [v.ID for v in vertex.getVertexNeighbors()]  # ids
                degree = len(neighbors)  # 本点的邻居数
                data += [degree] + [-1] * degree
                row += [i] * (degree + 1)  # 每一行有（degree+1）项不为0
                col += [i] + neighbors  # 依次为本点，以及各邻居所在列
            for i in range(self.K):
                data += [1]
                row += [self.N + i]
                col += [self.anchor_id_ls[i]]
            self.Ls = coo_matrix((data, (row, col)), shape=(self.N + self.K, self.N)).tocsr()  # 将处于矩阵中相同位置的值相加到一起
        elif self.mode == 'cot':
            pass
        else:
            print('Error: not supported mode!')

