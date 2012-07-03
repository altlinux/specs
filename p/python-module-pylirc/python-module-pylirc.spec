Name: python-module-pylirc
Version: 0.0.5
Release: alt3.1.1

Summary: Python lirc module. See http://www.lirc.org for more info on lirc

Group: Development/Python
License: LGPL
Url: http://pylirc.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: pylirc-%version.tar.bz2

%setup_python_module pylirc
#%add_python_req_skip audio image video misc

# manually removed: eric
# Automatically added by buildreq on Thu Dec 30 2004
BuildRequires: liblirc-devel python-devel python-modules-encodings

%description
Python lirc module

%prep
%setup -n pylirc-%version

%build
%python_build_debug

%install
%python_install

%files
%python_sitelibdir/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.5-alt3.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.5-alt3.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt3
- Rebuilt for debuginfo

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt2
- Rebuilt with python 2.6

* Tue Jan 29 2008 Grigory Batalov <bga@altlinux.ru> 0.0.5-alt1.1
- Rebuilt with python-2.5.

* Thu Mar 17 2005 Vitaly Lipatov <lav@altlinux.ru> 0.0.5-alt1
- new version
- build with python 2.4

* Thu Dec 30 2004 Vitaly Lipatov <lav@altlinux.ru> 0.0.4-alt1
- first build for ALT Linux Sisyphus
