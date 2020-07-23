%define oname proxmoxer

Name: python3-module-%oname
Version: 1.1.1
Release: alt3

Summary: Wrapper around Proxmox REST API v2
License: %mit
Group: Development/Python3
Url: https://github.com/proxmoxer/proxmoxer
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch


BuildRequires(pre): rpm-build-licenses rpm-build-python3

BuildRequires: python3-module-requests
BuildRequires: python3-module-paramiko

Requires: python3-module-requests
Requires: python3-module-paramiko
Requires: python3-module-openssh-wrapper


%description
Pythonic API for a Proxmox cluster manipulation.

%prep
%setup -q -n %name-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*

%changelog
* Thu Jul 23 2020 Alexander Makeenkov <amakeenk@altlinux.org> 1.1.1-alt3
- Don't package tests

* Thu Jul 23 2020 Alexander Makeenkov <amakeenk@altlinux.org> 1.1.1-alt2
- Added conflicts with python3-module-pymta-tests and python3-module-m2r

* Thu Jul 16 2020 Alexander Makeenkov <amakeenk@altlinux.org> 1.1.1-alt1
- Updated to version 1.1.1
- Fixed url tag

* Fri Jan 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2-alt5
- Porting on Python3.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt4
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt3
- NMU: remove %ubt from release

* Fri Jun 08 2018 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.0.2-alt2%ubt
- Fixed the dependencies and a bogus `Provides: python2.7(tests)`.

* Tue May 29 2018 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.0.2-alt1%ubt
- Initial build for ALTLinux Sisyphus
