%define oname grokcore.startup
Name: python-module-%oname
Version: 1.1
Release: alt2.1
Summary: Paster support for Grok projects
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/grokcore.startup/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires grokcore zope.component zope.publisher zope.dottedname
%py_requires zope.app.wsgi zope.app.debug

%description
This package provides elements for starting a Grok project with paster
and WSGI.

%package tests
Summary: Tests for grokcore.startup
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.appsetup zope.component zope.interface
%py_requires zope.testing zope.security

%description tests
This package provides elements for starting a Grok project with paster
and WSGI.

This package contains tests for grokcore.startup.

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
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

