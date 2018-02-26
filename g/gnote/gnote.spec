%define _libexecdir /usr/libexec

Name: gnote
Version: 0.8.1
Release: alt1
Summary: Note-taking application
Group: Graphical desktop/GNOME
License: GPLv3+
Url: http://live.gnome.org/Gnote
Packager: GNOME Maintainers Team <gnome at packages.altlinux.org>

Source0: http://ftp.gnome.org/pub/GNOME/sources/gnote/%version/%name-%version.tar
Patch0: %name-%version-%release.patch

%define gtk_ver 3.0
%define gtkmm_ver 3.0
%define glibmm_ver 2.28
%define libpanelapplet_ver 3.0
%define gtkspell_ver 2.0.9

BuildRequires: gcc-c++ boost-devel
BuildRequires: gnome-common gnome-doc-utils intltool
BuildRequires: libxml2-devel libxslt-devel
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libglibmm-devel >= %glibmm_ver
BuildRequires: libgtkmm3-devel >= %gtkmm_ver
BuildRequires: libgnome-panel-devel >= %libpanelapplet_ver
# BuildRequires: libgtkspell-devel >= %gtkspell_ver
BuildRequires: libpcrecpp-devel
BuildRequires: libuuid-devel
BuildRequires: desktop-file-utils

%description
Gnote is a desktop note-taking application which is simple and easy to use.
It lets you organize your notes intelligently by allowing you to easily link
ideas together with Wiki style interconnects. It is a port of Tomboy to C++
and consumes fewer resources.

%prep
%setup -q
%patch0 -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static --enable-applet

%make_build

%install
%make DESTDIR=%buildroot install

desktop-file-install \
 --dir=%buildroot%_datadir/applications \
%buildroot/%_datadir/applications/gnote.desktop

%find_lang %name --with-gnome

%files -f %name.lang
%doc COPYING README TODO NEWS AUTHORS
%_bindir/%name
%_man1dir/%name.*
%_desktopdir/%name.desktop
%_datadir/%name
%_iconsdir/hicolor/*/apps/%name.??g
%_libdir/gnote
%exclude %_libdir/gnote/addins/*/*.la
%_datadir/dbus-1/services/org.gnome.Gnote.service
%_datadir/glib-2.0/schemas/*.xml

# applet
%_datadir/dbus-1/services/org.gnome.panel.applet.GnoteAppletFactory.service
%_libexecdir/gnote-applet
%_datadir/gnome-panel/4.0/applets/org.gnome.gnote.panel-applet

%changelog
* Mon Oct 31 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Thu Oct 06 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0
- enable panel applet

* Fri May 27 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.4-alt2
- Disable panel applet

* Tue May 24 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.4-alt1
- 0.7.4

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt3.2
- Rebuilt with Boost 1.46.1

* Thu Dec 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.7.2-alt3.1
- rebuild with new icu44 and/or boost by request of git.alt administrator

* Tue Oct 19 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.2-alt3
- pre 0.7.3

* Mon May 24 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.2-alt2
- git snapshot bca27f4

* Fri Mar 12 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Fri Jan 15 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.1-alt1
- 0.7.1

* Tue Oct 06 2009 Alexey Shabalin <shaba@altlinux.ru> 0.6.2-alt1
- 0.6.2
- add packager
- update BuildRequires

* Thu Jun 18 2009 Anton Farygin <rider@altlinux.ru> 0.5.0-alt1
- first build for Sisyphus, based on RH spec
