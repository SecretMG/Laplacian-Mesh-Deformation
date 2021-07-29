import pickle


def load_obj(file_name):
    '''因为顺序的不确定性，没有使用本函数
    file_name: .obj文件的位置
    return: vertex list
    '''
    assert file_name.endswith('.obj')
    vertexes = []
    with open(file_name) as file:
        line_ls = file.readlines()
        for line in line_ls:
            words = line.split()
            if words[0] == 'v':
                # 只有以v为标志的是顶点，vt和vn都不是
                ver = words[1: 4]
                ver = [float(v) for v in ver]
                vertexes.append(ver)
    return vertexes


def load_pkl(file_name):
    '''
    file_name: .obj文件的位置
    return: vertex list (anchors)
    '''
    with open(file_name, 'rb') as file:
        # 注意以二进制读取.pkl文件
        anchors = pickle.load(file)
    return anchors