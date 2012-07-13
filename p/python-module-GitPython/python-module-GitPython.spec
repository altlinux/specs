%define module_name GitPython

Name: python-module-GitPython
Version: 0.3.2
Release: alt0rc1.1

Summary: GitPython is a python library used to interact with Git repositories

License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/GitPython/

Source: %name-%version.tar

BuildArch: noarch

%setup_python_module %module_name

BuildRequires: python-module-setuptools python-module-GitDB

%description
A simple, flexible, easy-to-use configfile and command-line parsing library
built on top of the standard library optparse module.

%prep
%setup

%build
%python_build

%install
%python_install

%check
python setup.py test

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/git/test

%changelog
* Fri Jul 13 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.2-alt0rc1.1
- 0.3.2-rc1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.0-alt1.1
- Rebuild with Python-2.7

* Fri Oct 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt1
- new version

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4.1-alt1.1
- Rebuilt with python 2.6

* Fri Nov 28 2008 Dmitry M. Maslennikov <rlz at altlinux.org> 0.1.4.1-alt1
- Initial build for ALTLinux Sisyphus

