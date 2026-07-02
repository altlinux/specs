Name:    netbox-dns
Version: 1.5.10
Release: alt1

Summary: NetBox DNS is a NetBox plugin for managing DNS data
License: MIT
Group:   Networking/WWW
URL:     https://github.com/peteeckel/netbox-plugin-dns

AutoReqProv: yes, nopython

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
Requires: netbox >= 4.5.0
Requires: python3-module-dns

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
* Thu Jul 02 2026 Alexander Burmatov <thatman@altlinux.org> 1.5.10-alt1
- New 1.5.10 version.

* Mon Jun 08 2026 Alexander Burmatov <thatman@altlinux.org> 1.5.9-alt1
- New 1.5.9 version.

* Fri May 08 2026 Alexander Burmatov <thatman@altlinux.org> 1.5.8-alt1
- New 1.5.8 version.

* Thu Apr 16 2026 Alexander Burmatov <thatman@altlinux.org> 1.5.7-alt1
- New 1.5.7 version.

* Tue Apr 14 2026 Alexander Burmatov <thatman@altlinux.org> 1.5.6-alt1
- New 1.5.6 version.

* Wed Mar 18 2026 Alexander Burmatov <thatman@altlinux.org> 1.5.5-alt1
- New 1.5.5 version.

* Wed Mar 18 2026 Alexander Burmatov <thatman@altlinux.org> 1.5.4-alt1
- New 1.5.4 version.

* Wed Mar 04 2026 Alexander Burmatov <thatman@altlinux.org> 1.5.3-alt1
- New 1.5.3 version.

* Wed Feb 18 2026 Alexander Burmatov <thatman@altlinux.org> 1.5.2-alt1
- New 1.5.2 version.

* Wed Jan 21 2026 Alexander Burmatov <thatman@altlinux.org> 1.5.1-alt1
- New 1.5.1 version.

* Tue Jan 13 2026 Alexander Burmatov <thatman@altlinux.org> 1.5.0-alt1
- New 1.5.0 version.

* Tue Jan 13 2026 Alexander Burmatov <thatman@altlinux.org> 1.4.7-alt1
- New 1.4.7 version.

* Wed Dec 24 2025 Alexander Burmatov <thatman@altlinux.org> 1.4.6-alt1
- New 1.4.6 version.

* Wed Dec 17 2025 Alexander Burmatov <thatman@altlinux.org> 1.4.5-alt1
- New 1.4.5 version.

* Mon Nov 24 2025 Alexander Burmatov <thatman@altlinux.org> 1.4.4-alt1
- New 1.4.4 version.

* Thu Oct 30 2025 Alexander Burmatov <thatman@altlinux.org> 1.4.3-alt1
- New 1.4.3 version.

* Mon Oct 06 2025 Alexander Burmatov <thatman@altlinux.org> 1.4.2-alt1
- New 1.4.2 version.

* Mon Sep 08 2025 Alexander Burmatov <thatman@altlinux.org> 1.4.1-alt1
- New 1.4.1 version.

* Wed Sep 03 2025 Alexander Burmatov <thatman@altlinux.org> 1.4.0-alt1
- New 1.4.0 version.

* Wed Aug 27 2025 Alexander Burmatov <thatman@altlinux.org> 1.3.6-alt1
- New 1.3.6 version.

* Mon Jul 28 2025 Alexander Burmatov <thatman@altlinux.org> 1.3.5-alt1
- New 1.3.5 version.

* Tue Jul 01 2025 Alexander Burmatov <thatman@altlinux.org> 1.3.4-alt1
- New 1.3.4 version.

* Mon Jun 30 2025 Alexander Burmatov <thatman@altlinux.org> 1.3.3-alt1
- New 1.3.3 version.

* Wed May 28 2025 Alexander Burmatov <thatman@altlinux.org> 1.3.2-alt1
- New 1.3.2 version.

* Fri May 16 2025 Alexander Burmatov <thatman@altlinux.org> 1.3.1-alt1
- New 1.3.1 version.

* Mon May 12 2025 Alexander Burmatov <thatman@altlinux.org> 1.3.0-alt1
- New 1.3.0 version.

* Mon May 12 2025 Alexander Burmatov <thatman@altlinux.org> 1.2.11-alt1
- New 1.2.11 version.

* Mon Apr 28 2025 Alexander Burmatov <thatman@altlinux.org> 1.2.9-alt1
- New 1.2.9 version.

* Thu Apr 17 2025 Alexander Burmatov <thatman@altlinux.org> 1.2.7-alt1
- New 1.2.7 version.

* Tue Mar 25 2025 Alexander Burmatov <thatman@altlinux.org> 1.2.6-alt1
- New 1.2.6 version.

* Thu Jan 30 2025 Alexander Burmatov <thatman@altlinux.org> 1.2.2-alt1
- New 1.2.2 version.

* Thu Dec 19 2024 Alexander Burmatov <thatman@altlinux.org> 1.1.6-alt1
- New 1.1.6 version.

* Fri Nov 08 2024 Alexander Burmatov <thatman@altlinux.org> 1.1.5-alt1
- New 1.1.5 version.

* Tue Aug 13 2024 Alexander Burmatov <thatman@altlinux.org> 1.0.5-alt1
- New 1.0.5 version.

* Mon May 20 2024 Alexander Burmatov <thatman@altlinux.org> 0.22.9-alt1
- New 0.22.9 version.

* Tue Mar 26 2024 Alexander Burmatov <thatman@altlinux.org> 0.22.6-alt1
- New 0.22.6 version.

* Fri Nov 10 2023 Alexander Burmatov <thatman@altlinux.org> 0.20.2-alt1
- Initial build for Sisyphus.
