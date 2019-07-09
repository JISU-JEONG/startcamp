import webbrowser

idols = ['bts','iu','izzy']
for idol in idols:
    webbrowser.open(f'https://search.naver.com/search.naver?&query={}'.format(idol))