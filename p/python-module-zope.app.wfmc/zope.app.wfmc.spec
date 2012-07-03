%define oname zope.app.wfmc
Name: python-module-%oname
Version: 0.1.2
Release: alt2.1
Summary: Zope Application integration for ``zope.wfmc``
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.wfmc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app zope.interface zope.schema zope.configuration
%py_requires zope.wfmc zope.component

%description
This package provides Zope application level integration of the
zope.wfmc package including ZCML directives.

%package tests
Summary: Tests for zope.app.wfmc
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing

%description tests
This package provides Zope application level integration of the
zope.wfmc package including ZCML directives.

This package contains tests for zope.app.wfmc.

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
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.2-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus

