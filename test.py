import ErrorHook
# ErrorHook.init()


with open(".\ErrorHook\README.md", "r", encoding='utf-8') as fh:
    print(fh.read())
# print(1/0)
# print(a)
raise BaseException('I am a Error.')