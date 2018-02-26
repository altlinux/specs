Name: xfce4-places-plugin
Version: 1.3.0
Release: alt1

Summary: This plugin is a menu with quick access to folders, documents, and removable media
License: %gpl2plus
Group: Graphical desktop/XFce
Url: http://goodies.xfce.org/projects/panel-plugins/%name
Packager: XFCE Team <xfce@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-devel libxfce4ui-devel libxfce4util-devel libexo-devel
BuildPreReq: libgio-devel libnotify-devel
BuildRequires: libxml2-devel intltool

Requires: xfce4-panel >= 4.8

%description
This xfce4-places-plugin brings much of the functionality of GNOME's
Places menu to Xfce.
The plugin looks a lot like a launcher with multiple items in a menu.
The main "launcher" button opens up Thunar at the user's home directory.
The arrow button opens up a menu with two sections: system-defined
locations and user-defined locations.
The system-defined locations are consistent with Thunar (including their
icons).
For user-defined bookmarks, the plugin reads the ~/.gtk-bookmarks file
so that it shares bookmarks with Thunar, Nautilus, the GNOME Panel, etc.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--enable-gio-unix \
	--enable-notifications \
	--enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README AUTHORS
%_bindir/xfce4-popup-places
%_libexecdir/xfce4/panel-plugins/*
%_datadir/xfce4/panel/plugins/*.desktop

%changelog
* Fri Apr 13 2012 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt1
- Updated to 1.3.0.

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt4.git20110107
- Rebuild with xfce4-panel-4.9.

* Thu Sep 01 2011 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt3.git20110107
- Rebuild for libnotify 0.7.

* Mon Mar 21 2011 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt2.git20110107
- Don't to package Changelog.
- Really fix implicit DSO linking.
- Port to gio (patch from Xfce bug #6663).
- Port to libxfce4ui (patch from Xfce bug #7317).
- Updated from upstream's git.

* Tue Feb 08 2011 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Fix desktop file path for xfce4-panel >= 4.8.
- Add patches from Fedora.
- Spec updated, tar.bz2 -> tar.
- Updated to 1.2.0.

* Fri May 08 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.0-alt2
- rebuild, update requires

* Sat Jan 05 2008 Eugene Ostapets <eostapets@altlinux.ru> 1.0.0-alt1
- new version
- add watch file

* Thu May 03 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.2.0-alt1
- first build

