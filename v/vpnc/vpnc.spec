Name: vpnc
Version: 0.5.3
Release: alt4

Summary: Client for cisco vpn concentrator
Group: Networking/Remote access
License: GPL

Url: http://www.unix-ag.uni-kl.de/~massar/vpnc/

Source0: %name-%version.tar.gz

Patch0: vpnc-0.4.0-alt-destdir.patch
Patch2: vpnc-0.5.3-cloexec.patch
Patch3: vpnc-0.5.1-dpd.patch
Patch4: vpnc-0.5.3-update-script.patch
Patch5: vpnc-0.5.3-make-flags.patch

Packager: Ilya Mashkin <oddity@altlinux.org>

BuildRequires: libgcrypt-devel perl-autodie
Requires: iproute2 vpnc-script

%add_findreq_skiplist %_sysconfdir/vpnc/vpnc-script

%description
vpnc is supposed to work with:

* Cisco VPN concentrator 3000 Series
* Cisco IOS routers
* Cisco PIX / ASA Zecurity Appliances
* Juniper/Netscreen 

Supported Authentications: Pre-Shared-Key + XAUTH, Pre-Shared-Key
Supported IKE DH-Groups: dh1 dh2 dh5
Supported Hash Algo (IKE/IPSEC): md5 sha1
Supported Encryptions (IKE/IPSEC): (null) (1des) 3des aes128 aes192 aes256
Perfect Forward Secrecy: nopfs dh1 dh2 dh5

%package script
Summary: Routing setup script for vpnc and openconnect
Group: Networking/Remote access
BuildArch: noarch

%description script
This script sets up routing for VPN connectivity, when invoked by vpnc
or openconnect.

%prep
%setup -q
%patch0 -p1
%patch2 -p1 -b .cloexec
%patch3 -p1 -b .dpd
%patch4 -p1
%patch5 -p1

%build
%make_build

%install
%make_install DESTDIR=%buildroot install

mkdir -p %buildroot%_var/run/vpnc
touch %buildroot%_var/run/vpnc/pid \
      %buildroot%_var/run/vpnc/defaultroute \
      %buildroot%_var/run/vpnc/resolv.conf-backup

%files
%doc README TODO COPYING
%config(noreplace) %_sysconfdir/vpnc/default.conf
%_bindir/*
%_sbindir/*
%_man1dir/*
%_man8dir/*
%dir %_var/run/vpnc
%ghost %verify(not md5 size mtime) %_var/run/vpnc/pid
%ghost %verify(not md5 size mtime) %_var/run/vpnc/defaultroute
%ghost %verify(not md5 size mtime) %_var/run/vpnc/resolv.conf-backup

%files script
%dir %_sysconfdir/vpnc
%config(noreplace) %_sysconfdir/vpnc/vpnc-script

%changelog
* Sun Nov 21 2010 Alexey Shabalin <shaba@altlinux.ru> 0.5.3-alt4
- update buildreq
- add PIE to CFLAGS, pie to LDFLAGS (patch5)

* Sun Jan 17 2010 Alexey Shabalin <shaba@altlinux.ru> 0.5.3-alt3
- package /var/run/vpnc as ghost
- split vpnc-script out into separate package (for openconnect)
- update vpnc-script to support IPv6 properly from git://git.infradead.org/users/dwmw2/vpnc-scripts.git

* Thu Mar 05 2009 Mikhail Efremov <sem@altlinux.org> 0.5.3-alt2
- added add_findreq_skiplist vpnc-script
	(to avoid resolvconf require)

* Sun Dec 28 2008 Ilya Mashkin <oddity@altlinux.org> 0.5.3-alt1
- 0.5.3

* Thu Mar 15 2007 Igor Zubkov <icesik@altlinux.org> 0.4.0-alt1
- build for Sisyphus

