import json
import os


class HandleJson:

    def get_json_data(self,filename):
        """
        读json文件
        :param filename: json文件的绝对路径，str
        :return: 返回一个字典
        """
        with open(filename,encoding="utf-8") as file:
            data_dict = json.load(file)
        return data_dict

    def get_case_data_from_json(self,filename):
        """
        从工程的case_data目录下的json格式的case文件中读取数据
        :param filename:表示case的文件名，str类型
        :return:返回一个字典
        """
        # file_path = os.chdir("../") + "/case_data/" + filename
        file_path = "E:/code/Python/Study/tcyapp_android/case_data/" + filename
        # print(file_path)
        data = self.get_json_data(file_path)
        return data

    def get_case_keys(self,filename):
        """
        从工程的case_data目录下的json格式的case文件中读取case的变量名
        :param filename: 表示case的文件名，str类型
        :return: 返回类似"name,password"的字符串
        """
        #获取所有case，得到可遍历的类列表对象类型：[{'username': 'zhao', 'password': 'zhaoll211'}, {'username': 'zhaoll', 'password': 'zhaoll21111111111'}]
        case = self.get_case_data_from_json(filename).values()
        #获取第一个case的key值，返回case的变量值，类型为字符串"name,password"
        keys = list(case)[0].keys()
        case_attr = ""
        for k in keys:
            case_attr = case_attr + str(k) + ","
        #去掉末尾的","号
        return case_attr[:-1]

    def get_case_values(self,filename):
        """
        从工程的case_data目录下的json格式的case文件中读取所有的case值（case数据）
        :param filename:
        :return: 返回类似[('zhao', '111'), ('zhaoll', '222')]的元组列表，一个元组为一个case
        """
        case = self.get_case_data_from_json(filename).values()
        # print(case)
        data_case_value = []
        for data in case:
            # print(data.values())
            data_case_value.append(tuple(data.values()))
        return data_case_value




if __name__ == '__main__':
    # os.chdir("../")
    # print(os.getcwd())
    # print(type(HandleJson().get_json_data(os.path.abspath(r"case_data/login_by_username_password_data.json"))))
    HandleJson().get_case_data_from_json("login_by_username_password_data.json")
    # type(HandleJson().get_case_keys("login_by_username_password_data.json"))
    HandleJson().get_case_values("login_by_username_password_data.json")
