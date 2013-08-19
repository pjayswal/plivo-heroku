from flask import Flask, request,make_response,Response
import plivo
import os
import json
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    print 
    xml=plivo.XML.Response()
    xml.addSpeak("Hello you are welcome")
    return Response(xml.to_xml(),mimetype='text/xml')


@app.route('/getparams',methods=['GET','POST'])
def printParams():
    if request.method == 'GET':
        import pdb;pdb.set_trace()
        keys = request.args.keys()
        values = request.args.values()
        print request.args
        return make_response(request.args)
    elif request.method == 'POST':
        import pdb; pdb.set_trace()
        print request.form
        return make_response(request.form)

 
if __name__ == '__main__':
    port = int(os.environ.get('PORT',5089))
    app.run(host='127.0.0.1',port=port)



