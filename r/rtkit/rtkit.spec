%define _libexecdir %_prefix/libexec

Name: rtkit
Version: 0.13
Release: alt1
Summary: Realtime Policy and Watchdog Daemon
Group: System/Servers
License: GPLv3+ and BSD
Url: https://github.com/heftig/rtkit

Requires: dbus polkit

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): meson >= 0.49
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(libcap)
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: /usr/bin/xxd

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
%meson \
	-Dsystemd_systemunitdir=%_unitdir \
	-Dinstalled_tests=false

%meson_build

%install
%meson_install

%check
export LD_LIBRARY_PATH=$(pwd)/%{__builddir}/src/shared:$(pwd)/%{__builddir}
%meson_test

%pre
groupadd -r -f rtkit >/dev/null 2>&1 || :
useradd -r -g rtkit -d '/proc' -M -s /sbin/nologin -c "RealtimeKit" rtkit >/dev/null 2>&1 ||:

%post
%post_service rtkit-daemon
dbus-send --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig >/dev/null 2>&1 || :

%preun
%preun_service rtkit-daemon

%files
%doc README
%_sbindir/%{name}*
%_libexecdir/%name-daemon
%_datadir/dbus-1/system-services/org.freedesktop.RealtimeKit1.service
%_datadir/dbus-1/interfaces/org.freedesktop.RealtimeKit1.xml
%_datadir/dbus-1/system.d/org.freedesktop.RealtimeKit1.conf
%_datadir/polkit-1/actions/org.freedesktop.RealtimeKit1.policy
%_unitdir/rtkit-daemon.service
%_man8dir/*.8*

%changelog
* Sat Jan 16 2021 Alexey Shabalin <shaba@altlinux.org> 0.13-alt1
- new version 0.13

* Thu Dec 17 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.11-alt2
- Bumped release to drop ubt suffix.

* Wed Jan 31 2018 Alexey Shabalin <shaba@altlinux.ru> 0.11-alt1
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

