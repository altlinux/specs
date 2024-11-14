%define pypi_name pytest-shard
%define mod_name pytest_shard

%def_with check

Name:    python3-module-%pypi_name
Version: 0.1.2
Release: alt1

Summary: Shard tests to support parallelism across multiple machines
License: MIT
Group:   Development/Python3
URL:     https://github.com/AdamGleave/pytest-shard

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-hypothesis
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
Shards tests based on a hash of their test name enabling easy parallelism across
machines, suitable for a wide variety of continuous integration services. Tests
are split at the finest level of granularity, individual test cases, enabling
parallelism even if all of your tests are in a single file (or even single
parameterized test method).

%prep
%setup -n %name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Nov 09 2024 Alexander Burmatov <thatman@altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus.
