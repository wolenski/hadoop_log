## merge all files
import os
 
def merge_files(fdir,outfile):
    
    file_list = os.listdir(fdir)
    file_to_write = file(outfile,'w')
    
    for f in file_list:
        file_to_read = file(fdir+str(f),'r')

        while True:
            line = file_to_read.readline()
            if len(line) == 0:
                break
            else:
                file_to_write.write(line)
        file_to_read.close()                                                                        
    
    file_to_write.close()
        
        
        
if __name__ == '__main__':
    merge_files('./part/','bbs_generator.txt') #fdir must end with '/'
