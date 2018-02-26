%define oname z3c.referercredentials
Name: python-module-%oname
Version: 0.1.0
Release: alt2.1
Summary: An HTTP referer credentials plugin
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.referercredentials/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app.authentication zope.app.component
%py_requires zope.app.container zope.app.session zope.component
%py_requires zope.interface zope.publisher zope.schema zope.traversing

%description
A package that uses the HTTP referer header to provide credentials.

%package tests
Summary: Tests for HTTP referer credentials plugin
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.testing

%description tests
A package that uses the HTTP referer header to provide credentials.

This package contains tests for HTTP referer credentials plugin.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus

