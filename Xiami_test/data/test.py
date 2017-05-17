import json
import os


def str2url(s):
    import urllib2
    # s = '9hFaF2FF%_Et%m4F4%538t2i%795E%3pF.265E85.%fnF9742Em33e162_36pA.t6661983%x%6%%74%2i2%22735'
    num_loc = s.find('h')
    rows = int(s[0:num_loc])
    strlen = len(s) - num_loc
    cols = strlen / rows
    right_rows = strlen % rows
    new_s = s[num_loc:]
    output = ''
    for i in xrange(len(new_s)):
        x = i % rows
        y = i / rows
        p = 0
        if x <= right_rows:
            p = x * (cols + 1) + y
        else:
            p = right_rows * (cols + 1) + (x - right_rows) * cols + y
        output += new_s[p]
    return urllib2.unquote(output).replace('^', '0')

if __name__ == "__main__":
    print(str2url("6hAFlc125%9834l3_D3bb8f9%-ut%oio1FE5%1_4.Fk8f6d7e55%lt2mcm%3%E292%mae47f46e5E5lpF5d%5125F%55puy97941-9%E%%.n2E1F9352E3t%89417145-32a.F%%373E6_%h3554b848En"))