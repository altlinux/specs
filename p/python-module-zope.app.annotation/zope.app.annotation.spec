# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.1.1
%define mname zope.app
%define oname %mname.annotation
Name: python-module-%oname
Version: 3.4.0
#Release: alt1
Summary: Zope Annotations
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/zope.app.annotation/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools
BuildPreReq: python-module-zope.deprecation
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.interface

%py_provides %oname
%py_requires %mname zope.deprecation zope.annotation zope.interface

%description
Zope Annotations.

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
%python_sitelibdir/zope/app/*
%python_sitelibdir/*.egg-info

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.4.0-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.4.0-alt1.1
- (AUTO) subst_x86_64.

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

