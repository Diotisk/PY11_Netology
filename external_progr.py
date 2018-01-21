import os
import subprocess
import shutil
# import sys


pictures = os.listdir("Source")
print("Files in the folder 'Source': ", pictures)
os.mkdir("Result")
result_path = os.path.abspath("Result")

for pic in pictures:
    pic_source_path = os.path.abspath(os.path.join("Source", pic))
    # print(pic_source_path)
    copy_process = subprocess.Popen("cp" + " {}".format(pic_source_path) + " {}".format(result_path),
                                    shell=True)
    data_cp = copy_process.communicate()

result_pictures = os.listdir("Result")

for pic in result_pictures:
    pic_result_path = os.path.abspath(os.path.join("Result", pic))
    # print(pic_result_path)
    resize_process = subprocess.Popen("sips --resampleWidth 100" + " {}".format(pic_result_path) +
                                      " {}".format(result_path), shell=True)
    data_sips = resize_process.communicate()
    # print(data)

print("Files in the folder 'Result': ", os.listdir("Result"))

answer = input("Print 'yes' if you want to delete the folder 'Result'? ")
if answer == "yes":
    shutil.rmtree(os.path.abspath("Result"))


# print(os.environ["USER"])
#
# print("This is stdout", file=sys.stdout)
# print("This is stderr", file=sys.stderr)
#
# with open("log.txt", "a") as log:
#     print("Some text in log", file=log)
#
# print(sys.argv)
#
# if len(sys.argv) == 1:
#     print("Hello world")
# else:
#     print("Hello", sys.argv[1])
#
# print("Start")
# process = subprocess.run("open -a 'Sublime Text'", shell=True, stdout=subprocess.PIPE)
# process = subprocess.run("python3 decodejson.py", shell=True, stdout=subprocess.PIPE)
# print("Args", process.args)
# print("Err", process.stderr)
# print("Out", process.stdout)
# print("Stop")
