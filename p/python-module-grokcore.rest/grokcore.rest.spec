%define oname grokcore.rest

%def_with python3

Name: python-module-%oname
Version: 1.3
Release: alt2
Summary: REST View component for Grok
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/grokcore.rest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires grokcore grokcore.component grokcore.security grokcore.view
%py_requires grokcore.traverser martian zope.component zope.interface
%py_requires zope.publisher

%description
This packages provides base classes and a advanced traversal mechanism
for Grok based REST-Views.

%package -n python3-module-%oname
Summary: REST View component for Grok
Group: Development/Python3
%py3_requires grokcore grokcore.component grokcore.security grokcore.view
%py3_requires grokcore.traverser martian zope.component zope.interface
%py3_requires zope.publisher

%description -n python3-module-%oname
This packages provides base classes and a advanced traversal mechanism
for Grok based REST-Views.

%package -n python3-module-%oname-tests
Summary: Tests for grokcore.rest
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires grokcore.content grokcore.view zope.app.appsetup
%py3_requires zope.app.wsgi zope.errorview zope.testing

%description -n python3-module-%oname-tests
This packages provides base classes and a advanced traversal mechanism
for Grok based REST-Views.

This package contains tests for grokcore.rest.

%package tests
Summary: Tests for grokcore.rest
Group: Development/Python
Requires: %name = %version-%release
%py_requires grokcore.content grokcore.view zope.app.appsetup
%py_requires zope.app.wsgi zope.errorview zope.testing

%description tests
This packages provides base classes and a advanced traversal mechanism
for Grok based REST-Views.

This package contains tests for grokcore.rest.

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
* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt2
- Added module for Python 3

* Fri Feb 22 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1
- Version 1.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt2.1
- Rebuild with Python-2.7

* Wed Jun 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

