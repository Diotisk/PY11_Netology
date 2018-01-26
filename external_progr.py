import os
import subprocess
import shutil
# import sys


def copy_resize_pics(source_dir, result_dir_name):
    source_pic_l = os.listdir(source_dir)
    os.mkdir(result_dir_name)
    result_dir = os.path.abspath(result_dir_name)
    print("Files in the folder {}: ".format(source_dir), source_pic_l)

    for pic in source_pic_l:
        source_pic_path = os.path.abspath(os.path.join(source_dir, pic))
        # print(source_pic_path)
        copy_process = subprocess.Popen("cp" + " {}".format(source_pic_path) + " {}".format(result_dir),
                                        shell=True)
        copy_process.communicate()

    result_pic_l = os.listdir(result_dir)

    for pic in result_pic_l:
        result_pic_path = os.path.abspath(os.path.join(result_dir, pic))
        # print(result_pic_path)
        resize_process = subprocess.Popen("sips --resampleWidth 150" + " {}".format(result_pic_path), shell=True)
        resize_process.communicate()

    print("Files in the folder {}: ".format(result_dir_name), result_pic_l)
    return

copy_resize_pics("Source", "Result")

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
