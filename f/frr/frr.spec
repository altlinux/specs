%define _unpackaged_files_terminate_build 1
%filter_from_requires /.etc.default.frr/d
%filter_from_requires /.etc.sysconfig.frr/d

%define _localstatedir /var
%define _runtimedir /run
%define frr_user frr
%define frr_group frr
%define frrvty_group frrvty
%define frr_home %_localstatedir/lib/%name
%define frr_statedir %_runtimedir/%name
%define frr_daemondir %_prefix/lib/%name
%define frr_moduledir %_libdir/%name/modules
%define frr_libdir %_libdir/%name

%def_enable doc
%def_enable doc_html
%def_disable tcmalloc
%def_enable snmp
%def_disable config_rollbacks
%def_disable grpc
%def_disable zeromq
%def_with libpam
%def_enable ospfapi
%def_enable ospfclient
%def_disable realms
%def_enable fpm
%def_enable pcre2posix
%def_disable cumulus
%def_disable datacenter
%def_enable protobuf
%def_disable rpki
%def_disable scripting
%def_disable backtrace
%def_disable dp_dpdk

Name: frr
Version: 10.6.0
Release: alt1
Summary: FRRouting Routing daemon
License: GPL-2.0-or-later AND LGPL-2.1-or-later
Group: Networking/Other
Url: http://www.frrouting.org
Vcs: https://github.com/FRRouting/frr.git
Source0: %name-%version.tar
Source1: %name-tmpfiles.conf
#Patch: %%name-%%version.patch
Patch1001: 0001-update-init-script.patch

# PVE patches
Patch0001: 0001-enable-bgp-bfd-daemons.patch
Patch0002: 0002-bgpd-add-an-option-for-RT-auto-derivation-to-force-A.patch
Patch0003: 0003-tests-add-bgp-evpn-autort-test.patch
Patch0004: 0004-fabricd-enable-dummy_as_loopback-option-per-default.patch
Patch0005: 0005-systemd-add-dependancy-to-networking.service.patch

BuildRequires(pre): rpm-macros-systemd
BuildRequires: gcc-c++
BuildRequires: bison >= 2.7
BuildRequires: flex
BuildRequires: python3-devel
BuildRequires: libjson-c-devel
BuildRequires: pkgconfig(libcares)
BuildRequires: libelf-devel
BuildRequires: libreadline-devel
BuildRequires: pkgconfig(libyang) 
BuildRequires: libcap-devel
BuildRequires: makeinfo
%{?_enable_doc:BuildRequires: python3-module-sphinx}
%{?_enable_tcmalloc:BuildRequires: libgperftools-devel}
%{?_enable_scripting:BuildRequires: liblua5.3-devel}
%{?_enable_snmp:BuildRequires: libnet-snmp-devel}
%{?_with_libpam:BuildRequires: libpam-devel}
%{?_enable_pcre2posix:BuildRequires: libpcre2-devel}
%{?_enable_config_rollbacks:BuildRequires: pkgconfig(sqlite3)}
%{?_enable_grpc:BuildRequires: pkgconfig(grpc) >= 6.0.0 pkgconfig(grpc++) >= 1.16.1 pkgconfig(protobuf) >= 3.6.1 /usr/bin/protoc}
%{?_enable_zeromq:BuildRequires: pkgconfig(libzmq) >= 4.0.0}
%{?_enable_rpki:BuildRequires: pkgconfig(rtrlib) >= 0.8.0}
%{?_enable_backtrace:BuildRequires: pkgconfig(libunwind)}
%{?_enable_protobuf:BuildRequires: /usr/bin/protoc /usr/bin/protoc-c pkgconfig(libprotobuf-c) >= 1.3.0}
%{?_enable_dp_dpdk:BuildRequires: pkgconfig(libdpdk)}

Requires: /usr/bin/less
Conflicts: quagga
Conflicts: zebra
Provides: FRRouting = %EVR frrouting = %EVR

%description
FRRouting is free software that manages TCP/IP based routing protocols. It takes
a multi-server and multi-threaded approach to resolve the current complexity
of the Internet.

FRRouting supports BGP4, OSPFv2, OSPFv3, ISIS, RIP, RIPng, PIM, NHRP, PBR, EIGRP and BFD.

FRRouting is a fork of Quagga.

%package pythontools
Summary: Python tools for frr
Group: Networking/Other
Requires: %name = %EVR
BuildArch: noarch

%description pythontools
FRRouting is free software that manages TCP/IP based routing protocols. It takes
a multi-server and multi-threaded approach to resolve the current complexity
of the Internet.

FRRouting supports BGP4, OSPFv2, OSPFv3, ISIS, RIP, RIPng, PIM, NHRP, PBR, EIGRP and BFD.

This package contains a small Python tool to provide configuration reload functionality.
This is useful when the interactive configuration shell is not used. Without
this package installed, "reload" will not work for the FRR daemons.

%package rpki-rtrlib
Summary: FRR BGP RPKI support (rtrlib)
Group: Networking/Other
Requires: %name = %EVR

%description rpki-rtrlib
Adds RPKI support to FRR's bgpd, allowing validation of BGP routes
against cryptographic information stored in WHOIS databases.  This is
used to prevent hijacking of networks on the wider internet.  It is only
relevant to internet service providers using their own autonomous system
number.

%package snmp
Summary: FRR SNMP support
Group: System Environment/Daemons
Group: Networking/Other
Requires: %name = %EVR

%description snmp
Adds SNMP support to FRR's daemons by attaching to net-snmp's snmpd
through the AgentX protocol.  Provides read-only access to current
routing state through standard SNMP MIBs.

%package grpc
Summary: FRR GRPC support for FRR daemons
Group: Networking/Other
License: GPLv3+
Requires: %name = %EVR

%description grpc
Adds GRPC support to the individual FRR daemons.

%prep
%setup
#%%patch -p1
%patch1001 -p1

#%%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1

%ifarch %e2k
# EDG frontend doesn't have MSVC extensions
sed -i 's/struct mgmt_msg_header;/uint16_t code, resv; uint32_t vsplit; uint64_t refer_id, req_id;/' \
    lib/mgmt_msg_native.h
# annoying warning
%add_optflags -Wno-discarded-qualifiers
%endif

%build
%autoreconf

%configure \
    --disable-static \
    %{subst_enable doc} \
    %{?_enable_doc_html:--enable-doc-html} \
    --sbindir=%frr_daemondir \
    --libdir=%frr_libdir \
    --with-pkgconfigdir=%_pkgconfigdir \
    --libexecdir=%_libexecdir/%name \
    --with-moduledir=%frr_moduledir \
    --runstatedir=%_runtimedir \
    --enable-user=%frr_user \
    --enable-group=%frr_group \
    --enable-vty-group=%frrvty_group \
    --enable-configfile-mask=0640 \
    --enable-logfile-mask=0640 \
    --with-vtysh-pager=less \
    --enable-multipath=64 \
    %{subst_enable tcmalloc} \
    %{subst_enable snmp} \
    %{?_enable_config_rollbacks:--enable-config-rollbacks} \
    %{subst_enable grpc} \
    %{subst_enable zeromq} \
    %{subst_with libpam} \
    %{subst_enable ospfapi} \
    %{subst_enable ospfclient} \
    %{subst_enable realms} \
    %{subst_enable fpm} \
    %{subst_enable pcre2posix} \
    %{subst_enable cumulus} \
    %{subst_enable datacenter} \
    %{subst_enable protobuf} \
    %{subst_enable rpki} \
    %{subst_enable scripting} \
    %{subst_enable backtrace} \
    %{?_enable_dp_dpdk:--enable-dp-dpdk} \
    --with-crypto=openssl

%make_build MAKEINFO="makeinfo --no-split" PYTHON=%__python3

# Build info documentation
#%%make_build -C doc info

%install
%makeinstall_std

install -d %buildroot%_sysconfdir/%name

install -d %buildroot%_docdir/%name
# remove stray buildinfo files
find %buildroot%_docdir/%name -type f -name .buildinfo -delete

install -d -m 0775 %buildroot%_logdir/%name

rm -rf %buildroot%_infodir/dir

install -p -D -m 644 %SOURCE1 %buildroot%_tmpfilesdir/%name.conf
sed -e "s|@frr_statedir@|%frr_statedir|g" -i %buildroot%_tmpfilesdir/%name.conf
install -p -D -m 644 tools/etc/frr/daemons %buildroot%_sysconfdir/%name/daemons
install -p -D -m 644 tools/frr.service %buildroot%_unitdir/%name.service
install -p -D -m 644 tools/etc/logrotate.d/frr %buildroot%_logrotatedir/%name
install -p -D -m 644 redhat/frr.pam %buildroot%_sysconfdir/pam.d/%name

rm -f %buildroot%frr_daemondir/ssd
mkdir -p %buildroot%_initdir
mv %buildroot%frr_daemondir/%name %buildroot%_initdir/%name

# Delete libtool archives
find %buildroot -type f -name "*.la" -delete -print

#Upstream does not maintain a stable API, these headers from -devel subpackage are no longer needed
rm %buildroot%_libdir/%name/*.so
rm -r %buildroot%_includedir
rm -f  %buildroot/%_pkgconfigdir/*.pc

touch %buildroot%_sysconfdir/%name/%name.conf
cat > %buildroot%_sysconfdir/%name/vtysh.conf << __EOF__
! vtysh is using PAM authentication allowing root to use it.
__EOF__

#%%check
#%%make_build check PYTHON=%%__python3

%pre
groupadd -r -f %frr_group
groupadd -r -f %frrvty_group

useradd -r -g %frr_group -G %frrvty_group -d %frr_home -s /sbin/nologin -c "FRRouting suite" %frr_user >/dev/null 2>&1 ||:
usermod -G %frrvty_group %frr_user >/dev/null 2>&1 ||:

%post
%tmpfiles_create %_tmpfilesdir/%name.conf ||:
%post_service %name

# Create dummy files if they don't exist so basic functions can be used.
if [ ! -e %_sysconfdir/%name/%name.conf ]; then
    echo "hostname `hostname`" > %_sysconfdir/%name/%name.conf
    echo "log file %_logdir/%name/%name.log"  >> %_sysconfdir/%name/%name.conf
    chown %frr_user:%frr_group %_sysconfdir/%name/%name.conf
    chmod 640 %_sysconfdir/%name/%name.conf
fi

%preun
%preun_service %name

%files
%doc README.md doc/mpls
%_docdir/%name/html
%dir %attr(750,%frr_user,%frr_group) %_sysconfdir/%name
%config(noreplace) %_logrotatedir/%name
%config(noreplace) %attr(644,%frr_user,%frr_group) %_sysconfdir/frr/daemons
%ghost %config(noreplace) %attr(640,%frr_user,%frr_group) %_sysconfdir/%name/%name.conf
%config(noreplace) %attr(640,%frr_user,%frrvty_group) %_sysconfdir/%name/vtysh.conf
%config(noreplace) %_sysconfdir/pam.d/frr
%dir %attr(775,root,%frr_group) %_logdir/%name
%_bindir/*
%_mandir/man?/*
%_infodir/*.info*
%dir %frr_libdir
%frr_libdir/*.so*
%frr_moduledir
%frr_daemondir
%_unitdir/%name.service
%_initdir/%name
%_datadir/yang/*.yang
%_tmpfilesdir/%name.conf

%exclude %frr_daemondir/*.py
%if_enabled rpki
%exclude %frr_moduledir/bgpd_rpki.so
%endif
%if_enabled snmp
%exclude %frr_libdir/libfrrsnmp.so*
%exclude %frr_moduledir/*snmp.so
%endif
%if_enabled grpc
%exclude %frr_libdir/libfrrgrpc_pb.*
%exclude %frr_moduledir/grpc.so
%endif

%files pythontools
%frr_daemondir/*.py

%if_enabled rpki
%post rpki-rtrlib
# add rpki module to daemons
sed -i -e 's/^\(bgpd_options=\)\(.*\)\(".*\)/\1\2 -M rpki\3/' %_sysconfdir/frr/daemons

%postun rpki-rtrlib
# remove rpki module from daemons
sed -i 's/ -M rpki//' %_sysconfdir/frr/daemons

%files rpki-rtrlib
%frr_moduledir/bgpd_rpki.so
%endif

%if_enabled snmp
%files snmp
%frr_libdir/libfrrsnmp.so*
%frr_moduledir/*snmp.so
%endif

%if_enabled grpc
%files grpc
%frr_libdir/libfrrgrpc_pb.*
%frr_moduledir/grpc.so
%endif

%changelog
* Tue Mar 31 2026 Pavel Shilov <zerospirit@altlinux.org> 10.6.0-alt1
- NMU: update to new version 10.6.0 build based on libyang 4 

* Tue Feb 24 2026 Alexey Shabalin <shaba@altlinux.org> 10.5.2-alt1
- updated from 10.3.1 to 10.5.2

* Thu Jul 03 2025 Alexey Shabalin <shaba@altlinux.org> 10.3.1-alt1
- 10.3.1

* Tue Jul 01 2025 Alexey Shabalin <shaba@altlinux.org> 10.2.2-alt3
- Fixed logdir permitions (ALT#54532)

* Sun Jun 29 2025 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 10.2.2-alt2
- e2k build fix

* Wed May 21 2025 Alexey Shabalin <shaba@altlinux.org> 10.2.2-alt1
- 10.2.2 (Fixes: CVE-2024-55553, affected for rpki-rtrlib only)
- Add patches from PVE project
- Build with ospfapi and ospfclient
- Add subpackages: pythontools, rpki-rtrlib, snmp, grpc

* Mon Nov 25 2024 Alexey Shabalin <shaba@altlinux.org> 10.2-alt1
- 10.2

* Thu Aug 22 2024 Alexey Shabalin <shaba@altlinux.org> 10.1-alt1
- 10.1 (Fixes: CVE-2024-34088)

* Thu May 02 2024 Alexey Shabalin <shaba@altlinux.org> 10.0-alt1
- 10.0

* Tue Jan 16 2024 Alexey Shabalin <shaba@altlinux.org> 9.0.2-alt1
- 9.0.2 (Fixes: CVE-2023-46752, CVE-2023-46753, CVE-2023-47234, CVE-2023-47235)

* Thu Nov 09 2023 Alexey Shabalin <shaba@altlinux.org> 9.0.1-alt1
- 9.0.1

* Fri Jul 07 2023 Alexey Shabalin <shaba@altlinux.org> 8.5.2-alt1
- 8.5.2

* Wed May 03 2023 Alexey Shabalin <shaba@altlinux.org> 8.5.1-alt1
- 8.5.1

* Sun Jan 22 2023 Alexey Shabalin <shaba@altlinux.org> 8.4.2-alt1
- 8.4.2

* Mon Oct 10 2022 Alexey Shabalin <shaba@altlinux.org> 8.3.1-alt1
- 8.3.1

* Mon Mar 21 2022 Alexey Shabalin <shaba@altlinux.org> 8.2.2-alt1
- 8.2.2

* Sat Feb 19 2022 Alexey Shabalin <shaba@altlinux.org> 8.1-alt1
- Initial build

