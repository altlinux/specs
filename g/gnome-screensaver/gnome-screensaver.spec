%define ver_major 3.4
%def_disable static
%def_disable docbook
%def_enable consolekit
%def_with systemd

%define _libexecdir %_prefix/libexec

Name: gnome-screensaver
Version: %ver_major.2
Release: alt1

Summary: GNOME Screensaver
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://live.gnome.org/GnomeScreensaver
Packager: GNOME Maintainers Team <gnome at packages.altlinux.org>

Provides: screen-saver-engine
Provides: screen-saver-frontend
Provides: gnome-screensaver-module

Source: http://download.gnome.org/sources/gnome-screensaver/%ver_major/%name-%version.tar.xz
Source1: unix2_chkpwd.c

Patch: gnome-screensaver-2.28.0-alt-pam.patch
# Put back helper authentication, removed by upstream
Patch1: gnome-screensaver-3.2.1-helper.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=579430
Patch2: gnome-screensaver-2.28.0-user_activity.patch

# From configure.ac
%define dbus_ver 0.30
%define glib_ver 2.28.0
%define gtk_ver 3.0.2
%define desktop_ver 3.1.91
%define libgnomekbd_ver 2.91.91
%define systemd_ver 37

BuildPreReq: gnome-common
BuildPreReq: xscreensaver-devel
# From configure.ac
BuildPreReq: intltool >= 0.35
BuildPreReq: libdbus-glib-devel >= %dbus_ver libdbus-devel >= %dbus_ver
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver GConf
BuildPreReq: libgnome-desktop3-devel >= %desktop_ver
BuildPreReq: libgnomekbd-devel >= %libgnomekbd_ver
BuildRequires: libpam-devel gsettings-desktop-schemas-devel
BuildRequires: xorg-proto-devel libXxf86vm-devel libSM-devel
BuildRequires:libXScrnSaver-devel libXext-devel libXtst-devel xorg-xf86vidmodeproto-devel
%{?_enable_docbook:Requires: xmlto}
%{?_with_systemd:BuildRequires: systemd-devel >= %systemd_ver}

%description
gnome-screensaver is a screen saver and locker that aims to have
simple, sane, secure defaults and be well integrated with the desktop.


%prep
%setup -q
%patch -p1
%patch1 -p1
%patch2 -p1 -b .user_activity

%build
%autoreconf
%configure  \
	%{subst_enable static} \
	--disable-schemas-compile \
	--enable-locking \
	--with-pam-prefix=%_sysconfdir \
	--with-kbd-layout-indicator \
	--enable-authentication-scheme=helper \
	--with-passwd-helper="%_libexecdir/%name/%name-chkpwd-helper" \
	%{?_enable_docbook:--enable-docbook-docs} \
	%{?_enable_consolekit:--with-console-kit} \
	%{subst_with systemd}

%make_build

gcc -o %name-chkpwd-helper $RPM_OPT_FLAGS %SOURCE1 -lpam

%install
%make DESTDIR=%buildroot install
mkdir -p %buildroot%_libexecdir/%name
install %name-chkpwd-helper %buildroot%_libexecdir/%name/

%find_lang %name

%files -f %name.lang
%_bindir/*
%dir %_libexecdir/%name
%attr(4511,root,root) %_libexecdir/%name/%name-chkpwd-helper
%_libexecdir/%name-dialog
%_man1dir/*
%_sysconfdir/xdg/autostart/gnome-screensaver.desktop
%config(noreplace) %_sysconfdir/pam.d/*
%doc AUTHORS NEWS README


%changelog
* Wed Jun 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Sun Apr 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Thu Mar 22 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Sun Feb 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Fri Feb 10 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0
- removed -devel subpackage

* Fri May 27 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt3
- rebuild

* Wed Apr 06 2011 Alexey Shabalin <shaba@altlinux.ru> 3.0.0-alt2
- Put back helper authentication, removed by upstream

* Tue Apr 05 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Tue Apr 05 2011 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt2
- updated buildreqs

* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Wed Mar 31 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Tue Mar 09 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92

* Sat Feb 13 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Sat Feb 13 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.3-alt1
- 2.28.3

* Mon Feb 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt1
- 2.29.90

* Fri Jan 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.1-alt1
- 2.29.1

* Fri Jan 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Mon Jan 18 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt3
- fixed GNOME bug #579430 (closes #22719)

* Sun Dec 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt2
- allow XFCE to use g-s-s (closes #22092)

* Wed Sep 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Mon Aug 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.26.1-alt2
- disabled XFree86-Misc

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Sun Apr 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt2
- fixed lock/unlock (fixed patch0 by shrek@)

* Wed Mar 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Tue Jan 27 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.2-alt1
- 2.25.2
- updated buildreqs

* Mon Dec 01 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt2
- updated buildreqs

* Fri Nov 14 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1
- don't call %%{update,clean}_menus in %%post{,un}

* Sun Oct 26 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt3
- rebuild

* Wed Oct 01 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0
- removed useless patches
- updated buildreqs

* Mon Aug 11 2008 Sir Raorn <raorn@altlinux.ru> 2.22.2-alt1.1
- Added generic screen-saver-engine/frontend provides
- Removed xscreensaver triggers
- xscreensaver migration script moved to -utils subpackage

* Thu Jul 10 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- new version 2.22.2

* Mon Mar 31 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- initial build for ALTLinux

