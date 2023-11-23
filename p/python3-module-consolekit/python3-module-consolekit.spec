%define _unpackaged_files_terminate_build 1
%define pypi_name consolekit

%def_with check

Name: python3-module-%pypi_name
Version: 1.5.2
Release: alt1

Summary: Additional utilities for click
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/consolekit/
Vcs: https://github.com/domdfcoding/consolekit

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%add_pyproject_deps_check_filter backports-entry-points-selectable
%add_pyproject_deps_check_filter pytest-mypy-plugins
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_pipreqfile tests/requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Nov 23 2023 Anton Zhukharev <ancieg@altlinux.org> 1.5.2-alt1
- Updated to 1.5.2.

* Fri Jul 21 2023 Anton Zhukharev <ancieg@altlinux.org> 1.5.1-alt1
- Updated to 1.5.1.

* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 1.4.1-alt2
- enable tests
- fix requires

* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 1.4.1-alt1
- initial build for Sisyphus (temporary broken)

