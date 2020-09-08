#encoding:utf-8
import socket,socketserver
import com.github.thecinfiniteteam.mineblock.mineblock.random_str as rs
import random
def random_uuid():
    uuid_1 = str(random.random(0, 32767)) + str(random.random(0, 32767)) + str(random.random(0, 32767)) + str(
        random.random(0, 32767)) + str(random.random(0, 32767)) + str(random.random(0, 32767)) + str(
        random.random(0, 32767)) + str(random.random(0, 32767))
    uuid_2 = str(random.random(0, 32767)) + str(random.random(0, 32767)) + str(random.random(0, 32767)) + str(
        random.random(0, 32767)) + str(random.random(0, 32767)) + str(random.random(0, 32767)) + str(
        random.random(0, 32767)) + str(random.random(0, 32767))
    uuid_3 = str(random.random(0, 32767)) + str(random.random(0, 32767)) + str(random.random(0, 32767)) + str(
        random.random(0, 32767)) + str(random.random(0, 32767)) + str(random.random(0, 32767)) + str(
        random.random(0, 32767)) + str(random.random(0, 32767))
    uuid_4 = rs.random_abc_s()+rs.random_abc_s()+rs.random_abc_s()+rs.random_abc_s()+rs.random_abc_s()+rs.random_abc_s()+rs.random_abc_s()+rs.random_abc_s()
    return {"uuid_1":uuid_1,"uuid_2":uuid_2,"uuid_3":uuid_3,"uuid_4":uuid_4,"uuid":uuid_1+uuid_2+uuid_3+uuid_4,"uuid_-":uuid_1+"-"+uuid_2+"-"+uuid_3+"-"+uuid_4}
