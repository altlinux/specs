%define _unpackaged_files_terminate_build 1
%define pypi_name filelock

%def_with check

Name: python3-module-%pypi_name
Version: 3.16.1
Release: alt1
Summary: A platform independent file lock for Python
License: Unlicense
Group: Development/Python3
Url: https://pypi.org/project/filelock/
VCS: https://github.com/tox-dev/py-filelock
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%add_pyproject_deps_check_filter diff-cover
%pyproject_builddeps_metadata_extra testing
%endif

%description
This package contains a single module, which implements a platform independent
file locking mechanism for Python.

The lock includes a lock counter and is thread safe. This means, when locking
the same lock object twice, it will not block.

%prep
%setup
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra tests

%files
%doc README.md
%python3_sitelibdir/filelock/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Sep 18 2024 Stanislav Levin <slev@altlinux.org> 3.16.1-alt1
- 3.16.0 -> 3.16.1.

* Tue Sep 10 2024 Stanislav Levin <slev@altlinux.org> 3.16.0-alt1
- 3.15.4 -> 3.16.0.

* Mon Jun 24 2024 Stanislav Levin <slev@altlinux.org> 3.15.4-alt1
- 3.15.3 -> 3.15.4.

* Thu Jun 20 2024 Stanislav Levin <slev@altlinux.org> 3.15.3-alt1
- 3.14.0 -> 3.15.3.

* Thu May 02 2024 Stanislav Levin <slev@altlinux.org> 3.14.0-alt1
- 3.13.4 -> 3.14.0.

* Wed Apr 10 2024 Stanislav Levin <slev@altlinux.org> 3.13.4-alt1
- 3.13.3 -> 3.13.4.

* Tue Mar 26 2024 Stanislav Levin <slev@altlinux.org> 3.13.3-alt1
- 3.13.1 -> 3.13.3.

* Wed Nov 01 2023 Stanislav Levin <slev@altlinux.org> 3.13.1-alt1
- 3.12.2 -> 3.13.1.

* Tue Jun 13 2023 Stanislav Levin <slev@altlinux.org> 3.12.2-alt1
- 3.12.0 -> 3.12.2.

* Fri Apr 21 2023 Stanislav Levin <slev@altlinux.org> 3.12.0-alt1
- 3.9.0 -> 3.12.0.

* Wed Feb 01 2023 Stanislav Levin <slev@altlinux.org> 3.9.0-alt1
- 3.8.2 -> 3.9.0.

* Tue Dec 06 2022 Stanislav Levin <slev@altlinux.org> 3.8.2-alt1
- 3.8.1 -> 3.8.2.

* Mon Dec 05 2022 Stanislav Levin <slev@altlinux.org> 3.8.1-alt1
- 3.8.0 -> 3.8.1.

* Wed Aug 10 2022 Stanislav Levin <slev@altlinux.org> 3.8.0-alt1
- 3.6.0 -> 3.8.0.

* Fri Mar 04 2022 Stanislav Levin <slev@altlinux.org> 3.6.0-alt1
- 3.4.2 -> 3.6.0.

* Wed Jan 12 2022 Stanislav Levin <slev@altlinux.org> 3.4.2-alt1
- 3.3.2 -> 3.4.2.

* Tue Nov 02 2021 Stanislav Levin <slev@altlinux.org> 3.3.2-alt1
- 3.3.1 -> 3.3.2.

* Mon Oct 25 2021 Stanislav Levin <slev@altlinux.org> 3.3.1-alt1
- 3.0.10 -> 3.3.1.

* Sun Jul 25 2021 Grigory Ustinov <grenka@altlinux.org> 3.0.10-alt2
- Drop python2 support.

* Mon Jan 14 2019 Stanislav Levin <slev@altlinux.org> 3.0.10-alt1
- 3.0.9 -> 3.0.10.

* Wed Oct 10 2018 Stanislav Levin <slev@altlinux.org> 3.0.9-alt1
- Initial build.

