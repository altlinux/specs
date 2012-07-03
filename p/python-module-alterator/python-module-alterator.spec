Name: python-module-alterator 
Version: 0.1
Release: alt1.1.1

Summary: Python module for writing backends for ALTLInux Alterator framework

Group: Development/Python
License: GPL
URL: http://www.aspirinka.net/alterator
Packager: Sergey Alembekov <rt@altlinux.ru>
Source: python-alterator-%version.tar.bz2

BuildArch: noarch
BuildRequires: python-devel

%define modulename alterator
%description
This module can be used to write backends for ALTLinux Alterator system.


%prep
%setup -q -n python-%modulename-%version

%build
%__python setup.py build

%install
%__python setup.py install --root %buildroot

%files
%doc README
%python_sitelibdir/%modulename/

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.1.1
- Rebuild with Python-2.7

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.1
- Rebuilt with python 2.6

* Thu May 22 2008 Sergey Alembekov <rt@altlinux.ru> 0.1-alt1
- initial build

