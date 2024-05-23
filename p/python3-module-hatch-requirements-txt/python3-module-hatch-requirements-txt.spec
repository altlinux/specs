%define _unpackaged_files_terminate_build 1
%define pypi_name hatch-requirements-txt
%define mod_name hatch_requirements_txt

%def_with check

Name: python3-module-%pypi_name
Version: 0.4.1
Release: alt1.git1aa21b8

Summary: Hatchling plugin to read project dependencies from requirements.txt
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/hatch-requirements-txt/
Vcs: https://github.com/repo-helper/hatch-requirements-txt

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
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
* Thu May 23 2024 Anton Zhukharev <ancieg@altlinux.org> 0.4.1-alt1.git1aa21b8
- Fixed FTBFS (updated to 1aa21b8).

* Fri Feb 09 2024 Anton Zhukharev <ancieg@altlinux.org> 0.4.1-alt1
- Updated to 0.4.1.

* Wed Mar 29 2023 Anton Zhukharev <ancieg@altlinux.org> 0.4.0-alt1
- New version.

* Mon Feb 13 2023 Anton Zhukharev <ancieg@altlinux.org> 0.3.0-alt1
- 0.1.1 -> 0.3.0

* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 0.1.1-alt1
- initial build for Sisyphus

