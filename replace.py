import os

folder_name= 'test' # enter the name of the target folder/directory
path = '{}/{}'.format(os.getcwd(), folder_name )# if this python file is outside the folder
extension = 'xml'# choose the intended extension to be searched
expression, replacement = 'testing_images', 'test' #the string we are searching for and its replacement


def main():
	matched = []

	def replace_all(file, search_exp, replace_exp):
		with open(file, "r", encoding="ISO-8859-1") as f:
			xml_str = f.read()
			if search_exp not in xml_str:
				# next line is for debugging
				#print('"{}" not found in {}.'.format(search_exp, file))
				return
			else:
				with open(file, "w", encoding="ISO-8859-1") as s:
					matched.append(file)
					# next line is for debugging
					# print('Changing "{}" to "{}" in {}'.format(search_exp, replace_exp, f))
					print('found')
					xml_str = xml_str.replace(search_exp, replace_exp)
					s.write(xml_str)

	contents = []
	for filename in os.listdir(path):
		if filename.endswith(extension):
			contents.append(filename)
			replace_all('{}/{}'.format(path, filename), expression, replacement)

	print('The directory is {} and a total of {} files found with extension {} with {} matches'.format(path, len(contents), extension, len(matched)))


if __name__ == '__main__':
	main()
