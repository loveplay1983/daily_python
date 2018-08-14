import shutil
import os

# source path
src_dir = os.getcwd() + '/test_dir'

# target path
# des_dir = os.mkdir(src_dir + '/des_dir')
des_dir = os.getcwd() + '/des_dir'


# traverse the source directionary and extract files from each sub_dir 
for each_dir in os.listdir(src_dir):
	# each sub_dir path
	file_dir = src_dir + '/' + each_dir
	# thraverse each sub_dir path
	files = os.listdir(file_dir)
	# for each file in each file_dir if it ends with .txt extension then copy it to the des_dir
	for each_file in files:
		if each_file.endswith('.txt'):
			file_path = file_dir + '/' + each_file
			print('Found {}.'.format(each_file))
			shutil.copy(file_path, des_dir)
		print('Copy files has done.')



