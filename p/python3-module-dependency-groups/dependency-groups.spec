%define pypi_name dependency-groups

%def_with check

Name:    python3-module-%pypi_name
Version: 1.3.0
Release: alt1

Summary: A standalone implementation of PEP 735 Dependency Groups

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/dependency-groups
VCS:     https://github.com/pypa/dependency-groups

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.rst
%_bindir/dependency-groups
%_bindir/lint-dependency-groups
%_bindir/pip-install-dependency-groups
%python3_sitelibdir/dependency_groups
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Feb 11 2025 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus.
