%define _unpackaged_files_terminate_build 1

Name: pve-cluster
Summary: Cluster Infrastructure for PVE
Version: 7.2.3
Release: alt1
License: AGPL-3.0+
Group: System/Servers
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

ExclusiveArch: x86_64 aarch64
Requires: chrony ntpdate corosync fuse rrd-cached >= 1.7.2-alt3 ksmtuned openvswitch
Requires: sqlite3 vixie-cron faketime tzdata openssh-server openssh-clients

Source: %name-%version.tar
Patch: %name-%version.patch

Source3: %name.filetrigger

BuildRequires: pve-common pve-doc-generator libcheck-devel xmlto
BuildRequires: pve-apiclient pve-access-control
BuildRequires: pkgconfig(libcpg) pkgconfig(libcpg) pkgconfig(libcmap) pkgconfig(libquorum) pkgconfig(libqb) pkgconfig(glib-2.0) pkgconfig(fuse) pkgconfig(sqlite3) pkgconfig(librrd)
BuildRequires: perl(ExtUtils/Embed.pm) perl(Term/ReadLine.pm) perl(Digest/HMAC_SHA1.pm) perl(XML/Parser.pm) perl(RRDs.pm)
BuildRequires: perl(Crypt/OpenSSL/Random.pm) perl(Crypt/OpenSSL/RSA.pm) perl(Net/SSLeay.pm)
BuildRequires: perl(MIME/Base32.pm) perl(Net/LDAP.pm) perl(Authen/PAM.pm) perl(UUID.pm)

%description
This package contains the Cluster Infrastructure for the PVE,
namely a distributed filesystem to store configuration data
on all nodes.

%package -n libpve-cluster-perl
Summary: Proxmox Virtual Environment cluster Perl modules.
Group: Development/Perl
Requires: rrd-cached

%description -n libpve-cluster-perl
%summary.
This package contains various cluster-related perl modules.

%package -n libpve-cluster-api-perl
Summary: Proxmox Virtual Environment cluster Perl API modules.
Group: Development/Perl
Requires: openssl rsync

%description -n libpve-cluster-api-perl
%summary.
This package contains the API2 endpoints and CLI binary 'pvecm'.

%prep
%setup
%patch -p1

%build
%make -C data

%install
%makeinstall_std -C data/PVE/Cluster
%makeinstall_std -C data
install -pD -m644 debian/%name.service %buildroot%systemd_unitdir/%name.service
install -pD -m644 debian/sysctl.d/10-pve.conf %buildroot%_sysctldir/10-pve.conf
install -pD -m0755 %SOURCE3 %buildroot%_prefix/lib/rpm/%name.filetrigger

mkdir -p %buildroot%_sysconfdir/cron.d
touch %buildroot%_sysconfdir/cron.d/vzdump

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

%post
%post_service %name

%preun
%preun_service %name

%pre
%_sbindir/groupadd -r -f www-data 2>/dev/null ||:
%_sbindir/useradd -g www-data -c 'www-data' -d /var/www -s '/sbin/nologin' -G www-data -r www-data 2>/dev/null || :

%triggerun -- %name <= 4.0.48-alt7
if [ -L %_sysconfdir/cron.d/vzdump ]; then
	rm -f %_sysconfdir/cron.d/vzdump
fi

%files
%config(noreplace) %_sysconfdir/sysconfig/%name
%systemd_unitdir/%name.service
%dir %_sysconfdir/network
%ghost %_sysconfdir/network/interfaces
%ghost %_sysconfdir/cron.d/vzdump
%_sysctldir/10-pve.conf
%_bindir/create_pmxcfs_db
%_bindir/pmxcfs
%perl_vendor_autolib/PVE/IPCC
%perl_vendor_privlib/PVE/Cluster.pm
%dir %perl_vendor_privlib/PVE/Cluster
%perl_vendor_privlib/PVE/Cluster/IPCConst.pm
%perl_vendor_privlib/PVE/IPCC.pm
%dir %_localstatedir/%name
%_man8dir/pmxcfs.8*
%_prefix/lib/rpm/%name.filetrigger

%files -n libpve-cluster-perl
%_man5dir/datacenter.cfg.5*
%perl_vendor_privlib/PVE/Corosync.pm
%perl_vendor_privlib/PVE/DataCenterConfig.pm
%perl_vendor_privlib/PVE/RRD.pm
%perl_vendor_privlib/PVE/SSHInfo.pm

%files -n libpve-cluster-api-perl
%_bindir/pvecm
%_datadir/bash-completion/completions/pvecm
%_datadir/zsh/vendor-completions/_pvecm
%_man1dir/pvecm.1*
%perl_vendor_privlib/PVE/API2/*
%perl_vendor_privlib/PVE/CLI/*
%perl_vendor_privlib/PVE/Cluster/Setup.pm

%changelog
* Wed Nov 23 2022 Andrew A. Vasilyev <andy@altlinux.org> 7.2.3-alt1
- 7.2-3

* Mon Oct 03 2022 Alexey Shabalin <shaba@altlinux.org> 7.2.2-alt1
- 7.2-2

* Thu May 05 2022 Andrew A. Vasilyev <andy@altlinux.org> 7.2.1-alt1
- 7.2-1

* Mon Mar 21 2022 Alexey Shabalin <shaba@altlinux.org> 7.1.3-alt1
- 7.1-3
- build pve-access-control and pve-apiclient from separated packages
- add libpve-cluster-perl and libpve-cluster-api-perl packages

* Fri Mar 18 2022 Alexey Shabalin <shaba@altlinux.org> 7.0.3-alt2
- drop rrdcached.service and rrdcached.socket
- drop ownership /var/lib/rrdcached/{db,journal}

* Tue Jul 27 2021 Valery Inozemtsev <shrek@altlinux.ru> 7.0.3-alt1
- pve-cluster 7.0-3
- pve-access-control 7.0-4
- pve-apiclient 3.2-1

* Mon Jun 07 2021 Valery Inozemtsev <shrek@altlinux.ru> 6.4.1-alt1
- pve-cluster 6.2-1
- pve-access-control 6.4-1
- pve-apiclient 3.1-3

* Tue Dec 08 2020 Valery Inozemtsev <shrek@altlinux.ru> 6.2.1-alt1
- pve-cluster 6.2-1
- pve-access-control 6.1-3
- pve-apiclient 3.1-2

* Tue Jul 14 2020 Valery Inozemtsev <shrek@altlinux.ru> 6.1.8-alt1
- pve-cluster 6.1-8
- pve-access-control 6.1-2

* Wed Jul 08 2020 Anton Farygin <rider@altlinux.ru> 6.0.7-alt4
- add upstream patch to prevent deadlock in pmxcfs

* Thu Oct 17 2019 Valery Inozemtsev <shrek@altlinux.ru> 6.0.7-alt3
- pve-cluster 6.0-7

* Tue Oct 08 2019 Valery Inozemtsev <shrek@altlinux.ru> 6.0.6-alt2
- added filetrigger to verify configuration

* Tue Jul 30 2019 Valery Inozemtsev <shrek@altlinux.ru> 6.0.6-alt1
- pve-cluster 6.0-6
- pve-access-control 6.0-2
- pve-apiclient 3.0-2

* Mon May 20 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.0.37-alt1
- pve-cluster 5.0-37
- pve-access-control 5.1-10
- pve-apiclient 2.0-5

* Thu Feb 21 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.0.33-alt4
- use /run instead of /var/run

* Thu Jan 31 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.0.33-alt3
- rebuild with perl 5.28.1

* Wed Jan 16 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.0.33-alt2
- pve-cluster 5.0-33

* Wed Dec 12 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.0.31-alt1
- pve-cluster 5.0-31
- pve-access-control 5.1-3

* Mon Nov 19 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.0.30-alt1
- pve-cluster 5.0-30
- pve-access-control 5.1-1
- pve-apiclient 2.0-4

* Fri Sep 28 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.0.27-alt2
- removed ubt

* Wed Jul 18 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.0.27-alt1.S1
- pve-cluster 5.0-27
- pve-access-control 5.0-8

* Wed Jan 10 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.0.19-alt3.S1
- fixed corosync.conf parce

* Thu Dec 14 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.19-alt1.M80P.3
- backport to p8 branch

* Tue Dec 12 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.19-alt3
- 5.0-19

* Tue Nov 28 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.15-alt1.M80P.1
- backport to p8 branch

* Wed Nov 01 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.15-alt2
- rebuild with rrd 1.7.0

* Mon Oct 23 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.15-alt1
- 5.0-15

* Tue Oct 10 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.14-alt1
- pve-cluster 5.0-14
- pve-access-control 5.0-7

* Mon Sep 25 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.12-alt0.M80C.1
- backport to c8 branch

* Fri Aug 04 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.12-alt1.M80P.1
- backport to p8 branch

* Fri Aug 04 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.12-alt2
- replace requires openntpd to ntp-server

* Thu Jul 20 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.12-alt0.M80P.1
- backport to p8 branch

* Thu Jul 13 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.12-alt1
- 5.0-12
- pve-access-control 5.0-5

* Thu Apr 13 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.0.49-alt8.M80P.1
- backport to p8 branch

* Fri Apr 07 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.0.49-alt9
- 4.0-49

* Tue Feb 21 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.0.48-alt8
- rebuild with perl 5.24.1

* Thu Dec 08 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.48-alt7
- don't make vzdump symlink in cron.d

* Mon Dec 05 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.48-alt6
- 4.0-48

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

