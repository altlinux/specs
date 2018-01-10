%define _libexecdir %_prefix/libexec
%define systemdsystemunitdir /lib/systemd/system
%define oname ConsoleKit
Name: ConsoleKit2
Version: 1.2.1
Release: alt1
Summary: System daemon for tracking users, sessions and seats
License: GPL
Group: System/Libraries
URL: https://github.com/ConsoleKit2/ConsoleKit2
Packager: Anton Midyukov <antohami@altlinux.org>

Requires: lib%name = %version-%release
Requires: pam-ck-connector2 = %version-%release
Provides: ConsoleKit = %version-%release
Obsoletes: ConsoleKit < %version-%release
PreReq: dbus polkit >= 0.93

Source: %name-%version.tar
Patch: %name-1.1.0-alt.patch

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
Provides: ConsoleKit-x11 = %version-%release
Obsoletes: ConsoleKit-x11 < %version-%release

%description x11
ConsoleKit contains some tools that require Xlib to be installed,
those are in this separate package so server systems need not install
X. Applications (such as xorg-x11-xinit) and login managers (such as
gdm) that need to register their X sessions with ConsoleKit needs to
have a requires for this package.

%package -n lib%name
Summary: ConsoleKit libraries
Group: System/Libraries
Provides: libConsoleKit = %version-%release
Obsoletes: libConsoleKit < %version-%release

%description -n lib%name
Libraries and a PAM module for interacting with ConsoleKit

%package -n lib%name-devel
Summary: Development libraries and headers for ConsoleKit
Group: Development/C++
Requires: lib%name = %version-%release
Provides: libConsoleKit-devel = %version-%release
Obsoletes: libConsoleKit-devel < %version-%release

%description -n lib%name-devel
Headers, libraries and API docs for ConsoleKit

%package -n pam-ck-connector2
Summary: Register sessin with ConsoleKit
Group: System/Base
Provides: pam-ck-connector = %version-%release
Obsoletes: pam-ck-connector < %version-%release

%description -n pam-ck-connector2
The pam_ck_connector PAM module registers a login session with the system-wide ConsoleKit daemon. This
PAM module should be used with caution; only local login managers such as login(1) should use this.
Since the ConsoleKit daemon can accept both an tty and an X11 display the normal parameters set by PAM
are not always useful.

%prep
%setup
%patch -p1

%build
touch gtk-doc.make
%autoreconf
%configure \
	--libexecdir=%_libexecdir \
	--localstatedir=%_var \
	--with-pid-file=%_var/run/console-kit-daemon.pid \
	--enable-pam-module \
	--with-pam-module-dir=/%_lib/security \
	--with-systemdsystemunitdir=%systemdsystemunitdir \
	--enable-docbook-docs
%make_build

%install
%makeinstall_std

#touch %buildroot%_var/run/%oname/database
mkdir -p %buildroot%_logdir/%oname
touch %buildroot%_logdir/%oname/history
for i in $(seq 1 5); do
	touch %buildroot%_logdir/%oname/history.$i.bz2
done

%find_lang %name

%triggerun -n %name -- %name < 0.2.6-alt1
/sbin/chkconfig --del consolekit ||:

%files -f %name.lang
%doc README NEWS COPYING AUTHORS
%exclude %_docdir/%name
%_sysconfdir/dbus-1/system.d/*
%_sysconfdir/X11/xinit/xinitrc.d/*
%_sysconfdir/%oname
%systemdsystemunitdir/*
%_logrotatedir/consolekit
%_sbindir/*
%_bindir/*
%dir %_libdir/%oname
%_libdir/%oname/scripts
#%%_libexecdir/ck-collect-session-info
#%%dir %_libexecdir/%oname
#%%dir %_libexecdir/%oname/run-session.d
#%%dir %_libexecdir/%oname/run-seat.d
#%%_libexecdir/%oname/scripts
%_datadir/dbus-1/system-services/*.service
%_datadir/polkit-1/actions/*.policy
#%%dir %_var/run/%oname
#%%ghost %_var/run/%oname/database
%dir %_logdir/%oname
%ghost %_logdir/%oname/history*

%files x11
%_libexecdir/ck-get-*
%_libexecdir/ck-collect-session-info
%_libexecdir/ck-remove-directory

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%doc doc/dbus/ConsoleKit.html
%_includedir/%oname
%_libdir/*.so
%_datadir/dbus-1/interfaces/*.xml
%_pkgconfigdir/*.pc

%files -n pam-ck-connector2
/%_lib/security/*.so
%exclude /%_lib/security/*.la
%_man8dir/*.8*
%_man1dir/*.1*

%changelog
* Wed Jan 10 2018 Anton Midyukov <antohami@altlinux.org> 1.2.1-alt1
- new version 1.2.1

* Thu Sep 07 2017 Anton Midyukov <antohami@altlinux.org> 1.2.0-alt2
- Fix obsoletes (Closes: 33859)

* Fri Jul 21 2017 Anton Midyukov <antohami@altlinux.org> 1.2.0-alt1
- New version 1.2.0
- Obsoletes ConsoleKit

* Sun Feb 12 2017 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt2
- Added conflict ConsoleKit2-x11 with ConsoleKit
- Remove subdir in /var/run

* Mon Feb 06 2017 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt1
- Initial build for ALT Linux Sisyphus.
