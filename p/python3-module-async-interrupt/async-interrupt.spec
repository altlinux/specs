Name: python3-module-async-interrupt
Version: 1.2.2
Release: alt1

Summary: Interrupt context manager for asyncio. 
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/async-interrupt
VCS: https://github.com/bluetooth-devices/async_interrupt

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
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
%doc LICENSE* README*
%python3_sitelibdir/async_interrupt
%python3_sitelibdir/async_interrupt-%version.dist-info

%changelog
* Fri Oct 17 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.2.2-alt1
- 1.2.2 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.2.0-alt1
- 1.2.0 released

* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.2-alt1
- 1.1.2 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.1-alt1
- 1.1.1 released

