Name:    netbox-ipcalculator
Version: 1.4.8
Release: alt1

Summary: IP Calculator plugin for Netbox
License: Apache-2.0
Group:   Networking/WWW
URL:     https://github.com/PieterL75/netbox_ipcalculator

AutoReqProv: yes, nopython

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
Requires: netbox

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
* Tue Aug 13 2024 Alexander Burmatov <thatman@altlinux.org> 1.4.8-alt1
- New 1.4.8 version.

* Thu Nov 09 2023 Alexander Burmatov <thatman@altlinux.org> 1.1-alt1
- Initial build for Sisyphus.
