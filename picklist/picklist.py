#/usr/bin/python
#-*- coding: utf-8 -*-

#picklist
class pickList(object):
    def __init__(self):
        pass

    def picklist(self, list):
        sit_index = 0
        rm_cnt = 0
        for i in xrange(sit_index, len(list)):
            if list[i] == 0:
                rm_cnt += 1
            else:
                if sit_index < i:
                    list[sit_index] = list[i]
                sit_index +=1
        print "rm_cnt:", rm_cnt
        while(rm_cnt != 0):
            list.pop()
            rm_cnt -=1

        return list

if __name__ == '__main__':
    list = [0,0,1,2,3,0,4,0,0,5,0,0,0,0,6,7,8,9,0,0]
    print "list.__len__:", len(list)

    picklist = pickList()
    print picklist.picklist(list)
