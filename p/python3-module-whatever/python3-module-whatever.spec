%define _unpackaged_files_terminate_build 1
%define pypi_name whatever

%def_with check

Name: python3-module-%pypi_name
Version: 0.7
Release: alt1

Summary: Easy anonymous functions by partial application of operators
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/whatever/
Vcs: https://github.com/Suor/whatever

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
An easy way to make lambdas by partial application of python operators.

Inspired by Perl 6 one,
see http://perlcabal.org/syn/S02.html#The_Whatever_Object

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE CHANGELOG README.rst
%python3_sitelibdir/*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun May 07 2023 Anton Zhukharev <ancieg@altlinux.org> 0.7-alt1
- New version.

* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 0.6-alt1
- initial build for Sisyphus

