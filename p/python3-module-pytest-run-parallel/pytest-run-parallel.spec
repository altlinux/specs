%define _unpackaged_files_terminate_build 1
%def_with check
%define pypi_name pytest-run-parallel
%define module_name pytest_run_parallel

Name: python3-module-%pypi_name
Version: 0.3.1
Release: alt1

Summary: A simple pytest plugin to run tests concurrently
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-run-parallel/
Vcs: https://github.com/Quansight-Labs/pytest-run-parallel

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
This pytest plugin takes a set of tests that would be normally be run
serially and execute them in parallel.
The main goal of pytest-run-parallel is to discover thread-safety issues
that could exist when using C libraries, this is of vital importance after
PEP703, which provides a path for a CPython implementation without depending
on the Global Interpreter Lock (GIL), thus allowing for proper parallelism
in programs that make use of the CPython interpreter.

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
%pyproject_run_pytest

%files
%doc LICENSE README.rst
%python3_sitelibdir/%module_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Apr 04 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.3.1-alt1
- Initial build for ALT Sisyphus.

