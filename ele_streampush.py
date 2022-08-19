# coding:gbk
import os
import threading


class streamPush():
    def cmd_streamlit(self,cmd):
        try:
            print ("命令开始运行")
            os.system(cmd)
            print ("命令结束运行")
        except Exception as e:
            print ('失败啦{}'.format(e))

    def threading_start(self,rtmpURL):
        if_parallel = True
        cmds = [r'ffmpeg -y -loop 1 -re -i D:\workspace_new\st_tools\ele_tools\1.mp4 -vcodec libx264 -acodec aac -f flv '+rtmp for rtmp in rtmpURL]
        print(cmds)
        if if_parallel:
            threads = []
            for cmd in cmds:
                th = threading.Thread(target=self.cmd_streamlit, args=(cmd,))
                th.start()
            for th in threads:
                th.join()

if __name__ == '__main__':
    st_push = streamPush()
    cmd1 = r'"rtmp://34771.livepush.9yiwums.com/live/34773_10007143_t31077?bizid=34771&txSecret=46d39be4958525fdc600b615d95b12d1&txTime=62FDF9CC&liveCode=t31077&userId=10007143"'
    cmd2 = r'"rtmp://34771.livepush.9yiwums.com/live/34773_10010086_t31078?bizid=34771&txSecret=534c7550dbcdcfab762dc8e24d413ed1&txTime=62FDF9CD&liveCode=t31078&userId=10010086"'
    cmd3 = r'"rtmp://34771.livepush.9yiwums.com/live/34773_10000979_t31079?bizid=34771&txSecret=de7150f72c308935f148d9690d9639f9&txTime=62FDF9CF&liveCode=t31079&userId=10000979"'
    cmd_list = [cmd1,cmd2,cmd3]
    print(cmd_list[0])
    st_push.threading_start(cmd_list)
    # cmd1 = r'ffmpeg -re -i D:\workspace_new\st_tools\ele_tools\1.mp4 -vcodec libx264 -acodec aac -f flv "rtmp://34771.livepush.9yiwums.com/live/34773_10006339_t31082?bizid=34771&txSecret=1aadea10f0cead3ac40b8b5bc39702f7&txTime=62FE08D5&liveCode=t31082&userId=10006339"'