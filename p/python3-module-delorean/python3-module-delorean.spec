%define _unpackaged_files_terminate_build 1
%define pypi_name delorean
%define mod_name delorean

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.0
Release: alt1

Summary: library for manipulating datetimes with ease and clarity
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/delorean/
Vcs: https://github.com/myusuf3/delorean

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter towncrier
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Delorean is a library for clearing up the inconvenient truths that arise dealing
with datetimes in Python. Understanding that timing is a delicate enough of a
problem delorean hopes to provide a cleaner less troublesome solution to
shifting, manipulating, and generating datetimes.

Delorean stands on the shoulders of giants: the standard library's zoneinfo and
dateutil

Delorean will provide natural language improvements for manipulating time, as
well as datetime abstractions for ease of use. The overall goal is to improve
datetime manipulations, with a little bit of software and philosophy.

Pretty much make you a badass time traveller.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Sep 22 2026 Anton Zhukharev <ancieg@altlinux.org> 2.0.0-alt1
- Updated to 2.0.0.

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 1.0.0-alt3.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Fri May 26 2023 Anton Vyatkin <toni@altlinux.org> 1.0.0-alt3
- Fix FTBFS

* Mon Apr 10 2023 Anton Vyatkin <toni@altlinux.org> 1.0.0-alt2
- Fix BuildRequires

* Sat Dec 10 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt1
- initial build for Sisyphus
