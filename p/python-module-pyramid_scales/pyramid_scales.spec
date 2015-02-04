%define oname pyramid_scales

%def_with python3

Name: python-module-%oname
Version: 1.1
Release: alt1
Summary: Viewing scales metrics from Pyramid
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_scales/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-scales python-module-pyramid-tests
BuildPreReq: python-module-webtest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-scales python3-module-pyramid-tests
BuildPreReq: python3-module-webtest
%endif

%py_provides %oname
%py_requires scales

%description
The excellent scales library to collect in-process metrics (see Coda
Hale's CodeConf talk 'Metrics everywhere' among many others for reasons
why you might want use it) comes with a flask-based HTTP server that
allows viewing the collected measurements and dumping them as JSON.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires pyramid.config.testing

%description tests
The excellent scales library to collect in-process metrics (see Coda
Hale's CodeConf talk 'Metrics everywhere' among many others for reasons
why you might want use it) comes with a flask-based HTTP server that
allows viewing the collected measurements and dumping them as JSON.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Viewing scales metrics from Pyramid
Group: Development/Python3
%py3_provides %oname
%py3_requires scales

%description -n python3-module-%oname
The excellent scales library to collect in-process metrics (see Coda
Hale's CodeConf talk 'Metrics everywhere' among many others for reasons
why you might want use it) comes with a flask-based HTTP server that
allows viewing the collected measurements and dumping them as JSON.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires pyramid.config.testing

%description -n python3-module-%oname-tests
The excellent scales library to collect in-process metrics (see Coda
Hale's CodeConf talk 'Metrics everywhere' among many others for reasons
why you might want use it) comes with a flask-based HTTP server that
allows viewing the collected measurements and dumping them as JSON.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export LC_ALL=en_US.UTF-8
python setup.py test
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.txt *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

