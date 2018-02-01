%define _libexecdir %_prefix/libexec

Name: rtkit
Version: 0.11
Release: alt1%ubt
Summary: Realtime Policy and Watchdog Daemon
Group: System/Servers
License: GPLv3+ and BSD
Url: http://git.0pointer.de/?p=rtkit.git

Requires: dbus polkit

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-ubt
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
	--with-systemdsystemunitdir=%_unitdir

%make_build
./rtkit-daemon --introspect > org.freedesktop.RealtimeKit1.xml

%install
%make DESTDIR=%buildroot install
install -Dm0644 org.freedesktop.RealtimeKit1.xml %buildroot%_datadir/dbus-1/interfaces/org.freedesktop.RealtimeKit1.xml

%pre
%_sbindir/groupadd -r -f rtkit >/dev/null 2>&1 || :
%_sbindir/useradd -r -g rtkit -d '/' -s /sbin/nologin -c "RealtimeKit" rtkit >/dev/null 2>&1 ||:

%post
%post_service rtkit-daemon
dbus-send --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig >/dev/null 2>&1 || :

%preun
%preun_service rtkit-daemon

%files
%doc README
%config(noreplace) %_sysconfdir/dbus-1/system.d/org.freedesktop.RealtimeKit1.conf
%_sbindir/%{name}*
%_libexecdir/%name-daemon
%_datadir/dbus-1/system-services/org.freedesktop.RealtimeKit1.service
%_datadir/dbus-1/interfaces/org.freedesktop.RealtimeKit1.xml
%_datadir/polkit-1/actions/org.freedesktop.RealtimeKit1.policy
%_unitdir/rtkit-daemon.service
%_man8dir/*.8*

%changelog
* Wed Jan 31 2018 Alexey Shabalin <shaba@altlinux.ru> 0.11-alt1%ubt
- 0.11 (with patches from master)
- add systemd unit
- add dbus-1/interfaces/org.freedesktop.RealtimeKit1.xml

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.8-alt1.qa1
- NMU: rebuilt for debuginfo.

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

