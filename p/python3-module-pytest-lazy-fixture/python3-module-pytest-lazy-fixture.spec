%define pypi_name pytest-lazy-fixture
%define mod_name pytest_lazyfixture

%def_with check

Name:    python3-module-%pypi_name
Version: 0.6.3
Release: alt1

Summary: It helps to use fixtures in pytest.mark.parametrize
License: MIT
Group:   Development/Python3
URL:     https://github.com/tvorog/pytest-lazy-fixture

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

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
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Oct 23 2023 Alexander Burmatov <thatman@altlinux.org> 0.6.3-alt1
- Initial build for Sisyphus.
