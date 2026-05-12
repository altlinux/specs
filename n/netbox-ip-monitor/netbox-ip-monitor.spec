Name:    netbox-ip-monitor
Version: 0.1.5
Release: alt1

Summary: Visual representation of IP addresses
License: Apache-2.0
Group:   Networking/WWW
URL:     https://github.com/Future998/netbox-ip-monitor

AutoReqProv: yes, nopython

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
Requires: netbox >= 4.3.0

BuildArch: noarch

Source: %name-%version.tar
Source1: README

%description
%summary.
IP monitor to display all IP addresses in a prefix.

%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/netbox
mkdir -p %buildroot%_datadir/netbox/netbox_ip_monitor
cp -r netbox_ip_monitor/* %buildroot%_datadir/netbox/netbox_ip_monitor
mkdir -p %buildroot%_defaultdocdir/%name
install -p -D -m 644 %SOURCE1 %buildroot%_defaultdocdir/%name/README

%files
%_datadir/netbox/netbox_ip_monitor
%_defaultdocdir/%name/README

%changelog
* Fri May 08 2026 Alexander Burmatov <thatman@altlinux.org> 0.1.5-alt1
- Update version to 0.1.5.

* Thu Feb 19 2026 Alexander Burmatov <thatman@altlinux.org> 0.1.4-alt1
- Update version to 0.1.4.

* Tue Jan 13 2026 Alexander Burmatov <thatman@altlinux.org> 0.1.3-alt1
- Update version to 0.1.3.

* Fri Oct 31 2025 Alexander Burmatov <thatman@altlinux.org> 0.1.2-alt1
- Update version to 0.1.2.

* Thu Sep 04 2025 Alexander Burmatov <thatman@altlinux.org> 0.1.1-alt1
- Update version to 0.1.1.

* Tue Jul 01 2025 Alexander Burmatov <thatman@altlinux.org> 0.1.0-alt1
- Update version to 0.1.0.

* Fri May 16 2025 Alexander Burmatov <thatman@altlinux.org> 0.0.1-alt2
- Add required NetBox version.

* Mon May 12 2025 Alexander Burmatov <thatman@altlinux.org> 0.0.1-alt1
- Update version to 0.0.1.

* Tue Apr 01 2025 Alexander Burmatov <thatman@altlinux.org> 0.0.0-alt1
- Initial build for Sisyphus.
