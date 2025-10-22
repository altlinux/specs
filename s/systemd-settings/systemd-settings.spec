Name: systemd-settings
Version: 7
Release: alt2
Summary: Popular settings for systemd components
Url: https://packages.altlinux.org/en/Sisyphus/srpms/%name
Group: System/Configuration/Boot and Init
License: GPLv2+
BuildArch: noarch

Source: %name-%version.tar

%description
This package contains drop-in settings for systemd components.

%package disable-user-systemd-for-selinux
Summary: Disable user systemd --user  for ALT selinux systems
Group: System/Configuration/Boot and Init

%description disable-user-systemd-for-selinux
Disabling user@.service, which attempts to start
systemd for user sessions, not needed or allowed
in ALT selinux systems.

%package disable-kill-user-processes
Summary: Globally set KillUserProcesses=no
Group: System/Configuration/Boot and Init
Requires: /lib/systemd/systemd-logind
Conflicts: %name-enable-kill-user-processes

%description disable-kill-user-processes
This package augments logind.conf, so that KillUserProcesses= is set to "no".

When a session terminates (e. g. a user logs out), systemd will not attempt
to kill any remaining processes in its cgroup. See logind.conf(5) for more info.

%package enable-kill-user-processes
Summary: Globally set KillUserProcesses=yes
Group: System/Configuration/Boot and Init
Requires: /lib/systemd/systemd-logind
Conflicts: %name-disable-kill-user-processes

%description enable-kill-user-processes
This package augments logind.conf, so that KillUserProcesses= is set to "yes".

When a session terminates (e. g. a user logs out), systemd will attempt
to kill any remaining processes in its cgroup. Resident processes, like tmux
or screen, would need to be run outside of session scope.

Note that there are ways to disable this per-user:
+ loginctl enable-linger; see loginctl(1)
+ KillOnlyUsers=, KillExcludeUsers=; see logind.conf(5)

%package enable-showstatus
Summary: Globally set ShowStatus=yes
Group: System/Configuration/Boot and Init

%description enable-showstatus
This package augments system.conf for the system manager, so that ShowStatus=
is set to "yes".

During system bootup the system manager would print terse service status
updates on /dev/console.
This is equivalent to "systemd.show_status" on the kernel command line.
Also, the ShowStatus=yes behaviour is the default unless "quiet" is passed on
the kernel command line.

%package enable-log-to-tty12
Summary: Globally set TTYPath=/dev/tty12 for journald logs
Group: System/Configuration/Boot and Init

%description enable-log-to-tty12
This package augments journald.conf, so that journal messages are printed
on VT 12.

%package disable-resolve-llmnr
Summary: Globally set LLMNR=no for systemd-resolve
Group: System/Configuration/Boot and Init

%description disable-resolve-llmnr
This package augments resolved.conf, so that LLMNR= is set to "no".

If this is installed, systemd-resolved would not consider making name
resolution queries over LLMNR.

%package ignore-handle-lid-switch
Summary: Globally set HandleLidSwitch=ignore
Group: System/Configuration/Boot and Init
Requires: /lib/systemd/systemd-logind

%description ignore-handle-lid-switch
This package augments logind.conf, so that HandleLidSwitch= is set to "ignore".

systemd-logind will take no system-wide action whenever a lid switch input
device reports a closed state. This does not apply if the machine is considered
"docked", i. e. it is connected to a dock device or to at least one external
monitor.
This is useful when a machine with a closable lid needs to be used as a server.

Note that processes can install inhibitors that can block or delay any logind
action (e. g.: suspend, hibernate, ...). DEs and DMs tend to hook into power
state changes extensively for many reasons, so, in addition to installing this
package, you might have to further configure those components.
See also:
+ https://systemd.io/INHIBITOR_LOCKS
+ man systemd-inhibit(1)

%prep
%setup

%build

%install
mkdir -p %buildroot/lib/systemd/{{logind,system,journald,resolved}.conf.d,system/user@.service.d}

install -p -m644 disable-kill-user-processes.conf \
    %buildroot/lib/systemd/logind.conf.d/disable-kill-user-processes.conf
install -p -m644 enable-kill-user-processes.conf \
    %buildroot/lib/systemd/logind.conf.d/enable-kill-user-processes.conf
install -p -m644 enable-showstatus.conf \
    %buildroot/lib/systemd/system.conf.d/enable-showstatus.conf
install -p -m644 enable-log-to-tty12.conf \
    %buildroot/lib/systemd/journald.conf.d/enable-log-to-tty12.conf
install -p -m644 disable-resolve-llmnr.conf \
    %buildroot/lib/systemd/resolved.conf.d/disable-resolve-llmnr.conf

install -p -m644 disable-user-systemd-for-selinux.conf \
    %buildroot/lib/systemd/system/user@.service.d/disable-user-systemd-for-selinux.conf

install -p -m644 ignore-handle-lid-switch.conf \
    %buildroot/lib/systemd/logind.conf.d/ignore-handle-lid-switch.conf

%files disable-kill-user-processes
/lib/systemd/logind.conf.d/disable-kill-user-processes.conf

%files enable-kill-user-processes
/lib/systemd/logind.conf.d/enable-kill-user-processes.conf

%files disable-user-systemd-for-selinux
/lib/systemd/system/user@.service.d/disable-user-systemd-for-selinux.conf

%files enable-showstatus
/lib/systemd/system.conf.d/enable-showstatus.conf

%files disable-resolve-llmnr
/lib/systemd/resolved.conf.d/disable-resolve-llmnr.conf

%files enable-log-to-tty12
/lib/systemd/journald.conf.d/enable-log-to-tty12.conf

%files ignore-handle-lid-switch
/lib/systemd/logind.conf.d/ignore-handle-lid-switch.conf

%changelog
* Mon Oct 20 2025 Arseny Maslennikov <arseny@altlinux.org> 7-alt2
- ignore-handle-lid-switch: Removed self-conflict introduced by mistake.
- Provided more informational summaries and descriptions.

* Mon Sep 09 2024 Vasiliy Kovalev <kovalev@altlinux.org> 7-alt1
- Added ignore-handle-lid-switch package

* Fri Nov 26 2021 Alexey Shabalin <shaba@altlinux.org> 6-alt1
- Drop disable-dumpcore package.

* Fri Jul 09 2021 Alexey Shabalin <shaba@altlinux.org> 5-alt1
- Added disable-resolve-llmnr package

* Tue Apr 27 2021 Vitaly Chikunov <vt@altlinux.org> 4-alt1
- Undo logind restart introduced in 3-alt1 (closes: #40002).

* Sun Apr 25 2021 Vitaly Chikunov <vt@altlinux.org> 3-alt1
- Automatically restart logind for disable-kill-user-processes.

* Thu Jul 25 2019 Alexey Shabalin <shaba@altlinux.org> 2-alt1
- Added packages:
  + enable-showstatus
  + disable-dumpcore
  + enable-log-to-tty12

* Thu Apr 05 2018 Denis Medvedev <nbr@altlinux.org> 1-alt2
- Added ALT selinux settings as additional packages. Changed
package group.

* Sat Mar 31 2018 Alexey Shabalin <shaba@altlinux.ru> 1-alt1
- Initial build

