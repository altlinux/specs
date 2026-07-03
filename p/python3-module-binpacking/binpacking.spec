%define _unpackaged_files_terminate_build 1
%define pypi_name binpacking

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.1
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

Requires: python3 >= 3.10

%if_with check
BuildRequires: python3(numpy)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-cov)
%endif

%description
Heuristic distribution of weighted items to bins (either a fixed number of
bins or a fixed number of volume per bin). Data may be in form of list,
dictionary, list of tuples or csv-file.

This package contains Python module '%%pypi_name'.

%package -n %pypi_name
Group: Sciences/Other
Requires: %name = %version-%release
License: MIT
Summary: An utility to solve two typical bin packing problems

%description -n %pypi_name
Heuristic distribution of weighted items to bins (either a fixed number of
bins or a fixed number of volume per bin). Data may be in form of list,
dictionary, list of tuples or csv-file.

This package contains command-line utility interfacing with the
Python module '%%pypi_name'.

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
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%files -n %pypi_name
%doc README.md
%_bindir/binpacking

%changelog
* Tue May 12 2026 Paul Wolneykien <manowar@altlinux.org> 2.0.1-alt1
- New version 2.0.1.

* Tue Jan 20 2026 Paul Wolneykien <manowar@altlinux.org> 2.0.0-alt2
- Extract the 'binpacking' utility into the separate package.
- Require Python3 >= 3.10.

* Tue Jan 20 2026 Paul Wolneykien <manowar@altlinux.org> 2.0.0-alt1
- Version 2.0.0 (initial build for Sisyphus).
