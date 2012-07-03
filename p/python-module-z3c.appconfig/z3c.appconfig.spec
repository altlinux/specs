%define oname z3c.appconfig
Name: python-module-%oname
Version: 1.0
Release: alt2.1
Summary: Simple application configuration system
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.appconfig/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.interface zope.component

%description
This package provides a method to configure an application via standard
.ini files. This is convenient for site admins since they are more
likely to be familiar with ini files than with ZCML.

%package tests
Summary: Tests for z3c.appconfig
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides a method to configure an application via standard
.ini files. This is convenient for site admins since they are more
likely to be familiar with ini files than with ZCML.

This package contains tests for z3c.appconfig.

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Mon Jun 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

