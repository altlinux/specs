%define ver_major 3.4
%define api_ver %ver_major
%define ua_ver %ver_major
%def_enable gtk_doc
%def_enable zeroconf
%def_enable introspection
%if_enabled introspection
%def_enable seed
%endif

Name: epiphany
Version: %ver_major.2
Release: alt1

Summary: Epiphany is a GNOME web browser.
Summary(ru_RU.UTF-8): Epiphany - интернет-браузер для графической оболочки GNOME.
Group: Networking/WWW
License: GPL
URL: http://www.gnome.org/projects/%name

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Provides: webclient

%define webkit_ver 1.7.92

Requires: %name-data = %version-%release indexhtml iso-codes libwebkitgtk3-webinspector

BuildPreReq: gnome-common
BuildPreReq: intltool >= 0.40.0
BuildPreReq: libgio-devel >= 2.31.2
BuildPreReq: libgtk+3-devel >= 3.3.8
BuildPreReq: libSM-devel
BuildPreReq: libxml2-devel >= 2.6.12
BuildPreReq: libxslt-devel >= 1.1.7
BuildPreReq: libwebkitgtk3-devel >= %webkit_ver
BuildPreReq: libsoup-gnome-devel >= 2.37.1
BuildPreReq: libgnome-keyring-devel >= 2.32.0
BuildRequires: libnotify-devel libnss-devel libsqlite3-devel
# Zeroconf support
%{?_enable_zeroconf:BuildPreReq: libavahi-devel libavahi-gobject-devel}
# GObject introspection support
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= 0.9.5 libgtk+3-gir-devel libwebkitgtk3-gir-devel}
# Seed support
%{?_enable_seed:BuildPreReq: libseed-gtk3-devel >= 3.1.1}

BuildPreReq: iso-codes-devel >= 0.35
BuildPreReq: lsb-core ca-certificates
BuildPreReq: gnome-doc-utils gtk-doc db2latex-xsl

BuildRequires: gcc-c++ gsettings-desktop-schemas-devel

%description
Epiphany is a GNOME web browser based on the Webkit rendering engine.
%description -l ru_RU.UTF8
Epiphany - интернет-браузер для графической
оболочки GNOME, основанный на движке
отрисовки страниц Webkit.

%package data
Summary: Epiphany data files
Group: Networking/WWW
BuildArch: noarch

%description data
Epiphany is a GNOME web browser based on the Webkit rendering engine.
This package contains common noarch files needed for Epiphany.

%package devel
Summary: Epiphany header files
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides header files needed for build Epiphany extensions.

%package devel-doc
Summary: Epiphany development documentation
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package contains documentation needed to develop Epipnahy
extensions.

%package gir
Summary: GObject introspection data for the Epiphany
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Epiphany

%package gir-devel
Summary: GObject introspection devel data for the Epiphany
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the Epiphany

%prep
%setup -q

%build
gnome-doc-prepare -f
%autoreconf
%configure \
	--disable-schemas-compile \
	--disable-scrollkeeper \
	--disable-dependency-tracking \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{subst_enable zeroconf} \
	%{subst_enable introspection} \
	%{subst_enable seed} \
	--with-distributor-name="ALTLinux"

%make_build

%install
%make_install install DESTDIR=%buildroot

%__mkdir_p %buildroot{%_libdir/epiphany/%ua_ver/extensions,%_datadir/epiphany-extensions}

%find_lang --with-gnome --output=%name.lang %name %name-2.0

%files
%_bindir/*
%dir %_libdir/%name/%ua_ver/extensions
%doc AUTHORS NEWS README TODO

%files data -f %name.lang
%_datadir/applications/*
%_datadir/%name
%_datadir/dbus-1/services/*
%config %_datadir/glib-2.0/schemas/org.gnome.epiphany.gschema.xml
%config %_datadir/glib-2.0/schemas/org.gnome.Epiphany.enums.xml
%_datadir/GConf/gsettings/epiphany.convert
%_man1dir/*

%files devel
%_includedir/*
%_libdir/pkgconfig/*
%_datadir/aclocal/*

%files devel-doc
%doc %_datadir/gtk-doc/html/*

%if_enabled introspection
%files gir
%_typelibdir/Epiphany-%ver_major.typelib

%files gir-devel
%_girdir/Epiphany-%ver_major.gir
%endif

%changelog
* Sat May 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Wed Apr 18 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Wed Mar 28 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0.1-alt1
- 3.4.0.1

* Tue Oct 18 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Tue Sep 27 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Fri Jul 01 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.4-alt1
- 3.0.4

* Fri May 13 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Mon May 02 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Sat Apr 23 2011 Yuri N. Sedunov <aris@altlinux.org> 2.30.6-alt2
- added x-scheme-handler/http{,s} mimetypes to epiphany.desktop

* Wed Oct 06 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.6-alt1
- 2.30.6

* Wed Sep 01 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.5-alt1
- 2.30.5

* Thu Apr 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Wed Mar 31 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt2
- rebuild with new rpm-build-gir (0.2-alt1)

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt2
- rebuild using rpm-build-gir

* Tue Feb 23 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Wed Feb 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90.1-alt1
- 2.29.90.1

* Wed Feb 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt2
- build for Sisyphus, untrospection support temporarily disabled

* Mon Feb 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt1
- 2.29.90

* Tue Jan 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.6-alt1
- 2.29.6

* Tue Jan 12 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.5-alt1
- 2.29.5
- updated buildreqs

* Wed Dec 02 2009 Yuri N. Sedunov <aris@altlinux.org> 2.29.3-alt1
- 2.29.3
- gobject-introspection, seed support

* Wed Sep 30 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt2
- restored defaulthome.patch

* Wed Sep 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Thu Sep 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Tue Aug 25 2009 Alexey Shabalin <shaba@altlinux.ru> 2.27.91-alt1
- 2.27.91
- webkit based

* Mon Jun 29 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3

* Mon May 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt2
- fixed path to mozilla plugins directory (patch2 by shrek@)

* Mon Apr 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Tue Mar 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.91-alt1
- 2.25.91
- updated buildreqs

* Tue Jan 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Mon Dec 29 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt2
- updated buildreqs

* Mon Nov 24 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- removed obsolete %%post* scripts

* Tue Oct 21 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Tue Sep 23 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0.1-alt1
- 2.24.0.1
- requires xulrunner-gnome-support

* Sat Sep 06 2008 Yuri N. Sedunov <aris@altlinux.org> 2.23.91-alt1
- new version
- don't rebild documentation
- requires xulrunner (altbug ##16334, 16435)

* Wed Jul 09 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.3-alt2
- rebuild with xulrunner
- update schemeas list

* Wed Jul 02 2008 Yuri N. Sedunov <aris@altlinux.org> 2.22.3-alt1
- new version.
- enabled gtk-doc
- zeroconf bookmarks support enabled

* Wed May 28 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.22.2-alt1
- 2.22.2

* Wed Apr 09 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.22.1.1-alt1
- 2.22.1.1

* Tue Mar 11 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.22.0-alt1
- 2.22.0

* Mon Jan 14 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.3-alt1
- 2.20.3

* Fri Dec 14 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.2-alt2
- Replace python2.4 by python%__python_version

* Thu Nov 29 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.2-alt1
- 2.20.2

* Fri Oct 19 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.1-alt1
- 2.20.1

* Thu Sep 20 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.0-alt1
- 2.20.0

* Mon Aug 20 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.3-alt1
- 2.18.3

* Sun Jun 24 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.2-alt2
- Correct buildreq

* Sat Jun 16 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.2-alt1
- 2.18.2

* Thu Apr 26 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.1-alt1
- 2.18.1

* Mon Mar 12 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.0-alt0.1
- 2.18.0

* Wed Mar 07 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.17.92-alt0.1
- 2.17.92 (!!!WARNING!!! this is an experimental build)

* Fri Feb 02 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.3-alt1
- 2.16.3

* Mon Nov 27 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.2-alt3
- Correct buildreq

* Mon Nov 27 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.2-alt1
- 2.16.2

* Mon Oct 09 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.1-alt1
- 2.16.1

* Thu Sep 07 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.0-alt1
- 2.16.0
- Rebuild with firefox (as yelp does)

* Thu Aug 17 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.3-alt2
- Correct auto buildreq list

* Tue Aug 15 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.3-alt1
- 2.14.3

* Thu Jun 01 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.2.1-alt1
- 2.14.2.1

* Fri Apr 14 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.1-alt1
- 2.14.1

* Tue Mar 14 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.0-alt2
- ChangeLog corrected

* Mon Mar 13 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.0-alt1
- 2.14.0

* Fri Mar 10 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 1.9.99-alt1
- 1.9.99

* Tue Mar 07 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 1.9.7-alt2
- Disable --as-needed flag for linker

* Wed Feb 15 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 1.9.7-alt1
- 1.9.7

* Fri Oct 28 2005 Sergey N. Yatskevich <syatskevich@altlinux.ru> 1.9.1-alt1
- 1.9.1

* Mon Oct 10 2005 Sergey N. Yatskevich <syatskevich@altlinux.ru> 1.8.2-alt2
- Correct BuildPreReq

* Mon Oct 03 2005 Sergey N. Yatskevich <syatskevich@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Tue Sep 13 2005 Sergey N. Yatskevich <syatskevich@altlinux.ru> 1.8.0-alt3
- 1.8.0

* Sat Jul 16 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.6.4-alt1.1
- rebuild with new libdbus-1.so.0 .

* Wed Jul 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.6.4-alt1
- 1.6.4

* Sat Apr 23 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.6.3-alt1
- 1.6.3
- fixed %%files (close #6448).

* Sat Apr 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Wed Mar 16 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.6.0-alt2
- run epiphany thru the wrapper to set proper MOZ_PLUGIN_PATH variable.

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Fri Mar 04 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.5.8-alt1
- 1.5.8

* Fri Jan 28 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.4.7-alt1
- 1.4.7

* Thu Dec 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.4.6-alt1
- 1.4.6

* Wed Oct 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.4.4-alt1
- 1.4.4

* Wed Sep 29 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Mon Sep 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.3.8-alt1
- 1.3.8

* Sat Aug 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.2.8-alt1
- 1.2.8
- requires mozilla-1.7.2
- truly fix #5009

* Wed Aug 18 2004 Vital Khilko <vk@altlinux.ru> 1.2.7-alt1
- 1.2.7
- fixed #5009

* Wed Jul 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.2.6-alt2
- rebuild against new mozilla-1.7

* Thu Jun 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.2.6-alt1
- 1.2.6

* Thu Apr 29 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Fri Apr 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Tue Feb 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.1.9-alt1
- 1.1.9

* Mon Feb 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.1.8-alt1
- 1.1.8

* Fri Feb 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.1.7-alt1
- 1.1.7

* Fri Dec 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.6-alt1
- new version.

* Thu Sep 18 2003 AEN <aen@altlinux.ru> 1.0-alt1
- release

* Wed Aug 27 2003 AEN <aen@altlinux.ru> 0.9.2-alt1
- new version
- pc-file moved to devel
- homedir patch from MDK

* Tue Aug 05 2003 AEN <aen@altlinux.ru> 0.8.2-alt1
- new version
- devel package

* Sun Jul 20 2003 AEN <aen@altlinux.ru> 0.8.0-alt1
- new version

* Wed Jul 02 2003 AEN <aen@altlinux.ru> 0.7.3-alt1
- new version
- new spec from aris@
- bump mozilla version up to 1.4

* Tue Jun 10 2003 AEN <aen@altlinux.ru> 0.7.0-alt1
- new version

* Mon Apr 14 2003 AEN <aen@altlinux.ru> 0.5.0-alt1
- first spec for Sisyphus
