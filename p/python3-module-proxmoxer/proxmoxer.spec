%define oname proxmoxer

Name: python3-module-%oname
Version: 1.0.2
Release: alt5

Summary: Wrapper around Proxmox REST API v2
License: %mit
Group: Development/Python3
Url: https://github.com/swayf/proxmoxer
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

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description tests
Pythonic API for a Proxmox cluster manipulation.

This package contains tests for %oname.

%prep
%setup -q -n %name-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests/

%files tests
%python3_sitelibdir/tests/


%changelog
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
