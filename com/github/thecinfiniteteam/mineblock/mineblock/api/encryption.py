#encoding:utf-8
import numbers,enum,sys,random,os,hashlib
def encrytion(resources_path,source_path,source_file_path_list):
    if os.path.isdir(resources_path):
        os.system("cd "+resources_path)
        for source in source_file_path_list:
            


