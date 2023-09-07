%define _unpackaged_files_terminate_build 1
%define pypi_name whatthepatch

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.5
Release: alt1

Summary: What The Patch!? -- A Python patch parsing library
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/whatthepatch/
Vcs: https://github.com/cscorley/whatthepatch

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch1: %name-1.0.4-alt-increase-tests-timeout.patch

%py3_provides %pypi_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-module-pytest
%endif

%description
What The Patch!? is a library for both parsing and applying patch files.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.rst HISTORY.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 07 2023 Anton Zhukharev <ancieg@altlinux.org> 1.0.5-alt1
- Updated to 1.0.5.

* Wed Feb 15 2023 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 1.0.4-alt1
- 1.0.4
- Increase tests timeout

* Thu Jan 19 2023 Anton Zhukharev <ancieg@altlinux.org> 1.0.3-alt1
- 1.0.3

* Tue Oct 04 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.2-alt1
- initial build for Sisyphus

