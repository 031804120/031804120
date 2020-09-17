try:
        t1 = open(file1,'r',encoding='UTF-8').read()
        t2 = open(file2,'r',encoding='UTF-8').read()
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    except IOError as e:
        print(e)
