# https://www.bilibili.com/video/av15478453
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys,os
from ui import *
import time,pyperclip
import re
import ssl
import urllib.request
import requests
import threading
import qdarkstyle
qdarkstyle.load_stylesheet_pyqt5
from concurrent.futures import ThreadPoolExecutor
from collections import Counter 
headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400",
"Cookie":"CURRENT_QUALITY=64; DedeUserID=227050458; "
}



class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        # self.show_web()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.display_table.verticalScrollBar().setStyleSheet(
        "QScrollBar:vertical{"        #垂直滑块整体  
          "padding-top:20px;"    #上预留位置（放置向上箭头）  
          "padding-bottom:20px;" #下预留位置（放置向下箭头）  
          "padding-left:3px;"    #左预留位置（美观）  
          "padding-right:3px;"   #右预留位置（美观）  
          "border-left:1px solid white;}"#左分割线  
          "QScrollBar::handle:vertical{"#滑块样式  
          "background:rgba(100,100,100,0.3);"  #滑块颜色  
          "border-radius:6px;"   #边角圆润  
          "min-height:60px;}"    #滑块最小高度  
          "QScrollBar::handle:vertical:hover{"#鼠标触及滑块样式  
          "background:rgba(0,0,0,0.3);}" #滑块颜色  
          "QScrollBar::add-line:vertical{"#向下箭头样式  
          "background:;}"  
          "QScrollBar::sub-line:vertical{"#向上箭头样式  
          "background:;}") 
        self.display_table.horizontalScrollBar().setStyleSheet(
        "QScrollBar:vertical{"        #垂直滑块整体  
          "padding-top:20px;"    #上预留位置（放置向上箭头）  
          "padding-bottom:20px;" #下预留位置（放置向下箭头）  
          "padding-left:3px;"    #左预留位置（美观）  
          "padding-right:3px;"   #右预留位置（美观）  
          "border-left:1px solid white;}"#左分割线  
          "QScrollBar::handle:vertical{"#滑块样式  
          "background:rgba(100,100,100,0.3);"  #滑块颜色  
          "border-radius:6px;"   #边角圆润  
          "min-height:60px;}"    #滑块最小高度  
          "QScrollBar::handle:vertical:hover{"#鼠标触及滑块样式  
          "background:rgba(0,0,0,0.3);}" #滑块颜色  
          "QScrollBar::add-line:vertical{"#向下箭头样式  
          "background:;}"  
          "QScrollBar::sub-line:vertical{"#向上箭头样式  
          "background:;}")
        self.display_table.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background:rgba(0,0,0,0.1); padding-left:4px; border:1px solid white; }"
            # "QHeaderView::section:checked{background-color:green; }"
            )
        self.display_table.verticalHeader().setStyleSheet(
            "QHeaderView::section{background:rgba(0,0,0,0.1); padding-left:4px; border:1px solid white; }"
            # "QHeaderView::section:checked{background-color:green; }"
            )
        self.run_dir = os.getcwd()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.input_url)
        self.timer.start(1000)
        self.display_table.setColumnWidth(0,60)
        self.display_table.setColumnWidth(1,250)
        self.display_table.setColumnWidth(2,70)
        self.display_table.setColumnWidth(3,70)
        self.display_table.setColumnWidth(4,250)
        self.display_table.setColumnWidth(5,100)
        self.workjiexi = Workjiexi()
        self.workjiexi.done.connect(self.jiexi_done)
        self.workjiexi.finished.connect(self.jiexi_finshed)
        self.workdownload = Workdownload()
        self.workdownload.update.connect(self.update_progress)
        self.workdownload.para_update.connect(self.para_done)

        self.list_ = []
        self.title = ''

    def mousePressEvent(self, event):
        x = (event.globalPos()-self.pos()).x()
        y = (event.globalPos()-self.pos()).y()
        if event.button()==Qt.LeftButton and x<915 and y<40:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
    
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))


    def input_url(self):
        if re.match(r'^https://www.bilibili.com/video/av',pyperclip.paste()):
            if self.url_edit.text() == "":
                self.url_edit.setText(pyperclip.paste())    

    def jiexi(self):
        
        self.list_ = []
        while self.display_table.rowCount():
            self.display_table.removeRow(0)
        if self.url_edit.text():
            self.workjiexi.url = self.url_edit.text()
            # self.workjiexi.url = "https://www.bilibili.com/video/av15478453"
            self.workjiexi.start()

    def jiexi_done(self,list_,title):
        self.title = title
        self.list_.append(list_)
        
        rowcount = self.display_table.rowCount()
        # if rowcount != 0:
        #     if int(list_[0]) >= rowcount:
        #         self.insert_table(rowcount,list_)
        #     else:
        #         for i in range(rowcount):
        #             if int(list_[0]) < int(self.display_table.item(i,1).text().split('.')[0]):
        #                 self.insert_table(i,list_)
        #                 break

        # else:
        self.insert_table(rowcount,list_)
        # self.display_table.setItem(rowcount,3,content)
    def insert_table(self,index,list_):
        check_radio = QCheckBox()
        progress = QProgressBar()
        self.display_table.insertRow(index)
        self.display_table.setCellWidget(index,0,check_radio)
        self.display_table.setItem(index,1,QTableWidgetItem(list_[1]))
        self.display_table.setItem(index,2,QTableWidgetItem(list_[2]))
        self.display_table.setItem(index,3,QTableWidgetItem(str(list_[3])+" M"))
        self.display_table.setCellWidget(index,4,progress)
        self.display_table.setItem(index,5,QTableWidgetItem("0/"+str(len(list_[4]))))

    def jiexi_finshed(self):
        self.all_select_check_button.animation = QPropertyAnimation(self.all_select_check_button, b'geometry')
        self.all_select_check_button.animation.setDuration(1000)
        self.all_select_check_button.animation.setStartValue(QRect(-150, 100,  121, 21))
        self.all_select_check_button.animation.setEndValue(QRect(20, 100, 121, 21))
        self.all_select_check_button.animation.start()

        self.download_button.animation = QPropertyAnimation(self.download_button, b'geometry')
        self.download_button.animation.setDuration(1000)
        self.download_button.animation.setStartValue(QRect(922,50, 93, 41))
        self.download_button.animation.setEndValue(QRect(780, 50, 93, 41))
        self.download_button.animation.start()

    def download(self):
        if not os.path.exists(self.title):
            os.makedirs(self.title)
        self.workdownload.num = []
        self.workdownload.title = self.title
        self.workdownload.list_ = self.list_
        for i in range(self.display_table.rowCount()):
            if self.display_table.cellWidget(i,0).isChecked():
                self.workdownload.num.append(i)
        self.workdownload.start()
        
    def all_select(self,v):
        for i in range(self.display_table.rowCount()):
            self.display_table.cellWidget(i,0).setChecked(v)

    def update_progress(self,percent,num):
        self.display_table.cellWidget(num,4).setValue(percent)

    def para_done(self,num,para):
        self.display_table.setItem(num,5,QTableWidgetItem(para+'/'+self.display_table.item(num,5).text().split('/')[1]))

    def close_click(self):
        self.close()

    def min_click(self):
        self.showMinimized()
  

    def conver_done(self):
        QMessageBox.information(self,'提示','转换成功！！')


class Workjiexi(QThread):
    """docstring for WorkThread"""
    done = pyqtSignal(list,str)
    all_done = pyqtSignal()
    error = pyqtSignal()
    def __init__(self):
        super(Workjiexi, self).__init__()
    def run(self):        
        executor = ThreadPoolExecutor(50)
        result = requests.get(self.url,headers=headers).text
        title_zz = '<h1 title="(.*?)">'
        self.title = re.findall(title_zz,result)[0].replace(' ','-')
        zz = 'page":(.*?),"from":"vupload","part":"(.*?)","duration":'
        executor.map(self.thread_jiexi,[i[0] for i in re.findall(zz,result)],[i[1] for i in re.findall(zz,result)])



    def thread_jiexi(self,page,title):
        url2 = self.url + '?p=' +str(page)
        respond2 = requests.get(url2,headers=headers).text
        zz2 = '"order":(.*?),"length":(.*?),"size":(.*?),.*?"url":"(.*?)"'
        result2 = re.findall(zz2,respond2)
        time =str(sum([int(i[1]) for i in result2])//60000) +":"+str(int((sum([int(i[1]) for i in result2])%60000)//1000))
        size =round (sum([int(i[2]) for i in result2])/1024/1024,1)
        url = [i[3] for i in result2]
        
        result3 = [page,title]
        result3.extend([time, size, url])
        self.done.emit(result3,self.title)



class Workdownload(QThread):
    """docstring for WorkThread"""
    update = pyqtSignal(int,int)
    para_update = pyqtSignal(int,str)
    all_done = pyqtSignal()
    error = pyqtSignal()
    def __init__(self):
        super(Workdownload, self).__init__()
    def run(self):
        self.before = 0
        list_thread = []
        for i in self.num:
            title = self.list_[i][1].replace(" ","-")
            url = self.list_[i][4] 
            t1 = threading.Thread(target=self.download_thread,args=(url,title),name=str(i))
            list_thread.append(t1)
        
        self.threadLock = threading.Lock()
        for j in list_thread:
            j.start()


    def download_thread(self,url,title):
        ssl._create_default_https_context = ssl._create_unverified_context
        opener = urllib.request.build_opener()
        opener.addheaders = [
                ('Host', 'tx.acgvideo.com'),
                ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:56.0) Gecko/20100101 Firefox/56.0'),
                ('Accept', '*/*'),
                ('Accept-Language', 'en-US,en;q=0.5'),
                ('Accept-Encoding', 'gzip, deflate, br'),
                ('Range', 'bytes=0-'),  # Range 的值要为 bytes=0- 才能下载完整视频
                ('Referer', 'https://www.bilibili.com/video/av14543079/'),
                ('Origin', 'https://www.bilibili.com'),
                ('Connection', 'keep-alive'),
            ]
        urllib.request.install_opener(opener)
        for i in enumerate(url):
            self.para_update.emit(int(threading.current_thread().name),str(i[0]+1))
            if not os.path.exists(os.path.join(run_dir,self.title)+"/"+ title+"__"+str(i[0]+1)+'.flv'):
                urllib.request.urlretrieve(i[1], filename=os.path.join(run_dir,self.title)+"/"+ title+"__"+str(i[0]+1)+'.flv', reporthook=self.report)
            else:
                print('已经存在!')

        self.threadLock.acquire()
        self.hecheng(title)
        self.threadLock.release()

    def hecheng(self,title):
        os.chdir(self.title)
        title_list = os.listdir('.')
        title_list = [i.split("__")[0] for i in title_list]
        c = Counter()
        for ch in title_list:
            c[ch] = c[ch] + 1

        if c[title] != 1:
            title_name_list = []    
            for num in range(c[title]):
                path_filename = title+'__'+str(num+1)
                os.system('''ffmpeg -i %s.flv -c copy -bsf:v h264_mp4toannexb -f mpegts %s.ts'''% (path_filename, path_filename))
                title_name_list.append(path_filename)

            add_list = "|".join([j+'.ts' for j in title_name_list])
            del_list = " ".join([j+'.ts' for j in title_name_list])
            del2_list = " ".join([j+'.flv' for j in title_name_list])
            os.system('''ffmpeg -i "concat:%s" -c copy -bsf:a aac_adtstoasc -movflags +faststart %s.mp4'''%(add_list,title))
            os.system('''del %s %s''' % (del_list,del2_list))
            print('''del %s %s''' % (del_list,del2_list))
        elif c[title] == 1:    
            os.system('''ffmpeg -i %s.flv -c copy -bsf:a aac_adtstoasc -movflags +faststart %s.mp4'''%(title+"__1",title))
            os.system('''del %s.flv''' % (title+"__1"))
        os.chdir(run_dir)

    def report(self,count, blockSize, totalSize):
        downloadedSize = count * blockSize
        percent = int(downloadedSize * 100 / totalSize)
        if not self.before == percent:
            self.before = percent
            self.update.emit(percent,int(threading.current_thread().name))
        # sys.stdout.write(f"\rDownloaded: {downloadedSize} bytes, Total: {totalSize} bytes, {percent} % complete")
        # sys.stdout.flush()

if __name__ == '__main__':
    run_dir = os.getcwd()
    path = ''
    app = QApplication(sys.argv)
    mywin = MyMainWindow()
    mywin.show()
    sys.exit(app.exec())
