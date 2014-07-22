%define oname grokcore.site

%def_with python3

Name: python-module-%oname
Version: 1.6.1
Release: alt2
Summary: Grok-like configuration for Zope local site and utilities
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/grokcore.site/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires grokcore ZODB3 grokcore.component martian zope.annotation
%py_requires zope.component zope.container zope.interface
%py_requires zope.lifecycleevent zope.site

%description
This package provides support to write local site and utilities for Zope
directly in Python (without ZCML).

%package -n python3-module-%oname
Summary: Grok-like configuration for Zope local site and utilities
Group: Development/Python3
%py3_requires grokcore ZODB3 grokcore.component martian zope.annotation
%py3_requires zope.component zope.container zope.interface
%py3_requires zope.lifecycleevent zope.site

%description -n python3-module-%oname
This package provides support to write local site and utilities for Zope
directly in Python (without ZCML).

%package -n python3-module-%oname-tests
Summary: Tests for grokcore.site
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.appsetup zope.component zope.configuration
%py3_requires zope.location zope.testing

%description -n python3-module-%oname-tests
This package provides support to write local site and utilities for Zope
directly in Python (without ZCML).

This pacckage contains tests for grokcore.site.

%package tests
Summary: Tests for grokcore.site
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.appsetup zope.component zope.configuration
%py_requires zope.location zope.testing

%description tests
This package provides support to write local site and utilities for Zope
directly in Python (without ZCML).

This pacckage contains tests for grokcore.site.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
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
* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt2
- Added module for Python 3

* Fri Feb 22 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1
- Version 1.6.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt2
- Added nececssary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1
- Initial build for Sisyphus

