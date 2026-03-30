%define _unpackaged_files_terminate_build 1
%define modulename outcome

%def_with check

Name: python3-module-%modulename
Version: 1.3.0
Release: alt1.1
Summary: Capture the outcome of Python function calls
License: MIT or Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/outcome/
Vcs: https://github.com/python-trio/outcome
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-cov

BuildRequires: python3-module-attrs
%endif

%description
Capture the outcome of Python function calls. Extracted from the Trio project.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra tests

%files
%doc README.*
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%{pyproject_distinfo %modulename}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt1.1
- Demodernized packaging.

* Sat Oct 21 2023 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt1
- Automatically updated to 1.3.0.

* Mon Apr 24 2023 Stanislav Levin <slev@altlinux.org> 1.2.0-alt2
- Modernized packaging.
- Fixed FTBFS (pytest 7.3.1).

* Wed Feb 08 2023 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt1
- Automatically updated to 1.2.0.
- Build with check.

* Tue Jan 15 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
