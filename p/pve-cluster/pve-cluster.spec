Name: pve-cluster
Summary: Cluster Infrastructure for Proxmox Virtual Environment
Version: 4.0.47
Release: alt5
License: GPLv3
Group: System/Servers
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

ExclusiveArch: x86_64
Requires: bridge-utils openntpd ntpdate corosync2 fuse rrd-cached ksmtuned openvswitch
Requires: sqlite3 vixie-cron faketime tzdata openssh-server openssh-clients

Source0: %name.tar.xz
Source1: pve-access-control.tar.xz
Patch0: %name.patch
Patch1: pve-access-control.patch

Source2: pve-firsttime

BuildRequires: pve-common pve-doc-generator libcheck-devel librrd-devel glib2-devel libfuse-devel libcorosync2-devel libsqlite3-devel xmlto
BuildRequires: perl(ExtUtils/Embed.pm) perl(Term/ReadLine.pm) perl(Digest/HMAC_SHA1.pm) perl(XML/Parser.pm) perl(RRDs.pm)
BuildRequires: perl(Crypt/OpenSSL/Random.pm) perl(Crypt/OpenSSL/RSA.pm) perl(Net/SSLeay.pm)
BuildRequires: perl(MIME/Base32.pm) perl(Net/LDAP.pm) perl(Authen/PAM.pm) perl(UUID.pm)

%description
This package contains the Cluster Infrastructure for the Proxmox
Virtual Environment, namely a distributed filesystem to store
configuration data on all nodes.

%package -n pve-access-control
Summary: Proxmox VE access control library
Version: 4.0.19
Group: Development/Perl

%description -n pve-access-control
This package contains the role based user management and access
control function used by Proxmox VE.

%prep
%setup -q -n %name -a1
%patch0 -p1
%patch1 -p0

%build
cd data
%autoreconf
%configure
%make

%install
install -pD -m644 debian/%name.service %buildroot%systemd_unitdir/%name.service
install -pD -m644 debian/sysctl.conf %buildroot%_sysconfdir/sysctl.d/pve-cluster.conf
cd data
%make DESTDIR=%buildroot install
cd ../pve-access-control
%make DESTDIR=%buildroot install

mkdir -p %buildroot%_datadir/doc/%name
install -m644 %SOURCE2 %buildroot%_datadir/doc/%name/

mkdir -p %buildroot%_sysconfdir/pve
mkdir -p %buildroot%_localstatedir/%name

mkdir -p %buildroot%_sysconfdir/network
cat << __EOF__ > %buildroot%_sysconfdir/network/interfaces
auto lo
iface lo inet loopback
__EOF__

mkdir -p %buildroot%_sysconfdir/sysconfig
cat << __EOF__ > %buildroot%_sysconfdir/sysconfig/%name
DAEMON_OPTS=""
__EOF__

cat << __EOF__ > %buildroot%_datadir/doc/%name/rrdcached.sysconfig
RRDCACHED_USER="root"
OPTS="-j /var/lib/rrdcached/journal/ -F -b /var/lib/rrdcached/db/ -B"
SOCKFILE="/var/run/rrdcached.sock"
SOCKPERMS=0660
__EOF__

%post
%post_service %name

%preun
%preun_service %name
if [ $1 -eq 0 ] ; then
        /sbin/systemctl disable %name.service >/dev/null 2>&1 || :
fi

%pre
%_sbindir/groupadd -r -f www-data 2>/dev/null ||:
%_sbindir/useradd -g www-data -c 'www-data' -d /var/www -s '/sbin/nologin' -G www-data -r www-data 2>/dev/null || :

%files
%systemd_unitdir/%name.service
%_sysconfdir/bash_completion.d/pvecm
%dir %_sysconfdir/network
%ghost %_sysconfdir/network/interfaces
%config(noreplace) %_sysconfdir/sysconfig/%name
%_sysconfdir/sysctl.d/pve-cluster.conf
%_bindir/create_pmxcfs_db
%_bindir/pmxcfs
%_bindir/pvecm
%dir %perl_vendor_autolib/PVE
%perl_vendor_autolib/PVE/IPCC
%dir %perl_vendor_privlib/PVE
%perl_vendor_privlib/PVE/Cluster.pm
%perl_vendor_privlib/PVE/IPCC.pm
%dir %perl_vendor_privlib/PVE/CLI
%perl_vendor_privlib/PVE/CLI/pvecm.pm
%dir %_localstatedir/%name
%_man1dir/pvecm.1*
%_man5dir/datacenter.cfg.5*
%_man8dir/pmxcfs.8*
%_datadir/doc/%name

%files -n pve-access-control
%_sysconfdir/bash_completion.d/pveum
%_bindir/oathkeygen
%_sbindir/pveum
%dir %perl_vendor_privlib/PVE
%perl_vendor_privlib/PVE/RPCEnvironment.pm
%perl_vendor_privlib/PVE/AccessControl.pm
%dir %perl_vendor_privlib/PVE/CLI
%perl_vendor_privlib/PVE/CLI/pveum.pm
%dir %perl_vendor_privlib/PVE/API2
%perl_vendor_privlib/PVE/API2/*.pm
%dir %perl_vendor_privlib/PVE/Auth
%perl_vendor_privlib/PVE/Auth/*.pm
%_man1dir/pveum.1*

%changelog
* Mon Nov 28 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.47-alt5
- 4.0-47+git.ab224148

* Wed Nov 23 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.47-alt4
- 4.0-47

* Mon Oct 03 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.46-alt3
- 4.0-46

* Fri Sep 16 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.45-alt2
- 4.0-45

* Mon Aug 22 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.44-alt1
- 4.0-44
- pve-access-control 4.0-19

* Thu Jul 21 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.43-alt2
- pve-access-control 4.0-18

* Fri Jul 15 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.43-alt1
- 4.0-43
- pve-access-control 4.0-17

* Thu Jun 23 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.42-alt6
- fixed upgrading from a previous version

* Wed Jun 15 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.42-alt5
- 4.0-42

* Thu Jun 09 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.40-alt4
- added requires openntpd, bridge-utils

* Tue Jun 07 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.40-alt3
- added requires faketime

* Mon Jun 06 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.40-alt2
- pve-access-control 4.0-16

* Wed Jun 01 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.40-alt1
- 4.0-40

* Fri May 20 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.39-alt1
- 4.0-39

* Mon Feb 08 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.31-alt1
- 4.0-31

* Fri Dec 11 2015 Valery Inozemtsev <shrek@altlinux.ru> 4.0.29-alt1
- 4.0-29

* Thu Dec 03 2015 Valery Inozemtsev <shrek@altlinux.ru> 4.0.28-alt1
- initial release

