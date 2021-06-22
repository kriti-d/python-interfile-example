import base64

def execer(foo):
    try:
        exec(base64.decodestring(bytes(foo, 'ascii')))
    except:
        pass