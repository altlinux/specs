%define _libexecdir %_prefix/libexec
Name: tuned
Version: 2.13.0
Release: alt1

Summary: A dynamic adaptive system tuning daemon

License: GPLv2+
Group: System/Configuration/Hardware
Url: https://fedorahosted.org/tuned/

# Source-url: https://github.com/redhat-performance/tuned/archive/v%version.tar.gz
Source: %name-%version.tar
Source1: tuned.init

Patch0: tuned-2.7.1-pkexec-fix.patch
Patch1: tuned-2.7.1-profile_info-traceback-fix.patch
Patch2: tuned-2.7.1-throughput-performance-summary.patch

BuildArch: noarch

BuildRequires: desktop-file-utils asciidoctor

Requires: virt-what ethtool hdparm util-linux polkit

#Requires(post): systemd
#Requires(preun): systemd
#Requires(postun): systemd

BuildRequires(pre): rpm-build-python3 rpm-build-intro
BuildRequires: python3-dev

# BuildRequires for 'make test'
#BuildRequires: python3-module-unittest2, python3-module-configobj, python3-module-mock

%py3_use decorator
%py3_use pyudev
%py3_use configobj
#py3_use schedutils
#py3_use linux-procfs
#py3_use perf
%py3_use dbus
%py3_use pygobject3

# Recommends: python3-dmidecode
#Recommends: kernel-tools
#Requires: python3-module-syspurpose

%define tuneddir %_prefix/lib/tuned

%description
The tuned package contains a daemon that tunes system settings dynamically.
It does so by monitoring the usage of several system components periodically.
Based on that information components will then be put into lower or higher
power saving modes to adapt to the current usage. Currently only ethernet
network and ATA harddisk devices are implemented.

%package gtk
Summary: GTK GUI for tuned
Group: System/Configuration/Other
Requires: %name = %EVR
Requires: powertop polkit

%description gtk
GTK GUI that can control tuned and provides simple profile editor.

%package utils
Group: System/Configuration/Other
Requires: %name = %EVR
Requires: powertop
Summary: Various tuned utilities

%description utils
This package contains utilities that can help you to fine tune and
debug your system and manage tuned profiles.

%package utils-systemtap
Group: System/Configuration/Other
Summary: Disk and net statistic monitoring systemtap scripts
Requires: %name = %EVR
Requires: systemtap

%description utils-systemtap
This package contains several systemtap scripts to allow detailed
manual monitoring of the system. Instead of the typical IO/sec it collects
minimal, maximal and average time between operations to be able to
identify applications that behave power inefficient (many small operations
instead of fewer large ones).

%package profiles-sap
Group: System/Configuration/Other
Summary: Additional tuned profile(s) targeted to SAP NetWeaver loads
Requires: %name = %EVR

%description profiles-sap
Additional tuned profile(s) targeted to SAP NetWeaver loads.

%package profiles-mssql
Group: System/Configuration/Other
Summary: Additional tuned profile(s) for MS SQL Server
Requires: %name = %EVR

%description profiles-mssql
Additional tuned profile(s) for MS SQL Server.

%package profiles-oracle
Group: System/Configuration/Other
Summary: Additional tuned profile(s) targeted to Oracle loads
Requires: %name = %EVR

%description profiles-oracle
Additional tuned profile(s) targeted to Oracle loads.

%package profiles-sap-hana
Group: System/Configuration/Other
Summary: Additional tuned profile(s) targeted to SAP HANA loads
Requires: %name = %EVR

%description profiles-sap-hana
Additional tuned profile(s) targeted to SAP HANA loads.

%package profiles-atomic
Group: System/Configuration/Other
Summary: Additional tuned profile(s) targeted to Atomic
Requires: %name = %EVR

%description profiles-atomic
Additional tuned profile(s) targeted to Atomic host and guest.

%package profiles-realtime
Group: System/Configuration/Other
Summary: Additional tuned profile(s) targeted to realtime
Requires: %name = %EVR
Requires: tuna

%description profiles-realtime
Additional tuned profile(s) targeted to realtime.

%package profiles-nfv-guest
Group: System/Configuration/Other
Summary: Additional tuned profile(s) targeted to Network Function Virtualization (NFV) guest
Requires: %name = %EVR
Requires: %name-profiles-realtime = %EVR
Requires: tuna

%description profiles-nfv-guest
Additional tuned profile(s) targeted to Network Function Virtualization (NFV) guest.

%package profiles-nfv-host
Group: System/Configuration/Other
Summary: Additional tuned profile(s) targeted to Network Function Virtualization (NFV) host
Requires: %name = %EVR
Requires: %name-profiles-realtime = %EVR
Requires: tuna
#Recommends: tuned-profiles-nfv-host-bin

%description profiles-nfv-host
Additional tuned profile(s) targeted to Network Function Virtualization (NFV) host.

%package profiles-cpu-partitioning
Group: System/Configuration/Other
Summary: Additional tuned profile(s) optimized for CPU partitioning
Requires: %name = %EVR

%description profiles-cpu-partitioning
Additional tuned profile(s) optimized for CPU partitioning.

%package profiles-compat
Group: System/Configuration/Other
Summary: Additional tuned profiles mainly for backward compatibility with tuned 1.0
Requires: %name = %EVR

%description profiles-compat
Additional tuned profiles mainly for backward compatibility with tuned 1.0.
It can be also used to fine tune your system for specific scenarios.

%prep
%setup
#patch0 -p1
#patch1 -p1
#patch2 -p1

%build
make html PYTHON=%__python3

%install
%makeinstall_std DOCDIR=%_docdir/%name
%__subst 's/\(dynamic_tuning[ \t]*=[ \t]*\).*/\10/' %buildroot%_sysconfdir/tuned/tuned-main.conf
%makeinstall_std DOCDIR=%_docdir/%name install-html

mkdir -p %buildroot%_datadir/tuned/grub2
mv %buildroot%_sysconfdir/grub.d/00_tuned %buildroot%_datadir/tuned/grub2/00_tuned

# conditional support for grub2, grub2 is not available on all architectures
# and tuned is noarch package, thus the following hack is needed
#mkdir -p %buildroot%_datadir/tuned/grub2
#mv %buildroot%_sysconfdir/grub.d/00_tuned %buildroot%_datadir/tuned/grub2/00_tuned
#rmdir %buildroot%_sysconfdir/grub.d

mkdir -p %buildroot%_logdir/tuned
touch %buildroot%_logdir/tuned/tuned.log

# ghost for persistent storage
mkdir -p %buildroot%_var/lib/tuned

cat << __EOF__ > %buildroot%_sysconfdir/tuned/active_profile
throughput-performance
__EOF__

mkdir -p %buildroot%_initdir
install -pDm755 %SOURCE1 %buildroot%_initdir/%name

#check
#make test

%post
%post_service %name
if [ $1 -eq 1 ] ; then
        /sbin/systemctl enable \
	tuned.service \
	>/dev/null 2>&1 || :
fi

%preun
%preun_service %name
if [ $1 -eq 0 ] ; then
	/sbin/systemctl disable \
	tuned.service \
	>/dev/null 2>&1 || :
       # clear persistent storage
       rm -f %_var/lib/tuned/* || :
fi

%files
#exclude %_docdir/README.utils
#exclude %_docdir/README.scomes
%doc %_docdir/%name
%_datadir/bash-completion/completions/tuned-adm
%exclude %python3_sitelibdir/tuned/gtk
%exclude %python3_sitelibdir/tuned/plugins/plugin_scheduler.p*
%python3_sitelibdir/tuned
%_sbindir/tuned
%_sbindir/tuned-adm
%exclude %_sysconfdir/tuned/realtime-variables.conf
%dir %_sysconfdir/tuned/
%dir %_libexecdir/%name/
%dir %tuneddir/
%tuneddir/balanced/
%tuneddir/desktop/
%tuneddir/functions/
%tuneddir/hpc-compute/
%tuneddir/latency-performance/
%tuneddir/network-latency/
%tuneddir/network-throughput/
%tuneddir/powersave/
%tuneddir/recommend.d/
%tuneddir/sst/
%tuneddir/throughput-performance/
%tuneddir/virtual-guest/
%tuneddir/virtual-host/

%config(noreplace) %_sysconfdir/tuned/active_profile
%config(noreplace) %_sysconfdir/tuned/tuned-main.conf
%config(noreplace) %_sysconfdir/tuned/profile_mode
%config(noreplace) %_sysconfdir/tuned/bootcmdline
%_sysconfdir/dbus-1/system.d/com.redhat.tuned.conf
%_sysconfdir/modprobe.d/tuned.conf
%_tmpfilesdir/tuned.conf
%_unitdir/tuned.service
%_initdir/tuned
%dir %_logdir/tuned
%ghost %_logdir/tuned/tuned.log
%_man5dir/tuned*
%_man7dir/tuned-profiles.7*
%_man8dir/tuned*
%dir %_datadir/tuned
%_datadir/tuned/grub2
%_datadir/polkit-1/actions/com.redhat.tuned.policy
%_libexecdir/tuned/defirqaffinity*

%files gtk
%_sbindir/tuned-gui
%python3_sitelibdir/tuned/gtk
%_datadir/tuned/ui
#_datadir/polkit-1/actions/com.redhat.tuned.gui.policy
%_iconsdir/hicolor/scalable/apps/tuned.svg
%_desktopdir/tuned-gui.desktop

%files utils
%doc COPYING
%_bindir/powertop2tuned
%_libexecdir/%name/pmqos-static*

# tuned-utils-systemtap#2.13.0-alt1    /usr/bin/stap
# tuned-utils-systemtap#2.13.0-alt1    systemtap
%if 0
%files utils-systemtap
%doc doc/README.utils
%doc doc/README.scomes
#doc COPYING
%_sbindir/varnetload
%_sbindir/netdevstat
%_sbindir/diskdevstat
%_sbindir/scomes
%_man8dir/varnetload.*
%_man8dir/netdevstat.*
%_man8dir/diskdevstat.*
%_man8dir/scomes.*
%endif

%files profiles-sap
%tuneddir/sap-netweaver
%_man7dir/tuned-profiles-sap.7*

%files profiles-sap-hana
%tuneddir/sap-hana
%_man7dir/tuned-profiles-sap-hana.7*

%files profiles-mssql
%tuneddir/mssql
%_man7dir/tuned-profiles-mssql.7*

%files profiles-oracle
%tuneddir/oracle
%_man7dir/tuned-profiles-oracle.7*

%files profiles-atomic
%tuneddir/atomic-host
%tuneddir/atomic-guest
%_man7dir/tuned-profiles-atomic.7*

# tuned-profiles-realtime#2.13.0-alt1    tuna
%if 0
%files profiles-realtime
%config(noreplace) %_sysconfdir/tuned/realtime-variables.conf
%tuneddir/realtime
%_man7dir/tuned-profiles-realtime.7*

%files profiles-nfv-guest
%config(noreplace) %_sysconfdir/tuned/realtime-virtual-guest-variables.conf
%tuneddir/realtime-virtual-guest
%_man7dir/tuned-profiles-nfv-guest.7*

%files profiles-nfv-host
%config(noreplace) %_sysconfdir/tuned/realtime-virtual-host-variables.conf
%tuneddir/realtime-virtual-host
%_man7dir/tuned-profiles-nfv-host.7*

# tuned-profiles-cpu-partitioning#2.13.0-alt1    /lib/dracut-lib.sh
%files profiles-cpu-partitioning
%config(noreplace) %_sysconfdir/tuned/cpu-partitioning-variables.conf
%tuneddir/cpu-partitioning
%_man7dir/tuned-profiles-cpu-partitioning.7*
%endif

%files profiles-compat
%tuneddir/default
%tuneddir/desktop-powersave
%tuneddir/laptop-ac-powersave
%tuneddir/server-powersave
%tuneddir/laptop-battery-powersave
%tuneddir/enterprise-storage
%tuneddir/spindown-disk
%_man7dir/tuned-profiles-compat.7*

%changelog
* Sat Feb 08 2020 Vitaly Lipatov <lav@altlinux.ru> 2.13.0-alt1
- sync spec with Fedora's one
- build with python3 only

* Mon Feb 27 2017 Michael Shigorin <mike@altlinux.org> 2.7.1-alt2
- added sysv initscript

* Thu Dec 29 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.7.1-alt1
- initial release

