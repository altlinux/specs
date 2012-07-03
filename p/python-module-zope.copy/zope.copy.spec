%define oname zope.copy
Name: python-module-%oname
Version: 3.5.0
Release: alt2.1
Summary: Pluggable object copying mechanism
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.copy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope zope.interface

%description
This package provides a pluggable way to copy persistent objects. It was
once extracted from the zc.copy package to contain much less
dependencies. In fact, we only depend on zope.interface to provide
pluggability.

%package tests
Summary: Tests for zope.copy
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.component zope.location zope.testing

%description tests
This package provides a pluggable way to copy persistent objects. It was
once extracted from the zc.copy package to contain much less
dependencies. In fact, we only depend on zope.interface to provide
pluggability.

This package contains tests for zope.copy.

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
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2
- Added necesssary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus

