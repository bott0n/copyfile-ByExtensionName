import fs
import shutil


class GetFile:

    def __init__(self):
        self.getDir()
        self.getFileExtension()
        self.findDirInPath()
        self.findFile()
        self.getOutputPath()

    def getDir(self):
        print('Input directory')
        path = input('>>>')
        if(fs.isdir(path)):
            self.path = path
        else:
            print('Please input a valid directory !')
            exit()

    def getFileExtension(self):
        print('Input file extension name')
        ext = input('>>>')
        ext = ext.split(' ')
        self.ext = ext
    
    def findDirInPath(self):
        path = [self.path]
        dirs = fs.listdirs(path[0])
        dirs = list(dirs)
        path.extend(dirs)
        self.path = path
       

    def findFile(self):
        path = self.path
        print(path)
        correctFile = []
    
        for p in path:
            print(p)
            for extname in self.ext:
                for filename in fs.find('*.'+extname, path=p):       
                
                    correctFile.append(filename)
                
 
        #  correctFile.extend(self.findCorrectFile(files))
        
        print('Find '+ str(len(correctFile))+' files with extension name ' + str(self.ext))
        self.correctFile = correctFile
        

    def getOutputPath(self):
        print('Input output folder path')
        self.output = input('>>>')
        self.outputFiles()

    def outputFiles(self):
        for file in self.correctFile:
            name = fs.basename(file)
            shutil.copyfile(file,self.output+'/'+name)
            #fs.rename(file,self.output+'/'+name)
        print('finish')
gf = GetFile()

