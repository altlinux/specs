Summary: Python extension module for reading flow-tools' data
Name: python-module-pyflowtools
Version: 0.3.4
Release: alt2.1.1
%setup_python_module pyflowtools
Url: http://code.google.com/p/pyflowtools/
Source0: %modulename-%version.tar.gz
License: GPL
Group: Development/Python
Packager: Python Development Team <python at packages.altlinux.org>
Requires: flow-tools zlib
BuildRequires: libflow-tools-devel zlib-devel
Obsoletes: pyflowtools

%description
This extension module gives you a simple python interface to NetFlow
data as stored by Mark Fullmer's flow-tools package (see
http://www.splintered.net/sw/flow-tools).

%prep
%setup -n %modulename-%version

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%install
%python_install \
	  --optimize=2 \
	  --record=INSTALLED_FILES

%clean

%files -f INSTALLED_FILES
%doc CHANGES README COPYING example.py flowprint-full

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.4-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.4-alt2.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt2
- Rebuilt for debuginfo

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1
- Version 0.3.4

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt6
- Rebuilt with python 2.6

* Mon Feb 11 2008 Grigory Batalov <bga@altlinux.ru> 0.3-alt5.1
- Rebuilt with python-2.5.

* Fri May  6 2005 Konstantin Klimchev <koka@altlinux.ru> 0.3-alt5
- python2.4

* Fri May 21 2004 Konstantin Klimchev <koka@altlinux.ru> 0.3-alt4
- new python policy

* Wed Feb 18 2004 Konstantin Klimchev <koka@altlinux.ru> 0.3-alt3
- rebuild for Sisyphus

* Thu Feb 5 2004 Konstantin Klimchev <koka@altlinux.ru> 0.3-alt2
- rebuild

* Sat Dec 27 2003 Konstantin Klimchev <koka@altlinux.ru> 0.3-alt1
- Initial build for Daedalus

* Fri Sep 12 2003 Konstantin Klimchev <koka@atvc.ru> 0.3-1
- Initial build.
