%define ver_major 3.0
%def_disable static
%def_disable docbook
%def_enable consolekit
%def_with systemd

%define _libexecdir %_prefix/libexec

Name: cinnamon-screensaver
Version: %ver_major.0
Release: alt1

Summary: Cinnamon Screensaver
License: GPLv2+
Group: Graphical desktop/GNOME
Url: https://github.com/linuxmint/cinnamon-screensaver

Provides: screen-saver-engine
Provides: screen-saver-frontend
Provides: cinnamon-screensaver-module

Source: %name-%version.tar

Patch: %name-%version-%release.patch

# From configure.ac
%define dbus_ver 0.30
%define glib_ver 2.28.0
%define gtk_ver 3.0.2
%define desktop_ver 1.9.0
%define libgnomekbd_ver 2.91.91
%define systemd_ver 37

BuildPreReq: gnome-common
BuildPreReq: xscreensaver-devel
# From configure.ac
BuildPreReq: intltool >= 0.35
BuildPreReq: libdbus-glib-devel >= %dbus_ver libdbus-devel >= %dbus_ver
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libcinnamon-desktop-devel >= %desktop_ver
BuildPreReq: libgnomekbd-devel >= %libgnomekbd_ver
BuildRequires: libpam-devel gsettings-desktop-schemas-devel
BuildRequires: xorg-proto-devel libXxf86vm-devel libSM-devel
BuildRequires: libXScrnSaver-devel libXext-devel libXtst-devel xorg-xf86vidmodeproto-devel
BuildRequires: libwebkit2gtk-devel
%{?_enable_docbook:Requires: xmlto}
%{?_with_systemd:BuildRequires: systemd-devel >= %systemd_ver libsystemd-login-devel libsystemd-daemon-devel}

%description
cinnamon-screensaver is a screen saver and locker that aims to have
simple, sane, secure defaults and be well integrated with the Cinnamon desktop.


%prep
%setup -q
%patch0 -p1

%build
%autoreconf
%add_optflags -D_GNU_SOURCE
%configure  \
	%{subst_enable static} \
	--disable-schemas-compile \
	--enable-locking \
	--with-pam-prefix=%_sysconfdir \
	--with-kbd-layout-indicator \
	%{?_enable_docbook:--enable-docbook-docs} \
	%{?_enable_consolekit:--with-console-kit} \
	%{subst_with systemd}

%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_datadir/dbus-1/services/org.cinnamon.ScreenSaver.service
%_datadir/applications/%name.desktop
%attr(2711,root,chkpwd) %_libexecdir/%name-dialog
%_datadir/%name
%_man1dir/*
%attr(640,root,chkpwd) %config(noreplace) %_sysconfdir/pam.d/*
%doc AUTHORS NEWS README

%changelog
* Mon Apr 25 2016 Vladimir Didenko <cow@altlinux.org> 3.0.0-alt1
- 3.0.0

* Mon Oct 19 2015 Vladimir Didenko <cow@altlinux.org> 2.8.0-alt1
- 2.8.0

* Tue Jun 2 2015 Vladimir Didenko <cow@altlinux.org> 2.6.3-alt1
- 2.6.3

* Sat May 23 2015 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt2
- git20150523

* Tue May 19 2015 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt1
- 2.6.0

* Fri May 8 2015 Vladimir Didenko <cow@altlinux.org> 2.5.0-alt1
- git20150506

* Mon Mar 30 2015 Vladimir Didenko <cow@altlinux.org> 2.4.2-alt1
- 2.4.2

* Fri Oct 31 2014 Vladimir Didenko <cow@altlinux.org> 2.4.0-alt1
- 2.4.0

* Tue Oct 14 2014 Vladimir Didenko <cow@altlinux.org> 2.3.0-alt1
- git20140923

* Tue Jul 22 2014 Vladimir Didenko <cow@altlinux.org> 2.2.4-alt1
- 2.2.4

* Mon May 12 2014 Vladimir Didenko <cow@altlinux.org> 2.2.3-alt1
- 2.2.3

* Mon May 5 2014 Vladimir Didenko <cow@altlinux.org> 2.2.2-alt1
- 2.2.2

* Wed Apr 30 2014 Vladimir Didenko <cow@altlinux.org> 2.2.0-alt2
- 2.2.0-1-g68b6a34

* Mon Apr 14 2014 Vladimir Didenko <cow@altlinux.org> 2.2.0-alt1
- 2.2.0

* Mon Apr 7 2014 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt2
- git20140327

* Tue Oct 29 2013 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt1
- 2.0.3

* Mon Oct 21 2013 Vladimir Didenko <cow@altlinux.org> 2.0.1-alt1
- 2.0.1

* Thu Oct 10 2013 Vladimir Didenko <cow@altlinux.org> 2.0.0-alt1.1
- fix build

* Thu Oct 10 2013 Vladimir Didenko <cow@altlinux.org> 2.0.0-alt1
- 2.0.0

* Fri Sep 27 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt3.1
- fixed build

* Wed Sep 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt3
- rebuild for GNOME-3.10

* Thu Aug 29 2013 Vladimir Didenko <cow@altlinux.org> 1.8.0-alt2
- git20130829

* Mon May 6 2013 Vladimir Didenko <cow@altlinux.org> 1.8.0-alt1
- 1.8.0

* Fri Feb 22 2013 Vladimir Didenko <cow@altlinux.org> 1.7.1-alt1
- Initial build for Alt Linux
