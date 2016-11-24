#!/usr/bin/env python
# -*- coding:utf-8 -*-

import Tkinter

# 최상위 윈도우
top = Tkinter.Tk()

# 라벨
label = Tkinter.Label(top, text='Hello World')
label.pack()

# 버튼
quit = Tkinter.Button(top, text='Bye World', command=top.quit, bg='red', fg='white')
quit.pack(fill=Tkinter.X, expand=1)

Tkinter.mainloop()