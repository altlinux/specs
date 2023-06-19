%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-mock

%def_with check

Name: python3-module-%pypi_name
Version: 3.11.1
Release: alt1
Summary: Thin-wrapper around the mock package for easier use with py.test
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-mock/
Vcs: https://github.com/pytest-dev/pytest-mock/
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
%py3_provides %pypi_name
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Thin-wrapper around the mock package for easier use with py.test

This plugin installs a mocker fixture which is a thin-wrapper around the
patching API provided by the mock package, but with the benefit of not having
to worry about undoing patches at the end of a test

%prep
%setup
%patch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore tests

%files
%doc CHANGELOG.rst README.rst
%python3_sitelibdir/pytest_mock/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Jun 16 2023 Stanislav Levin <slev@altlinux.org> 3.11.1-alt1
- 3.10.0 -> 3.11.1.

* Thu Oct 06 2022 Stanislav Levin <slev@altlinux.org> 3.10.0-alt1
- 3.9.0 -> 3.10.0.

* Fri Sep 30 2022 Stanislav Levin <slev@altlinux.org> 3.9.0-alt1
- 3.8.2 -> 3.9.0.

* Wed Jul 20 2022 Stanislav Levin <slev@altlinux.org> 3.8.2-alt1
- 3.7.0 -> 3.8.2.

* Fri Mar 18 2022 Stanislav Levin <slev@altlinux.org> 3.7.0-alt2
- Fixed FTBFS (Pytest 7.1.1).

* Thu Feb 03 2022 Stanislav Levin <slev@altlinux.org> 3.7.0-alt1
- 3.5.1 -> 3.7.0.

* Mon Apr 19 2021 Stanislav Levin <slev@altlinux.org> 3.5.1-alt1
- 3.3.1 -> 3.5.1.

* Mon Sep 07 2020 Stanislav Levin <slev@altlinux.org> 3.3.1-alt1
- 1.10.4 -> 3.3.1.

* Mon Jun 10 2019 Stanislav Levin <slev@altlinux.org> 1.10.4-alt2
- Added missing dep on Pytest.

* Fri May 31 2019 Stanislav Levin <slev@altlinux.org> 1.10.4-alt1
- 1.10.1 -> 1.10.4.

* Sun Mar 17 2019 Stanislav Levin <slev@altlinux.org> 1.10.1-alt1
- 1.10.0 -> 1.10.1.

* Sun Oct 21 2018 Stanislav Levin <slev@altlinux.org> 1.10.0-alt1
- 1.9.0 -> 1.10.0.

* Thu Apr 12 2018 Stanislav Levin <slev@altlinux.org> 1.9.0-alt1
- 1.6.2 -> 1.9.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.6.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.2-alt1
- Updated to upstream version 1.6.2.

* Sat Jan 21 2017 Anton Midyukov <antohami@altlinux.org> 1.5.0-alt1
- Initial build for ALT Linux Sisyphus.
