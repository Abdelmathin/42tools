import os;
import datetime;

endl = '\n';

def get_creation_time(filename):
	try:
		ctime = datetime.datetime.fromtimestamp(os.stat(filename).st_birthtime);
	except:
		ctime = datetime.datetime.now();	
	ctime = str(ctime);
	ctime = ctime.split('.')[0].replace('-', '/');
	return (ctime);

def get_modification_time(filename):
	try:
		mtime = datetime.datetime.fromtimestamp(os.path.getmtime(filename));
	except:
		mtime = datetime.datetime.now();
	mtime = str(mtime);
	mtime = mtime.split('.')[0].replace('-', '/');
	return (mtime);

def get_prefix(filename):
	ext = filename.split('.')[-1].lower();
	if (ext in ['h', 'hpp', 'c', 'cpp']):
		return ('/*');
	return ('# ');

def get_suffix(filename):
	ext = filename.split('.')[-1].lower();
	if (ext in ['h', 'hpp', 'c', 'cpp']):
		return ('*/');
	return (' #');

def getfileinfo(filename):
	ctime = datetime.datetime.now();	
	ctime = str(ctime);
	ctime = ctime.split('.')[0].replace('-', '/');
	ret = {
		'prefix': get_prefix(filename),
		'suffix': get_suffix(filename),
		'created': {
			'date': get_creation_time(filename),
			'user': os.getlogin()
			},
		'updated': {
			'date': get_modification_time(filename),
			'user': os.getlogin()
		}
	};
	try:
		for l in open(filename, 'r'):
			l = l.strip().lower().replace('\t', ' ');
			if ((len(l) < 80) or (l[12] != ':') or (l[18] != '/')):
				continue ;
			if ((l[21] != '/') or (l[27] != ':') or (l[30] != ':')):
				continue ;
			if ((l[55] != '#') or (l[62] != '#') or (l[34:37] != 'by ')):
				continue ;
			l = l.split(' ');
			while ('' in l):
				l.remove('');
			if ((len(l[0]) > 2) or (len(l[-1]) > 2)):
				continue ;
			key = l[1].split(':')[0];
			if not (key in ['created', 'updated']):
				continue ;
			if not (key in ret):
				ret[key] = {};
			d = l[2] + ' ' + l[3]
			d1 = ret[key]['date'].replace('/', '-');
			d2 = d.replace('/', '-');
			dt1 = datetime.datetime.fromisoformat(d1);
			dt2 = datetime.datetime.fromisoformat(d2);
			if (dt1.timestamp() > dt2.timestamp()):
				ret[key]['date'] = d;
			ret[key]['user'] = l[5];
			ret['prefix'] = (l[0] + '# ')[:2];
			ret['suffix'] = (l[-1] + ' #')[:2];
	except:
		pass;
	ret['updated']['date'] = get_modification_time(filename);
	return (ret);

def get42header(filename, user = None, email = None):
	info = getfileinfo(filename);
	if (user):
		info['created']['user'] = user;
		info['updated']['user'] = user;
	if (not email):
		email = info['created']['user'] + '@student.1337.ma'
	basename = filename.split(os.sep)[-1];
	text = '';
	prefix = info['prefix'];
	suffix = info['suffix'];
	text += prefix + ' ' + '*' * 74 + ' ' + suffix + endl;
	text += prefix + ' ' + ' ' * 74 + ' ' + suffix + endl;
	text += prefix + (' ' * 57) + ':::      ::::::::  ' + suffix + endl;
	text += prefix + '   ' + basename + (51 - len(basename)) * ' ';
	text += ':+:      :+:    :+:   ' + suffix + endl;
	text += prefix + ' ' * 52 + '+:+ +:+         +:+     ' + suffix + endl;
	text += prefix + '   By: ' + info['created']['user'];
	text += ' <' + email + '>' + (' ' * (32 - len(email)));
	text += '+#+  +:+       +#+        ' + suffix + endl;
	text += prefix + (' ' * 48) + '+#+#+#+#+#+   +#+           ';
	text +=  suffix + endl;
	text += prefix + '   Created: ' + info['created']['date'];
	text += ' by ' + info['created']['user'];
	text += '          #+#    #+#             ' + suffix + endl;
	text += prefix + '   Updated: ' + info['updated']['date'];
	text += ' by ' + info['updated']['user'];
	text += '         ###   ########.fr       ' + suffix + endl;
	text += prefix + ' ' + ' ' * 74 + ' ' + suffix + endl;
	text += prefix + ' ' + '*' * 74 + ' ' + suffix + endl;
	return (text.strip());

def get1337header(filename, user = None, email = None, unit = '█'):
	u = 2 * unit;
	info = getfileinfo(filename);
	prefix = info['prefix'];
	suffix = info['suffix'];
	text = get42header(filename, user, email) + endl;
	# text += prefix + ' ' + ('*' * 74) + ' ' + suffix + endl;
	text += prefix + (76 * ' ') + suffix + endl;
	text += prefix + '  ' + (unit * 9) + '            ' + (unit * 10) + '         ' + (unit * 10) + '         ' + (unit * 10) + '     ' + suffix + endl;
	text += prefix + '  ' + u + '     ' + u + (20 * ' ') + u + (17 * ' ') + u + '         ' + u + '      ' + u + '     ' + suffix + endl;
	text += prefix + (9 * ' ') + u + (20 * ' ') + u + (17 * ' ') + u + '         ' + u + '      ' + u + '     ' + suffix + endl;
	text += prefix + (9 * ' ') + u + (20 * ' ') + u + (17 * ' ') + u + (17 * ' ') + u + '     ' + suffix + endl;
	text += prefix + (9 * ' ') + u + '            ' + (unit * 10) + '         ' + (unit * 10) + (17 * ' ') + u + '     ' + suffix + endl;
	text += prefix + (9 * ' ') + u + (20 * ' ') + u + (17 * ' ') + u + (17 * ' ') + u + '     ' + suffix + endl;
	text += prefix + (9 * ' ') + u + (20 * ' ') + u + (17 * ' ') + u + (17 * ' ') + u + '     ' + suffix + endl;
	text += prefix + (9 * ' ') + u + (20 * ' ') + u + (17 * ' ') + u + (17 * ' ') + u + '     ' + suffix + endl;
	text += prefix + (6 * ' ') + (unit * 8) + '         ' + (unit * 10) + '         ' + (unit * 10) + (17 * ' ') + u + '     ' + suffix + endl;
	text += prefix + (76 * ' ') + suffix + endl;
	text += prefix + ' ' + ('*' * 74) + ' ' + suffix + endl;
	return (text.strip());

def append_tofile(filename):
	pass


print (get1337header(
	'/Users/ahabachi/Desktop/Projects/42cursus-minishell/parser/parser.c'))

