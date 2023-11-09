Name:    netbox-topology-views
Version: 3.7.0
Release: alt1

Summary: A netbox plugin that draws topology views
License: Apache-2.0
Group:   Networking/WWW
URL:     https://github.com/mattieserver/netbox-topology-views

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

%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/netbox
mkdir -p %buildroot%_datadir/netbox/netbox_topology_views
cp -r netbox_topology_views/* %buildroot%_datadir/netbox/netbox_topology_views
mkdir -p %buildroot%_defaultdocdir/netbox-topology-views
install -p -D -m 644 %SOURCE1 %buildroot%_defaultdocdir/netbox-topology-views/README

%files
%_datadir/netbox/netbox_topology_views
%_defaultdocdir/netbox-topology-views/README

%changelog
* Thu Nov 09 2023 Alexander Burmatov <thatman@altlinux.org> 3.7.0-alt1
- Initial build for Sisyphus.