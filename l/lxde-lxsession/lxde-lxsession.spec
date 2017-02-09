%define upstreamname lxsession
%define gtkver 2
Name: lxde-%upstreamname
Version: 0.5.3
Release: alt2

Summary: LXSession is the default X11 session manager of LXDE
License: GPL
Group: Graphical desktop/Other
Url: https://git.lxde.org/gitweb/?p=lxde/lxsession.git

Provides: lxde-lxsession-lite
Obsoletes: lxde-lxsession-lite

Provides: lxde-settings-daemon
Obsoletes: lxde-settings-daemon

Packager: LXDE Development Team <lxde at packages.altlinux.org>

Source: %name-%version.tar
Patch: lxsession-0.4.6.1-alt-kdmfix.patch
Patch1: lxsession-0.5.2-notify-daemon-default.patch
Patch2: lxsession-0.5.2-reload.patch
Patch3: lxsession-edit-0.5.2-fix-invalid-memcpy.patch

BuildPreReq: intltool libXau-devel libdbus-devel libgtk+%gtkver-devel xsltproc docbook-dtds docbook-style-xsl pkgconfig(dbus-glib-1) pkgconfig(gio-unix-2.0) pkgconfig(glib-2.0) pkgconfig(unique-1.0) pkgconfig(x11) pkgconfig(polkit-agent-1) vala pkgconfig(appindicator-0.1) pkgconfig(indicator-0.4) pkgconfig(libnotify)
%add_findreq_skiplist %_bindir/lxlock

#Requires: lxde-lxpolkit = %version-%release
# required for suspend and hibernate
Requires: upower

%description
LXSession is lightweiht, and it's not tighted to "any" desktop environment.
It's desktop-independent and can be used with any window manager.
With proper configuration, you can make your own desktop environment with
LXSession. This is very useful to the users and developers of non-mainstream
window managers and desktop environemts.

%package -n lxde-lxpolkit
Summary: Simple PolicyKit authentication agent
Group: Graphical desktop/Other
Requires: polkit >= 0.95

%description -n lxde-lxpolkit
LXPolKit is a simple PolicyKit authentication agent developed for LXDE, the
Lightweight X11 Desktop Environment.

%package -n %name-edit
Summary: LXDE Desktop Session Settings
Group: Graphical desktop/Other
Requires: %name = %version-%release

%description -n %name-edit
lxsession-edit is a tool used to manage desktop session autostarts, especially
for lxsession lite.

%prep
%setup
%patch -p2
%patch1 -p1
%patch2 -p1
%patch3 -p1

sed -i 's/^NotShowIn=GNOME;KDE;MATE;/OnlyShowIn=LXDE;/g' data/lxpolkit.desktop.in.in

%build
%__subst '/m4/ d' Makefile.am
%autoreconf
%configure --enable-man \
           --enable-debug \
           --disable-silent-rules \
%if %gtkver==3
           --enable-gtk3
%endif

%make_build

%install
%makeinstall_std

mkdir -p -m 755 %buildroot%_sysconfdir/xdg/%name

%find_lang %upstreamname

%files -f %upstreamname.lang
%doc AUTHORS ChangeLog COPYING README data/desktop.conf.example
%_bindir/%upstreamname
%_bindir/%upstreamname-logout
%_bindir/%upstreamname-db
%_bindir/%upstreamname-default
%_bindir/%upstreamname-default-apps
%_bindir/%upstreamname-default-terminal
%_libexecdir/%upstreamname
%_bindir/lxsettings-daemon
%_bindir/%upstreamname-xdg-autostart
%_bindir/lxlock
%_bindir/lxclipboard
%_datadir/%upstreamname
%exclude %_datadir/%upstreamname/ui/lxsession-edit.ui
%exclude %_datadir/%upstreamname/ui/lxpolkit.ui
%_man1dir/*
%_desktopdir/*.desktop
%exclude %_desktopdir/lxsession-edit.desktop

%files -n %name-edit
%_bindir/lxsession-edit
%_desktopdir/lxsession-edit.desktop
%_datadir/%upstreamname/ui/lxsession-edit.ui

%files -n lxde-lxpolkit
%_bindir/lxpolkit
%config %_sysconfdir/xdg/autostart/lxpolkit.desktop
%dir %_datadir/%upstreamname
%dir %_datadir/%upstreamname/ui
%_datadir/%upstreamname/ui/lxpolkit.ui

%changelog
* Wed Feb 08 2017 Anton Midyukov <antohami@altlinux.org> 0.5.3-alt2
- Delete requires lxde-lxpolkit

* Tue Jan 10 2017 Anton Midyukov <antohami@altlinux.org> 0.5.3-alt1
- New version 0.5.3
- New subpackage lxde-lxpolkit

* Sun May 22 2016 Anton Midyukov <antohami at altlinux.org> 0.5.2-alt2.20160418.1
- New package lxde-session-edit.

* Tue May 17 2016 Anton Midyukov <antohami@altlinux.org> 0.5.2-alt1.20160418.1
- New snapshot
- New provides lxde-session-edit
- Added patch (thank you fedora team).

* Mon Jun 11 2012 Radik Usupov <radik@altlinux.org> 0.4.6.1-alt3
- new upstream snapshot

* Tue Jan 31 2012 Radik Usupov <radik@altlinux.org> 0.4.6.1-alt2
- Added kdm support (Closes: 26823)

* Mon Aug 29 2011 Radik Usupov <radik@altlinux.org> 0.4.6.1-alt1
- new upstream snapshot

* Wed Apr 27 2011 Mykola Grechukh <gns@altlinux.ru> 0.4.5-alt1
- new upstream snapshot

* Mon Apr 12 2010 Nick S. Grechukh <gns@altlinux.ru> 0.4.4-alt1
- new version

* Fri Mar 12 2010 Nick S. Grechukh <gns@altlinux.ru> 0.4.2-alt1
- new version

* Tue Dec 22 2009 Mykola Grechukh <gns@altlinux.ru> 0.4.1-alt3
- settings daemon now integrated into lxsession

* Sat Dec 12 2009 Mykola Grechukh <gns@altlinux.ru> 0.4.1-alt2
- provides lxsession-lite to satisfy dependencies

* Sat Dec 12 2009 Nick S. Grechukh <gns@altlinux.ru> 0.4.1-alt1
- new version

* Wed Dec 09 2009 Mykola Grechukh <gns@altlinux.ru> 0.4.0-alt1
- new version

* Tue May 19 2009 Nick S. Grechukh <gns@altlinux.org> 0.3.8-alt1
- new version. Now lxsession is replaced by lxsession-lite in upstream.

* Fri Jan 09 2009 Eugene Ostapets <eostapets@altlinux.ru> 0.3.2-alt2
- Add conflicts to lxde-lxsession
- remove obsoletes %%update_menu macros

* Fri Jul 18 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.3.2-alt1
- new version 

* Fri May 23 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.1-alt1
- First version of RPM package for Sisyphus.
