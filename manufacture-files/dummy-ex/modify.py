# dummy-ex 폴더 내의 모든 txt 파일이름을 지원자_xx 에서 합격자_xx 로 변경
import os

# C:\Users\Woong\PycharmProjects\hackerthon-python\manufacture-files\dummy-ex

os.chdir(r'C:\Users\Woong\PycharmProjects\hackerthon-python\manufacture-files\dummy-ex')
filenames = os.listdir('.')

# print(filenames)
for filename in filenames:
    txt = os.path.splitext(filename)[-1]

    if txt == '.txt':
        os.rename(filename, filename.replace('지원자', '합격자'))








