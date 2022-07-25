#coding=utf-8

class BaseHandle():
    """
    操作元素的基类
    """

    # 在输入框中输入内容
    def input_text(self,element,text):
        element.clear()
        element.send_keys(text)

    # 获取toast信息
    def get_toast_text(self,toast):
        return toast.get_attribute("text")


