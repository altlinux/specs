%define _unpackaged_files_terminate_build 1
%define pypi_name pyfakefs

%def_with check

Name: python3-module-%pypi_name
Version: 5.5.0
Release: alt1
Summary: Implements a fake file system that mocks the Python file system modules
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/pyfakefs/
Vcs: https://github.com/pytest-dev/pyfakefs
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_check
%endif

%description
%pypi_name implements a fake file system that mocks the Python file system
modules. Using pyfakefs, your tests operate on a fake file system in memory
without touching the real disk. The software under test requires no
modification to work with pyfakefs.

%prep
%setup
%autopatch -p1

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_pipreqfile requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install
# don't package tests (useless)
rm -r %buildroot%python3_sitelibdir/%pypi_name/{tests,pytest_tests}

%check
%pyproject_run -- python -m pyfakefs.tests.all_tests
%pyproject_run -- python -m pyfakefs.tests.all_tests_without_extra_packages
%pyproject_run -- python -m pytest pyfakefs/pytest_tests/pytest_plugin_test.py

%files
%python3_sitelibdir/pyfakefs/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon May 13 2024 Stanislav Levin <slev@altlinux.org> 5.5.0-alt1
- 5.4.1 -> 5.5.0.

* Fri Apr 12 2024 Stanislav Levin <slev@altlinux.org> 5.4.1-alt1
- 5.4.0 -> 5.4.1.

* Mon Apr 08 2024 Stanislav Levin <slev@altlinux.org> 5.4.0-alt1
- 5.3.5 -> 5.4.0.

* Wed Feb 07 2024 Stanislav Levin <slev@altlinux.org> 5.3.5-alt1
- 5.2.2 -> 5.3.5.

* Tue Apr 18 2023 Stanislav Levin <slev@altlinux.org> 5.2.2-alt1
- 5.0.0 -> 5.2.2.

* Mon Oct 10 2022 Stanislav Levin <slev@altlinux.org> 5.0.0-alt1
- 4.7.0 -> 5.0.0.

* Tue Sep 27 2022 Stanislav Levin <slev@altlinux.org> 4.7.0-alt1
- 4.6.3 -> 4.7.0.

* Wed Aug 10 2022 Stanislav Levin <slev@altlinux.org> 4.6.3-alt1
- 4.5.6 -> 4.6.3.

* Mon Mar 21 2022 Stanislav Levin <slev@altlinux.org> 4.5.6-alt1
- 4.5.5 -> 4.5.6.

* Thu Feb 24 2022 Stanislav Levin <slev@altlinux.org> 4.5.5-alt1
- 3.7.1 -> 4.5.5.

* Wed Feb 12 2020 Stanislav Levin <slev@altlinux.org> 3.7.1-alt1
- Initial build.
