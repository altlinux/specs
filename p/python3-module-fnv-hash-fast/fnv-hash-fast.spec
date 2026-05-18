Name: python3-module-fnv-hash-fast
Version: 2.0.3
Release: alt1

Summary: A fast version of fnv1a
License: MIT
Group: Development/Python
URL: https://pypi.org/project/fnv-hash-fast
VCS: https://github.com/bluetooth-devices/fnv-hash-fast

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_poetry dev

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/fnv_hash_fast
%python3_sitelibdir/fnv_hash_fast-%version.dist-info

%changelog
* Mon May 18 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.3-alt1
- 2.0.3 released

* Tue Mar 17 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.2-alt1
- 2.0.2 released

* Wed Oct 15 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.6.0-alt1
- 1.6.0 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.2-alt1
- 1.0.2 released

* Fri Nov 03 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.0-alt1
- 0.5.0 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt1
- 0.4.1 released

* Fri May 05 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.1-alt1
- 0.3.1 released
