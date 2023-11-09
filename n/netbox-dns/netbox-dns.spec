Name:    netbox-dns
Version: 0.20.2
Release: alt1

Summary: NetBox DNS is a NetBox plugin for managing DNS data
License: MIT
Group:   Networking/WWW
URL:     https://github.com/peteeckel/netbox-plugin-dns

AutoReqProv: yes, nopython

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
Requires: netbox

BuildArch: noarch

Source: %name-%version.tar
Source1: README

%description
NetBox DNS is a NetBox plugin for managing DNS views, zones, name servers
and records.

%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/netbox
mkdir -p %buildroot%_datadir/netbox/netbox_dns
cp -r netbox_dns/* %buildroot%_datadir/netbox/netbox_dns
mkdir -p %buildroot%_defaultdocdir/netbox-dns
install -p -D -m 644 %SOURCE1 %buildroot%_defaultdocdir/netbox-dns/README

%files
%_datadir/netbox/netbox_dns
%_defaultdocdir/netbox-dns/README

%changelog
* Fri Nov 10 2023 Alexander Burmatov <thatman@altlinux.org> 0.20.2-alt1
- Initial build for Sisyphus.
