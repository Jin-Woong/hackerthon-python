import os

# os.chdir ('폴더경로') 지정한 폴더로 이동
# os.listdir('폴더경로') 폴더에 저장된 전체 파일목록을 list 로 반환
# os.rename('현재파일명', '바꿀파일명') 파일이름 변경
# os.path.splitext('파일이름') 파일 경로와 확장자를 분리하여 반환

# C:\Users\Woong\PycharmProjects\hackerthon-python\manufacture-files\dummy-ex

# r'~~~'  r : escape 문자 무시
# filename = os.path.splitext(r'C:\Users\Woong\PycharmProjects\hackerthon-python\manufacture-files\dummy-ex\dummy.py')
# print(filename)

os.chdir(r'C:\Users\Woong\PycharmProjects\hackerthon-python\manufacture-files\dummy-ex')
filenames = os.listdir('.')
# print(filenames)

for filename in filenames:
    txt = os.path.splitext(filename)[-1]
    if txt == '.txt':
        os.rename(filename, f'지원자_{filename}')



