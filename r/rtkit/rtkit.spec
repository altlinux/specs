Name: rtkit
Version: 0.8
Release: alt1
Summary: Realtime Policy and Watchdog Daemon
Group: System/Servers
License: GPLv3+ and BSD
Url: http://git.0pointer.de/?p=rtkit.git

Requires: dbus polkit

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libcap-devel libdbus-devel

%description
RealtimeKit is a D-Bus system service that changes the
scheduling policy of user processes/threads to SCHED_RR (i.e. realtime
scheduling mode) on request. It is intended to be used as a secure
mechanism to allow real-time scheduling to be used by normal user
processes.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--libexecdir=%_prefix/libexec
%make_build

%install
%make DESTDIR=%buildroot install

%pre
%_sbindir/groupadd -r -f rtkit >/dev/null 2>&1 || :
%_sbindir/useradd -r -g rtkit -d '/' -s /sbin/nologin -c "RealtimeKit" rtkit >/dev/null 2>&1 ||:

%files
%doc README
%_sysconfdir/dbus-1/system.d/org.freedesktop.RealtimeKit1.conf
%_sbindir/%{name}*
%_prefix/libexec/%name-daemon
%_datadir/dbus-1/system-services/org.freedesktop.RealtimeKit1.service
%_datadir/polkit-1/actions/org.freedesktop.RealtimeKit1.policy
%_man8dir/*.8*

%changelog
* Mon Jul 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.8-alt1
- 0.8

* Mon May 17 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.7-alt1
- 0.7

* Sun Jan 31 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6-alt1
- 0.6

* Mon Dec 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.5-alt1
- 0.5

* Sat Sep 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.4-alt1
- initial release

