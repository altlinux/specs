Name: python3-module-chacha20poly1305-reuseable
Version: 0.13.2
Release: alt1

Summary: ChaCha20Poly1305 that is reuseable for asyncio
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/chacha20poly1305-reuseable/

Source0: %name-%version-%release.tar
Source1: pyproject_deps.json

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
%pyproject_run_pytest tests

%files
%python3_sitelibdir/chacha20poly1305_reuseable
%python3_sitelibdir/chacha20poly1305_reuseable-%version.dist-info

%changelog
* Wed Jul 24 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.13.2-alt1
- 0.13.2 released

* Fri Jan 26 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12.0-alt1
- 0.12.0 released

* Tue Sep 12 2023 Grigory Ustinov <grenka@altlinux.org> 0.2.5-alt2
- fixed ftbfs

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.5-alt1
- 0.2.5 released

* Wed Nov 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.4-alt1
- 0.0.4 released

