while True:
      a=input('Введите название Batch-файла: ')
      d=open(a+'.bat','a')
      d.write('@echo off\n')
      d.write('python'+a+'.py')
      d.close()
      break
