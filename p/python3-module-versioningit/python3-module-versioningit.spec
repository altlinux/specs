%define pypi_name versioningit

%def_with check

Name:    python3-module-%pypi_name
Version: 3.3.0
Release: alt1

Summary: Versioning It with your Version In Git
License: MIT
Group:   Development/Python3
URL:     https://github.com/jwodder/versioningit

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-pydantic
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
%pyproject_run_pytest --ignore=test/test_end2end.py

%files
%doc *.rst
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Oct 16 2025 Alexander Burmatov <thatman@altlinux.org> 3.3.0-alt1
- Initial build for Sisyphus.
