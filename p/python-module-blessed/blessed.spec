%define oname blessed

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.9.5
Release: alt1.git20150112.1.1
Summary: A feature-filled fork of Erik Rose's blessings project
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/blessed/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jquast/blessed.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools /dev/pts
BuildPreReq: python-module-tox python-module-wcwidth
BuildPreReq: python-module-coverage python-module-pytest-flakes
BuildPreReq: python-module-pytest-xdist python-module-pytest-pep8
BuildPreReq: python-module-pytest-cov python-module-mock
BuildPreReq: python-modules-curses
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-tox python3-module-wcwidth
BuildPreReq: python3-module-coverage python3-module-pytest-flakes
BuildPreReq: python3-module-pytest-xdist python3-module-pytest-pep8
BuildPreReq: python3-module-pytest-cov python3-module-mock
BuildPreReq: python3-modules-curses
%endif

%py_provides %oname
Requires: /dev/pts
%py_requires wcwidth curses

%description
A feature-filled fork of Erik Rose's blessings project.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A feature-filled fork of Erik Rose's blessings project.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A feature-filled fork of Erik Rose's blessings project
Group: Development/Python3
%py3_provides %oname
Requires: /dev/pts
%py3_requires wcwidth curses

%description -n python3-module-%oname
A feature-filled fork of Erik Rose's blessings project.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A feature-filled fork of Erik Rose's blessings project.

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
export LC_ALL=en_US.UTF-8
py.test \
	--strict --flakes \
	--junit-xml=results.{envname}.xml --verbose \
	--cov blessed blessed/tests --cov-report=term-missing
%if_with python3
pushd ../python3
py.test-%_python3_version \
	--strict --flakes \
	--junit-xml=results.{envname}.xml --verbose \
	--cov blessed blessed/tests --cov-report=term-missing
popd
%endif

%files
%doc *.rst docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.9.5-alt1.git20150112.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.5-alt1.git20150112.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.5-alt1.git20150112
- Initial build for Sisyphus

