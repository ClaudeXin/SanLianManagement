#-*- coding:utf-8 -*-
from Books import SingleBook
from Books import Handle
from models import Book

import Queue
import threading
from django.template import RequestContext, loader
from django.shortcuts import render


class WorkManager(object):
    def __init__(self, work_num=1000, thread_num=7):
        self.work_queue = Queue.Queue()
        self.threads = []
        self.__init_work_queue(work_num)
        self.__init_thread_pool(thread_num)
        
    def __init_work_queue(self, jobs_num):
        for index in range(1, jobs_num):
            self.add_job(groupTask, index)
    
    def add_job(self, func, arg):
        self.work_queue.put((func, arg))
        
    def __init_thread_pool(self, thread_num):
        for i in range(thread_num):
            self.threads.append(Work(self.work_queue))
        
    def wait_allcomplete(self):
        for item in self.threads:
            if item.isAlive():
                item.join()

#thread work
class Work(threading.Thread):
    def __init__(self, work_queue):
        threading.Thread.__init__(self)
        self.work_queue = work_queue
        self.start()
        
    def run(self):
        while True:
            try:
                task, arg = self.work_queue.get(block=False)
                task(arg)
                print "task in"
                self.work_queue.task_done()
            except:
                print "fail two"
                pass
                


#single index page mining information
def groupTask(index):
    single_obj = Book()
    url_template = "http://category.dangdang.com/pg%d-cp01.00.00.00.00.00.html"
    handle = Handle(url_template % index)
    urls = handle.getValue()
    for element in urls:
        book = SingleBook(element)
        result = book.getValue()
        try:
            single_obj.insert(result)
            single_obj.save()
            print "book: %s" % result["book_name"]
        except Exception as error:
            print "fail one"

def webming(request, index, threadnum, page_path):
    #start thread to dict information
    manage = WorkManager(index, threadnum)
    #manage.wait_allcomplete()
    return render(request, page_path, {"message": "成功运行，现在可以离开这个页面"})