Name: gshutdown
Version: 0.3
Release: alt0.svn634.1
License: GPL
Group: Graphical desktop/Other
Url: http://gshutdown.tuxfamily.org
Packager: Eugene Ostapets <eostapets@altlinux.org>

Summary: An advanced shutdown utility

Source: %name-%version.tar.gz
Patch1: gshutdown-0.3-alt-libnotify-api.patch
Patch2: gshutdown-0.3-alt-fix-linking.patch
Patch3: gshutdown-0.3-alt-glib2.patch

BuildRequires: intltool libXau-devel libX11-devel libdbus-glib-devel libglade-devel libnotify-devel

%description
GShutdown is an advanced shutdown utility which allows you to schedule
the shutdown or the restart of your computer. With it, you can simply
and quickly choose the turn off time.

The graphical user interface uses Gtk+2.

Features :

* Shutdown, reboot and logout : immediately or scheduled
* No need to be root
* Possibility to choose custom commands for the actions
* Three different ways to schedule the action
* Systray icon
* Visuals notifications

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p2

%build
%autoreconf
%configure --enable-libnotify=yes
%make_build

%install
%make DESTDIR=%buildroot install
%find_lang %name

%files -f %name.lang
%doc README ChangeLog NEWS AUTHORS COPYING
%_bindir/*
%dir %_datadir/%name
%_datadir/%name/*
%_pixmapsdir/%name.png
%_desktopdir/%name.desktop
%_mandir/*/*

%changelog
* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt0.svn634.1
- Fixed build

* Thu Sep 01 2011 Alexey Shabalin <shaba@altlinux.ru> 0.3-alt0.svn634
- NMU
- svn snapshot 634
- add patch for libnotify-0.7
- add patch for fix linking
- update build dependencies

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.2-alt1.1
- NMU:
  * updated build dependencies

* Sat Jan 26 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.2-alt1
- first build

