Name: pve-manager
Summary: The Proxmox Virtual Environment
Version: 4.2.15
Release: alt6
License: GPLv3
Group: System/Servers
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

ExclusiveArch: x86_64
Requires: cstream lzop pve-vncterm pve-novnc pve-spiceterm
Requires: ceph gdisk parted hdparm

Source0: pve-manager.tar.xz
Source1: pve-container.tar.xz
Source2: pve-firewall.tar.xz
Source3: pve-ha-manager.tar.xz
Source4: qemu-server.tar.xz
Source5: pve-manager-altwww.patch
Source6: basealt_logo.png

Source10: 50-rbd.rules
Source11: 60-ceph-partuuid-workaround.rules
Source12: 95-ceph-osd.rules

Patch1: pve-manager-alt.patch
Patch2: pve-firewall-alt.patch
Patch3: pve-ha-manager-alt.patch
Patch4: pve-container-alt.patch
Patch5: qemu-server-alt.patch

BuildRequires: glib2-devel libnetfilter_log-devel pve-doc-generator pve-storage librados2-perl libsystemd-daemon-devel
BuildRequires: perl-AnyEvent-AIO perl-AnyEvent-HTTP perl-AptPkg perl-Crypt-SSLeay perl-File-ReadBackwards
BuildRequires: perl-IO-Multiplex perl-Locale-PO perl-UUID unzip xmlto
BuildRequires: perl(File/Sync.pm) perl(Net/DNS/Resolver.pm) perl(Pod/Select.pm)

%description
This package contains the Proxmox Virtual Environment management tools

%package -n pve-container
Summary: Proxmox VE Container management tool
Version: 1.0.70
Group: Development/Perl
Requires: pve-lxc dtach

%description -n pve-container
Tool to manage Linux Containers on Proxmox VE

%package -n pve-firewall
Summary: Proxmox VE Firewall
Version: 2.0.29
Group: System/Servers
Requires: ipset iptables iptables-ipv6

%description -n pve-firewall
This package contains the Proxmox VE Firewall

%package -n pve-ha-manager
Summary: Proxmox VE HA Manager
Version: 1.0.31
Group: System/Servers

%description -n pve-ha-manager
HA Manager Proxmox VE

%package -n pve-qemu-server
Summary: Qemu Server Tools
Version: 4.0.83
Group: System/Servers
Requires: nc6 pve-qemu-system socat
Provides: qemu-server = %version-%release
Obsoletes: qemu-server < %version-%release

%description -n pve-qemu-server
This package contains the Qemu Server tools used by Proxmox VE

%add_findreq_skiplist %_datadir/cluster/pvevm
%add_findreq_skiplist %perl_vendor_privlib/PVE/HA/Env/PVE2.pm

%prep
%setup -q -c -n pve -a1 -a2 -a3 -a4
%patch1 -p0 -b .alt
%patch2 -p0 -b .alt
%patch3 -p0 -b .alt
%patch4 -p0 -b .alt
%patch5 -p0 -b .alt

install -m0644 %SOURCE5 pve-manager/www/manager6/

%build
for d in pve-manager pve-firewall/src pve-ha-manager/src qemu-server; do
    pushd $d
    %make
    popd
done

%install
for d in pve-manager pve-firewall/src pve-ha-manager/src pve-container/src qemu-server; do
    pushd $d
    %make DESTDIR=%buildroot install
    popd
done

mkdir -p %buildroot%_datadir/pve-docs

install -m0644 %SOURCE6 %buildroot%_datadir/pve-manager/images/basealt_logo.png

install -m0644 pve-firewall/debian/*.service %buildroot%systemd_unitdir/
install -m0644 pve-firewall/debian/pve-firewall.logrotate %buildroot%_sysconfdir/logrotate.d/pve-firewall
mkdir -p %buildroot%_localstatedir/pve-firewall

install -m0644 pve-ha-manager/debian/*.service %buildroot%systemd_unitdir/

mkdir -p %buildroot/lib/tmpfiles.d
cat << __EOF__ > %buildroot/lib/tmpfiles.d/%name.conf
d /var/run/pveproxy 0700 www-data www-data -
f /var/lock/pveproxy.lck 0644 www-data www-data
f /var/lock/spiceproxy.lck 0644 www-data www-data
__EOF__

cat << __EOF__ > %buildroot%_datadir/doc/%name/rrdcached.sysconfig
RRDCACHED_USER="root"
OPTS="-j /var/lib/rrdcached/journal/ -F -b /var/lib/rrdcached/db/ -B"
SOCKFILE="/var/run/rrdcached.sock"
SOCKPERMS=0660
__EOF__

install -m0644 %SOURCE10 %buildroot%_datadir/doc/%name/
install -m0644 %SOURCE11 %buildroot%_datadir/doc/%name/
install -m0644 %SOURCE12 %buildroot%_datadir/doc/%name/

%post
%post_service pvedaemon
%post_service pveproxy
%post_service pvestatd
%post_service spiceproxy

%preun
%preun_service pvedaemon
%preun_service pveproxy
%preun_service pvestatd
%preun_service spiceproxy

%post -n pve-firewall
%post_service pve-firewall
%post_service pvefw-logger

%preun -n pve-firewall
%preun_service pve-firewall
%preun_service pvefw-logger

%files
%_sysconfdir/bash_completion.d/pveam
%_sysconfdir/bash_completion.d/pveceph
%_sysconfdir/bash_completion.d/pvedaemon
%_sysconfdir/bash_completion.d/pveproxy
%_sysconfdir/bash_completion.d/pvestatd
%_sysconfdir/bash_completion.d/pvesubscription
%_sysconfdir/bash_completion.d/spiceproxy
%_sysconfdir/bash_completion.d/vzdump
%_sysconfdir/logrotate.d/pve
%config(noreplace) %_sysconfdir/vz/vznet.conf
%config(noreplace) %_sysconfdir/vzdump.conf
#systemd_unitdir/pvebanner.service
%systemd_unitdir/pvedaemon.service
%systemd_unitdir/pve-manager.service
#systemd_unitdir/pvenetcommit.service
%systemd_unitdir/pveproxy.service
%systemd_unitdir/pvestatd.service
%systemd_unitdir/spiceproxy.service
/lib/tmpfiles.d/%name.conf
%_bindir/pveam
#_bindir/pvebanner
%_bindir/pveceph
%_bindir/pvedaemon
%_bindir/pvemailforward
%_bindir/pvemailforward.pl
%_bindir/pveperf
%_bindir/pveproxy
%_bindir/pvereport
%_bindir/pvesh
%_bindir/pvestatd
%_bindir/pvesubscription
%_bindir/pveupdate
#_bindir/pveupgrade
%_bindir/pveversion
%_bindir/spiceproxy
%_bindir/vzdump
%dir %_datadir/cluster
%dir %_datadir/pve-docs
%attr(0755,root,root) %_datadir/cluster/pvevm
%dir %perl_vendor_privlib/PVE
%dir %perl_vendor_privlib/PVE/API2
%dir %perl_vendor_privlib/PVE/CLI
%dir %perl_vendor_privlib/PVE/Service
%dir %perl_vendor_privlib/PVE/Status
%dir %perl_vendor_privlib/PVE/VZDump
%perl_vendor_privlib/PVE/API2/Formatter
%perl_vendor_privlib/PVE/API2Client.pm
%perl_vendor_privlib/PVE/API2.pm
%perl_vendor_privlib/PVE/API2Tools.pm
%perl_vendor_privlib/PVE/APLInfo.pm
%perl_vendor_privlib/PVE/AutoBalloon.pm
%perl_vendor_privlib/PVE/CephTools.pm
%perl_vendor_privlib/PVE/ExtJSIndex.pm
%perl_vendor_privlib/PVE/HTTPServer.pm
%perl_vendor_privlib/PVE/NoVncIndex.pm
%perl_vendor_privlib/PVE/pvecfg.pm
%perl_vendor_privlib/PVE/Report.pm
%perl_vendor_privlib/PVE/REST.pm
%perl_vendor_privlib/PVE/TouchIndex.pm
%perl_vendor_privlib/PVE/VZDump.pm
%perl_vendor_privlib/PVE/API2/APT.pm
%perl_vendor_privlib/PVE/API2/Backup.pm
%perl_vendor_privlib/PVE/API2/Ceph.pm
%perl_vendor_privlib/PVE/API2/Cluster.pm
%perl_vendor_privlib/PVE/API2/HAConfig.pm
%perl_vendor_privlib/PVE/API2/Network.pm
%perl_vendor_privlib/PVE/API2/Nodes.pm
%perl_vendor_privlib/PVE/API2/Pool.pm
%perl_vendor_privlib/PVE/API2/Services.pm
%perl_vendor_privlib/PVE/API2/Subscription.pm
%perl_vendor_privlib/PVE/API2/Tasks.pm
%perl_vendor_privlib/PVE/API2/VZDump.pm
%perl_vendor_privlib/PVE/CLI/pveceph.pm
%perl_vendor_privlib/PVE/CLI/pvesubscription.pm
%perl_vendor_privlib/PVE/CLI/vzdump.pm
%perl_vendor_privlib/PVE/Service/pvedaemon.pm
%perl_vendor_privlib/PVE/Service/pveproxy.pm
%perl_vendor_privlib/PVE/Service/pvestatd.pm
%perl_vendor_privlib/PVE/Service/spiceproxy.pm
%perl_vendor_privlib/PVE/Status/Graphite.pm
%perl_vendor_privlib/PVE/Status/InfluxDB.pm
%perl_vendor_privlib/PVE/Status/Plugin.pm
%perl_vendor_privlib/PVE/VZDump/Plugin.pm
%perl_vendor_privlib/PVE/CLI/pveam.pm
%_datadir/pve-manager
%_localstatedir/pve-manager
%dir %_localstatedir/vz/images
%dir %_localstatedir/vz/template/iso
%dir %_localstatedir/vz/template/qemu
%attr(0700,www-data,www-data) %_logdir/pveproxy
%_man1dir/pveceph.1*
%_man1dir/pveperf.1*
%_man1dir/pvereport.1*
%_man1dir/pvesh.1*
%_man1dir/pvesubscription.1*
#_man1dir/pveupgrade.1*
%_man1dir/pveversion.1*
%_man1dir/vzdump.1*
%_man1dir/pveam.1.xz
%_man8dir/pvedaemon.8*
%_man8dir/pveproxy.8*
%_man8dir/pvestatd.8*
%_man8dir/spiceproxy.8*
%dir %_datadir/doc/%name
%_datadir/doc/%name/aplinfo.dat
%_datadir/doc/%name/*.pubkey
%_datadir/doc/%name/*.rules
%_datadir/doc/%name/rrdcached.sysconfig

%files -n pve-container
%_sysconfdir/bash_completion.d/pct
%_sbindir/pct
%_sbindir/pve-update-lxc-config
%_datadir/lxc
%dir %perl_vendor_privlib/PVE
%dir %perl_vendor_privlib/PVE/API2
%dir %perl_vendor_privlib/PVE/CLI
%dir %perl_vendor_privlib/PVE/VZDump
%perl_vendor_privlib/PVE/LXC
%perl_vendor_privlib/PVE/LXC.pm
%perl_vendor_privlib/PVE/API2/LXC
%perl_vendor_privlib/PVE/API2/LXC.pm
%perl_vendor_privlib/PVE/CLI/pct.pm
%perl_vendor_privlib/PVE/VZDump/ConvertOVZ.pm
%perl_vendor_privlib/PVE/VZDump/LXC.pm
%_man1dir/pct.1*
%_man5dir/*ct.conf.5*

%files -n pve-firewall
%_sysconfdir/bash_completion.d/pve-firewall
%_sysconfdir/logrotate.d/pve-firewall
#_sysconfdir/sysctl.d/pve-firewall.conf
%systemd_unitdir/pve-firewall.service
%systemd_unitdir/pvefw-logger.service
%_sbindir/pve-firewall
%_sbindir/pvefw-logger
%dir %perl_vendor_privlib/PVE
%dir %perl_vendor_privlib/PVE/API2
%dir %perl_vendor_privlib/PVE/Service
%perl_vendor_privlib/PVE/Firewall.pm
%perl_vendor_privlib/PVE/FirewallSimulator.pm
%perl_vendor_privlib/PVE/API2/Firewall
%perl_vendor_privlib/PVE/Service/pve_firewall.pm
%_localstatedir/pve-firewall
%_man8dir/pve-firewall.8*

%files -n pve-ha-manager
%_sysconfdir/bash_completion.d/ha-manager
%_sysconfdir/bash_completion.d/pve-ha-crm
%_sysconfdir/bash_completion.d/pve-ha-lrm
%systemd_unitdir/pve-ha-crm.service
%systemd_unitdir/pve-ha-lrm.service
%systemd_unitdir/watchdog-mux.service
%_sbindir/ha-manager
%_sbindir/pve-ha-crm
%_sbindir/pve-ha-lrm
%_sbindir/watchdog-mux
%dir %perl_vendor_privlib/PVE
%dir %perl_vendor_privlib/PVE/API2
%dir %perl_vendor_privlib/PVE/CLI
%dir %perl_vendor_privlib/PVE/HA
%dir %perl_vendor_privlib/PVE/Service
%dir %perl_vendor_privlib/PVE/HA/Resources
%perl_vendor_privlib/PVE/API2/HA
%perl_vendor_privlib/PVE/CLI/ha_manager.pm
%perl_vendor_privlib/PVE/HA/Env
%perl_vendor_privlib/PVE/HA/Config.pm
%perl_vendor_privlib/PVE/HA/CRM.pm
%perl_vendor_privlib/PVE/HA/Env.pm
%perl_vendor_privlib/PVE/HA/Groups.pm
%perl_vendor_privlib/PVE/HA/LRM.pm
%perl_vendor_privlib/PVE/HA/Manager.pm
%perl_vendor_privlib/PVE/HA/NodeStatus.pm
%perl_vendor_privlib/PVE/HA/Resources.pm
%perl_vendor_privlib/PVE/HA/Tools.pm
%perl_vendor_privlib/PVE/HA/Fence.pm
%perl_vendor_privlib/PVE/HA/FenceConfig.pm
%perl_vendor_privlib/PVE/Service/pve_ha_crm.pm
%perl_vendor_privlib/PVE/Service/pve_ha_lrm.pm
%perl_vendor_privlib/PVE/HA/Resources/PVEVM.pm
%perl_vendor_privlib/PVE/HA/Resources/PVECT.pm
%_man1dir/ha-manager.1*
%_man8dir/pve-ha-crm.8*
%_man8dir/pve-ha-lrm.8*

%files -n pve-qemu-server
%_sysconfdir/bash_completion.d/qm
%_sysconfdir/bash_completion.d/qmrestore
%_prefix/lib/qemu-server
%_sbindir/qm
%_sbindir/qmrestore
%dir %perl_vendor_privlib/PVE
%dir %perl_vendor_privlib/PVE/API2
%dir %perl_vendor_privlib/PVE/CLI
%dir %perl_vendor_privlib/PVE/VZDump
%dir %perl_vendor_privlib/PVE/QemuServer
%perl_vendor_privlib/PVE/QemuMigrate.pm
%perl_vendor_privlib/PVE/QemuServer.pm
%perl_vendor_privlib/PVE/QemuConfig.pm
%perl_vendor_privlib/PVE/QMPClient.pm
%perl_vendor_privlib/PVE/API2/Qemu.pm
%perl_vendor_privlib/PVE/CLI/qm.pm
%perl_vendor_privlib/PVE/CLI/qmrestore.pm
%perl_vendor_privlib/PVE/VZDump/QemuServer.pm
%perl_vendor_privlib/PVE/QemuServer/Memory.pm
%perl_vendor_privlib/PVE/QemuServer/PCI.pm
%perl_vendor_privlib/PVE/QemuServer/USB.pm
%_datadir/qemu-server
%_localstatedir/qemu-server
%_man1dir/qm.1*
%_man1dir/qmrestore.1*
%_man5dir/*m.conf.5*

%changelog
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

