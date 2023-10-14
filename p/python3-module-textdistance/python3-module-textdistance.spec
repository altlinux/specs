%define _unpackaged_files_terminate_build 1
%define pypi_name textdistance

%def_with check

Name: python3-module-%pypi_name
Version: 4.6.0
Release: alt1

Summary: Compute distance between sequences
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/textdistance/
Vcs: https://github.com/life4/textdistance

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra all
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_check
%endif

%description
TextDistance -- python library for comparing distance between two
or more sequences by many algorithms.

Features:

* 30+ algorithms
* Pure python implementation
* Simple usage
* More than two sequences comparing
* Some algorithms have more than one implementation in one class
* Numpy usage for maximum speed

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sat Oct 14 2023 Anton Zhukharev <ancieg@altlinux.org> 4.6.0-alt1
- Built for ALT Sisyphus.

