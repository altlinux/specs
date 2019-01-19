# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define _libexecdir %_prefix/libexec
%define systemdsystemunitdir /lib/systemd/system
%define oname ConsoleKit
Name: ConsoleKit2
Version: 1.2.1
Release: alt4
Summary: System daemon for tracking users, sessions and seats
License: GPL
Group: System/Libraries
URL: https://github.com/ConsoleKit2/ConsoleKit2
Packager: Anton Midyukov <antohami@altlinux.org>

Requires: lib%name = %EVR
Requires: pam-ck-connector2 = %EVR
Provides: ConsoleKit = %EVR
PreReq: dbus polkit >= 0.93

Source: %name-%version.tar
Patch: %name-1.1.0-alt.patch

BuildRequires: gcc-c++
BuildRequires: libpam-devel
BuildRequires: libdbus-glib-devel
BuildRequires: libpolkit1-devel
BuildRequires: libudev-devel
BuildRequires: libacl-devel
BuildRequires: xmlto
BuildRequires: zlib-devel
BuildRequires: libX11-devel
BuildRequires: libselinux-devel
BuildRequires: libdrm-devel
BuildRequires: libevdev-devel
BuildRequires: libcgmanager

%description
ConsoleKit is a system daemon for tracking what users are logged
into the system and how they interact with the computer (e.g. which
keyboard and mouse they use).

It provides asynchronous notification via the system message bus.

%package service
Summary: Dbus service ConsoleKit
Group: System/X11
Requires: %name-x11 = %EVR
Conflicts: systemd-services

%description service
Dbus service ConsoleKit.

%package x11
Summary: X11-requiring add-ons for ConsoleKit
Group: System/X11
Requires: %name = %EVR
Provides: ConsoleKit-x11 = %EVR

%description x11
ConsoleKit contains some tools that require Xlib to be installed,
those are in this separate package so server systems need not install
X. Applications (such as xorg-x11-xinit) and login managers (such as
gdm) that need to register their X sessions with ConsoleKit needs to
have a requires for this package.

%package -n lib%name
Summary: ConsoleKit libraries
Group: System/Libraries
Provides: libConsoleKit = %EVR

%description -n lib%name
Libraries and a PAM module for interacting with ConsoleKit

%package -n lib%name-devel
Summary: Development libraries and headers for ConsoleKit
Group: Development/C++
Requires: lib%name = %EVR
Provides: libConsoleKit-devel = %EVR

%description -n lib%name-devel
Headers, libraries and API docs for ConsoleKit

%package -n pam-ck-connector2
Summary: Register session with ConsoleKit
Group: System/Base
Provides: pam-ck-connector = %EVR

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
    --with-rundir=/run \
    --with-pid-file=/run/lock/console-kit-daemon.pid \
    --enable-pam-module \
    --with-pam-module-dir=/%_lib/security \
    --enable-docbook-docs \
    --enable-polkit \
    --enable-libudev \
    --enable-libselinux \
    --enable-udev-acl \
    --enable-libdrm \
    %nil
%make_build

%install
%makeinstall_std

mkdir -p %buildroot%_logdir/%oname
touch %buildroot%_logdir/%oname/history
for i in $(seq 1 5); do
    touch %buildroot%_logdir/%oname/history.$i.bz2
done

rm -fr %buildroot/%_datadir/locale/es_419
rm -fr %buildroot/%_lib/security/*.la

# DBus config belongs into %%_datadir
mkdir -p %buildroot%_datadir/dbus-1
mv -f %buildroot%_sysconfdir/dbus-1/* %buildroot%_datadir/dbus-1/

%find_lang %name

%files -f %name.lang
%_docdir/%name
%_datadir/dbus-1/system.d/*
%_sysconfdir/X11/xinit/xinitrc.d/*
%_sysconfdir/%oname
%_logrotatedir/consolekit
%_sbindir/*
%_bindir/*
%_libdir/%oname
%_datadir/polkit-1/actions/*.policy
%dir %_logdir/%oname
%ghost %_logdir/%oname/history*
%_udevrulesdir/*.rules
/lib/udev/udev-acl
%_libexecdir/udev-acl

%files service
%_datadir/dbus-1/system-services/org.freedesktop.ConsoleKit.service

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
%_man8dir/*.8*
%_man1dir/*.1*

%changelog
* Sat Jan 19 2019 Anton Midyukov <antohami@altlinux.org> 1.2.1-alt4
- Fix conflict with systemd-services
- New subpackage ConsoleKit2-service
- Drop obsoletes ConsoleKit2

* Sun Oct 21 2018 Anton Midyukov <antohami@altlinux.org> 1.2.1-alt3
- disable systemd support
- enable udev support
- enable selinux support
- enable drm support

* Mon Oct 08 2018 Anton Midyukov <antohami@altlinux.org> 1.2.1-alt2
- fix unpackages directory

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
