%define _unpackaged_files_terminate_build 1
%define _localstatedir /var

%define libdnssec_sover 10
%define libknot_sover 16
%define libzscanner_sover 5

%def_disable dnstap
%def_enable maxminddb
%def_enable xdp
%def_enable documentation
%def_enable quic

Name: knot
Version: 3.5.3
Release: alt2
Summary: High-performance authoritative DNS server
Group: System/Servers
License: GPL-3.0-or-later
Url: https://www.knot-dns.cz
Vcs: https://gitlab.nic.cz/knot/knot-dns.git
Source0: %name-%version.tar
Patch0: %name-%version.patch

# Required dependencies
BuildRequires: pkgconfig(liburcu)
BuildRequires: pkgconfig(gnutls) >= 3.6.10
BuildRequires: pkgconfig(libedit)

# Optional dependencies
BuildRequires: pkgconfig(libcap-ng)
BuildRequires: pkgconfig(libidn2)
BuildRequires: pkgconfig(libnghttp2)
%{?_enable_maxminddb:BuildRequires: pkgconfig(libmaxminddb)}
%{?_enable_xdp:BuildRequires: pkgconfig(libbpf) >= 0.0.6 pkgconfig(libmnl) pkgconfig(libxdp)}
%{?_enable_quic:BuildRequires: pkgconfig(libngtcp2) >= 0.17.0 pkgconfig(gnutls) >= 3.7.3}
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(systemd)
%{?_enable_documentation:BuildRequires: /usr/bin/sphinx-build}
BuildRequires: liblmdb-devel
%{?_enable_dnstap:BuildRequires: /usr/bin/protoc-c pkgconfig(libfstrm) pkgconfig(libprotobuf-c) >= 1.0.0}

%description
Knot DNS is a high-performance authoritative DNS server implementation.

%package devel
Summary: Development files for the Knot DNS libraries
Group: Development/C

Requires: libdnssec%libdnssec_sover = %EVR
Requires: libknot%libknot_sover = %EVR
Requires: libzscanner%libzscanner_sover = %EVR

%description devel
Knot DNS is a high-performance authoritative DNS server implementation.

Development files for knot.

%package utils
Summary: DNS client utilities shipped with the Knot DNS server
Group: Networking/Other

%description utils
The package contains DNS client utilities shipped with the Knot DNS server.

%package -n libdnssec%libdnssec_sover
Summary: Knot DNS DNSSEC library
Group: System/Libraries

Provides: libdnssec = %EVR
Obsoletes: libdnssec < %EVR

%description -n libdnssec%libdnssec_sover
Knot DNS DNSSEC library

%package -n libknot%libknot_sover
Summary: Knot DNS library
Group: System/Libraries

Provides: libknot = %EVR
Obsoletes: libknot < %EVR

# Knot DNS 3.2+ isn't compatible with earlier knot-resolver
Conflicts: knot-resolver < 5.7.0

%description -n libknot%libknot_sover
Knot DNS library

%package -n libzscanner%libzscanner_sover
Summary: Knot DNS Zone Parsing library
Group: System/Libraries

Provides: libzscanner = %EVR
Obsoletes: libzscanner < %EVR

%description -n libzscanner%libzscanner_sover
Knot DNS Zone Parsing library

%package doc
Summary: Documentation for the Knot DNS server
Group: Documentation
BuildArch: noarch

%description doc
The package contains documentation for the Knot DNS server.
On-line version is available on https://www.knot-dns.cz/documentation/

%prep
%setup
%patch0 -p1

%build
# disable debug code (causes unused warnings)
%add_optflags -DNDEBUG -Wno-unused

%ifarch armv7hl %ix86 mips32 mipsn32
# 32-bit architectures sometimes do not have sufficient amount of
# contiguous address space to handle default values
%define configure_db_sizes --with-conf-mapsize=64
%endif

%autoreconf
%configure \
  --libexecdir=/usr/lib/%name \
  --with-rundir=/run/%name \
  --with-storage=/var/lib/%name \
  %{?configure_db_sizes} \
%if_enabled dnstap
  --enable-dnstap=yes \
  --with-module-dnstap=yes \
%endif
  %{subst_enable documentation} \
  %{subst_enable quic} \
  --disable-static

%make_build
%if_enabled documentation
%make html
%endif

%install
%makeinstall_std

# install documentation
rm -f doc/_build/html/.buildinfo

# install configuration file
rm -f %buildroot%_sysconfdir/%name/*
install -p -m 0644 -D samples/%name.sample.conf %buildroot%_sysconfdir/%name/%name.conf

# install systemd files
install -p -m 0644 -D distro/common/%name.service %buildroot%_unitdir/%name.service
install -p -m 0644 -D distro/common/cz.nic.knotd.conf %buildroot%_datadir/dbus-1/system.d/cz.nic.knotd.conf

# create storage dir and key dir
install -d %buildroot%_sharedstatedir
install -d -m 0775 -D %buildroot%_sharedstatedir/%name
install -d -m 0770 -D %buildroot%_sharedstatedir/%name/keys

# remove libarchive files
find %buildroot -type f -name "*.la" -delete -print

%check
V=1 %make check ||:

%pre
%_sbindir/groupadd -r -f %name
%_sbindir/useradd -M -r -d /var/lib/%name -s /bin/false -c "Knot DNS server" -g %name %name >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc COPYING NEWS README.md samples
%dir %attr(750,root,%name) %_sysconfdir/%name
%config(noreplace) %attr(640,root,%name) %_sysconfdir/%name/%name.conf
%_datadir/dbus-1/system.d/cz.nic.knotd.conf
%dir %attr(775,root,%name) %_sharedstatedir/%name
%dir %attr(770,root,%name) %_sharedstatedir/%name/keys
%_unitdir/%name.service
%_bindir/kzone*
%_sbindir/*
%if_enabled documentation
%_man1dir/kzone*
%_man5dir/*
%_man8dir/*
%exclude %_man8dir/kxdpgun.*
%endif
%exclude %_sbindir/kxdpgun

%files utils
%_bindir/*
%if_enabled xdp
%_sbindir/kxdpgun
%if_enabled documentation
%_man8dir/kxdpgun.*
%endif
%endif
%if_enabled documentation
%_man1dir/*
%exclude %_man1dir/kzone*
%endif
%exclude %_bindir/kzone*

%files devel
%_includedir/*
%_pkgconfigdir/*
%_libdir/libdnssec.so
%_libdir/libknot.so
%_libdir/libzscanner.so

%files -n libdnssec%libdnssec_sover
%_libdir/libdnssec.so.%{libdnssec_sover}*

%files -n libknot%libknot_sover
%_libdir/libknot.so.%{libknot_sover}*

%files -n libzscanner%libzscanner_sover
%_libdir/libzscanner.so.%{libzscanner_sover}*

%if_enabled documentation
%files doc
%doc doc/_build/html
%endif

%changelog
* Thu May 21 2026 Aleksandr Gamzin <gamzin@altlinux.org> 3.5.3-alt2
- Switch shared libraries to ABI-versioned packages (Shared Libs Policy).

* Tue Feb 17 2026 Alexey Shabalin <shaba@altlinux.org> 3.5.3-alt1
- updated from 3.4.8 to 3.5.3

* Thu Sep 04 2025 Alexey Shabalin <shaba@altlinux.org> 3.4.8-alt1
- New version 3.4.8.

* Wed Jun 18 2025 Alexey Shabalin <shaba@altlinux.org> 3.4.7-alt1
- New version 3.4.7.

* Mon May 19 2025 Alexey Shabalin <shaba@altlinux.org> 3.4.6-alt1
- New version 3.4.6.

* Fri Jan 31 2025 Alexey Shabalin <shaba@altlinux.org> 3.4.4-alt1
- New version 3.4.4.

* Fri Dec 06 2024 Alexey Shabalin <shaba@altlinux.org> 3.4.3-alt1
- New version 3.4.3.

* Wed Sep 25 2024 Alexey Shabalin <shaba@altlinux.org> 3.4.0-alt1
- New version 3.4.0.
- Enable build with quic support (DoQ).

* Thu Aug 29 2024 Alexey Shabalin <shaba@altlinux.org> 3.3.9-alt1
- New version 3.3.9.

* Thu Aug 22 2024 Alexey Shabalin <shaba@altlinux.org> 3.3.8-alt1
- New version 3.3.8.

* Thu Jul 04 2024 Alexey Shabalin <shaba@altlinux.org> 3.3.7-alt1
- New version 3.3.7.

* Thu May 02 2024 Alexey Shabalin <shaba@altlinux.org> 3.3.5-alt1
- New version 3.3.5.

* Mon Jan 29 2024 Alexey Shabalin <shaba@altlinux.org> 3.3.4-alt1
- New version 3.3.4.

* Fri Dec 15 2023 Alexey Shabalin <shaba@altlinux.org> 3.3.3-alt1
- New version 3.3.3.

* Fri Oct 27 2023 Alexey Shabalin <shaba@altlinux.org> 3.3.2-alt1
- New version 3.3.2.

* Thu Oct 19 2023 Alexey Shabalin <shaba@altlinux.org> 3.3.1-alt1
- New version 3.3.1.

* Fri Sep 01 2023 Alexey Shabalin <shaba@altlinux.org> 3.3.0-alt1
- New version 3.3.0.

* Fri Aug 18 2023 Alexey Shabalin <shaba@altlinux.org> 3.2.9-alt1
- New version 3.2.9.

* Tue May 30 2023 Alexey Gladkov <legion@altlinux.ru> 3.2.6-alt3
- Add BuildRequires on libxdp to use with libbpf-1.x

* Thu May 18 2023 Anton Farygin <rider@altlinux.ru> 3.2.6-alt2
- disabled quic for building without unsupported libngtcp2-0.15.0

* Mon Apr 17 2023 Alexey Shabalin <shaba@altlinux.org> 3.2.6-alt1
- New version 3.2.6.

* Fri Mar 24 2023 Alexey Shabalin <shaba@altlinux.org> 3.2.5-alt1
- New version 3.2.5.

* Wed Jan 11 2023 Alexey Shabalin <shaba@altlinux.org> 3.2.4-alt1
- new version 3.2.4

* Thu Nov 03 2022 Alexey Shabalin <shaba@altlinux.org> 3.2.2-alt1
- new version 3.2.2

* Thu Sep 29 2022 Alexey Shabalin <shaba@altlinux.org> 3.2.1-alt1
- new version 3.2.1

* Fri Aug 26 2022 Alexey Shabalin <shaba@altlinux.org> 3.1.9-alt1
- new version 3.1.9

* Fri Jun 03 2022 Alexey Shabalin <shaba@altlinux.org> 3.1.8-alt1
- new version 3.1.8

* Fri Apr 08 2022 Alexey Shabalin <shaba@altlinux.org> 3.1.7-alt1
- new version 3.1.7

* Fri Mar 04 2022 Alexey Shabalin <shaba@altlinux.org> 3.1.6-alt1
- new version 3.1.6

* Fri Jan 07 2022 Alexey Shabalin <shaba@altlinux.org> 3.1.5-alt1
- new version 3.1.5

* Thu Nov 11 2021 Alexey Shabalin <shaba@altlinux.org> 3.1.4-alt1
- new version 3.1.4

* Mon Nov 01 2021 Alexey Shabalin <shaba@altlinux.org> 3.1.3-alt1
- new version 3.1.3

* Mon Sep 13 2021 Alexey Shabalin <shaba@altlinux.org> 3.1.2-alt1
- new version 3.1.2

* Fri Aug 06 2021 Alexey Shabalin <shaba@altlinux.org> 3.1.0-alt1
- new version 3.1.0

* Mon Jul 19 2021 Alexey Shabalin <shaba@altlinux.org> 3.0.8-alt1
- new version 3.0.8

* Tue May 18 2021 Alexey Shabalin <shaba@altlinux.org> 3.0.6-alt1
- new version 3.0.6

* Thu Apr 22 2021 Alexey Shabalin <shaba@altlinux.org> 3.0.5-alt1
- new version 3.0.5

* Fri Feb 12 2021 Alexey Shabalin <shaba@altlinux.org> 3.0.4-alt1
- new version 3.0.4

* Wed Dec 16 2020 Alexey Shabalin <shaba@altlinux.org> 3.0.3-alt1
- new version 3.0.3

* Thu Nov 12 2020 Alexey Shabalin <shaba@altlinux.org> 3.0.2-alt1
- new version 3.0.2

* Thu Sep 10 2020 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt1
- new version 3.0.0

* Sun May 31 2020 Alexey Shabalin <shaba@altlinux.org> 2.9.5-alt1
- new version 2.9.5

* Fri May 08 2020 Alexey Shabalin <shaba@altlinux.org> 2.9.4-alt1
- new version 2.9.4

* Wed Mar 18 2020 Alexey Shabalin <shaba@altlinux.org> 2.9.3-alt1
- Initial build.

