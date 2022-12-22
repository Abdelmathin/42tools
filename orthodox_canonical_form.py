import os;
import sys;
from _42header_generator import get42header;

__TEMPLATE_H__ = '''
#ifndef {{identifier}}
# define {{identifier}}

# include <iostream>
# include <string>

class {{class_name}}
{
	public:
		{{class_name}}();
		{{class_name}}(std::string s1, std::string s2, ...);
		{{class_name}}({{class_name}} const &other);
		~{{class_name}}();
		{{class_name}} &operator=({{class_name}} const &other);
};

#endif//{{identifier}}

'''

__TEMPLATE_C__ = '''
#include "{{class_name}}.hpp"
#include <iostream>

{{class_name}}::{{class_name}}()
{
	std::cout << "Default constructor called" << std::endl;
}

{{class_name}}::{{class_name}}({{class_name}} const &other)
{
	std::cout << "Copy constructor called" << std::endl;
}

{{class_name}}::{{class_name}}(std::string s1, std::string s2, ...)
{
	std::cout << "Parameterized constructor called" << std::endl;
}

{{class_name}}::~{{class_name}}()
{
	std::cout << "Destructor called" << std::endl;
}

{{class_name}} &{{class_name}}::operator=({{class_name}} const &other)
{
	std::cout << "Assignation operator called" << std::endl;
	return (*this);
}

'''

endl = '\n';

def create_directory(dirname):
	filename = '';
	for i in dirname.split(os.sep):
		filename += i;
		try:
			os.mkdir(filename);
		except:
			pass;
		filename += os.sep;

def fix_class_name(class_name):
	class_name = class_name.capitalize();
	class_name = class_name.split('.')[0];
	return (class_name);

def generate_header_file(dirname, class_name):
	class_name = fix_class_name(class_name);
	d = {
		(class_name + '.cpp') : __TEMPLATE_C__,
		(class_name + '.hpp') : __TEMPLATE_H__
	};
	for basename,value in d.items():
		filename = dirname + os.sep + basename;
		identifier = class_name.upper() + '_' + basename.split('.')[-1].upper();
		text = value;
		text = text.replace('{{class_name}}', class_name);
		text = text.replace('{{identifier}}', identifier);
		text = text.strip() + endl;
		text = get42header(filename) + endl + text;
		with open(filename, 'w') as fp:
			fp.write(text);

def usage():
	print ('usage: orthodox-canonical-form [class_name] [dirname]\n')
	print ('try for example:\n\torthodox-canonical-form '
		'"Fixed" "~/Desktop/CPP-Module-02/ex00"')
	print ('or:\n\tcd "~/Desktop/CPP-Module-02/ex00"'
		'\n\torthodox-canonical-form "Fixed"')	

def main(argc, argv):
	if (argc < 2 or argc > 3):
		return (usage());
	[class_name, dirname] = (list(argv) + ['.'])[1:3];
	generate_header_file(dirname, class_name);

if (__name__ == '__main__'):
	main(len(sys.argv), sys.argv);
