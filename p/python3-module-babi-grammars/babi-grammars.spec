%define _unpackaged_files_terminate_build 1
%define pypi_name babi-grammars

# %check is disabled because python3-module-cson not packaged
%def_without check

Name: python3-module-%pypi_name
Version: 0.0.62
Release: alt1.1

Summary: grammars for babi
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/babi-grammars/
Vcs: https://github.com/asottile/babi-grammars

BuildArch: noarch
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-babi
BuildRequires: python3-module-cson
%endif

%description
grammars for babi

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md LICENSE
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/babi_grammars.py
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%_datadir/babi/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.0.62-alt1.1
- Demodernized packaging.

* Wed Aug 20 2025 Vladislav Glinkin <smasher@altlinux.org> 0.0.62-alt1
- 0.0.61 -> 0.0.62

* Fri Mar 21 2025 Vladislav Glinkin <smasher@altlinux.org> 0.0.61-alt1
- 0.0.57 -> 0.0.61

* Thu Oct 31 2024 Vladislav Glinkin <smasher@altlinux.org> 0.0.57-alt1
- 0.0.54 -> 0.0.57

* Sun Nov 05 2023 Vladislav Glinkin <smasher@altlinux.org> 0.0.54-alt1
- Updated to 0.0.54

* Wed Aug 30 2023 Vladislav Glinkin <smasher@altlinux.org> 0.0.52-alt1
- Initial build for ALT

