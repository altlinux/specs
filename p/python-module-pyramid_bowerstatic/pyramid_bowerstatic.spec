%define oname pyramid_bowerstatic

%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt1.dev0.git20141108
Summary: BowerStatic integration for Pyramid
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_bowerstatic/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mrijken/pyramid_bowerstatic.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid-tests python-module-bowerstatic
BuildPreReq: python-module-pytest-cov python-module-webtest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid-tests python3-module-bowerstatic
BuildPreReq: python3-module-pytest-cov python3-module-webtest
%endif

%py_provides %oname

%description
pyramid_bowerstatic integrates BowerStatic into Pyramid.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires pyramid.testing

%description tests
pyramid_bowerstatic integrates BowerStatic into Pyramid.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: BowerStatic integration for Pyramid
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
pyramid_bowerstatic integrates BowerStatic into Pyramid.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires pyramid.testing

%description -n python3-module-%oname-tests
pyramid_bowerstatic integrates BowerStatic into Pyramid.

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
cp -fR %oname/tests/bower_components \
	%buildroot%python_sitelibdir/%oname/tests/

%if_with python3
pushd ../python3
%python3_install
cp -fR %oname/tests/bower_components \
	%buildroot%python3_sitelibdir/%oname/tests/
popd
%endif

%check
python setup.py test
rm -fR build
py.test
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
rm -fR build
py.test-%_python3_version
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.dev0.git20141108
- Initial build for Sisyphus

