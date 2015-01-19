%define oname nose-watch

%def_with python3

Name: python-module-%oname
Version: 0.9.1
Release: alt1.dev.git20130219
Summary: A nose plugin that re-runs test suite on filesystem event
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/nose-watch/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/lukaszb/nose-watch.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose python-module-watchdog
BuildPreReq: python-module-mock python-module-argh
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-module-watchdog
BuildPreReq: python3-module-mock python3-module-argh
BuildPreReq: python3-module-yaml
%endif

%py_provides nosewatch
%py_requires nose watchdog

%description
A Nose plugin that allows to run tests continuously (uses watchdog for
listening to filesystem events).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires mock

%description tests
A Nose plugin that allows to run tests continuously (uses watchdog for
listening to filesystem events).

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A nose plugin that re-runs test suite on filesystem event
Group: Development/Python3
%py3_provides nosewatch
%py3_requires nose watchdog

%description -n python3-module-%oname
A Nose plugin that allows to run tests continuously (uses watchdog for
listening to filesystem events).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires mock

%description -n python3-module-%oname-tests
A Nose plugin that allows to run tests continuously (uses watchdog for
listening to filesystem events).

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
rm -fR build
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
rm -fR build
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.dev.git20130219
- Initial build for Sisyphus

