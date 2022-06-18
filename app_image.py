import os
from tkinter import *


class Application(object):
    def __init__(self):
        self.root = Tk()
        self.root.title('格式化图片尺寸')
        self.path = StringVar()
        self.size = StringVar()

        Label(self.root, text="目标路径:").grid(row=0, column=0)
        Entry(self.root, textvariable=self.path).grid(row=0, column=1)
        Button(self.root, text="路径选择", command=self.selectPath).grid(row=0, column=2)

        Label(self.root, text="目标大小:").grid(row=1, column=0)
        Entry(self.root, textvariable=self.size).grid(row=1, column=1)
        Button(self.root, text="确定选择", command=self.formatSize).grid(row=1, column=2)

        Button(self.root, text="退出程序", command=self.root.destroy).grid(row=2, column=2)

    def run(self):
        self.root.mainloop()

    def selectPath(self):
        from tkinter.filedialog import askdirectory
        path_ = askdirectory()
        self.path.set(path_)

    def formatSize(self):
        from PIL import Image
        from glob import glob
        import tkinter.messagebox as messagebox
        sourcesPathList = glob(os.path.join(self.path.get(), '*.png'))
        sourcesPathList.extend(glob(os.path.join(self.path.get(), '*.jpg')))
        sourcesPathList.extend(glob(os.path.join(self.path.get(), '*.jpeg')))
        sourcesPathList.extend(glob(os.path.join(self.path.get(), '*.bmp')))

        if not os.path.exists('result'):
            os.mkdir('result')
        try:
            if not sourcesPathList:
                messagebox.showinfo('警告', '所选文件夹内容为空')
                assert not '0'
            for p in sourcesPathList:
                tmp = Image.open(p)
                try:
                    res = tmp.resize([int(i) for i in self.size.get().split(',')], Image.ANTIALIAS)
                except ValueError:
                    res = tmp.resize([int(i) for i in self.size.get().split('，')], Image.ANTIALIAS)
                res.save(os.path.join('result', p.split('\\')[-1]), quality=95)
            messagebox.showinfo('提示', '修改成功')
        except (FileNotFoundError, AssertionError):
            messagebox.showinfo('警告', '修改失败')


if __name__ == '__main__':
    app = Application()
    app.run()