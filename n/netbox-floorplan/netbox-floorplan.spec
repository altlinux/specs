Name:    netbox-floorplan
Version: 0.2
Release: alt1

Summary: A netbox plugin providing floorplan mapping capability for locations and sites
License: LGPL-3.0
Group:   Networking/WWW
URL:     https://github.com/tbotnz/netbox_floorplan

AutoReqProv: yes, nopython

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
Requires: netbox

BuildArch: noarch

Source: %name-%version.tar
Source1: README

%description
A netbox plugin providing floorplan mapping capability for locations and sites
- provides graphical ability to draw racks & unracked devices on a floorplan
- support for metadata such as labels, areas, walls, coloring
- floorplan object mapped to sites or locations and click through rack/devices
- keyboard controls supported
- export to svg

%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/netbox
mkdir -p %buildroot%_datadir/netbox/netbox_floorplan
cp -r netbox_floorplan/* %buildroot%_datadir/netbox/netbox_floorplan
mkdir -p %buildroot%_defaultdocdir/netbox-floorplan
install -p -D -m 644 %SOURCE1 %buildroot%_defaultdocdir/netbox-floorplan/README

%files
%_datadir/netbox/netbox_floorplan
%_defaultdocdir/netbox-floorplan/README

%changelog
* Fri Nov 10 2023 Alexander Burmatov <thatman@altlinux.org> 0.2-alt1
- Initial build for Sisyphus.
