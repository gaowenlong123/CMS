import os


def change_path(path="../Yamls/test/test1.yaml"):
    ''' "../Yamls/test/Login.yaml"     根据当前路径获得新路径 '''

    # 暂时不用
    back_num = len(path.split('/')[0])
    if back_num >3:
        return back_three(path ,back_num)


    PATH=lambda p : os.path.abspath(
        os.path.join(os.path.dirname(__file__),p)
    )
    return PATH(path)



def write_sys_path(path=''):
    ''' 在该进程中，写进path中  '''
    import sys
    sys.path.append(path)

def back_three(path ,count):
    pass
