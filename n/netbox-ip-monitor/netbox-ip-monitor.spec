Name:    netbox-ip-monitor
Version: 0.0.0
Release: alt1

Summary: Visual representation of IP addresses
License: Apache-2.0
Group:   Networking/WWW
URL:     https://github.com/Future998/netbox-ip-monitor

AutoReqProv: yes, nopython

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
Requires: netbox

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
* Tue Apr 01 2025 Alexander Burmatov <thatman@altlinux.org> 0.0.0-alt1
- Initial build for Sisyphus.
