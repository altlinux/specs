%define _unpackaged_files_terminate_build 1
%define pypi_name makefun
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.15.3
Release: alt1

Summary: Dynamically create python functions with a proper signature
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/makefun/
Vcs: https://github.com/smarie/python-makefun

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch1: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%add_pyproject_deps_build_filter pytest-runner
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter nox
%add_pyproject_deps_check_filter virtualenv
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Small library to dynamically create python functions.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile noxfile-requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.md docs
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Jul 05 2024 Anton Zhukharev <ancieg@altlinux.org> 1.15.3-alt1
- Updated to 1.15.3.

* Fri Nov 10 2023 Anton Zhukharev <ancieg@altlinux.org> 1.15.2-alt1
- Updated to 1.15.2.

* Tue Aug 01 2023 Anton Zhukharev <ancieg@altlinux.org> 1.15.1-alt1
- Updated to 1.15.1.

* Wed Sep 28 2022 Anton Zhukharev <ancieg@altlinux.org> 1.15.0-alt1
- 1.14.0 -> 1.15.0
- clean up spec
- fix description

* Sat Jul 23 2022 Anton Zhukharev <ancieg@altlinux.org> 1.14.0-alt1
- initial build for Sisyphus

