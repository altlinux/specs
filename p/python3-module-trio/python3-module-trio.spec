%define _unpackaged_files_terminate_build 1
%define pypi_name trio
%define modulename %pypi_name

%def_with check

Name: python3-module-%modulename
Version: 0.23.1
Release: alt1
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
%pyproject_builddeps_metadata
BuildRequires: /proc
BuildRequires: python3-module-pytest
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

%build
%pyproject_build

%install
%pyproject_install

%check
# see ci.sh for details
%pyproject_run_pytest -ra \
    -p trio._tests.pytest_plugin \
    --skip-optional-imports \
    -m 'not redistributors_should_skip' \

%files
%doc README.*
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%modulename/_tests
%exclude %python3_sitelibdir/%modulename/testing
%exclude %python3_sitelibdir/%modulename/_core/_tests
%exclude %python3_sitelibdir/%modulename/tests.py
%exclude %python3_sitelibdir/%modulename/__pycache__/tests.*

%files tests
%python3_sitelibdir/%modulename/_tests
%python3_sitelibdir/%modulename/testing
%python3_sitelibdir/%modulename/_core/_tests
%python3_sitelibdir/%modulename/tests.py
%python3_sitelibdir/%modulename/__pycache__/tests.*

%changelog
* Tue Nov 07 2023 Stanislav Levin <slev@altlinux.org> 0.23.1-alt1
- 0.22.0 -> 0.23.1.

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
