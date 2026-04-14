Name:    netbox-topology-views
Version: 4.5.1
Release: alt1

Summary: A netbox plugin that draws topology views
License: Apache-2.0
Group:   Networking/WWW
URL:     https://github.com/mattieserver/netbox-topology-views

AutoReqProv: yes, nopython

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
Requires: netbox >= 4.5.0

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
* Tue Apr 14 2026 Alexander Burmatov <thatman@altlinux.org> 4.5.1-alt1
- New 4.5.1 version.

* Tue Jan 13 2026 Alexander Burmatov <thatman@altlinux.org> 4.5.0-alt1
- New 4.5.0 version.

* Wed Oct 15 2025 Alexander Burmatov <thatman@altlinux.org> 4.4.0-alt1
- New 4.4.0 version.

* Thu Aug 07 2025 Alexander Burmatov <thatman@altlinux.org> 4.3.0-alt2
- Branch p11 was merged.

* Sat Jun 07 2025 Alexander Burmatov <thatman@altlinux.org> 4.3.0-alt1
- New 4.3.0 version.

* Tue Mar 25 2025 Alexander Burmatov <thatman@altlinux.org> 4.2.1-alt1
- New 4.2.1 version.

* Thu Jan 30 2025 Alexander Burmatov <thatman@altlinux.org> 4.2.0-alt1
- New 4.2.0 version.

* Thu Nov 07 2024 Alexander Burmatov <thatman@altlinux.org> 4.1.0-alt1
- New 4.1.0 version.

* Mon Aug 12 2024 Alexander Burmatov <thatman@altlinux.org> 4.0.0-alt1
- New 4.0.0 version.

* Mon May 20 2024 Alexander Burmatov <thatman@altlinux.org> 3.9.1-alt1
- New 3.9.1 version.

* Tue Mar 26 2024 Alexander Burmatov <thatman@altlinux.org> 3.9.0-alt1
- New 3.9.0 version.

* Thu Nov 09 2023 Alexander Burmatov <thatman@altlinux.org> 3.7.0-alt1
- Initial build for Sisyphus.
