%define _unpackaged_files_terminate_build 1
%define pypi_name apeye-core
%define mod_name apeye_core

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.4
Release: alt1

Summary: Core (offline) functionality for the apeye library
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/apeye-core/
Vcs: https://github.com/domdfcoding/apeye-core

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%py3_provides %pypi_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary

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
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Jul 20 2023 Anton Zhukharev <ancieg@altlinux.org> 1.1.4-alt1
- Updated to 1.1.4.

* Wed Mar 29 2023 Anton Zhukharev <ancieg@altlinux.org> 1.1.1-alt1
- New version.

* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt3
- add convenient 'python3(apeye-core)' provide

* Fri Sep 30 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt2
- enable tests

* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt1
- initial build for Sisyphus

