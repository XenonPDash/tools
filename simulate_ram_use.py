#encoding=utf-8
# 参考 https://blog.csdn.net/wy_hhxx/article/details/104731859/
import sys, time

def men_eat():

    size = input("请输入要消耗的内存大小（单位支持M、G，单位默认为M，可手动输入）:")
    mem_list = []

    try:
        blocks = int(size)
        print("使用内存"+str(blocks)+"MB")
        for i in range(0, blocks ):
            mem_list.append (' ' * 1024 * 1024)
        while(True):
                pass

    except ValueError: 
        if size[-1].upper()=="G":
            try:
                blocks = int(size[0:-1])
                print("使用内存"+str(blocks)+"GB")
                for i in range(0, blocks):
                    mem_list.append ( ' ' * 1024 * 1024 *1024 )
                while(True):
                    pass
            except ValueError:
                print("请输入正确的参数")

        elif size[-1].upper()=="M":
            try:
                blocks = int(size[0:-1])
                print("使用内存"+str(blocks)+"MB")
                for i in range(0, blocks ):
                    mem_list.append ( ' ' * 1024 * 1024)
                while(True):
                    pass
            except ValueError:
                print("请输入正确的参数")
            
        else:
            print("请输入正确的参数")


if __name__ == '__main__':
    try:
        men_eat()
    except KeyboardInterrupt:
        print("即将释放内存.")



