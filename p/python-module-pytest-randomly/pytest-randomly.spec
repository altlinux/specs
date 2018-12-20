%define _unpackaged_files_terminate_build 1
%define oname pytest-randomly

%def_with check

Name: python-module-%oname
Version: 1.2.3
Release: alt1

Summary: Pytest plugin to randomly order tests and control random.seed
License: BSD 3-Clause
Group: Development/Python
# Source-git: https://github.com/pytest-dev/pytest-randomly
Url: https://pypi.org/project/pytest-randomly/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python-module-numpy
BuildRequires: python-module-pytest
BuildRequires: python3-module-numpy
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

%description
Randomness in testing can be quite powerful to discover hidden flaws in the
tests themselves, as well as giving a little more coverage to your system.

By randomly ordering the tests, the risk of surprising inter-test dependencies
is reduced - a technique used in many places.

By resetting the random seed to a repeatable number for each test, tests can
create data based on random numbers and yet remain repeatable, for example
factory boy's fuzzy values. This is good for ensuring that tests specify the
data they need and that the tested system is not affected by any data that is
filled in randomly due to not being specified.

%package -n python3-module-%oname
Summary: Pytest plugin to randomly order tests and control random.seed
Group: Development/Python3

%description -n python3-module-%oname
Randomness in testing can be quite powerful to discover hidden flaws in the
tests themselves, as well as giving a little more coverage to your system.

By randomly ordering the tests, the risk of surprising inter-test dependencies
is reduced - a technique used in many places.

By resetting the random seed to a repeatable number for each test, tests can
create data based on random numbers and yet remain repeatable, for example
factory boy's fuzzy values. This is good for ensuring that tests specify the
data they need and that the tested system is not affected by any data that is
filled in randomly due to not being specified.

%prep
%setup
%patch -p1

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
PYTHONPATH="$(pwd)" %_bindir/py.test -vv

pushd ../python3
PYTHONPATH="$(pwd)" %_bindir/py.test3 -vv
popd

%files
%doc README.rst
%python_sitelibdir/pytest_randomly.py*
%python_sitelibdir/pytest_randomly-*.egg-info/

%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir/pytest_randomly.py
%python3_sitelibdir/__pycache__/pytest_randomly.*.py*
%python3_sitelibdir/pytest_randomly-*.egg-info/

%changelog
* Wed Dec 19 2018 Stanislav Levin <slev@altlinux.org> 1.2.3-alt1
- Initial build.

