%define pypi_name trio

%def_with check

Name: python3-module-%pypi_name
Version: 0.26.2
Release: alt1
Summary: Trio - Pythonic async I/O for humans and snake people
License: MIT or Apache-2.0
Group: Development/Python3
URL: https://pypi.org/project/trio
VCS: https://github.com/python-trio/trio
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: /proc
BuildRequires: python3-module-pytest
BuildRequires: python3-module-attrs
BuildRequires: python3-module-sniffio
BuildRequires: python3-module-outcome
BuildRequires: python3-module-sortedcontainers
BuildRequires: python3-module-idna
# these are optional
BuildRequires: python3-module-trustme
BuildRequires: python3-module-astor
BuildRequires: python3-module-openssl
BuildRequires: python3-module-isort
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
Summary: Tests for %pypi_name
Group: Development/Python3
Requires: %name = %EVR

%description tests
The Trio project's goal is to produce a production-quality, permissively
licensed, async/await-native I/O library for Python. Like all async libraries,
its main purpose is to help you write programs that do multiple things at the
same time with parallelized I/O.

This package contains tests for %pypi_name.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# see ci.sh for details
%pyproject_run_pytest -ra \
    --pyargs trio --verbose \
    -p trio._tests.pytest_plugin \
    --skip-optional-imports \
    -m 'not redistributors_should_skip' \

%files
%doc README.*
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%exclude %python3_sitelibdir/%pypi_name/_tests
%exclude %python3_sitelibdir/%pypi_name/testing
%exclude %python3_sitelibdir/%pypi_name/_core/_tests

%files tests
%python3_sitelibdir/%pypi_name/_tests
%python3_sitelibdir/%pypi_name/testing
%python3_sitelibdir/%pypi_name/_core/_tests

%changelog
* Wed Aug 21 2024 Grigory Ustinov <grenka@altlinux.org> 0.26.2-alt1
- Automatically updated to 0.26.2.

* Tue Jul 23 2024 Grigory Ustinov <grenka@altlinux.org> 0.26.0-alt1
- Automatically updated to 0.26.0.

* Thu May 16 2024 Grigory Ustinov <grenka@altlinux.org> 0.25.1-alt1
- Automatically updated to 0.25.1.

* Mon Apr 01 2024 Grigory Ustinov <grenka@altlinux.org> 0.25.0-alt1
- Automatically updated to 0.25.0.

* Wed Jan 24 2024 Grigory Ustinov <grenka@altlinux.org> 0.24.0-alt1
- Automatically updated to 0.24.0.
- Fixed cringe obninsk-style packaging.

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
