import bpy
import bmesh
import pickle


if __name__ == '__main__':
    obj = bpy.context.object  # 在对象模式下激活的物体，与编辑模式无关
    anchor_file = 'anchor.pkl'  # 注意，因为本脚本是被blender调用的，所以是以.blend文件为根目录的，最好使.blend文件和本文件在同一目录下
    anchor_ls = [v.index for v in bmesh.from_edit_mesh(bpy.context.active_object.data).verts if v.select]
    print('锚点集：', anchor_ls)
    with open(anchor_file, 'wb') as file:
        pickle.dump(anchor_ls, file)
        print(f'save 锚点集 to {anchor_file}')
