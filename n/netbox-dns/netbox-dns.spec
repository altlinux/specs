Name:    netbox-dns
Version: 1.0.5
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
* Tue Aug 13 2024 Alexander Burmatov <thatman@altlinux.org> 1.0.5-alt1
- New 1.0.5 version.

* Mon May 20 2024 Alexander Burmatov <thatman@altlinux.org> 0.22.9-alt1
- New 0.22.9 version.

* Tue Mar 26 2024 Alexander Burmatov <thatman@altlinux.org> 0.22.6-alt1
- New 0.22.6 version.

* Fri Nov 10 2023 Alexander Burmatov <thatman@altlinux.org> 0.20.2-alt1
- Initial build for Sisyphus.
