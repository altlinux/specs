Name: python3-module-atomicwrites
Version: 1.4.1
Release: alt2

Summary: Python Atomic file writes on POSIX
License: MIT
Group: Development/Python3
# Source-git: https://github.com/untitaker/python-atomicwrites.git
Url: https://pypi.org/project/atomicwrites

Source: %name-%version.tar

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(pytest)

BuildArch: noarch

%description
This module provides atomic file writes on POSIX operating systems.
It supports:
* Race-free assertion that the target file doesn't yet exist
* Simple high-level API that wraps a very flexible class-based AP
* Consistent error handling across platforms

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%doc LICENSE README.rst
%python3_sitelibdir/atomicwrites
%python3_sitelibdir/atomicwrites-%version.dist-info

%changelog
* Tue Jan 30 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.1-alt2
- cleaned up check section

* Thu May 11 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Tue Feb 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Mon Aug 02 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt4
- Drop python2 support.

* Tue Sep 08 2020 Stanislav Levin <slev@altlinux.org> 1.3.0-alt3
- Disabled tests against Python2.

* Tue Aug 06 2019 Stanislav Levin <slev@altlinux.org> 1.3.0-alt2
- Fixed testing against Pytest 5.

* Mon Feb 11 2019 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- 1.2.1 -> 1.3.0.

* Tue Oct 09 2018 Stanislav Levin <slev@altlinux.org> 1.2.1-alt1
- 1.2.0 -> 1.2.1.

* Thu Aug 30 2018 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- 1.1.5 -> 1.2.0.

* Mon Aug 20 2018 Stanislav Levin <slev@altlinux.org> 1.1.5-alt1
- Initial build.

