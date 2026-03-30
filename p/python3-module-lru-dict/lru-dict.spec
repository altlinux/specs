Name: python3-module-lru-dict
Version: 1.5.0
Release: alt1

Summary: Fast LRU dict implementation
License: MIT
Group: Development/Python
URL: https://pypi.org/project/lru-dict
VCS: https://github.com/amitdev/lru-dict

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest test

%files
%python3_sitelibdir/lru
%python3_sitelibdir/lru_dict-%version.dist-info

%changelog
* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.5.0-alt1
- 1.5.0 released

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.4.0-alt1.1
- Demodernized packaging.

* Fri Sep 19 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.4.0-alt1
- 1.4.0 released

* Fri Jan 19 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt1
- 1.3.0 released

* Fri Jul 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt1
- 1.2.0 released

* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.8-alt1
- 1.1.8 released

* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.7-alt1
- initial
