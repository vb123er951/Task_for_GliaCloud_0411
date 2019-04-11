urls = [
	"http://www.google.com/a.txt",
	"http://www.google.com.tw/a.txt",
	"http://www.google.com/download/c.jpg",
	"http://www.google.co.jp/a.txt",
	"http://www.google.com/b.txt",
	"https://facebook.com/movie/b.txt",
	"http://yahoo.com/123/000/c.jpg",
	"http://gliacloud.com/haha.png",
]

files = dict()
for u in urls:
	sp = u.split('/')
	if sp[-1] not in files:
		files[sp[-1]] = 1
	else:
		files[sp[-1]] += 1
		
### sort by count value
sorted_d = sorted(files.items(), key=lambda x: x[1], reverse=True)[:3]
### sort by name
sorted_f = sorted(sorted_d, key=lambda x: x[0])
for d in sorted_f:
	print (d[0], d[1])