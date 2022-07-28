def read_and_convert_file(file_name, file_extension):
    #create final file name
    file_name_without_extension = file_name.split(".")[0]
    final_file_name = file_name_without_extension + "." + file_extension
    #open XML file and get content
    meta_file = open(file_name,"rt")
    meta_file_content = meta_file.read()
    print(final_file_name)
    print(meta_file_content)
    #create new file with different file type (not xml)
    final_file = open(final_file_name , "x")
    final_file.write(meta_file_content)
    final_file.close()