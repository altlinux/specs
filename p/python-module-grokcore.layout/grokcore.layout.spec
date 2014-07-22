%define oname grokcore.layout

%def_with python3

Name: python-module-%oname
Version: 1.6
Release: alt1
Summary: A layout component package for zope3 and Grok
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/grokcore.layout
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires grokcore.component grokcore.view zc.buildout zope.security
%py_requires zope.publisher zope.interface zope.errorview
%py_requires zope.component

%description
The grokcore.layout package provides a simple way to write view
components which can be included into a defined layout. It turns around
two main components : the Page and the Layout.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires grokcore.component.testing zope.testing
%py_requires zope.traversing.testing zope.site zope.session
%py_requires zope.container zope.component.testlayer

%description tests
The grokcore.layout package provides a simple way to write view
components which can be included into a defined layout. It turns around
two main components : the Page and the Layout.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A layout component package for zope3 and Grok
Group: Development/Python3
%py3_requires grokcore.component grokcore.view zc.buildout zope.security
%py3_requires zope.publisher zope.interface zope.errorview
%py3_requires zope.component

%description -n python3-module-%oname
The grokcore.layout package provides a simple way to write view
components which can be included into a defined layout. It turns around
two main components : the Page and the Layout.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires grokcore.component.testing zope.testing
%py3_requires zope.traversing.testing zope.site zope.session
%py3_requires zope.container zope.component.testlayer

%description -n python3-module-%oname-tests
The grokcore.layout package provides a simple way to write view
components which can be included into a defined layout. It turns around
two main components : the Page and the Layout.

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
%doc PKG-INFO *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1
- Initial build for Sisyphus

