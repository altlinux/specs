%define oname z3c.iplocation
Name: python-module-%oname
Version: 0.5.0
Release: alt2.1
Summary: Geo location utility for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.iplocation/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc.catalog zope.app.container zope.app.intid
%py_requires zope.app.keyreference zope.component zope.schema z3c.schema

%description
This package provides a solution which allows geolocation of IP blocks,
country and continent of the visitor connection. The dataset, which must
be downloaded form www.ipligence.com, contains IP location at a
worldwide level. There are different commercial and free version
available at the homepage of ipligence.

%package tests
Summary: Tests for Geo location utility for Zope3
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.coverage zope.annotation zope.app.testing zope.testing

%description tests
This package provides a solution which allows geolocation of IP blocks,
country and continent of the visitor connection. The dataset, which must
be downloaded form www.ipligence.com, contains IP location at a
worldwide level. There are different commercial and free version
available at the homepage of ipligence.

This package contains tests for Geo location utility for Zope3.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus

