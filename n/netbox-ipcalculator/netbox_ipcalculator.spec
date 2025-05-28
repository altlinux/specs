Name:    netbox-ipcalculator
Version: 1.4.10
Release: alt1

Summary: IP Calculator plugin for Netbox
License: Apache-2.0
Group:   Networking/WWW
URL:     https://github.com/PieterL75/netbox_ipcalculator

AutoReqProv: yes, nopython

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
Requires: netbox >= 3.7.0

BuildArch: noarch

Source: %name-%version.tar
Source1: README

%description
Adds an IP Calculator to the views of
- Aggregate,
- Prefix,
- Ip Address.

%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/netbox
mkdir -p %buildroot%_datadir/netbox/netbox_ipcalculator
cp -r netbox_ipcalculator/* %buildroot%_datadir/netbox/netbox_ipcalculator
mkdir -p %buildroot%_defaultdocdir/netbox-ipcalculator
install -p -D -m 644 %SOURCE1 %buildroot%_defaultdocdir/netbox-ipcalculator/README

%files
%_datadir/netbox/netbox_ipcalculator
%_defaultdocdir/netbox-ipcalculator/README

%changelog
* Wed May 28 2025 Alexander Burmatov <thatman@altlinux.org> 1.4.10-alt1
- New 1.4.10 version.

* Fri May 16 2025 Alexander Burmatov <thatman@altlinux.org> 1.4.9-alt2
- Add required NetBox version.

* Fri Nov 08 2024 Alexander Burmatov <thatman@altlinux.org> 1.4.9-alt1
- New 1.4.9 version.

* Tue Aug 13 2024 Alexander Burmatov <thatman@altlinux.org> 1.4.8-alt1
- New 1.4.8 version.

* Thu Nov 09 2023 Alexander Burmatov <thatman@altlinux.org> 1.1-alt1
- Initial build for Sisyphus.
