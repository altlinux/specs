%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-forked

%def_with check

Name: python3-module-%pypi_name
Version: 1.6.0
Release: alt1
Summary: pytest plugin for running tests in isolated forked subprocesses
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-forked/
VCS: https://github.com/pytest-dev/pytest-forked
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc CHANGELOG.rst README.rst
%python3_sitelibdir/pytest_forked/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu May 04 2023 Stanislav Levin <slev@altlinux.org> 1.6.0-alt1
- 1.4.0 -> 1.6.0.

* Mon Jan 23 2023 Stanislav Levin <slev@altlinux.org> 1.4.0-alt2
- Fixed FTBFS (pytest 7.2.0).

* Mon Feb 28 2022 Stanislav Levin <slev@altlinux.org> 1.4.0-alt1
- 1.3.0 -> 1.4.0.

* Wed Oct 14 2020 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- 1.1.3 -> 1.3.0.
- Stopped Python2 package build(Python2 EOL).

* Thu May 07 2020 Stanislav Levin <slev@altlinux.org> 1.1.3-alt1
- 1.0.2 -> 1.1.3.

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 1.0.2-alt2
- Fixed testing against Pytest 5.

* Sun Mar 17 2019 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1
- 1.0.1 -> 1.0.2.

* Wed Jan 16 2019 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1
- 0.2 -> 1.0.1.

* Fri Apr 13 2018 Stanislav Levin <slev@altlinux.org> 0.2-alt1
- Initial build for ALT.
