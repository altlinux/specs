%define module_name enum

Name: python-module-%module_name
Version: 0.4.3
Release: alt1.1.1

Summary: This package provides a module for robust enumerations in Python

License: GPL/Python
Group: Development/Python
Url: http://pypi.python.org/pypi/GitPython/

Packager: Dmitry M. Maslennikov <rlz at altlinux.org>
Source: %module_name-%version.tar

BuildArch: noarch

%setup_python_module %module_name

BuildRequires: python-module-setuptools

%description
This package provides a module for robust enumerations in Python.

%prep
%setup -q -n %module_name-%version

%build
%__python setup.py build

%install
%__python setup.py install --root %buildroot

%files
%python_sitelibdir/*

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.3-alt1.1.1
- Rebuild with Python-2.7

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt1.1
- Rebuilt with python 2.6

* Tue Dec 02 2008 Dmitry M. Maslennikov <rlz at altlinux.org> 0.4.3-alt1
- Initial build for ALTLinux Sisyphus

