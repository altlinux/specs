%def_disable check

%define mname zc
%define oname %mname.set
Name: python-module-%oname
Version: 0.1
Release: alt2.dev.r75642
Summary: The persistent set module
License: Free
Group: Development/Python
Url: http://www.zope.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# from http://download.zope.org/distribution/
Source: %name-%version.tar

BuildRequires: python-module-pytest python-module-zope.app.folder python-module-zope.testing
#BuildPreReq: python-module-setuptools-tests
#BuildPreReq: python-module-ZODB3
#BuildPreReq: python-module-zope.app.folder
#BuildPreReq: python-module-zope.testing

%py_provides %oname

%description
The persistent set module contains a simple persistent version of a set,
that inherits from persistent.Persistent and marks _p_changed = True for
any potentially mutating operation.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The persistent set module contains a simple persistent version of a set,
that inherits from persistent.Persistent and marks _p_changed = True for
any potentially mutating operation.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
install -d %buildroot%python_sitelibdir/%mname
cp -fR src/zc/set %buildroot%python_sitelibdir/%mname/
cp -fR src/*.egg-info %buildroot%python_sitelibdir/

%check
python setup.py test
py.test -vv $(find src/ -name '*.py')

%files
%doc PKG-INFO
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%changelog

* Wed Feb 03 2016 Sergey Alembekov <rt@altlinux.ru> 0.1-alt2.dev.r75642
- Disable tests

* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.dev.r75642
- Initial build for Sisyphus

