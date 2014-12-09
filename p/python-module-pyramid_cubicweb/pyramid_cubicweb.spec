%define oname pyramid_cubicweb

%def_without python3

Name: python-module-%oname
Version: 0.1.3
Release: alt1
Summary: Integrate CubicWeb with a Pyramid application
License: Public domain
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_cubicweb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid-tests python-module-waitress
BuildPreReq: python-module-cubicweb-tests python-module-wsgicors
BuildPreReq: python-module-markdown python-module-logilab-constraint
BuildPreReq: python-module-webtest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid-tests python3-module-waitress
BuildPreReq: python3-module-cubicweb-tests python3-module-wsgicors
BuildPreReq: python3-module-markdown python3-module-logilab-constraint
BuildPreReq: python3-module-webtest
%endif

%py_provides %oname

%description
Integrate CubicWeb with a Pyramid application.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Integrate CubicWeb with a Pyramid application.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Integrate CubicWeb with a Pyramid application
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Integrate CubicWeb with a Pyramid application.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Integrate CubicWeb with a Pyramid application.

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

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc PKG-INFO
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Tue Dec 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1
- Version 0.1.3

* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1
- Version 0.1.2

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus

