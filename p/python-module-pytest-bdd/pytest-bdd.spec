%define _unpackaged_files_terminate_build 1
%define oname pytest-bdd

%def_with check

Name: python-module-%oname
Version: 3.0.0
Release: alt1

Summary: BDD library for the py.test runner
License: MIT
Group: Development/Python

Url: https://pypi.org/project/pytest-bdd/
# https://github.com/pytest-dev/pytest-bdd.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python-module-execnet
BuildRequires: python-module-glob2
BuildRequires: python-module-mako
BuildRequires: python-module-parse
BuildRequires: python-module-parse_type
BuildRequires: python-module-pytest
BuildRequires: python3-module-execnet
BuildRequires: python3-module-glob2
BuildRequires: python3-module-mako
BuildRequires: python3-module-parse
BuildRequires: python3-module-parse_type
BuildRequires: python3-module-pytest
%endif

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
%patch -p1
# python mock is actually not used
grep -qs 'import mock' tests/feature/test_wrong.py || exit 1
sed -i '/import mock/d' tests/feature/test_wrong.py

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd

%python_install

%check
PYTHONPATH=$(pwd) py.test -vv
pushd ../python3
PYTHONPATH=$(pwd) py.test3 -vv
popd

%files
%doc CHANGES.rst README.rst
%_bindir/pytest-bdd
%python_sitelibdir/pytest_bdd/
%python_sitelibdir/pytest_bdd-*.egg-info/

%files -n python3-module-%oname
%doc CHANGES.rst README.rst
%_bindir/pytest-bdd.py3
%python3_sitelibdir/pytest_bdd/
%python3_sitelibdir/pytest_bdd-*.egg-info/

%changelog
* Mon Dec 24 2018 Stanislav Levin <slev@altlinux.org> 3.0.0-alt1
- 2.19.0 -> 3.0.0.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.19.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Nov 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.19.0-alt1
- Updated to upstream version 2.19.0.

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

