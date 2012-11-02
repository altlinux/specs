Name: lldpd
Version: 0.6.1
Release: alt2
Summary: Link Layer Discovery Protocol Daemon
Source: %name-%version.tar
Group: Networking/Other
License: GPL

Source1: lldpd.init
Source2: lldpd.sysconfig
Source3: lldpd.all
Source4: lldpd.conf

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
    %{subst_with xml} \
    --with-privsep-chroot=%_localstatedir/%name

%make

%install
%make_install DESTDIR=%buildroot install
mv %buildroot%_datadir/doc/lldpd %buildroot%_datadir/doc/%name-%version
install -m755 -D %SOURCE1 %buildroot%_initdir/lldpd
install -m644 -D %SOURCE2 %buildroot%_sysconfdir/sysconfig/lldpd
install -m750 -D %SOURCE3 %buildroot%_sysconfdir/chroot.d/lldpd.all
install -m750 -D %SOURCE4 %buildroot%_sysconfdir/chroot.d/lldpd.conf
mkdir -p %buildroot%_localstatedir/%name/etc

%pre
if [ $1 = 1 ]; then
        %_sbindir/groupadd -r _lldpd >/dev/null 2>&1 ||:
        %_sbindir/useradd -M -r _lldpd -g _lldpd -s /dev/null -c "LLDP Daemon" \
        -d / >/dev/null 2>&1 ||:
fi

%post
%post_service %name

%preun
%preun_service %name

%files
%_initdir/*
%_sysconfdir/sysconfig/lldpd
%_sysconfdir/chroot.d/*
%_sbindir/*
%_libdir/liblldpctl.so*
%_datadir/doc/%name-%version/
%_man8dir/*
%attr(0750, _lldpd, _lldpd) %_localstatedir/%name/

%files devel
%_includedir/*
%_libdir/liblldpctl.a
%_pkgconfigdir/*

%changelog
* Fri Nov 02 2012 Afanasov Dmitry <ender@altlinux.org> 0.6.1-alt2
- add init scripts

* Wed Oct 31 2012 Afanasov Dmitry <ender@altlinux.org> 0.6.1-alt1
- first build

