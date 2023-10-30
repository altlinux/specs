%define pypi_name pytest-random-order

%def_with check

Name:    python3-module-%pypi_name
Version: 1.1.0
Release: alt1

Summary: pytest plugin to randomise the order of tests with some control over the randomness
License: MIT
Group:   Development/Python3
URL:     https://github.com/jbasko/pytest-random-order

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-py
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
pytest-random-order is a pytest plugin that randomises the order of tests.
This can be useful to detect a test that passes just because it happens to
run after an unrelated test that leaves the system in a favourable state.
The plugin allows user to control the level of randomness they want to
introduce and to disable reordering on subsets of tests. Tests can be rerun in
a specific order by passing a seed value reported in a previous test run.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.rst
%python3_sitelibdir/random_order/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Oct 19 2023 Alexander Burmatov <thatman@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus.
