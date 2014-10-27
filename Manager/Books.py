# -* coding:utf-8 -*-
#author:Claude
#date:2014.9.6
import urllib2
import re
import string


class SingleBook:
    def __init__(self, book_url):
        #some keys (targets)
        self.url = book_url
        self.result = {}
        #compile the result
        self.re_book_name = re.compile(
            u"name=\"Title_pub\">.*?<h1>([^']+?)<span", re.DOTALL)
        self.re_book_id = re.compile(
            u"\"show_info_right\">([0-9]+?)</div>", re.DOTALL)
        self.re_book_img_url = re.compile(
            u"\"largePic\".*?src=\"(http:[^']+?)\"", re.DOTALL)
        self.re_publish_time = re.compile(
            u"\"show_info_right\">([0-9]{4}-[0-9]{1,2}-[0-9]{1,2})", re.DOTALL)
        self.re_book_categorical = re.compile(
            u"<a href=\".*?/cp01.[0-9]{2,3}.00.00.00.00.html\".*?>([^']*?)</a>",
            re.DOTALL)
        self.re_book_price = re.compile(
            u"salePriceTag\">([^']*?)</span>", re.DOTALL)

        self.re_book_word = re.compile(
            u"<li>.*?([0-9]{5,})</li>", re.DOTALL)
        self.re_book_introduce = re.compile(
            u"\"content_all\">([^']*?)</div", re.DOTALL)
        self.re_author_name = re.compile(
            u"<a href.*?/author/.*?>([^']*?)</a>", re.DOTALL)
        self.re_publish_comp = re.compile(
            u"<a href.*?/publish/.*?>([^']*?)</a>", re.DOTALL)

        #obtain the context of self.url
        try:
            self.context = urllib2.urlopen(self.url).read().decode(
                "gbk", "ignore").encode("utf-8")
        except Exception as error:
            #print "url:%s with error:%s" % (self.url, error)
            pass
        self.work()

    #we get the value only if the self.work() 's return value is True
    def work(self):
        #necessary
        temp_book_name = self.re_book_name.search(self.context)
        temp_book_id = self.re_book_id.search(self.context)
        temp_book_img_url = self.re_book_img_url.search(self.context)
        temp_book_categorical = self.re_book_categorical.findall(self.context)
        temp_author_name = self.re_author_name.search(self.context)
        temp_book_price = self.re_book_price.search(self.context)

        temp_publish_time = self.re_publish_time.search(self.context)
        temp_book_word = self.re_book_word.search(self.context)
        temp_book_introduce = self.re_book_introduce.search(self.context)
        temp_publish_comp = self.re_publish_comp.search(self.context)

        #if failure , return false
        try:
            self.result["book_name"] = self.secondHandle(
                temp_book_name.group(1))
            self.result["book_isbn"] = int(self.secondHandle(
                temp_book_id.group(1)))
            self.result["book_img_url"] = self.secondHandle(
                temp_book_img_url.group(1))
            self.result["book_auth_name"] = self.secondHandle(
                temp_author_name.group(1))
            self.result["book_categorical"] = self.secondHandle(
                temp_book_categorical[1])
            self.result["book_price"] = string.atof(self.secondHandle(
                temp_book_price.group(1)))
        except Exception as error:
            #print "dict error:%s" % error
            return False

        #those results are not necessary
        try:
            self.result["book_publish_time"] = self.secondHandle(
                temp_publish_time.group(1))
        except Exception:
            self.result["book_publish_time"] = None
            pass

        try:
            self.result["book_word"] = int(self.secondHandle(
                temp_book_word.group(1)))
        except Exception:
            self.result["book_word"] = None
            pass

        try:
            self.result["book_introduce"] = self.secondHandle(
                temp_book_introduce.group(1))
        except Exception:
            self.result["book_introduce"] = None
            pass

        try:
            self.result["book_publisher"] = self.secondHandle(
                temp_publish_comp.group(1))
        except Exception:
            self.result["book_publisher"] = None
            pass

        #print "book %s get" % self.result["book_name"].decode("utf-8", "ignore")
        return True

    #handle the blank and <>
    def secondHandle(self, context):
         #compile the <>
        div_jian = re.compile(u"<[^']*?>", re.DOTALL)
        context = "".join(re.sub(div_jian, "", context).strip().split())
        div_kuo = re.compile(u"([^']*?)", re.DOTALL)
        context = div_kuo.sub("", context)
        return context

    #user interface
    def getValue(self):
        return self.result


class Handle():
    def __init__(self, url):
        self.url = url
        self.re_url = re.compile(
            u"http://product.dangdang.com/[0-9]+?.html", re.DOTALL)
        self.target = []

    def firstHandle(self):
        temp_context = urllib2.urlopen(self.url).read().decode("gbk", "ignore")
        re_context = re.compile(
             u"component_0__0__3058.*?>([^']*?)</ul>", re.DOTALL)
        result = re_context.search(temp_context)
        try:
            return result.group(0).encode('utf-8')
        except Exception as error:
            #print "page not found with error:%s" % error
            pass

    def work(self):
        context = self.firstHandle()
        if isinstance(context, str):
            try:
                temp_url = self.re_url.findall(context)
                for element in temp_url:
                    self.target.append(element)
                    #print "obtain url:%s" % element
            except Exception:
                pass

    def getValue(self):
        self.work()
        return set(self.target)