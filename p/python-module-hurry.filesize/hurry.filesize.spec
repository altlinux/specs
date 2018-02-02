# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.1.1
%define mname hurry
%define oname %mname.filesize
Name: python-module-%oname
Version: 0.9
#Release: alt1
Summary: A simple Python library for human readable file sizes (or anything sized in bytes)
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/hurry.filesize/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools

%py_provides %oname
%py_requires %mname

%description
hurry.filesize a simple Python library that can take a number of bytes
and returns a human-readable string with the size in it, in kilobytes
(K), megabytes (M), etc.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
hurry.filesize a simple Python library that can take a number of bytes
and returns a human-readable string with the size in it, in kilobytes
(K), megabytes (M), etc.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc *.txt
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9-alt1.1
- (AUTO) subst_x86_64.

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1
- Initial build for Sisyphus

