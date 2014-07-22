%define oname grokcore.catalog

%def_with python3

Name: python-module-%oname
Version: 2.0
Release: alt1
Summary: Grok-like configuration for catalog and indexes
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/grokcore.catalog/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires grokcore.component grokcore.site zc.buildout zope.catalog
%py_requires zope.component zc.catalog zope.interface
%py_requires zope.lifecycleevent zope.intid zope.exceptions

%description
Grok-like configuration for catalog and indexes.

%package -n python3-module-%oname
Summary: Grok-like configuration for catalog and indexes
Group: Development/Python3
%py3_requires grokcore.component grokcore.site zc.buildout zope.catalog
%py3_requires zope.component zc.catalog zope.interface
%py3_requires zope.lifecycleevent zope.intid zope.exceptions

%description -n python3-module-%oname
Grok-like configuration for catalog and indexes.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires grokcore.content zope.index zope.configuration
%py3_requires zope.app.wsgi.testlayer zope.testing

%description -n python3-module-%oname-tests
Grok-like configuration for catalog and indexes.

This package contains tests for %oname.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires grokcore.content zope.index zope.configuration
%py_requires zope.app.wsgi.testlayer zope.testing

%description tests
Grok-like configuration for catalog and indexes.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
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
* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1
- Initial build for Sisyphus

