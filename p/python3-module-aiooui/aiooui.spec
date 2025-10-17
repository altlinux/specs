Name: python3-module-aiooui
Version: 0.1.9
Release: alt1

Summary: Async OUI lookups
License: MIT
Group: Development/Python
Url: https://pypi.org/project/aiooui
VCS: https://github.com/bluetooth-devices/aiooui

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
%python3_sitelibdir/aiooui
%python3_sitelibdir/aiooui-%version.dist-info

%changelog
* Fri Oct 17 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.1.9-alt1
- 0.1.9 released

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.1.7-alt1
- 0.1.7 released

* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.1.6-alt1
- 0.1.6 released

* Wed Mar 13 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.5-alt1
- 0.1.5 released
