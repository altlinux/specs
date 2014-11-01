%define mname zope.app
%define oname %mname.annotation
Name: python-module-%oname
Version: 3.4.0
Release: alt1
Summary: Zope Annotations
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/zope.app.annotation/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc *.txt
%python_sitelibdir/zope/app/*
%python_sitelibdir/*.egg-info

%changelog
* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

