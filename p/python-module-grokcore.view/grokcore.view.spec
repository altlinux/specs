%define oname grokcore.view
Name: python-module-%oname
Version: 2.6.1
Release: alt1
Summary: Grok-like configuration for Zope browser pages
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/grokcore.view/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires grokcore.component grokcore.security martian
%py_requires zope.browserresource zope.component zope.interface
%py_requires zope.pagetemplate zope.ptresource zope.publisher
%py_requires zope.security zope.traversing

%description
This package provides support for writing browser pages for Zope and
registering them directly in Python (without ZCML).

%package tests
Summary: Tests for grokcore.view
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.wsgi zope.container zope.securitypolicy zope.site
%py_requires zope.testing zope.login zope.configuration
%py_requires zope.app.appsetup zope.app.publication zope.browserpage
%py_requires zope.password zope.principalregistry

%description tests
This package provides support for writing browser pages for Zope and
registering them directly in Python (without ZCML).

This package contains tests for grokcore.view.

%package -n python-module-grokcore
Summary: Core files for grokcore
Group: Development/Python

%description -n python-module-grokcore
This package provides support for writing browser pages for Zope and
registering them directly in Python (without ZCML).

This package contains corefiles for grokcore.

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

touch %buildroot%python_sitelibdir/grokcore/__init__.py

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/grokcore/__init__.py*
%exclude %python_sitelibdir/*/*/*test*

%files -n python-module-grokcore
%python_sitelibdir/grokcore/__init__.py*

%files tests
%python_sitelibdir/*/*/*test*

%changelog
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.1-alt1
- Version 2.6.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt2
- Added necessary requirents
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1
- Initial build for Sisyphus

