%define _unpackaged_files_terminate_build 1
%define pypi_name jaraco.classes
%define ns_name jaraco
%define mod_name classes

%def_with check

Name: python3-module-%pypi_name
Version: 3.3.0
Release: alt1
Summary: Utility functions for Python class constructs
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/jaraco.classes/
Vcs: https://github.com/jaraco/jaraco.classes
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-%release.patch
%pyproject_runtimedeps_metadata
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra testing
%endif

%description
%summary

%prep
%setup
%patch0 -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore

%files
%dir %python3_sitelibdir/%ns_name/
%python3_sitelibdir/%ns_name/%mod_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Wed Aug 16 2023 Stanislav Levin <slev@altlinux.org> 3.3.0-alt1
- 3.2.2 -> 3.3.0.

* Mon Sep 12 2022 Danil Shein <dshein@altlinux.org> 3.2.2-alt1
- update version to 3.2.2
  + migrate to pyproject macroses

* Wed Nov 18 2020 Danil Shein <dshein@altlinux.org> 3.1.0-alt1
- update version to 3.1.0
- build with check enabled

* Tue Dec 03 2019 Anton Farygin <rider@altlinux.ru> 2.0-alt1
- first build for ALT

