#encoding:utf-8
import easygui
def openMessageWindow(msg,title,ok_button,image):
    easygui.msgbox(msg,title,ok_button,image)
def openChoiceWindow(msg,title,choices,image):
    easygui.buttonbox(msg,title,choices,image)
def openPasswodWindow(msg,title,image,default):
    easygui.passwordbox(msg, title,default,image);