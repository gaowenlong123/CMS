#把字典数据写进临时文件中
import pickle
from CMSTestServer.Supplement.Base_File import remove_file
import os

def write_pickle_init(data, path="test.pickle"):           #首先生成临时文件，会直接覆盖之前的文件
    with open(path, 'wb') as f:
        pickle.dump(data, f, 0)


def read_pickle(path='test.pickle' , is_clear=False):                #读取全部，然后删除文件
    data = {}
    with open(path, 'rb') as f:
        try:
            data = pickle.load(f)
        except EOFError:
            data = {}
            print("Error ====> 文件为空")
    if is_clear:
        remove_file(path)
    return data


def writeInfo(data, path="test.pickle"):          #一个一个往里面写数据

    _read = read_pickle(path)
    result = {}
    if _read:
        _read.update(data)
        result = _read
    else:
        result.update(data)
    with open(path, 'wb') as f:

        pickle.dump(result, f)

if __name__ == "__main__":
    pass
    # write_pickle_init({})  #生成文件
    # writeInfo({'112344':1223})       #写一个数据
    # a=read(is_clear=True)             #读数据，删除临时文件
    # print(a)                            #{'112344': 1223}
