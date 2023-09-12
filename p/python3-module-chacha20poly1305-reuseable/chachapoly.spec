Name: python3-module-chacha20poly1305-reuseable
Version: 0.2.5
Release: alt2

Summary: ChaCha20Poly1305 that is reuseable for asyncio
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/chacha20poly1305-reuseable/

Source0: %name-%version-%release.tar
Source1: pyproject_deps.json

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-cov)
BuildRequires: python3(cryptography)

%description
%summary

%prep
%setup

%build
%pyproject_deps_resync_build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%python3_sitelibdir/chacha20poly1305_reuseable
%python3_sitelibdir/chacha20poly1305_reuseable-%version.dist-info

%changelog
* Tue Sep 12 2023 Grigory Ustinov <grenka@altlinux.org> 0.2.5-alt2
- fixed ftbfs

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.5-alt1
- 0.2.5 released

* Wed Nov 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.4-alt1
- 0.0.4 released

