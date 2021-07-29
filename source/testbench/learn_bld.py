import bpy
import bmesh


'--- 生成cube阵列'
# for k in range(5):
#     for j in range(5):
#         for i in range(5):
#             bpy.ops.mesh.primitive_cube_add(size=0.5, location=[i, j, k])
#             # size is the length, and location belongs to the center


'--- 查看对象'
# objs = bpy.context.selected_objects     # 获取所选对象列表
# print(objs)
# for obs in objs:
#     print(obs.name, obs.location)   # 查看某对象的名字和位置


'--- 选择对象'
def select(name, additive=True):
    if not additive:
        bpy.ops.object.select_all(action='DESELECT')
        # action=['TOGGLE', 'SELECT', 'DESELECT', 'INVERT']
        # TOGGLE：全部取消选中，若已经全部取消选中，则全部选中
        # SELECT：全部选中
        # DESELECT：全部取消选中
        # INVERT：全部反转（原先选中的取消，原先取消的选中）
    bpy.data.objects[name].select_set(True)
# select('Sphere')
# bpy.ops.transform.translate(value=[-1, -1, 0])

'--- 查看激活对象'
# # 若有多个选中对象，则激活对象为最后被选中的对象
# print(bpy.context.object)
# print(bpy.context.active_object)    # 二者等效
def activate(name):
    bpy.context.view_layer.objects.active = bpy.data.objects[name]
# activate('Sphere')
# print(bpy.context.object.name)
# print(bpy.context.selected_objects)


'--- 切换模式'
def mode_set(mode):
    bpy.ops.object.mode_set(mode=mode)
    if mode == 'EDIT':
        bpy.ops.mesh.select_all(action='DESELECT')  # 进入编辑模式时，对于所激活对象的所有点都不进行选中，更加安全
# mode_set('EDIT')


'--- 尝试使用bmesh'
# bpy.ops.mesh.primitive_cube_add(size=2, location=[0, 0, 0])
# bpy.ops.object.mode_set(mode='EDIT')    # 添加一个cube并进入编辑模式


'--- 轻微形变'
def clear():
    # 如果画布本身为空，则调用该函数会报错
    bpy.ops.object.mode_set(mode="OBJECT")  # 首先要进入对象模式
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()
# clear()
# bpy.ops.mesh.primitive_cube_add(size=1, location=[3, 0, 0])
# bpy.ops.object.mode_set(mode='EDIT')
# bpy.ops.mesh.select_all(action='SELECT')
# bpy.ops.transform.vertex_random(offset=0.5)     # 对所有顶点进行随机偏移
# bpy.ops.object.mode_set(mode='OBJECT')
