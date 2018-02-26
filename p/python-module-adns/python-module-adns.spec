Name: python-module-adns
Version: 1.2.1
Release: alt3.1.1

%define sname adns-python

Summary: Python interface for the GNU adns library
Group: Development/Python
License: GPLv2+
Url: http://code.google.com/p/%sname/
Packager: Dmitry V. Levin <ldv@altlinux.org>

%setup_python_module adns

# http://%sname.googlecode.com/files/%sname-%version.tar.gz
Source: %sname-%version.tar

Provides: %sname = %version-%release
Obsoletes: %sname

BuildRequires: libadns-devel

%description
The adns module provides an interface to the GNU ADNS asynchronous
DNS resolver library.

%prep
%setup -n %sname-%version

%build
%python_build_debug

%install
%python_install

%files
%python_sitelibdir/*
%doc README PKG-INFO

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.1-alt3.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.1-alt3.1
- Rebuild with Python-2.7

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt3
- Rebuilt for debuginfo

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt2
- Rebuilt with python 2.6

* Fri Feb 20 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2.1-alt1
- Updated to 1.2.1.
- Specfile cleanup.

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.1.0-alt0.2.1.1
- Rebuilt with python-2.5.

* Tue Mar 29 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.1.0-alt0.2.1
- Rebuilt with python-2.4.

* Mon Mar 07 2005 LAKostis <lakostis at altlinux.ru> 1.1.0-alt0.2
- First build for Sisyphus.

