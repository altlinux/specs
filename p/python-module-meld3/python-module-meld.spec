%define modulename meld3

Name: python-module-%modulename
Version: 0.6.5
Release: alt1.1.1

Summary: Elementree based templating system
License: ZPL
Group: Development/Python
Url: http://www.plope.com/software/meld3/
Packager: Maxim Ivanov <redbaron at altlinux.org>
BuildArch: noarch

BuildRequires: python-module-setuptools
Requires: python-module-elementtree
Source: %modulename-%version.tar

%setup_python_module %modulename

%description
meld3 is an HTML/XML templating system for Python 2.3+ which keeps template 
markup and dynamic rendering logic separate from one another. 
See http://www.entrian.com/PyMeld for a treatise on the benefits of this pattern.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*
%doc *.txt

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.5-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.5-alt1.1
- Rebuilt with python 2.6

* Fri May 22 2009 Maxim Ivanov <redbaron at altlinux.org> 0.6.5-alt1
- Initial build for ALTLinux

