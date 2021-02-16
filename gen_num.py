import random

def gen_num1(n):
    '''
    gen num list without double num
    '''
    num_list=list(range(n))#[0,n-1]
    random.shuffle(num_list)
    return num_list

def gen_num2(n):
    '''
    gen num list n 
    '''
    num_list = [random.randint(0,100) for _ in range(n)]#[0,100] [0,n-1]
    return num_list

num_list = gen_num2(100)
# print(num_list)


