import os
import glob
import time

# Turns the input file into a list of package keys
def get_packages(input_file):
    fid = open(input_file, 'r')
    package_list = [x.rstrip() for x in fid.readlines()]
    fid.close()
    return package_list

# Searches the package_key provided in the client input file, returns True if found
def package_chase(client_file, package_key):
    fid = open(client_file, 'r')
    info_list = fid.read()
    fid.close()
    if info_list.find(package_key) >= 0:
        return True
    return False


def result_builder(client_file, package_key,return_path):
    fid = open(return_path, 'a')
    fid.write(package_key + ';' + client_file + '\n')
    fid.close()

    
# Change input_file value according to the name of your file containing the keys you want to find
input_file = 'test.txt'
input_path = os.path.join('./input',input_file)

searchable_folder = './searchable_files/'

return_folder = './output'
return_file = 'result_' + time.strftime("%Y%m%d_%H%M%S") + '.txt'
return_path = os.path.join(return_folder, return_file)

file_type = '*.TXT'

package_list = get_packages(input_path)

for package in package_list:
    found = False
    for client_file in glob.glob(os.path.join(searchable_folder, file_type)):
        if package_chase(client_file,package):
            result_builder(client_file,package,return_path)
            found = True
            break
    if not found:
        result_builder('not found',package,return_path)
print('Feito!')