import ErrorHook
# ErrorHook.init()

# print(1/0)
# print(a)
def aaa():
    raise BaseException('I am a Error.')
def bbb():
    aaa()
def ccc():
    bbb()
# while True:
#     pass
ccc()