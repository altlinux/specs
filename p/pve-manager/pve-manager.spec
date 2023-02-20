%global _unpackaged_files_terminate_build 1
%add_findreq_skiplist %perl_vendor_privlib/PVE/ExtMetric.pm
%add_findreq_skiplist %perl_vendor_privlib/PVE/Status/InfluxDB.pm

%define ver_major 7.2
%define ver_minor 15
Name: pve-manager
Summary: The Proxmox Virtual Environment
Version: %ver_major.%ver_minor
Release: alt4
License: AGPL-3.0+ AND GPLv3 AND MIT
Group: System/Servers
Url: https://git.proxmox.com/
Vcs: git://git.proxmox.com/git/pve-manager.git
Packager: Valery Inozemtsev <shrek@altlinux.ru>

ExclusiveArch: x86_64 aarch64

Requires: cstream lzop zstd wget schedutils gdisk hdparm rsync pciutils
Requires: perl-LWP-Protocol-https
Requires: pve-common >= 7.2.6 pve-guest-common >= 4.2.1
Requires: pve-vncterm pve-novnc >= 1.2.2 pve-spiceterm pve-xtermjs >= 4.7.1 pve-acme
Requires: pve-cluster >= 7.2.3 pve-container >= 4.0.9 pve-firewall pve-ha-manager pve-qemu-server >= 7.2.8 pve-i18n >= 1.0.3 pve-docs
Requires: proxmox-widget-toolkit >= 3.4.9 proxmox-mini-journalreader fonts-font-awesome javascript-extjs javascript-qrcodejs
Requires: libproxmox-rs-perl >= 0.2.0 libpve-rs-perl >= 0.7.1

Source: %name-%version.tar

Source6: basealt_logo.png
Source8: basealt_favicon.ico
Source9: basealt_logo-128.png

BuildRequires: pve-doc-generator >= 7.2.3 xmlto perl-Pod-Parser
BuildRequires: pve-storage >= 7.2.12 pve-cluster >= 7.2.3
BuildRequires: libpve-cluster-perl >= 6.1.6 libpve-cluster-api-perl >= 7.0.5 pve-container pve-qemu-server >= 7.2.8
BuildRequires: pve-acme pve-http-server >= 2.0.12 pve-access-control >= 7.0.2
BuildRequires: perl(AptPkg/Cache.pm) perl(File/ReadBackwards.pm) perl(Template.pm) perl(Net/DNS/Resolver.pm)
BuildRequires: unzip gnupg

%description
This package contains the PVE management tools

%prep
%setup

grep '/var/run' * -rl | while read f; do
    sed -i 's|/var/run|/run|' $f
done

%build
%make PACKAGE="pve-manager" VERSION="%ver_major-%ver_minor" PVERELEASE="%ver_major" REPOID="%release"

%install
%makeinstall_std

install -m0644 %SOURCE6 %buildroot%_datadir/%name/images/basealt_logo.png
install -m0644 %SOURCE8 %buildroot%_datadir/%name/images/favicon.ico
install -m0644 %SOURCE9 %buildroot%_datadir/%name/images/logo-128.png

# fix config backup job retention
mkdir -p %buildroot%_localstatedir/%name/jobs

mkdir -p %buildroot%_tmpfilesdir
cat << __EOF__ > %buildroot%_tmpfilesdir/%name.conf
d /run/pveproxy 0700 www-data www-data -
f /var/lock/pveproxy.lck 0644 www-data www-data
f /var/lock/spiceproxy.lck 0644 www-data www-data
__EOF__

# Cleanup
rm -rf %buildroot%_sysconfdir/apt
rm -rf %buildroot%_sysconfdir/initramfs-tools
rm -f  %buildroot%_sysconfdir/modprobe.d/pve-blacklist.conf
rm -rf %buildroot%_sysconfdir/network
rm -f  %buildroot%_unitdir/pve-daily-update.service
rm -f  %buildroot%_unitdir/pve-daily-update.timer
rm -f  %buildroot%_unitdir/pvebanner.service
rm -f  %buildroot%_unitdir/pvenetcommit.service
rm -f  %buildroot%_bindir/pvebanner
rm -f  %buildroot%_bindir/pvesubscription
rm -f  %buildroot%_bindir/pveupgrade
rm -f  %buildroot%_datadir/doc/pve-manager/aplinfo.dat
rm -f  %buildroot%_man1dir/pvesubscription.1*
rm -f  %buildroot%_man1dir/pveupgrade.1*

%post
%post_service pvedaemon
%post_service pvestatd
%post_service pveproxy
%post_service spiceproxy
%post_service pvescheduler

%preun
%preun_service pvedaemon
%preun_service pveproxy
%preun_service pvestatd
%preun_service spiceproxy
%preun_service pvescheduler

%files
%_datadir/doc/%name
%_datadir/bash-completion/completions/*
%_datadir/zsh/vendor-completions/*
%_sysconfdir/logrotate.d/pve
%config(noreplace) %_sysconfdir/vzdump.conf
%_unitdir/*
%_tmpfilesdir/%name.conf
%_bindir/*
%perl_vendor_privlib/PVE/*.pm
%perl_vendor_privlib/PVE/API2/*.pm
%perl_vendor_privlib/PVE/API2/Hardware
%perl_vendor_privlib/PVE/API2/Ceph
%perl_vendor_privlib/PVE/API2/Cluster
%perl_vendor_privlib/PVE/CLI/*.pm
%perl_vendor_privlib/PVE/Ceph
%perl_vendor_privlib/PVE/Jobs
%perl_vendor_privlib/PVE/Service
%perl_vendor_privlib/PVE/Status
%_datadir/pve-manager
%_localstatedir/pve-manager
%_localstatedir/vz
%attr(0770,root,www-data) %_logdir/pveproxy
%_man1dir/*
%_man8dir/*

%changelog
* Mon Feb 20 2023 Alexey Shabalin <shaba@altlinux.org> 7.2.15-alt4
- change delimiter between major and minor parts of the VERSION

* Sat Feb 04 2023 Alexey Shabalin <shaba@altlinux.org> 7.2.15-alt3
- package /var/lib/pve-manage/jobs for fix config backup jobs

* Thu Jan 12 2023 Alexey Shabalin <shaba@altlinux.org> 7.2.15-alt2
- fix show version

* Wed Nov 23 2022 Andrew A. Vasilyev <andy@altlinux.org> 7.2.15-alt1
- 7.2-15

* Wed Nov 16 2022 Andrew A. Vasilyev <andy@altlinux.org> 7.2.12-alt2
- fix "Outdated OSDs"
- do not add proxmox-offline-mirror-helper package

* Mon Nov 14 2022 Alexey Shabalin <shaba@altlinux.org> 7.2.12-alt1
- 7.2-12

* Tue Nov 08 2022 Andrew A. Vasilyev <andy@altlinux.org> 7.2.11-alt2
- fix for Help button in Notes Editor

* Mon Oct 03 2022 Alexey Shabalin <shaba@altlinux.org> 7.2.11-alt1
- 7.2-11

* Wed Jul 06 2022 Andrew A. Vasilyev <andy@altlinux.org> 7.2.6-alt1
- 7.2-6

* Thu May 05 2022 Andrew A. Vasilyev <andy@altlinux.org> 7.2.3-alt1
- 7.2-3

* Wed Mar 16 2022 Alexey Shabalin <shaba@altlinux.org> 7.1.10-alt1
- 7.1-10
- build pve-manager only, all other build as separated packages.

* Mon Jan 24 2022 Alexey Shabalin <shaba@altlinux.org> 7.0.11-alt5
- build with external packages:
  + proxmox-mini-journalreader
  + proxmox-widget-toolkit
  + pve-i18n
  + javascript-extjs
  + javascript-bootstrap
  + javascript-jquery

* Sun Nov 07 2021 Valery Inozemtsev <shrek@altlinux.ru> 7.0.11-alt4
- pve-mini-journalreader, pve-widget-toolkit moved to subpackages

* Fri Oct 22 2021 Valery Inozemtsev <shrek@altlinux.ru> 7.0.11-alt3
- package trustedkeys.gpg to make pveam functioning

* Mon Oct 04 2021 Andrew A. Vasilyev <andy@altlinux.org> 7.0.11-alt2
- restart network to apply new settings, no need for ifupdown2

* Thu Sep 23 2021 Valery Inozemtsev <shrek@altlinux.ru> 7.0.11-alt1
- pve-manager 7.0-11
- pve-container 4.0-9
- pve-firewall 4.2-2
- pve-ha-manager 3.3-1
- qemu-server 7.0-13
- pve-guest-common 4.0-2
- pve-http-server 4.0-2
- pve-widget-toolkit 3.3-6
- pve-i18n 2.5-1

* Thu Jul 08 2021 Valery Inozemtsev <shrek@altlinux.ru> 6.3.3-alt5
- pve-container@.service wants pve-lxc-syscalld.service

* Mon Jun 28 2021 Valery Inozemtsev <shrek@altlinux.ru> 6.3.3-alt4
- pve-guests.service wants qmeventd.service

* Mon May 31 2021 Valery Inozemtsev <shrek@altlinux.ru> 6.3.3-alt3
- qemu-server: naming network interfaces as in branch p9

* Tue May 18 2021 Andrew A. Vasilyev <andy@altlinux.org> 6.3.3-alt2
- merge changelog with p9

* Fri Dec 11 2020 Valery Inozemtsev <shrek@altlinux.ru> 6.3.3-alt1
- pve-manager 6.3-3
- pve-container 3.3-2
- pve-firewall 4.1-3
- pve-ha-manager 3.1-1
- qemu-server 6.3-2
- pve-guest-common 3.1-3
- pve-http-server 3.1-1
- pve-widget-toolkit 2.4-3
- pve-i18n 2.2-2
- pve-acme 1.0.6

* Fri Oct 09 2020 Valery Inozemtsev <shrek@altlinux.ru> 6.2.4-alt2
- fixed booting VM on Kunpeng-920

* Fri Oct 09 2020 Valery Inozemtsev <shrek@altlinux.ru> 6.2.4-alt1.M90P.1
- fixed booting VM on Kunpeng-920

* Mon Aug 24 2020 Valery Inozemtsev <shrek@altlinux.ru> 6.2.4-alt1
- pve-manager 6.2-4
- pve-container 3.1-5
- pve-firewall 4.1-2
- qemu-server 6.2-2
- pve-ha-manager 3.0-9
- pve-guest-common 3.0-10
- pve-http-server 3.0-5
- pve-widget-toolkit 2.2-1
- pve-i18n 2.1-3
- pve-acme 1.0.4

* Fri Jul 17 2020 Valery Inozemtsev <shrek@altlinux.ru> 6.0.7-alt10
- fixed pvecfg.pm (closes: #38725)

* Wed Jan 22 2020 Valery Inozemtsev <shrek@altlinux.ru> 6.0.7-alt9
- qemu-server: fixed qxl display

* Tue Jan 21 2020 Valery Inozemtsev <shrek@altlinux.ru> 6.0.7-alt8
- pve-widget-toolkit: merged some upstream patches

* Wed Jan 15 2020 Valery Inozemtsev <shrek@altlinux.ru> 6.0.7-alt7
- fixed get/set timezone

* Thu Nov 28 2019 Valery Inozemtsev <shrek@altlinux.ru> 6.0.7-alt6
- qemu-server 6.0-9

* Wed Nov 20 2019 Valery Inozemtsev <shrek@altlinux.ru> 6.0.7-alt5
- pve-firewall 4.0-8
- fixed mini-journalreader on aarch64

* Wed Nov 13 2019 Valery Inozemtsev <shrek@altlinux.ru> 6.0.7-alt4
- fixed creation/launch of VM on aarch64 (closes: #37441)

* Thu Oct 17 2019 Valery Inozemtsev <shrek@altlinux.ru> 6.0.7-alt3
- fixed start pve-firewall

* Wed Sep 18 2019 Valery Inozemtsev <shrek@altlinux.ru> 6.0.7-alt2
- pve-manager 6.0-7
- pve-container 3.0-7

* Mon Aug 26 2019 Valery Inozemtsev <shrek@altlinux.ru> 6.0.6-alt1
- pve-manager 6.0-6
- pve-widget-toolkit 2.0-7

* Tue Aug 06 2019 Valery Inozemtsev <shrek@altlinux.ru> 6.0.5-alt1
- pve-manager 6.0-5
- pve-container 3.0-5
- pve-firewall 4.0-7
- qemu-server 6.0-7
- pve-ha-manager 3.0-2
- pve-guest-common 3.0-1
- pve-http-server 3.0-2
- pve-widget-toolkit 2.0-5
- pve-i18n 2.0-2

* Tue Jun 25 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.4.6-alt3
- fixed aarch64 VM parameters

* Fri May 24 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.4.6-alt2
- pve-mini-journalreader 1.1-1

* Mon May 20 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.4.6-alt1
- pve-manager 5.4-6
- pve-container 2.0-39
- pve-firewall 3.0-21
- qemu-server 5.0-51
- pve-ha-manager 2.0-9
- pve-guest-common 2.0-20
- pve-http-server 2.0-13
- pve-widget-toolkit 1.0-28
- pve-i18n 1.1-4

* Fri Feb 01 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.3.8-alt11
- pve-manager 5.3-8
- pve-container 2.0-33
- pve-firewall 3.0-17
- qemu-server 5.0-45
- pve-ha-manager 2.0-6
- pve-guest-common 2.0-19

* Wed Dec 12 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.3.5-alt10
- pve-manager 5.3-5
- pve-container 2.0-31
- pve-firewall 3.0-16
- qemu-server 5.0-43
- pve-widget-toolkit 1.0-22
- extjs 6.0.1-2
- pve-i18n 1.0-9

* Mon Nov 26 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.3.3-alt9
- pve-manager 5.3-3
- pve-container 2.0-30
- pve-firewall 3.0-15
- qemu-server 5.0-42
- pve-guest-common 2.0-18

* Wed Oct 10 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.2.3-alt8
- pve-http-server 2.0-11

* Thu Oct 04 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.2.3-alt7
- updated russian translation

* Tue Oct 02 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.2.3-alt6
- pve-firewall 3.0-12

* Fri Sep 28 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.2.3-alt5
- removed ubt

* Wed Sep 19 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.2.3-alt4.S1
- fixed version check qemu 3.0.0

* Tue Sep 04 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.2.3-alt3.S1
- pve-manager 5.2-3
- qemu-server 5.0-27

* Thu Aug 09 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.2.2-alt2.S1
- updated russian translation

* Wed Jul 18 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.2.2-alt1.S1
- pve-manager 5.2-2
- pve-container 2.0-24
- pve-firewall 3.0-10
- pve-ha-manager 2.0-5
- qemu-server 5.0-26
- pve-guest-common 2.0-17
- pve-http-server 2.0-9

* Wed Jan 10 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.1.39-alt3.S1
- merged patches PCID flags from upstream

* Thu Dec 14 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.1.39-alt1.M80P.3
- backport to p8 branch

* Tue Dec 12 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.1.39-alt3
- pve-manager 5.1-39
- pve-firewall 3.0-5
- pve-ha-manager 2.0-4
- pve-http-server 2.0-8

* Tue Nov 28 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.1.35-alt1.M80P.1
- backport to p8 branch

* Mon Oct 23 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.1.35-alt2
- pve-manager 5.1-35

* Mon Oct 23 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.34-alt1
- pve-manager 5.0-34
- pve-container 2.0-17
- pve-firewall 3.0-3
- pve-ha-manager 2.0-3
- qemu-server 5.0-17
- pve-guest-common 2.0-13
- pve-http-server 2.0-6

* Mon Sep 25 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt5.M80C.8
- backport to c8 branch

* Thu Sep 21 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt5.M80P.8
- fixed creation osd in ceph 10

* Tue Sep 19 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt4.M80P.8
- backport to p8 branch

* Tue Sep 19 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt8
- pve-container 2.0-16

* Wed Aug 09 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt4.M80P.1
- backport to p8 branch

* Wed Aug 09 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt7
- don't uses ssh if install vzdump.cron to localhost (closes: #33746)
- qemu-server 5.0-15

* Fri Aug 04 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt3.M80P.1
- backport to p8 branch

* Fri Aug 04 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt6
- updates services list

* Thu Aug 03 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt2.M80P.1
- backport to p8 branch

* Thu Aug 03 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt5
- do not use force when migrating vm uses local device

* Tue Aug 01 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt1.M80P.1
- backport to p8 branch

* Tue Aug 01 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt4
- fixed FontAwesome path

* Tue Jul 25 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt3
- pve-container 2.0-15
- qemu-server 5.0-14

* Thu Jul 20 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.24-alt2
- pve-manager 5.0-24
- pve-firewall 3.0-2

* Thu Jul 20 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.23-alt0.M80P.1
- backport to p8 branch

* Mon Jul 17 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.23-alt1
- pve-manager 5.0-23
- pve-container 2.0-14
- qemu-server 5.0-13
- pve-ha-manager 2.0-2
- pve-guest-common 2.0-11
- pve-http-server 2.0-5

* Wed Jul 05 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.4.1-alt15
- removed "Package version" button (closes: #33615)

* Tue Jun 20 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.4.1-alt14
- firewall now works

* Wed Jun 14 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.4.1-alt13
- fixed date/time column resize in snapshots (closes: #33528)

* Mon May 15 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.4.1-alt12
- pve-container: added lxcnetdelbr script

* Thu May 11 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.4.1-alt11
- various fixes

* Thu Apr 20 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.4.1-alt10
- fixed create/start unprivileged container

* Tue Apr 18 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.4.1-alt9
- fixed creation of containers by the user

* Mon Mar 27 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.4.1-alt8
- added LSI Logic SAS 1068 support

* Sat Mar 25 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.4.1-alt7
- corrected the names of MegaRAID SAS controllers

* Sat Mar 25 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.4.1-alt6
- added LSI MegaRAID SAS 2108 support

* Mon Feb 20 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.4.1-alt5
- fixed node network status

* Mon Dec 12 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.4.1-alt4
- 4.4-1
- pve-container 1.0-88

* Thu Dec 08 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.14-alt3
- install regular file to cron.d (closes: #32835)

* Wed Dec 07 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.14-alt2
- 4.3-14
- qemu-server 4.0-101

* Mon Dec 05 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.13-alt1
- 4.3-13
- pve-container 1.0-87
- pve-firewall 2.0-33
- pve-ha-manager 1.0-38
- qemu-server 4.0-100

* Mon Nov 28 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.12-alt10
- 4.3-12

* Thu Nov 24 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.11-alt9
- pve-container 1.0-84

* Wed Nov 23 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.11-alt8
- 4.3-11
- pve-container 1.0-83
- pve-ha-manager 1.0-37
- qemu-server 4.0-96

* Fri Oct 21 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.6-alt7
- 4.3-6
- qemu-server 4.0-92

* Sun Oct 09 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.3-alt6
- 4.3-3
- qemu-server 4.0-91
- pve-firewall 2.0-31

* Mon Oct 03 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.23-alt5
- qemu-server 4.0-89
- pve-container 1.0-78

* Mon Sep 26 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.23-alt4
- requires pve-docs

* Thu Sep 22 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.23-alt3
- 4.2-23
- pve-container 1.0-75

* Wed Sep 21 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.21-alt2
- added support altlinux container

* Mon Sep 19 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.21-alt1
- 4.2-21
- pve-container 1.0-74
- pve-firewall 2.0-30
- pve-ha-manager 1.0-35
- qemu-server 4.0-88

* Mon Sep 05 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.18-alt9
- Network Device: replace rate limit MB/s to MBit/s

* Mon Aug 22 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.18-alt8
- 4.2-18
- pve-container 1.0-73
- pve-ha-manager 1.0-33
- qemu-server 4.0-85

* Fri Jul 08 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.16-alt7
- 4.2-16
- pve-ha-manager 1.0-32

* Tue Jun 28 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.15-alt6
- pve-container 1.0-70

* Sun Jun 26 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.15-alt5
- pve-container: requires pve-lxc

* Tue Jun 21 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.15-alt4
- pve-manager 4.2-15
- qemu-server 4.0-83

* Wed Jun 15 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.14-alt3
- 4.2-14

* Tue Jun 07 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.11-alt2
- rebuild

* Mon Jun 06 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.11-alt1
- 4.2-11

* Mon Feb 08 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.1.10-alt1
- update version

* Thu Dec 10 2015 Valery Inozemtsev <shrek@altlinux.ru> 4.0.64-alt1
- initial release

