with  open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    info = ((line.split()[0], line.split()[5], line.split()[6]) for line in f)
    for i in info:

        print(i)

  

