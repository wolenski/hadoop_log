## merge all files
import os


def extract_hosts(in_dir,out_dir):
    file_list = os.listdir(in_dir)
    
    for url_file in file_list:
        extract_host_by_generator(url_file,in_dir,out_dir)
        break


def extract_host_by_generator(file_name,in_dir,out_dir):
    # dictionary for {generator : url} mapping
    host_dict = {}

    file_to_read = open(in_dir + file_name, 'r')

    count = 0
    thres = 1000
    for line in file_to_read:
        if len(line) == 0:
            break
        else:
            tmp = line.find(".baidu.com")
            if tmp != -1:
                continue
            idx = line.find(":")
            if idx == -1:
                continue
            item = line[idx+1:].strip()
            host_dict[item] = 1
            count += 1
            if count >= thres :
                break

    file_to_read.close() 

    #output the urls into different files based on theis generators
    out_fname = out_dir + file_name
    file_to_write = open(out_fname,"a")
    
    for d_key in host_dict: 
        file_to_write.write(d_key)
        file_to_write.write("\n")
            
    file_to_write.close()

                                                                
if __name__ == '__main__':
    extract_hosts("unique_url_20130930/","diff/")
