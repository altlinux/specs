%define _unpackaged_files_terminate_build 1
%define pypi_name funcy

%def_with check

Name: python3-module-%pypi_name
Version: 2.0
Release: alt1

Summary: A fancy and practical functional tools
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/funcy/
Vcs: https://github.com/Suor/funcy

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
A collection of fancy functional tools focused on practicality.

Inspired by clojure, underscore and my own abstractions.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_pipreqfile test_requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE CHANGELOG README.rst TODO.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun May 07 2023 Anton Zhukharev <ancieg@altlinux.org> 2.0-alt1
- New version.

* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 1.17-alt1
- initial build for Sisyphus

