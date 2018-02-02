# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.1.1
%define mname dm
%define oname %mname.reuse
Name: python-module-%oname
Version: 1.1
#Release: alt1
Summary: Support for object reuse with slight modifications
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/dm.reuse/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools

%py_provides %oname
%py_requires %mname

%description
Utilities to reuse (slightly modified) objects in new contexts.

Currently, there is a single utility: rebindFunction. It allows to reuse
the code of a function while changing name, globals, default arguments,
properties and/or names used.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Utilities to reuse (slightly modified) objects in new contexts.

Currently, there is a single utility: rebindFunction. It allows to reuse
the code of a function while changing name, globals, default arguments,
properties and/or names used.

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
%doc PKG-INFO
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt1.1
- (AUTO) subst_x86_64.

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

