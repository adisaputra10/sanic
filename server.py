from sanic import Sanic
from sanic.response import text
import simplejson 

app = Sanic()


@app.route('/post', methods=['POST'])
async def post_handler(request):
    rj=request.json
    dt=simplejson.dumps(rj).replace("'",'"')
    print(dt)
    data  = simplejson.loads(dt)
    print(data["data"])
    return text(data["first_name"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
