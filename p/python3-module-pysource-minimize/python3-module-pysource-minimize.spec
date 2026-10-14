%define pypi_name pysource-minimize
%define mod_name pysource_minimize

%def_with check

Name: python3-module-%pypi_name
Version: 0.10.1
Release: alt1

Summary: minimize python source code to find bugs more easily
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pysource-minimize
Vcs: https://github.com/15r10nk/pysource-minimize

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-click
BuildRequires: python3-module-inline-snapshot
BuildRequires: python3-module-black
BuildRequires: python3-module-pysource-codegen
%endif

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
%doc README.*
%_bindir/%pypi_name
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Wed Oct 14 2026 Anton Vyatkin <toni@altlinux.org> 0.10.1-alt1
- Initial build for Sisyphus.
