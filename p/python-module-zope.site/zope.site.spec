%define oname zope.site
Name: python-module-%oname
Version: 3.9.2
Release: alt4.1
Summary: Local registries for zope component architecture
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.site/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.annotation zope.container zope.security
%py_requires zope.component zope.event zope.interface
%py_requires zope.lifecycleevent zope.location

%description
This package provides a local and persistent site manager
implementation, so that one can register local utilities and adapters.
It uses local adapter registries for its adapter and utility registry.
The module also provides some facilities to organize the local software
and ensures the correct behavior inside the ZODB.

%package tests
Summary: Tests for zope.site
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.configuration zope.testing

%description tests
This package provides a local and persistent site manager
implementation, so that one can register local utilities and adapters.
It uses local adapter registries for its adapter and utility registry.
The module also provides some facilities to organize the local software
and ensures the correct behavior inside the ZODB.

This package contains tests for zope.site.

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
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.9.2-alt4.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.2-alt4
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.2-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.2-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.2-alt1
- Initial build for Sisyphus

