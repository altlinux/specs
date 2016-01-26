%define oname z3c.unconfigure
%def_disable check

Name: python-module-%oname
Version: 1.1
Release: alt2
Summary: Disable specific ZCML directives in other package's configuration
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/z3c.unconfigure/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildRequires: python-module-pytest python-module-zope.security python-module-zope.testing

#BuildPreReq: python-module-setuptools-tests
#BuildPreReq: python-module-zope.configuration
#BuildPreReq: python-module-zope.component
#BuildPreReq: python-module-zope.security
#BuildPreReq: python-module-zope.event
#BuildPreReq: python-module-zope.testing

%py_provides %oname
#%py_requires z3c zope.configuration zope.component zope.security
#%py_requires zope.event

%description
This package allows you to disable specific bits of ZCML configuration
that may occur in other packages.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
#%py_requires zope.testing

%description tests
This package allows you to disable specific bits of ZCML configuration
that may occur in other packages.

This package contains tests for %oname.

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
rm -fR build
py.test

%files
%doc *.txt
%python_sitelibdir/z3c/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/z3c/*/test*

%files tests
%python_sitelibdir/z3c/*/test*

%changelog
* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 1.1-alt2
- Rebuild with "def_disable check"
- Cleanup buildreq

* Fri Dec 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

