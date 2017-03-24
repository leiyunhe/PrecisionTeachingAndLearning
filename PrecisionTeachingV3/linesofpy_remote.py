#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os  

# function from: http://blog.csdn.net/u013687821/article/details/42432653
class PyfileInfo:  
  
    def __init__(self, file):  
        self.file_name = file  
        self.total_line_num = 0  
        self.blank_line_num = 0  
        self.comment_line_num = 0  
          
    def count_lines(self):  
        if self.file_name[-3:] != '.py':  
            print(self.file_name + ' is not a .py file!')  
            return  
        mc_flag = False  
        try:  
            with open(self.file_name) as code:  
                for each_line in code:
                    self.total_line_num += 1  
                    temp = each_line.strip()  
                    if temp == '':  
                        self.blank_line_num += 1  
                    elif temp[0] == '#':  
                        self.comment_line_num += 1  
                    else:  
                        if False == mc_flag:  
                            if temp[0:3] == '"""''"""': 
                                mc_flag = True 
                        elif temp[-3:] == '"""':  
                            mc_flag = False  
                            self.comment_line_num += 1  
                    if mc_flag:  
                        self.comment_line_num += 1  
        except IOError as err:  
            print('File error: ' + str(err)) 


if __name__ == "__main__":
	print("Please input a path which include some .py files.") # input format: "./foldername"
	target_path = input(">")

	file_list = [f for f in os.listdir(target_path)  
					if os.path.isfile(os.path.join(target_path, f))]

	pyfile_list = [os.path.join(target_path, f) for f in file_list  
	               if f[-3:] == '.py']

	for file in pyfile_list:
		f = PyfileInfo(file)
		f.count_lines()
		print(f.total_line_num, f.blank_line_num, f.comment_line_num)
