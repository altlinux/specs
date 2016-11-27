%define ver_major 3.22
%define _libexecdir /usr/libexec
%def_without x11_support

Name: gnote
Version: %ver_major.1
Release: alt1

Summary: Note-taking application
Group: Graphical desktop/GNOME
License: GPLv3+
Url: https://wiki.gnome.org/Apps/Gnote

Source: http://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define gtk_ver 3.20
%define gtkmm_ver 3.18
%define glibmm_ver 2.32
%define gtkspell_ver 3.0.0
%define libsecret_ver 0.8
%define boost_ver 1.34

BuildRequires: gcc-c++ boost-devel
BuildRequires: yelp-tools intltool
BuildRequires: pkgconfig(glibmm-2.4)  >= %glibmm_ver
BuildRequires: pkgconfig(gtk+-3.0) >= %gtk_ver
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(gtkmm-3.0) >= %gtkmm_ver
BuildRequires: pkgconfig(glib-2.0) >= 2.32
BuildRequires: pkgconfig(libxml-2.0) pkgconfig(libxslt)
BuildRequires: pkgconfig(gtkspell3-3.0) >= %gtkspell_ver
BuildRequires: pkgconfig(libsecret-1) >= %libsecret_ver
BuildRequires: pkgconfig(uuid)
BuildRequires: desktop-file-utils

%description
Gnote is a desktop note-taking application which is simple and easy to use.
It lets you organize your notes intelligently by allowing you to easily link
ideas together with Wiki style interconnects. It is a port of Tomboy to C++
and consumes fewer resources.

%prep
%setup

%build
# NOCONFIGURE=1 ./autogen.sh
#%autoreconf
%configure \
	%{?_with_x11_support:--with-x11-support} \
	--with-cxx11-support \
	--disable-static

%make_build

%install
%makeinstall_std

desktop-file-install \
 --dir=%buildroot%_datadir/applications \
%buildroot/%_datadir/applications/gnote.desktop

%find_lang %name --with-gnome

%check
%make check

%files -f %name.lang
%_bindir/%name
%_libdir/libgnote-*.so.*
%_man1dir/%name.*
%_desktopdir/%name.desktop
%_datadir/%name
%_iconsdir/hicolor/*/apps/%name.??g
%_libdir/gnote/
%exclude %_libdir/gnote/addins/*/*.la
%_datadir/dbus-1/services/org.gnome.Gnote.service
%_datadir/glib-2.0/schemas/*.xml
%_datadir/appdata/gnote.appdata.xml
%_datadir/gnome-shell/search-providers/gnote-search-provider.ini
%doc README TODO NEWS AUTHORS

%changelog
* Sun Nov 27 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 26 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Sun Sep 18 2016 Yuri N. Sedunov <aris@altlinux.org> 3.21.1-alt1
- 3.21.1

* Sun May 15 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Sat Mar 26 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Sat Nov 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Sun Sep 27 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Sun Sep 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.17.1-alt1
- 3.17.1

* Sun Jul 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Mon Jun 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.16.0-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Mon Mar 30 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Jan 19 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Tue Sep 30 2014 Alexey Shabalin <shaba@altlinux.ru> 3.14.0-alt1
- 3.14.0

* Wed Mar 26 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.0-alt1
- 3.12.0

* Mon Feb 24 2014 Alexey Shabalin <shaba@altlinux.ru> 3.10.3-alt1
- 3.10.3

* Tue Dec 31 2013 Alexey Shabalin <shaba@altlinux.ru> 3.10.2-alt1
- 3.10.2

* Mon Oct 28 2013 Alexey Shabalin <shaba@altlinux.ru> 3.10.1-alt1
- 3.10.1

* Tue Oct 08 2013 Alexey Shabalin <shaba@altlinux.ru> 3.10.0-alt1
- 3.10.0

* Mon May 13 2013 Alexey Shabalin <shaba@altlinux.ru> 3.8.1-alt1
- 3.8.1

* Wed Mar 27 2013 Alexey Shabalin <shaba@altlinux.ru> 3.8.0-alt1
- 3.8.0

* Tue Jan 22 2013 Alexey Shabalin <shaba@altlinux.ru> 3.6.2-alt1
- 3.6.2

* Wed Oct 31 2012 Alexey Shabalin <shaba@altlinux.ru> 3.6.1-alt1
- 3.6.1

* Fri Oct 26 2012 Alexey Shabalin <shaba@altlinux.ru> 3.6.0-alt1
- 3.6.0

* Fri Jul 20 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.1-alt1
- 0.9.1
- upstream drop support for panel applet

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
