%define version 1.0.1
%define release alt3
%setup_python_module smbpasswd

Summary: Python SMB Password Hash Generator module
Name: %packagename
Version: %version
Release: %release.1
Source0: py-%modulename-%version.tar.gz
License: GPL
Group: Development/Python
URL: http://barryp.org/software/py-smbpasswd
Packager: Python Development Team <python@packages.altlinux.org>

%description
Python SMB Password Hash Generator module

%prep
%setup -n py-%modulename-%version

%build
%python_build_debug

%install
%python_install --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt3.1
- Rebuild with Python-2.7

* Wed Mar 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt3
- Rebuilt for debuginfo

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2
- Rebuilt with python 2.6

* Tue Jan 29 2008 Grigory Batalov <bga@altlinux.ru> 1.0.1-alt1.1
- Rebuilt with python-2.5.

* Sat Dec 31 2005 Ivan Fedorov <ns@altlinux.ru> 1.0.1-alt1
- Initial build for ALT Linux
