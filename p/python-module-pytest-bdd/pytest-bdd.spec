%define oname pytest-bdd

%def_with python3
#def_disable check

Name: python-module-%oname
Version: 2.14.1
Release: alt1.git20150713.1
Summary: BDD library for the py.test runner
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-bdd/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/olegpidsadnyi/pytest-bdd.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-glob2 python-module-mako
BuildPreReq: python-module-detox python-module-mock
BuildPreReq: python-module-pytest-pep8 python-module-pytest-cov
BuildPreReq: python-module-pytest-cache python-module-pytest-xdist
BuildPreReq: python-module-markupsafe python-module-greenlet
BuildPreReq: python-module-virtualenv python-module-parse_type
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-glob2 python3-module-mako
BuildPreReq: python3-module-detox python3-module-mock
BuildPreReq: python3-module-pytest-pep8 python3-module-pytest-cov
BuildPreReq: python3-module-pytest-cache python3-module-pytest-xdist
BuildPreReq: python3-module-markupsafe python3-module-greenlet
BuildPreReq: python3-module-virtualenv python3-module-parse_type
%endif

%py_provides pytest_bdd

%description
pytest-bdd implements a subset of Gherkin language for the automation of
the project requirements testing and easier behavioral driven
development.

Unlike many other BDD tools it doesn't require a separate runner and
benefits from the power and flexibility of the pytest. It allows to
unify your unit and functional tests, easier continuous integration
server configuration and maximal reuse of the tests setup.

Pytest fixtures written for the unit tests can be reused for the setup
and actions mentioned in the feature steps with dependency injection,
which allows a true BDD just-enough specification of the requirements
without maintaining any context object containing the side effects of
the Gherkin imperative declarations.

%package -n python3-module-%oname
Summary: BDD library for the py.test runner
Group: Development/Python3
%py3_provides pytest_bdd

%description -n python3-module-%oname
pytest-bdd implements a subset of Gherkin language for the automation of
the project requirements testing and easier behavioral driven
development.

Unlike many other BDD tools it doesn't require a separate runner and
benefits from the power and flexibility of the pytest. It allows to
unify your unit and functional tests, easier continuous integration
server configuration and maximal reuse of the tests setup.

Pytest fixtures written for the unit tests can be reused for the setup
and actions mentioned in the feature steps with dependency injection,
which allows a true BDD just-enough specification of the requirements
without maintaining any context object containing the side effects of
the Gherkin imperative declarations.

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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
export PYTHONPATH=$PWD
py.test -vv
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.rst docs/*.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.14.1-alt1.git20150713.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.14.1-alt1.git20150713
- Version 2.14.1

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.3-alt1.git20141229
- Version 2.5.3

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.git20141119
- Version 2.5.1

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.git20141110
- Initial build for Sisyphus

