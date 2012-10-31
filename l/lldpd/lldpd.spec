Name: lldpd
Version: 0.6.1
Release: alt1
Summary: Link Layer Discovery Protocol Daemon
Source: %name-%version.tar
Group: Networking/Other
License: GPL

%def_enable cdp
%def_enable fdp
%def_enable edp
%def_enable sonmp
%def_enable lldpmed
%def_enable dot1
%def_enable dot3

%def_with snmp
%def_with xml

BuildRequires: libssl-devel
BuildRequires: doxygen
BuildRequires: libevent-devel

%{?_with_snmp:BuildRequires: libnet-snmp-devel}
%{?_with_xml:BuildRequires: libxml2-devel}

%description
LLDP (Link Layer Discovery Protocol) (also known as 802.1ab) is an
industry standard protocol designed to supplant proprietary Link-Layer
protocols such as Extreme's EDP (Extreme Discovery Protocol) and CDP
(Cisco Discovery Protocol). The goal of LLDP is to provide an
inter-vendor compatible mechanism to deliver Link-Layer notifications
to adjacent network devices.

lldpd is a lldp daemon for GNU/Linux and implements both reception and
sending. It supports both LLDP and LLDP-MED (contributed by Michael
Hanig). It also implements an SNMP subagent for net-snmp to get local
and remote LLDP information. The LLDP MIB is partially implemented but
the most useful tables are here.

lldpd supports bridge, vlan and bonding. bonding need to be done on
real physical devices, not on bridges, vlans, etc. However, vlans can
be mapped on the bonding device. You can bridge vlan but not add vlans
on bridges. More complex setups may give false results.

%package devel
Group: Development/C
Summary: Link Layer Discovery Protocol Daemon

%description devel
Header files for LLDP Daemon

%prep
%setup

%build
%autoreconf
%configure \
    %{subst_enable cdp} \
    %{subst_enable fdp} \
    %{subst_enable edp} \
    %{subst_enable sonmp} \
    %{subst_enable lldpmed} \
    %{subst_enable dot1} \
    %{subst_enable dot3} \
    %{subst_with snmp} \
    %{subst_with xml}

%make

%install
%make_install DESTDIR=%buildroot install
mv %buildroot%_datadir/doc/lldpd %buildroot%_datadir/doc/%name-%version

%post

%preun

%files
%_sbindir/*
%_libdir/liblldpctl.so*
%_datadir/doc/%name-%version/
%_man8dir/*

%files devel
%_includedir/*
%_libdir/liblldpctl.a
%_pkgconfigdir/*

%changelog
* Wed Oct 31 2012 Afanasov Dmitry <ender@altlinux.org> 0.6.1-alt1
- first build

