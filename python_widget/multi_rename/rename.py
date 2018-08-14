# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os

file_path = r'/opt/home_ext/maizi_python/Python_full_stack/spider/project/wallpaper'

# Function to rename multiple files
def main():
    i = 0
	
    for filename in os.listdir(file_path):
        dst = "landscape" + str(i) + ".jpg"
        src = file_path + '/' + filename
        dst = file_path + '/' + dst

        # rename() function will
        # rename all the files
        os.rename(src, dst)
        i += 1

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()

