%define _unpackaged_files_terminate_build 1
%define pypi_name type_lens
%define mod_name type-lens

%def_enable check

Name: python3-module-%mod_name
Version: 0.2.6
Release: alt1

Summary: Runtime type introspection utilities for Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/%mod_name

Vcs: https://github.com/litestar-org/type-lens
Source: https://pypi.io/packages/source/t/%mod_name/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3(hatchling)

%{?_enable_check:
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-covdefaults python3(typing_extensions)}

%py3_provides %pypi_name

%description
type-lens is a library for introspecting Python type annotations at runtime.
It aims to provide a unified, ergonomic API that works consistently across
Python versions, smoothing over the many version-specific quirks and
behavioral differences in Python's typing module.

%prep
%setup -n %{pypi_name}-%{version}

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}/

%changelog
* Thu Sep 25 2026 Yuri N. Sedunov <aris@altlinux.org> 0.2.6-alt1
- first build for Sisyphus

