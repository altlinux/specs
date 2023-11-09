Name:    netbox-proxbox
Version: 0.0.5
Release: alt1

Summary: Netbox Plugin for integration between Proxmox and Netbox
License: Apache-2.0
Group:   Networking/WWW
URL:     https://github.com/netdevopsbr/netbox-proxbox

AutoReqProv: yes, nopython

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-poetry
Requires: netbox
Requires: python3-module-pynetbox
Requires: python3-module-proxmoxer

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
* Thu Nov 09 2023 Alexander Burmatov <thatman@altlinux.org> 0.0.5-alt1
- Initial build for Sisyphus.