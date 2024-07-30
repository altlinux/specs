%define pypi_name pytest-lazy-fixtures
%define mod_name pytest_lazy_fixtures

%def_with check

Name:    python3-module-%pypi_name
Version: 1.1.0
Release: alt1

Summary: Allows you to use fixtures in @pytest.mark.parametrize
License: MIT
Group:   Development/Python3
URL:     https://github.com/dev-petrov/pytest-lazy-fixtures

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-poetry

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
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Jul 18 2024 Alexander Burmatov <thatman@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus.
