%add_python3_lib_path %_libexecdir/UDSClient
%allow_python3_import_path %_libexecdir/UDSClient

Name: openuds-client
Version: 3.6.0
Release: alt1
Summary: Client for Universal Desktop Services (UDS) Broker
License: BSD-3-Clause
Group: Networking/Remote access
URL: https://github.com/dkmstr/openuds
Provides: udsclient = %EVR

Source0: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-xdg rpm-build-python3
Requires: /usr/bin/xfreerdp
Requires: /usr/bin/x2goclient
Requires: /usr/bin/remote-viewer
%py3_requires paramiko
%py3_requires Crypto

%description
This package provides the required components
to allow connection to services offered by UDS Broker.

%prep
%setup

sed -i 's|#!/usr/bin/env python3|#!/usr/bin/python3|' \
    $(find . -name '*.py')

%install
pushd linux
%makeinstall_std
popd

%files
%_libexecdir/UDSClient
%_desktopdir/UDSClient.desktop

%changelog
* Thu May 25 2023 Alexander Burmatov <thatman@altlinux.org> 3.6.0-alt1
- v3.6 snapshot 0363ac3a6acc31582f2f70c0801250f976518e44

* Mon Aug 22 2022 Alexey Shabalin <shaba@altlinux.org> 3.5.0-alt1
- v3.5 snapshot 83394f0d34daf18722923be8d57b35627b330121

* Wed Sep 15 2021 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt4
- Run usbip-export to redirect USB devices before connect to session.

* Sat Aug 21 2021 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt3
- v3.0 snapshot 51b0cec5365698dffdb9a3a468d52bbba4656ba4

* Fri Jul 09 2021 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt2
- Update requires

* Thu Nov 05 2020 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt1
- 3.0.0 Release

* Tue Apr 14 2020 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt0.1.git.d7e30d14
- Initial build for ALT

