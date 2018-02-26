%define oname py-rrdtool
Name: python-module-rrdtool
Version: 1.0b1
Release: alt1.1.1.1

Summary: Python Interface to RRDTool

License: LGPL
Group: Development/Python
Url: http://sourceforge.net/projects/py-rrdtool/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://dl.sf.net/%oname/%oname-%version.tar.bz2

# Automatically added by buildreq on Wed Nov 22 2006
BuildRequires: librrd-devel python-devel python-modules-encodings

%description
The python-rrdtool provides a interface to rrdtool, the wonderful
graphing and logging utility. This wrapper implementation has
worked from the scratch (without SWIG), and it's under LGPL.

This module have not documented yet. Please refer pydoc.

%prep
%setup -n %oname-%version

%build
%python_build_debug

%install
%python_install

%files
%doc AUTHORS README THANKS
%python_sitelibdir/*


%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0b1-alt1.1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0b1-alt1.1.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt1.1
- Rebuilt for debuginfo

* Tue Apr 20 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0b1-alt1
- rebuild with new librrd

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt0.1.2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.0b1-alt0.1.1
- Rebuilt with python-2.5.

* Wed Nov 22 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0b1-alt0.1
- initial build for ALT Linux Sisyphus

