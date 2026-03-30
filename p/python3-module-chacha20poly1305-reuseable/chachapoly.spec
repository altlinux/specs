%def_with check

Name: python3-module-chacha20poly1305-reuseable
Version: 0.13.2
Release: alt1.1

Summary: ChaCha20Poly1305 that is reuseable for asyncio
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/chacha20poly1305-reuseable/

Source0: %name-%version-%release.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-poetry-core

%if_with check
BuildRequires: python3-module-cryptography
%endif

%description
%summary

%prep
%setup

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
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.13.2-alt1.1
- Demodernized packaging.

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

