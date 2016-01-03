
#coding:utf-8
import re,sys,re,os

def Scopus2HistCite():
    try:
        auStart=False
        N1CNT=0
        LT=['TI','T2','AU','VL','IS','SP','EP','PY','DO']
        
        if not os.path.isdir('C:/fakepath'):
            os.path.mkdir('C:/fakepath')
        Scopus=open('./Scopus.ris','r')
        HistCite=open('C:/fakepath/savedrecs.txt','wb+')
        HistCite.write('FN Thomson Reuters Web of Knowledge™\nVR 1.0\n')
        for line in Scopus.readlines():
            line=line.replace(r'  - ',' ')
            BG=line[:2]

            if BG=='ER':
                HistCite.write('ER\n\n')
                auStart=False
                continue
            if BG in LT and line[2]==' ':
                line=line.replace(r'TI ','PT J\nTI ').replace(r'T2 ',r'SO ').replace(r'SP ',r'BP ')
                if not auStart and BG=='AU':
                    auStart=True
                else:
                    line=line.replace(r'AU ','')
                HistCite.write(line)
        HistCite.write('\nEF')
        Scopus.close()
        HistCite.close()
        print "finished"
    except Exception, e:
        raise e


if __name__ == '__main__':
    Scopus2HistCite()