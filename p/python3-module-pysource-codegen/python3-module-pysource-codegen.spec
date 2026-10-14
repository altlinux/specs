%define pypi_name pysource-codegen
%define mod_name pysource_codegen

# circular dependencies pysource-minimize
%def_without check

Name: python3-module-%pypi_name
Version: 0.7.1
Release: alt1

Summary: generate random python code to test linter/formatter/and other tools
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pysource-codegen/
Vcs: https://github.com/15r10nk/pysource-codegen

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
%if_with check
BuildRequires: python3-module-pytest
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
* Wed Oct 14 2026 Anton Vyatkin <toni@altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus.
