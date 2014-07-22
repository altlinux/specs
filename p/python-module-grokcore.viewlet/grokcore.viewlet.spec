%define oname grokcore.viewlet

%def_with python3

Name: python-module-%oname
Version: 1.11
Release: alt2
Summary: Grok-like configuration for zope viewlets
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/grokcore.viewlet/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires grokcore grokcore.component grokcore.security
%py_requires grokcore.view martian zope.viewlet zope.contentprovider
%py_requires zope.browserpage zope.component zope.interface
%py_requires zope.publisher zope.security

%description
This package provides support to write and register Zope Viewlets
directly in Python (without ZCML). It's designed to be used with
grokcore.view which let you write and register Zope Views.

%package -n python3-module-%oname
Summary: Grok-like configuration for zope viewlets
Group: Development/Python3
%py3_requires grokcore grokcore.component grokcore.security
%py3_requires grokcore.view martian zope.viewlet zope.contentprovider
%py3_requires zope.browserpage zope.component zope.interface
%py3_requires zope.publisher zope.security

%description -n python3-module-%oname
This package provides support to write and register Zope Viewlets
directly in Python (without ZCML). It's designed to be used with
grokcore.view which let you write and register Zope Views.

%package -n python3-module-%oname-tests
Summary: Tests for grokcore.viewlet
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.annotation zope.app.appsetup zope.app.publication
%py3_requires zope.app.wsgi zope.configuration zope.container
%py3_requires zope.principalregistry zope.securitypolicy zope.site
%py3_requires zope.testing zope.traversing

%description -n python3-module-%oname-tests
This package provides support to write and register Zope Viewlets
directly in Python (without ZCML). It's designed to be used with
grokcore.view which let you write and register Zope Views.

This package contains tests for grokcore.viewlet.

%package tests
Summary: Tests for grokcore.viewlet
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.annotation zope.app.appsetup zope.app.publication
%py_requires zope.app.wsgi zope.configuration zope.container
%py_requires zope.principalregistry zope.securitypolicy zope.site
%py_requires zope.testing zope.traversing

%description tests
This package provides support to write and register Zope Viewlets
directly in Python (without ZCML). It's designed to be used with
grokcore.view which let you write and register Zope Views.

This package contains tests for grokcore.viewlet.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*test*

%files tests
%python_sitelibdir/*/*/*test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*test*
%exclude %python3_sitelibdir/*/*/*/*test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*test*
%python3_sitelibdir/*/*/*/*test*
%endif

%changelog
* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11-alt2
- Added module for Python 3

* Fri Feb 22 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11-alt1
- Version 1.11

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9-alt1
- Version 1.9

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt1
- Initial build for Sisyphus

