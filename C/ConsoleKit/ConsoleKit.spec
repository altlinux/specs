%define _libexecdir %_prefix/libexec
%define systemdsystemunitdir /lib/systemd/system

Name: ConsoleKit
Version: 0.4.5
Release: alt1
Summary: System daemon for tracking users, sessions and seats
License: GPL
Group: System/Libraries
URL: http://www.freedesktop.org/wiki/Software/hal
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: lib%name = %version-%release
Requires: pam-ck-connector = %version-%release
PreReq: dbus polkit >= 0.93

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ libpolkit1-devel libX11-devel libdbus-glib-devel libpam-devel xmlto zlib-devel

%description
ConsoleKit is a system daemon for tracking what users are logged
into the system and how they interact with the computer (e.g. which
keyboard and mouse they use).

It provides asynchronous notification via the system message bus.

%package x11
Summary: X11-requiring add-ons for ConsoleKit
Group: System/X11
Requires: %name = %version-%release

%description x11
ConsoleKit contains some tools that require Xlib to be installed,
those are in this separate package so server systems need not install
X. Applications (such as xorg-x11-xinit) and login managers (such as
gdm) that need to register their X sessions with ConsoleKit needs to
have a requires for this package.

%package -n lib%name
Summary: ConsoleKit libraries
Group: System/Libraries

%description -n lib%name
Libraries and a PAM module for interacting with ConsoleKit

%package -n lib%name-devel
Summary: Development libraries and headers for ConsoleKit
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
Headers, libraries and API docs for ConsoleKit

%package -n pam-ck-connector
Summary: Register sessin with ConsoleKit
Group: System/Base

%description -n pam-ck-connector
The pam_ck_connector PAM module registers a login session with the system-wide ConsoleKit daemon. This
PAM module should be used with caution; only local login managers such as login(1) should use this.
Since the ConsoleKit daemon can accept both an tty and an X11 display the normal parameters set by PAM
are not always useful.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--libexecdir=%_libexecdir \
	--localstatedir=%_var \
	--with-pid-file=%_var/run/console-kit-daemon.pid \
	--enable-pam-module \
	--with-pam-module-dir=/%_lib/security \
	--with-systemdsystemunitdir=%systemdsystemunitdir \
	--enable-docbook-docs
%make

%install
%make DESTDIR=%buildroot install

touch %buildroot%_var/run/%name/database
mkdir -p %buildroot%_logdir/%name
touch %buildroot%_logdir/%name/history
for i in $(seq 1 5); do
	touch %buildroot%_logdir/%name/history.$i.bz2
done

mkdir -p %buildroot%_logrotatedir
cat <<__EOF__ > %buildroot%_logrotatedir/%name
# Logrotate file for %name

%_logdir/%name/history {
	missingok
	compress
	notifempty
	daily
	rotate 5
}
__EOF__

%triggerun -n %name -- %name < 0.2.6-alt1
/sbin/chkconfig --del consolekit ||:

%files
%doc README NEWS COPYING AUTHORS
%_sysconfdir/dbus-1/system.d/*
%_sysconfdir/%name
%systemdsystemunitdir/*
%_logrotatedir/%name
%_sbindir/*
%_bindir/*
%_libexecdir/ck-collect-session-info
%dir %_libexecdir/%name
%dir %_libexecdir/%name/run-session.d
%dir %_libexecdir/%name/run-seat.d
%_libexecdir/%name/scripts
%_datadir/dbus-1/system-services/*.service
%_datadir/polkit-1/actions/*.policy
%dir %_var/run/%name
%ghost %_var/run/%name/database
%dir %_logdir/%name
%ghost %_logdir/%name/history*

%files x11
%_libexecdir/ck-get-*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%doc doc/dbus/ConsoleKit.html
%_includedir/%name
%_libdir/*.so
%_datadir/dbus-1/interfaces/*.xml
%_pkgconfigdir/*.pc

%files -n pam-ck-connector
/%_lib/security/*.so
%_man8dir/*.8*

%changelog
* Tue May 03 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.4.5-alt1
- 0.4.5

* Thu Feb 17 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.4.4-alt1
- 0.4.4

* Tue Feb 08 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.4.3-alt2
- add systemd service files (closes: #24992)

* Wed Nov 17 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.4.3-alt1
- 0.4.3

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.4.2-alt2
- added logrotate config

* Tue Sep 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.4.2-alt1
- 0.4.2

* Fri Sep 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Thu Aug 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Wed May 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.3.0-alt4
- relocated devel files

* Mon Jan 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.3.0-alt3
- fix up D-Bus permissions

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.3.0-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Fri Aug 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.3.0-alt1
- 0.3.0

* Fri Mar 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.2.10-alt1
- 0.2.10

* Fri Jan 25 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.2.6-alt2
- fixed unmet dependency

* Fri Jan 25 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.2.6-alt1
- 0.2.6

* Fri Dec 14 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.2.3-alt3
- fixed initscript

* Thu Dec 13 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.2.3-alt2
- rebuild

* Fri Oct 12 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.2.3-alt1
- 0.2.3

* Mon Jun 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.2.1-alt1
- Initial build
