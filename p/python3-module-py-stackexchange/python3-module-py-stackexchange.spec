%define _unpackaged_files_terminate_build 1
%define pypi_name py-stackexchange
%define short_name stackexchange

# Network connection required for tests
%def_without check

Name:    python3-module-%pypi_name
Version: 2.2.7
Release: alt1

Summary: Stack overflow command line interface
License: BSD-3-Clause
Group:   Other
URL:     https://pypi.org/project/%pypi_name
VCS:     https://github.com/lucjon/Py-StackExchange.git

BuildRequires(pre): rpm-build-pyproject

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

%if_with check
BuildRequires: python3(pytest)
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

BuildArch: noarch

Source:  %name-%version.tar
Source1: %pyproject_deps_config_name

%description
Stack Overflow command line written in python. Using SoCLI you can
search and browse Stack Overflow without leaving the terminal.

%package demo
Summary: Demo for %name
Group: Development/Python3
Requires: %name = %EVR

%description demo
Stack Overflow command line written in python. Using SoCLI you can
search and browse Stack Overflow without leaving the terminal.

This package contains demo for %pypi_name.

%prep
%setup -n %name-%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra ./testsuite.py -k "not test_fetch_question and not test_pagesize_independence"

%files
%doc *.md
%python3_sitelibdir/%short_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%python3_sitelibdir/stackauth.py
%python3_sitelibdir/__pycache__/*

%files demo
%doc demo/*

%changelog
* Tue Nov 19 2024 Andrey Limachko <liannnix@altlinux.org> 2.2.7-alt1
- initial build (thx Yuri Kozyrev)
