%define pypi_name pytest-snapshot
%define mod_name pytest_snapshot

%def_with check

Name:    python3-module-%pypi_name
Version: 0.9.0
Release: alt1

Summary: A plugin for snapshot testing with pytest
License: MIT
Group:   Development/Python3
URL:     https://github.com/joseph-roitman/pytest-snapshot

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
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%mod_name-0.0.0.dist-info/

%changelog
* Thu Oct 19 2023 Alexander Burmatov <thatman@altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus.
