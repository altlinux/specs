Name: dict-yo
Version: 20031216
Release: alt2.2.1

Summary: The list of russian words with yo letter
Summary(ru_RU.KOI8-R): Список русских слов, содержащих букву 'ё'

License: GPL
Group: Text tools
#Group: Applications/Dictionaries
Url: http://python.anabar.ru/yo.htm

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Need build own package from http://python.anabar.ru/macros/emin/yo/yobase.gz
Source: %name-%version.tar.bz2

%define dictdir %_datadir/dict

BuildArchitectures: noarch

%description
The list of russian words with yo letter

%description -l ru_RU.KOI8-R
Список русских слов, содержащих букву 'ё'

%prep
%setup -q
%__subst "s|c:.*yo\.txt|%dictdir/yobase.list|g" yo.py
%__subst "s|~.*yo\.txt|%dictdir/yobase.list|g" yo.el
%__subst "s|cp866|utf8|g" yo.py

%install
%__install -d %buildroot/{%dictdir,%_datadir/%name}
%__install -m 0644 yobase.list %buildroot/%dictdir
%__install yo.el yo.py %buildroot/%_datadir/%name


%files
%dictdir/*
%_datadir/%name

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 20031216-alt2.2.1
- Rebuild with Python-2.7

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20031216-alt2.2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 20031216-alt2.1
- Rebuilt with python-2.5.

* Tue May 22 2007 Vitaly Lipatov <lav@altlinux.ru> 20031216-alt2
- fix summary encoding (bug #11842)

* Sun Feb 27 2005 Vitaly Lipatov <lav@altlinux.ru> 20031216-alt1
- first build for Sisyphus

