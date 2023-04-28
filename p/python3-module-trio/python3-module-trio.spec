%define _unpackaged_files_terminate_build 1
%define pypi_name trio
%define modulename %pypi_name

%def_with check

Name: python3-module-%modulename
Version: 0.22.0
Release: alt3
Summary: Trio - Pythonic async I/O for humans and snake people
License: MIT or Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/trio/
Vcs: https://github.com/python-trio/trio
BuildArch: noarch
Source: %modulename-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter types-
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

# Self provides
%add_python3_req_skip _common simple_excepthook
# Only in ubuntu
%add_python3_req_skip apport_python_hook

%description
The Trio project's goal is to produce a production-quality, permissively
licensed, async/await-native I/O library for Python. Like all async libraries,
its main purpose is to help you write programs that do multiple things at the
same time with parallelized I/O.

%package tests
Summary: Tests for %modulename
Group: Development/Python3
Requires: %name = %EVR

%description tests
The Trio project's goal is to produce a production-quality, permissively
licensed, async/await-native I/O library for Python. Like all async libraries,
its main purpose is to help you write programs that do multiple things at the
same time with parallelized I/O.

This package contains tests for %modulename.

%prep
%setup -n %modulename-%version

# Upstream doesn't care about version
sed -i 's/0.21.0+dev/%version/' trio/_version.py

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile test-requirements.in
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -m 'not redistributors_should_skip'

%files
%doc README.*
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%modulename/tests
%exclude %python3_sitelibdir/%modulename/testing
%exclude %python3_sitelibdir/%modulename/_core/tests

%files tests
%python3_sitelibdir/%modulename/tests
%python3_sitelibdir/%modulename/testing
%python3_sitelibdir/%modulename/_core/tests

%changelog
* Thu Apr 27 2023 Stanislav Levin <slev@altlinux.org> 0.22.0-alt3
- Modernized packaging.
- Fixed FTBFS (setuptools 67.7.2).

* Wed Feb 08 2023 Grigory Ustinov <grenka@altlinux.org> 0.22.0-alt2
- Fixed packaging tests.

* Wed Feb 08 2023 Grigory Ustinov <grenka@altlinux.org> 0.22.0-alt1
- Automatically updated to 0.22.0.
- Bring tests back as separate subpackage.

* Mon Feb 14 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 0.19.0-alt1
- Updated to upstream version 0.19.0 to fix python-3.10 compatibility issues

* Tue Nov 10 2020 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt2
- don't pack tests (ALT bug 39239)

* Mon Jan 14 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.10.0-alt1
- Initial build for Sisyphus
