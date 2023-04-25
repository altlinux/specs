%define _unpackaged_files_terminate_build 1
%define pypi_name coincidence

%def_with check

Name: python3-module-%pypi_name
Version: 0.6.5
Release: alt1
Summary: Helper functions for pytest
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/coincidence/
Vcs: https://github.com/python-coincidence/coincidence
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter backports-entry-points-selectable
%pyproject_builddeps_check
%endif

%description
%summary

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%if_with check
%pyproject_deps_resync_check_pipreqfile tests/requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra tests

%files
%doc README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Apr 24 2023 Stanislav Levin <slev@altlinux.org> 0.6.5-alt1
- 0.6.3 -> 0.6.5.

* Mon Nov 14 2022 Stanislav Levin <slev@altlinux.org> 0.6.3-alt3
- Fixed FTBFS (pytest 7.2).

* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 0.6.3-alt2
- enable tests

* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 0.6.3-alt1
- initial build for Sisyphus

