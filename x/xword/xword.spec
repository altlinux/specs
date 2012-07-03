Name: xword
Version: 1.0
Release: alt1.2.1

Summary: Xword is a GNOME crossword puzzle program

License: BSD
Group: Text tools
Url: http://x-word.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://x-word.org/%name-%version.tar.bz2

BuildArchitectures: noarch

# Automatically added by buildreq on Mon Dec 19 2005
BuildRequires: python-base python-modules-encodings

Requires: python-module-pygtk
Provides: gedam
Obsoletes: gedam


%description
Gedam is a GNOME program I wrote for doing crossword puzzles. It is
similar to the AcrossLite program for Windows, and it can read and write
the file format of that program. Consequently, it works well for doing
puzzles from The New York Times. Although there is an existing version
of AcrossLite for Linux, it has several glaring problems: poor support,
the use of Motif, and the lack of a clock.

For crossword files search in Google by "AcrossLite", f.i.
http://puzzles.about.com/library/weekly/aa040697.htm

%prep
%setup -q
%__subst "s|HOME_PATH =.*|HOME_PATH=\'%python_sitelibdir/%name\'|" %name
%__subst "s,/usr/bin/python,/usr/bin/env python," %name


%build

%install
mkdir -p %buildroot/%_bindir
ln -s ../../%python_sitelibdir/%name/%name %buildroot/%_bindir/%name
install -D %name %buildroot%python_sitelibdir/%name/%name
install *.png %buildroot%python_sitelibdir/%name/


%files
%doc LICENSE
%_bindir/%name
%python_sitelibdir/%name

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.2.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.2
- Rebuilt with python 2.6

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 1.0-alt1.1
- Rebuilt with python-2.5.

* Wed Sep 20 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- rename package, fix url, source

* Mon Dec 19 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt0.1
- initial build for ALT Linux Sisyphus

