Name: pychecker
Version: 0.8.18
Release: alt3.1.1

Summary: Tool for finding bugs in Python source code

License: BSD-like
Group: Development/Other
Url: http://pychecker.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/pychecker/%name-%version.tar.bz2
# Debian manpage
Patch: %name-0.8.10-add-manpage.patch

BuildArch: noarch

# Automatically added by buildreq on Sat Apr 11 2009 (-bi)
BuildRequires: python-devel

%description
PyChecker is a tool for finding bugs in Python source code. It finds
problems that are typically caught by a compiler for less dynamic
languages, like C and C++.

%prep
%setup -q
%patch -p2

%build
%python_build

%install
%python_install
# remove docs
rm `find %buildroot%python_sitelibdir/%name | grep -v 'py[^/]*$'`

mkdir -p %buildroot%_bindir
echo -e '#!/bin/sh
/usr/bin/env python %python_sitelibdir/pychecker/checker.pyc "$@"
' > %buildroot%_bindir/%name

# pychecker2
mkdir -p %buildroot%python_sitelibdir/pychecker2
install -m 0644 pychecker2/*.py %buildroot%python_sitelibdir/pychecker2/
install -D %name.1 %buildroot%_man1dir/%name.1

%files
%doc README CHANGELOG MAINTAINERS KNOWN_BUGS TODO pycheckrc pychecker2/NOTES.txt
%attr(755,root,root) %_bindir/%name
%_man1dir/%name.*
%python_sitelibdir/%name/
%python_sitelibdir/*.egg-info
%python_sitelibdir/pychecker2/

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.18-alt3.1.1
- Rebuild with Python-2.7

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.18-alt3.1
- Rebuilt with python 2.6

* Tue Apr 14 2009 Vitaly Lipatov <lav@altlinux.ru> 0.8.18-alt3
- build for Sisyphus

* Sat Apr 11 2009 Fr. Br. George <george@altlinux.ru> 0.8.18-alt2
- PyChecker2 include
- Debian manpage add

* Wed Jan 07 2009 Vitaly Lipatov <lav@altlinux.ru> 0.8.18-alt1
- new version 0.8.18 (with rpmrb script)

* Wed Sep 20 2006 Vitaly Lipatov <lav@altlinux.ru> 0.8.17-alt0.1
- new version 0.8.17 (with rpmrb script)

* Tue Jan 31 2006 Vitaly Lipatov <lav@altlinux.ru> 0.8.16-alt0.1
- initial build for ALT Linux Sisyphus (spec from PLD)

