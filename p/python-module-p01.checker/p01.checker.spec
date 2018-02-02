# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.1.1
%define mname p01
%define oname %mname.checker
Name: python-module-%oname
Version: 0.5.6
#Release: alt1
Summary: Python, ZCML, PT, HTML, JS, CSS source checking/linting
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/p01.checker/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools
BuildPreReq: python-module-cssutils python-module-polib pyflakes
BuildPreReq: python-module-lxml python-module-zope.testing
BuildRequires: python-module-pytest

%py_provides %oname
%py_requires %mname cssutils polib pyflakes lxml zope.testing

%description
This package provides a source checking/linting tool.

%prep
%setup

sed -i 's|\r||' $(find src -name '*.txt')

%build
%python_build_debug

%install
%python_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
export PYTHONPATH=$PWD/src
py.test -vv src/p01/checker/tests.py

%files
%doc *.txt
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.6-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.6-alt1.1
- (AUTO) subst_x86_64.

* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.6-alt1
- Initial build for Sisyphus

