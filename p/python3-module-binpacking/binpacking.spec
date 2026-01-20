%define _unpackaged_files_terminate_build 1
%define pypi_name binpacking

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.0
Release: alt1

Summary: Contains greedy algorithms to solve two typical bin packing problems

License: MIT
Group: Development/Python3
URL: https://github.com/benmaier/binpacking
VCS: https://github.com/benmaier/binpacking

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(Cython)

BuildArch: noarch

%if_with check
BuildRequires: python3(numpy)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-cov)
%endif

%description
Heuristic distribution of weighted items to bins (either a fixed number of
bins or a fixed number of volume per bin). Data may be in form of list,
dictionary, list of tuples or csv-file.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md
%_bindir/binpacking
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jan 20 2026 Paul Wolneykien <manowar@altlinux.org> 2.0.0-alt1
- Version 2.0.0 (initial build for Sisyphus).
