filename = 'pi_digits.txt'
# 简单文件读取在这个程序中，
# 第1行代码做了大量的工作。我们先来看看函数open() 。要以任何方式使用文件——哪怕仅仅是打印其内容，都得先打开 文件，
# 这样才能访问它。函数open() 接受一个参数:要打开的文件的名称。Python在当前执行的文件所在的目录中查找指定的文件。
# 在这个示例中，当前运行的是file_reader.py，因此Python在file_reader.py所在的目录中 查找pi_digits.txt。
# 函数open() 返回一个表示文件的对象。在这里，open('pi_digits.txt') 返回一个表示文件pi_digits.txt 的对象;
# Python将这个对象存储在我们将 在后面使用的变量中。
# 关键字with 在不再需要访问文件后将其关闭。在这个程序中，注意到我们调用了open() ，但没有调用close() ;
# 你也可以调用open() 和close() 来打开和关闭文件，但 这样做时，如果程序存在bug，导致close() 语句未执行，文件将不会关闭。
# 这看似微不足道，但未妥善地关闭文件可能会导致数据丢失或受损。如果在程序中过早地调 用close() ，
# 你会发现需要使用文件时它已关闭 (无法访问)，这会导致更多的错误。并非在任何情况下都能轻松确定关闭文件的恰当时机，
# 但通过使用前面所示的结构，可 让Python去确定:你只管打开文件，并在需要时使用它，Python自会在合适的时候自动将其关闭。

# 逐行读取
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
    print(line.rstrip())

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    #字符串循环拼接
    pi_string += line.rstrip()
    #print(pi_string)

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")



