%define modulename quixote

Name: python-module-%modulename
Version: 2.5
Release: alt1.1.1.1

Summary: framework for developing Web applications in Python
License: CNRI
Group: Development/Python

Url: http://quixote.ca
Packager: Vladimir V. Kamarzin <vvk@altlinux.org>

Source: %name-%version.tar

%setup_python_module %modulename

%description
Quixote is a simple yet flexible and powerful framework for writing Web-based applications using Python.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5-alt1.1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5-alt1.1.1
- Rebuild with Python-2.7

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1.1
- Rebuilt with python 2.6

* Tue Mar 31 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.5-alt1
- Initial build for Sisyphus
- Real version is v2.5-6-ga310893
