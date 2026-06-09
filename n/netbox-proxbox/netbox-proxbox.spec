Name:    netbox-proxbox
Version: 0.0.20.post1
Release: alt1

Summary: Netbox Plugin for integration between Proxmox and Netbox
License: Apache-2.0
Group:   Networking/WWW
URL:     https://github.com/emersonfelipesp/netbox-proxbox

AutoReqProv: yes, nopython

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
Requires: netbox >= 4.5.8
Requires: python3-module-pydantic
Requires: python3-module-requests
Requires: python3-module-websockets
Conflicts: netbox > 4.6.99

BuildArch: noarch

Source: %name-%version.tar
Source1: README

%description
%summary.

%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/netbox
mkdir -p %buildroot%_datadir/netbox/netbox_proxbox
cp -r netbox_proxbox/* %buildroot%_datadir/netbox/netbox_proxbox
mkdir -p %buildroot%_defaultdocdir/netbox-proxbox
install -p -D -m 644 %SOURCE1 %buildroot%_defaultdocdir/netbox-proxbox/README


%files
%_datadir/netbox/netbox_proxbox
%_defaultdocdir/netbox-proxbox/README

%changelog
* Mon Jun 08 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.20.post1-alt1
- New 0.0.20.post1 version.

* Thu May 28 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.18-alt1
- New 0.0.18 version.

* Fri May 08 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.14-alt1
- New 0.0.14 version.

* Tue Apr 28 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.12-alt1
- New 0.0.12 version.

* Fri Apr 17 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.11-alt1
- New 0.0.11 version.

* Fri May 16 2025 Alexander Burmatov <thatman@altlinux.org> 0.0.5-alt2
- Add compatable Netbox versions.

* Thu Nov 09 2023 Alexander Burmatov <thatman@altlinux.org> 0.0.5-alt1
- Initial build for Sisyphus.
