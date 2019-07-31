import pymysql
import json
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
define("port", default=8080, help="run on the given port", type=int)

class index(tornado.web.RequestHandler):
    def get(self):
        try:
            print('-'*100)
            self.set_header("Access-Control-Allow-Origin","https://chienhsiung.github.io")
            # self.set_header("Access-Control-Allow-Origin", "*")
            username = self.get_argument("username")
            password = self.get_argument("password")
            row = self.get_argument("row")
            if row is None:
                pass
            tmp = self.read_mysql("select * from bank order by date desc limit 0,{0}".format(row))
            # tmp = self.read_mysql(sql)
            print("數據 : ",username,password,row)
            tmp = json.dumps(tmp)
            self.write(tmp)
        except BaseException:
            pass
        finally:
            pass
    def post(self):
        try:
            pass
        except:
            pass
            
    def read_mysql(self,sql):
        # 連接資料庫
        db = pymysql.connect('127.0.0.1','root','','rate',charset='utf8')
        cur = db.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        res = []
        content = {}
        for row in rows:
            content = {"bank":row[1],"date":row[2],"time":row[3],"ask":row[4],"bid":row[5]}
            res.append(content)
            content = {}
        # print(res)
        return res

class test(tornado.web.RequestHandler):
    def get(self):
        pass

if __name__ == '__main__':
    print("start")
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', index),
                  (r'/test',test)
                  ],
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()