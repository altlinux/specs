%define oname grokcore.view

%def_with python3

Name: python-module-%oname
Version: 2.9
Release: alt2
Summary: Grok-like configuration for Zope browser pages
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/grokcore.view/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires grokcore.component grokcore.security martian
%py_requires zope.browserresource zope.component zope.interface
%py_requires zope.pagetemplate zope.ptresource zope.publisher
%py_requires zope.security zope.traversing

%description
This package provides support for writing browser pages for Zope and
registering them directly in Python (without ZCML).

%package -n python3-module-%oname
Summary: Grok-like configuration for Zope browser pages
Group: Development/Python3
%py3_requires grokcore.component grokcore.security martian
%py3_requires zope.browserresource zope.component zope.interface
%py3_requires zope.pagetemplate zope.ptresource zope.publisher
%py3_requires zope.security zope.traversing

%description -n python3-module-%oname
This package provides support for writing browser pages for Zope and
registering them directly in Python (without ZCML).

%package -n python3-module-%oname-tests
Summary: Tests for grokcore.view
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.wsgi zope.container zope.securitypolicy zope.site
%py3_requires zope.testing zope.login zope.configuration
%py3_requires zope.app.appsetup zope.app.publication zope.browserpage
%py3_requires zope.password zope.principalregistry

%description -n python3-module-%oname-tests
This package provides support for writing browser pages for Zope and
registering them directly in Python (without ZCML).

This package contains tests for grokcore.view.

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

%package -n python3-module-grokcore
Summary: Core files for grokcore
Group: Development/Python3

%description -n python3-module-grokcore
This package provides support for writing browser pages for Zope and
registering them directly in Python (without ZCML).

This package contains corefiles for grokcore.

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
touch %buildroot%python_sitelibdir/grokcore/__init__.py

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
touch %buildroot%python3_sitelibdir/grokcore/__init__.py
%endif

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

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/grokcore/__init__.py
%exclude %python3_sitelibdir/grokcore/__pycache__/__init__.*
%exclude %python3_sitelibdir/*/*/*test*
%exclude %python3_sitelibdir/*/*/*/*test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*test*
%python3_sitelibdir/*/*/*/*test*

%files -n python3-module-grokcore
%python3_sitelibdir/grokcore/__init__.py
%python3_sitelibdir/grokcore/__pycache__/__init__.*
%endif

%changelog
* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9-alt2
- Added module for Python 3

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9-alt1
- Version 2.9

* Fri Feb 22 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8-alt1
- Version 2.8

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.1-alt1
- Version 2.6.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt2
- Added necessary requirents
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1
- Initial build for Sisyphus

