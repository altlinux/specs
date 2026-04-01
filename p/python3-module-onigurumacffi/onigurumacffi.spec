%define _unpackaged_files_terminate_build 1
%define pypi_name onigurumacffi

%def_with check

Name: python3-module-%pypi_name
Version: 1.5.0
Release: alt1

Summary: python cffi bindings for the oniguruma regex engine
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/onigurumacffi
Vcs: https://github.com/asottile/onigurumacffi

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools
BuildRequires: liboniguruma-devel

%if_with check
BuildRequires: python3-module-covdefaults
BuildRequires: python3-module-coverage
BuildRequires: python3-module-pytest
BuildRequires: python3-module-cffi
%endif

%description
python cffi bindings for the oniguruma regex engine

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
%python3_sitelibdir/%pypi_name.py
%python3_sitelibdir/_%pypi_name.abi3.so
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Apr 01 2026 Vladislav Glinkin <smasher@altlinux.org> 1.5.0-alt1
- New version

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.4.1-alt1.1
- Demodernized packaging.

* Fri Mar 21 2025 Vladislav Glinkin <smasher@altlinux.org> 1.4.1-alt1
- Updated to 1.4.1

* Sun Nov 05 2023 Vladislav Glinkin <smasher@altlinux.org> 1.3.0-alt1
- Updated to 1.3.0

* Sat Sep 02 2023 Vladislav Glinkin <smasher@altlinux.org> 1.2.0-alt1
- Initial build for ALT

