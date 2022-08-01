chagirmalar = (17,5,50)
(kopm,tel1,tel2) = chagirmalar

maxsulotlar = {1:{'name':'DELL','prise':475,'model':'DELL vostro 3500','company':'DELL kom','chergirma':kopm},
     2:{'name':'LENOVO','prise':1700,'model':'LENOVO ideapad s473','company':'LENOVO tech kom','chergirma':kopm},
     3:{'name':'IPHONE','prise':1100,'model':'IPHONE 13 pro','company':'APPLE','chergirma':tel1},
     4:{'name':'SAMSUNG','prise':950,'model':'SAMSUNG s22 ulra','company':'SAMSUNG kom','chergirma':tel2},
     5:{'name':'Acer','prise':1000,'model':'Acer Aspire','company':'Acer kom','chergirma':kopm},
     6:{'name':'Asus','prise':1200,'model':'Asus Vivabook','company':'Asus kom','chergirma':kopm},
     7:{'name':'Realme','prise':950,'model':'Realme 9+ pro','company':'Realme kom','chergirma':tel2},
     8:{'name':'POCO','prise':500,'model':'POCO X3 Pro','company':'POCO kom','chergirma':tel2}}

Barcha  = {'DELL','LENOVO','IPHONE','SAMSUNG','Acer','kompuyter','telefon','Asus','Realme','POCO'}
Model = {'DELL vostro 3500','LENOVO ideapad s473','IPHONE 13 pro','SAMSUNG s22 ulra','Acer Aspire','Realme','Asus Vivabook','POCO X3 Pro'}
maxMu = {'DELL vostro 3500':1,'LENOVO ideapad s473':2,
        'IPHONE 13 pro':3,'SAMSUNG s22 ulra':4,'Acer Aspire':5,'Asus Vivavbook':6,'Realme 9+ pro':7,'POCO X3 Pro':8}

print('Xush kelibsiz!')
m = input('Nima qidiryapsiz ? ')
if m in Barcha:
   print('ushbu maxsulot mavjud!')
   n = input('sizga kerak bo\'lgan modelni kiriting ? :')
   if n in Model:
     i = maxMu[n]
     print('  maxsulot :',maxsulotlar[i]['name'])
     print('  narxi :',maxsulotlar[i]['prise'] + '$')
     print('  modeli :',maxsulotlar[i]['model'])
     print('  kompanyniyasi :',maxsulotlar[i]['company'])
     b = input('\nsotib olasizmi ? :')
     if b == 'ha':
         print('  maxsulot :',maxsulotlar[i]['name'])
         print('  narxi :',maxsulotlar[i]['prise' + '$'])
         print('  chegirma narxi :',maxsulotlar[i]['prise']*(1 - maxsulotlar[i]['chergirma']/100))
     else :
        print('tashrifingiz uchun rahmat.')
   else :
     print('uzur hozircha ushbu maxsulot mavjud emas!')
else :
  print('kechirasiz buanday maxsulot yoq.')