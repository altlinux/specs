# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.dev0.git20130304.1.1
%define oname zope.untrustedpython

Name: python-module-%oname
Version: 4.0.1
#Release: alt1.dev0.git20130304
Summary: Zope Untrusted Python Library
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/zope.untrustedpython/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/zope.untrustedpython.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-RestrictedPython
BuildPreReq: python-module-zope.security

%py_provides %oname
%py_requires zope zope.security

%description
Sandboxed environment for untrusted code / templates, using
zope.security and RestrictedPython

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Sandboxed environment for untrusted code / templates, using
zope.security and RestrictedPython

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
%doc *.rst docs/*.rst
%python_sitelibdir/zope/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/zope/*/tests.*

%files tests
%python_sitelibdir/zope/*/tests.*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.0.1-alt1.dev0.git20130304.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.1-alt1.dev0.git20130304.1
- (AUTO) subst_x86_64.

* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.dev0.git20130304
- Initial build for Sisyphus

