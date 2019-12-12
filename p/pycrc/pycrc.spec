Name: pycrc
Version: 0.9.2
Release: alt1

Summary: A parametrizable Cyclic Redundancy Check (CRC) calculation utility and C source code generator written in Python

Url: https://pycrc.org/
License: BSD like
Group: Development/Python

BuildArch: noarch

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/tpircher/pycrc/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%description
Pycrc provides a CRC reference implementation in Python and a source
code generator for C. The used CRC variant can be chosen from a fast
but space-consuming implementation to slower but smaller implementations
suitable especially for embedded applications. The following functions
are implemented:
 * generate the checksum of a string  
 * generate the C header and source files for a client implementation. The
   algorithm can be chosen from fast but big implementation to slower but
   smaller implementations suitable especially for embedded applications.

%prep
%setup
%__subst "s|^#!/usr/bin/env python$|#!/usr/bin/python3|" *.py

%build
%python3_build
# TODO: need saxon-xslt
#make -C doc

%install
#python3_install
install -m755 -D %name.py %buildroot%_bindir/%name
#install -m644 -D doc/%name.1 %buildroot%_man1dir/%name.1
mkdir -p %buildroot%python3_sitelibdir/pycrc/
install -m644 pycrc/*.py %buildroot%python3_sitelibdir/pycrc/

%files
#doc doc/pycrc.html
%doc CHANGELOG.md README.md COPYING
%_bindir/%name
#_man1dir/*
%python3_sitelibdir/*

%changelog
* Thu Dec 12 2019 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt1
- new version (0.9.2) with rpmgs script
- build with python3
- fix URL

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.7-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.7-alt1.1
- Rebuilt with python 2.6

* Sun Dec 28 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.7-alt1
- new version 0.6.7 (with rpmrb script)

* Mon Jul 07 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.6-alt2
- add missed files
- change license to BSD like
- use noarch

* Sat Jul 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.6-alt1
- new version 0.6.6 (with rpmrb script)

* Wed Oct 24 2007 Vitaly Lipatov <lav@altlinux.ru> 0.6.3-alt1
- new version 0.6.3 (with rpmrb script)

* Sat Jan 20 2007 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt0.1
- initial build for ALT Linux Sisyphus
