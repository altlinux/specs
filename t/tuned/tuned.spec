Summary: A dynamic adaptive system tuning daemon
Name: tuned
Version: 2.7.1
Release: alt1
License: GPLv2+
Group: System/Configuration/Hardware
URL: https://fedorahosted.org/tuned/

Requires: virt-what ethtool hdparm util-linux polkit

Source: https://fedorahosted.org/releases/t/u/tuned/tuned-%version.tar.bz2
Patch0: tuned-2.7.1-pkexec-fix.patch
Patch1: tuned-2.7.1-profile_info-traceback-fix.patch
Patch2: tuned-2.7.1-throughput-performance-summary.patch

BuildArch: noarch
BuildRequires: desktop-file-utils

%description
The tuned package contains a daemon that tunes system settings dynamically.
It does so by monitoring the usage of several system components periodically.
Based on that information components will then be put into lower or higher
power saving modes to adapt to the current usage. Currently only ethernet
network and ATA harddisk devices are implemented.

%package gtk
Summary: GTK GUI for tuned
Group: System/Configuration/Other
Requires: %name = %version-%release
Requires: powertop

%description gtk
GTK GUI that can control tuned and provides simple profile editor.

%package utils
Group: System/Configuration/Other
Requires: %name = %version-%release
Requires: powertop
Summary: Various tuned utilities

%description utils
This package contains utilities that can help you to fine tune and
debug your system and manage tuned profiles.

%define docdir %_docdir/%name-%version
%define _libexecdir %_prefix/libexec

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build

%install
make DESTDIR=%buildroot DOCDIR=%docdir install
sed -i 's/\(dynamic_tuning[ \t]*=[ \t]*\).*/\10/' %buildroot%_sysconfdir/tuned/tuned-main.conf

mkdir -p %buildroot%_datadir/tuned/grub2
mv %buildroot%_sysconfdir/grub.d/00_tuned %buildroot%_datadir/tuned/grub2/00_tuned

mkdir -p %buildroot%_logdir/tuned
touch %buildroot%_logdir/tuned/tuned.log

cat << __EOF__ > %buildroot%_sysconfdir/tuned/active_profile
throughput-performance
__EOF__

%post
if [ $1 -eq 1 ] ; then
        /sbin/systemctl enable \
	tuned.service \
	>/dev/null 2>&1 || :
fi

%preun
if [ $1 -eq 0 ] ; then
	/sbin/systemctl disable \
	tuned.service \
	>/dev/null 2>&1 || :
fi

%files
%exclude %docdir/README.utils
%exclude %docdir/README.scomes
%doc %docdir
%_datadir/bash-completion/completions/tuned-adm
%exclude %python_sitelibdir/tuned/gtk
%exclude %python_sitelibdir/tuned/plugins/plugin_scheduler.p*
%python_sitelibdir/tuned
%_sbindir/tuned
%_sbindir/tuned-adm
%exclude %_sysconfdir/tuned/realtime-variables.conf
%exclude %_prefix/lib/tuned/default
%exclude %_prefix/lib/tuned/desktop-powersave
%exclude %_prefix/lib/tuned/laptop-ac-powersave
%exclude %_prefix/lib/tuned/server-powersave
%exclude %_prefix/lib/tuned/laptop-battery-powersave
%exclude %_prefix/lib/tuned/enterprise-storage
%exclude %_prefix/lib/tuned/spindown-disk
%exclude %_prefix/lib/tuned/sap-netweaver
%exclude %_prefix/lib/tuned/sap-hana
%exclude %_prefix/lib/tuned/sap-hana-vmware
%exclude %_prefix/lib/tuned/atomic-host
%exclude %_prefix/lib/tuned/atomic-guest
%exclude %_prefix/lib/tuned/realtime
%exclude %_prefix/lib/tuned/realtime-virtual-guest
%exclude %_prefix/lib/tuned/realtime-virtual-host
%_prefix/lib/tuned
%dir %_sysconfdir/tuned
%dir %_libexecdir/tuned
%config(noreplace) %_sysconfdir/tuned/active_profile
%config(noreplace) %_sysconfdir/tuned/tuned-main.conf
%config(noreplace) %_sysconfdir/tuned/bootcmdline
%_sysconfdir/dbus-1/system.d/com.redhat.tuned.conf
%_sysconfdir/modprobe.d/tuned.conf
%_tmpfilesdir/tuned.conf
%_unitdir/tuned.service
%dir %_logdir/tuned
%ghost %_logdir/tuned/tuned.log
%_man5dir/tuned*
%_man7dir/tuned-profiles.7*
%_man7dir/tuned-profiles-oracle.7*
%_man8dir/tuned*
%dir %_datadir/tuned
%_datadir/tuned/grub2
%_datadir/polkit-1/actions/com.redhat.tuned.policy

%files gtk
%_sbindir/tuned-gui
%python_sitelibdir/tuned/gtk
%_datadir/tuned/ui
%_datadir/polkit-1/actions/com.redhat.tuned.gui.policy
%_datadir/icons/hicolor/scalable/apps/tuned.svg
%_datadir/applications/tuned-gui.desktop

%files utils
%doc COPYING
%_bindir/powertop2tuned
%_libexecdir/tuned/pmqos-static*

%changelog
* Thu Dec 29 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.7.1-alt1
- initial release

