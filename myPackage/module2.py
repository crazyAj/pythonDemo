def test2():
    print('module2.test2')


__encoding = "utf-8"
path = "D:\\python-project\\"
with open(path + "2.txt", "a", encoding=__encoding) as w, open(path + "1.txt", "r", encoding=__encoding) as r:
    for line in r:
        w.write(line)