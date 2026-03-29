Name: python3-module-propcache
Version: 0.4.1
Release: alt1.1

Summary: Fast implementation of cached properties
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/propcache
VCS: https://github.com/aio-libs/propcache

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-expandvars
BuildRequires: python3-module-Cython

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/propcache
%python3_sitelibdir/propcache-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.4.1-alt1.1
- Demodernized packaging.

* Wed Oct 15 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.4.1-alt1
- 0.4.1 released

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.1-alt1
- 0.2.1 released

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.0-alt1
- 0.2.0 released
