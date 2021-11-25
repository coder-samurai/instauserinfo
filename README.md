# Instagram User Info

Under construction! Its only a test! Currently experimenting and planning!

Developed by Samurai Coder (c) 2021

## Example of How To Use

Get User FullName As Example

```python
from InstaUserInfo import InstaUserInfo

fullname = InstaUserInfo(user).FullName()
```

## Important

There is a problem in the library. I don't know how to solve this error. I will search more for this error.


Error:
```
Traceback (most recent call last):
  File "/home/samuraicoder/maiin.py", line 3, in <module>
    print(InstaUserInfo("samuraicoder").Bio())
  File "/home/samuraicoder/.local/lib/python3.9/site-packages/InstaUserInfo/instauserinfo.py", line 9, in __init__
    self.result = requests.get(self.url).json()
  File "/usr/lib/python3/dist-packages/requests/models.py", line 900, in json
    return complexjson.loads(self.text, **kwargs)
  File "/usr/lib/python3/dist-packages/simplejson/__init__.py", line 525, in loads
    return _default_decoder.decode(s)
  File "/usr/lib/python3/dist-packages/simplejson/decoder.py", line 370, in decode
    obj, end = self.raw_decode(s)
  File "/usr/lib/python3/dist-packages/simplejson/decoder.py", line 400, in raw_decode
    return self.scan_once(s, idx=_w(s, idx).end())
simplejson.errors.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```