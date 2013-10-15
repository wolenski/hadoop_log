## merge all files
import os

def seperate_url_by_generator(in_file,output_dir):
    # dictionary for {generator : url} mapping
    type_dict = {}

    file_to_read = open(in_file,'r')

    for line in file_to_read:
        if len(line) == 0:
            break
        else:
            items = line.split(";")
            # hash urls based on the generators
            if type_dict.has_key(items[0]):
                type_dict[items[0]] = type_dict.get(items[0]) + ";" + items[2]
            else:
                type_dict[items[0]] = items[2]
    file_to_read.close() 

    #output the urls into different files based on theis generators
    for d_key in type_dict:
        
        val = type_dict.get(d_key)
        urls = val.split(";")

        file_to_write = open(output_dir + str(d_key),"w")
        for url in urls:
            file_to_write.write(url)
        file_to_write.close()

                                                                
if __name__ == '__main__':
    seperate_url_by_generator("bbs_generator.txt","generators/")
