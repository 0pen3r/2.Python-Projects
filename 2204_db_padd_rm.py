## 서브라임에서 사용 최적화
## 경로와 스위칭 단어 선택


import os

#파일 내용 바꿀 대상 경로
dir_path='.\\db_list'

print('\n# Path is = ' + dir_path + '\n')
print('# Database List\n')

#파일 리스트
file_list = os.listdir(dir_path)
print(file_list)

#old_word를 new_word로, 공백도 제거 가능
def replace_blank(old_word, new_word):
	for file_name in file_list:
		db_path = dir_path + '\\' + file_name
		f = open(db_path, 'r')
		lines = f.readlines()
		f.close()

		fw = open(db_path, 'w')
		for line in lines:
			fw.write(line.replace(old_word, new_word))
			fw.close()
		print('- clear  ' + file_name)

#어떻게 교환 할건지
replace_blank('2', '55')

#끝
print('\nend')


