%define oname zope.cachedescriptors
Name: python-module-%oname
Version: 3.5.1
Release: alt2.1
Summary: Method and property caching decorators
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.cachedescriptors/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope

%description
Cached descriptors cache their output. They take into account instance
attributes that they depend on, so when the instance attributes change,
the descriptors will change the values they return.

Cached descriptors cache their data in _v_ attributes, so they are also
useful for managing the computation of volatile attributes for
persistent objects.

%package tests
Summary: Tests for zope.cachedescriptors
Group: Development/Python
Requires: %name = %version-%release

%description tests
Cached descriptors cache their output. They take into account instance
attributes that they depend on, so when the instance attributes change,
the descriptors will change the values they return.

Cached descriptors cache their data in _v_ attributes, so they are also
useful for managing the computation of volatile attributes for
persistent objects.

This package contains tests for zope.cachedescriptors.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt2
- Added necesssary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1
- Initial build for Sisyphus

