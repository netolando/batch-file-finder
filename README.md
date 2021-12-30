#file-finder

This is one of my first projects. This code basically works like a batch grep. You can find out whether a specific key is contained within specific files or not.

#Instructions

Place a txt file containing the list of keys that you want to find inside the folder 'input'. Place the files that you want to analyze inside the folder 'searchable_files'.

Adjust the following parameters inside the code, according to your search:

input_file = 'test.txt' <------ change the name of the input file according to the one you will use.

file_type = '.TXT' <---- this is set to search among files ending with '.TXT'. If you want to search among .csv files, for example, you shall change it to: file_type = '.csv'

and so on.

Once you have run the script, a .txt file containing the final report will be placed into the folder 'output'.