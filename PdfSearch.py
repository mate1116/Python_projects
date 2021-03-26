import PyPDF3
import os
import shutil

root=r'C:\Users\Benutzer_1\OneDrive\Dokumentumok\TUG\Prozessmanagement\VO_Unterlagen_20200512'
os.chdir(root)



from os import listdir
from os.path import isfile, join




# onlyfiles = [f for f in listdir(root) if isfile(join(root, f))]

# for i in onlyfiles:
#     if " " in i:
#         os.rename(i,i[11:].replace(" ","_"))












class Search:
    
    def __init__(self,word,rootdir,overwrite=False):
        self.word=word
        self.rootdir=rootdir
        self.overwrite=overwrite
    
    def find(self): 
        
        if self.overwrite == True:
            
            onlyfiles = [f for f in listdir(self.rootdir) if isfile(join(self.rootdir, f))]
    
            for i in onlyfiles:
                if " " in i:
                    os.rename(i,i.replace(" ","_"))
        
      
        newdir=os.path.join(root, self.word)
        
        if os.path.exists(newdir):
            shutil.rmtree(newdir)
        os.makedirs(newdir)
        fil=[]
        nums=[]
        for subdir, dirs, files in os.walk(self.rootdir):
            
            for file in files:
                
                try:
                    pdf=(os.path.join(subdir, file))
                    pdfFileObj=open(pdf,'rb')
                    pdfReader=PyPDF3.PdfFileReader(pdfFileObj)
                    if pdfReader.isEncrypted:
                          pdfReader.decrypt('')
                    
                    nums.append(pdfReader.getNumPages())           
                    fil.append(pdf)
                    
                    for i in range(pdfReader.getNumPages()):
                        pageObj=pdfReader.getPage(i)
                        text=pageObj.extractText()
                        if text.find(self.word) != -1:
                            st='copy '+str(pdf)+' '+str(newdir+"\\"+file)
                            os.popen(st)
                            break
                
                except:
                    print(pdf+"not decryptable")
                
                    
        return fil

e=Search("processflow",root,overwrite=True)
a=e.find()
