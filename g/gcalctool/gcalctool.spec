%define ver_major 6.4
%def_without newtranslations

Name: gcalctool
Version: %ver_major.2.1
Release: alt1

Summary: GTK+3 based desktop calculator
License: %gpl2plus
Group: Sciences/Mathematics

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
%if_with newtranslations
Source1: %name-0.4.16.ru.po.bz2
%endif

Provides: gnome-calculator

BuildPreReq: rpm-build-licenses rpm-build-gnome

# Taken from configure.in
BuildPreReq: intltool yelp-tools itstool
BuildPreReq: libgtk+3-devel >= 3.0.7
BuildRequires: libgio-devel >= 2.31.0 libxml2-devel flex

%description
This package provides gcalctool, the calculator application that was
previously in the OpenWindows Deskset of the Solaris 8 operating system.

It incorporates a multiple precision arithmetic packages based on the work
of Professor Richard Brent.

A single graphics driver for GTK included with this package.

%prep
%setup -q

%if_with newtranslations
bzcat %SOURCE1 po/ru.po
%endif

%build
%configure \
    --disable-schemas-compile
%make_build

%install
%make_install DESTDIR=%buildroot install

# man page
install -pD -m644 data/%name.1 %buildroot%_man1dir/%name.1

%find_lang --with-gnome %name


%files -f %name.lang
%_bindir/*
%dir %_datadir/%name
%_datadir/%name/*.ui
%_desktopdir/*
%_man1dir/*
%config %_datadir/glib-2.0/schemas/org.gnome.gcalctool.gschema.xml
%doc AUTHORS NEWS README

%changelog
* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 6.4.2.1-alt1
- 6.4.2.1

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 6.4.1.1-alt1
- 6.4.1.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 6.4.0-alt1
- 6.4.0

* Tue Sep 27 2011 Yuri N. Sedunov <aris@altlinux.org> 6.2.0-alt1
- 6.2.0

* Tue May 24 2011 Yuri N. Sedunov <aris@altlinux.org> 6.0.2-alt1
- 6.0.2

* Mon Nov 15 2010 Yuri N. Sedunov <aris@altlinux.org> 5.32.1-alt1
- 5.32.1

* Mon Oct 04 2010 Yuri N. Sedunov <aris@altlinux.org> 5.32.0-alt1
- 5.32.0

* Tue Jun 22 2010 Yuri N. Sedunov <aris@altlinux.org> 5.30.2-alt1
- 5.30.2

* Mon Apr 26 2010 Yuri N. Sedunov <aris@altlinux.org> 5.30.1-alt1
- 5.30.1

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 5.30.0-alt1
- 5.30.0

* Tue Mar 09 2010 Yuri N. Sedunov <aris@altlinux.org> 5.29.92-alt1
- 5.29.92
- updated buildreqs

* Mon Feb 22 2010 Yuri N. Sedunov <aris@altlinux.org> 5.29.91-alt1
- 5.29.91

* Tue Feb 09 2010 Yuri N. Sedunov <aris@altlinux.org> 5.29.90-alt1
- 5.29.90

* Wed Dec 16 2009 Yuri N. Sedunov <aris@altlinux.org> 5.28.2-alt1
- 5.28.2

* Mon Oct 19 2009 Yuri N. Sedunov <aris@altlinux.org> 5.28.1-alt1
- 5.28.1

* Tue Sep 22 2009 Yuri N. Sedunov <aris@altlinux.org> 5.28.0-alt1
- 5.28.0

* Thu Aug 20 2009 Yuri N. Sedunov <aris@altlinux.org> 5.27.90-alt1
- 5.27.90

* Tue Jun 30 2009 Yuri N. Sedunov <aris@altlinux.org> 5.26.3-alt1
- 5.26.3

* Sun May 17 2009 Yuri N. Sedunov <aris@altlinux.org> 5.26.2-alt1
- 5.26.2

* Sun Apr 12 2009 Yuri N. Sedunov <aris@altlinux.org> 5.26.1-alt1
- 5.26.1

* Wed Mar 18 2009 Yuri N. Sedunov <aris@altlinux.org> 5.26.0-alt1
- 5.26.0
- updated buildreqs

* Mon Jan 26 2009 Yuri N. Sedunov <aris@altlinux.org> 5.24.3.1-alt1
- new version

* Mon Jan 12 2009 Yuri N. Sedunov <aris@altlinux.org> 5.24.3-alt1
- 5.24.3

* Tue Nov 25 2008 Yuri N. Sedunov <aris@altlinux.org> 5.24.2-alt1
- 5.24.2
- removed obsolete %%post* scripts

* Mon Oct 20 2008 Yuri N. Sedunov <aris@altlinux.org> 5.24.1-alt1
- 5.24.1

* Mon Sep 29 2008 Yuri N. Sedunov <aris@altlinux.org> 5.24.0-alt1
- 5.24.0

* Mon Apr 28 2008 Alexey Rusakov <ktirf@altlinux.org> 5.23.1-alt1
- New version (5.23.1); the stable version appeared to be less stable than
  the unstable one...

* Sun Apr 27 2008 Alexey Rusakov <ktirf@altlinux.org> 5.22.1-alt1
- New version (5.22.1).
- No more scrollkeeper in Sisyphus.
- Files list updated.

* Wed Feb 13 2008 Alexey Rusakov <ktirf@altlinux.org> 5.21.91-alt1
- New version (5.21.91).
- Updated buildreqs.

* Thu Oct 18 2007 Alexey Rusakov <ktirf@altlinux.org> 5.20.2-alt1
- new version (5.20.2)
- use more macros, including those from rpm-build-{licenses,gnome}
- added update/clean_menus calls to support WMs that don't know how to deal
  with .desktop files.
- updated dependencies
- eliminated %%__ macro usages

* Tue Jul 31 2007 Alexey Rusakov <ktirf@altlinux.org> 5.19.6-alt1
- new version 5.19.6 (with rpmrb script)

* Mon Jul 09 2007 Alexey Rusakov <ktirf@altlinux.org> 5.19.5-alt1
- new version 5.19.5 (with rpmrb script)

* Mon Jun 18 2007 Alexey Rusakov <ktirf@altlinux.org> 5.19.4-alt1
- new version (5.19.4)
- In this version, libgnome{,ui} dependency has been removed. Startup times
  should improve, and libgnome should die anyway.

* Tue May 15 2007 Alexey Rusakov <ktirf@altlinux.org> 5.19.2-alt1
- new version 5.19.2 (with rpmrb script)

* Mon Apr 02 2007 Alexey Rusakov <ktirf@altlinux.org> 5.9.14-alt1
- new version 5.9.14 (with rpmrb script)

* Mon Feb 12 2007 Alexey Rusakov <ktirf@altlinux.org> 5.9.12-alt1
- new version 5.9.12 (with rpmrb script)

* Mon Sep 25 2006 Alexey Rusakov <ktirf@altlinux.ru> 5.8.24-alt1
- new version 5.8.24 (with rpmrb script)

* Fri Aug 18 2006 Alexey Rusakov <ktirf@altlinux.ru> 5.8.23-alt1
- new version 5.8.23 (with rpmrb script)

* Tue Aug 08 2006 Alexey Rusakov <ktirf@altlinux.ru> 5.8.20-alt1
- new version 5.8.20 (with rpmrb script)

* Mon Jul 17 2006 Alexey Rusakov <ktirf@altlinux.ru> 5.8.17-alt2
- Added Provides: gnome-calculator

* Fri Jul 14 2006 Alexey Rusakov <ktirf@altlinux.ru> 5.8.17-alt1
- new version 5.8.17 (with rpmrb script)

* Sun Jun 11 2006 Alexey Rusakov <ktirf@altlinux.ru> 5.8.16-alt1
- new version
- updated buildreqs

* Wed Apr 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 5.7.30-alt2
- removed Debian menu support.
- spec cleanup.

* Tue Feb 28 2006 Alexey Rusakov <ktirf@altlinux.ru> 5.7.30-alt1
- new version (5.7.30)

* Wed Feb 01 2006 Alexey Rusakov <ktirf@altlinux.ru> 5.7.28-alt1
- new version

* Tue Jan 24 2006 Alexey Rusakov <ktirf@altlinux.ru> 5.7.27-alt1
- new version

* Wed Jan 18 2006 Alexey Rusakov <ktirf@altlinux.ru> 5.7.26-alt1
- new version

* Sun Jan 15 2006 Alexey Rusakov <ktirf@altlinux.ru> 5.7.23-alt1
- new version

* Tue Nov 15 2005 Alexey Rusakov <ktirf@altlinux.ru> 5.7.11-alt1
- new version

* Fri Oct 14 2005 Alexey Rusakov <ktirf@altlinux.ru> 5.7.8-alt1
- new version

* Sun Sep 25 2005 Alexey Rusakov <ktirf@altlinux.ru> 5.6.31-alt1
- 5.6.31
- Removed excess buildreqs.

* Mon Apr 18 2005 Yuri N. Sedunov <aris@altlinux.ru> 5.5.42-alt1
- new version.

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 5.5.41-alt1
- 5.5.41

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 4.4.18-alt1
- 4.4.18

* Sat Jul 31 2004 Yuri N. Sedunov <aris@altlinux.ru> 4.4.16-alt1
- 4.4.16

* Thu Jul 29 2004 Yuri N. Sedunov <aris@altlinux.ru> 4.4.14-alt1
- 4.4.14

* Tue Mar 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 4.3.51-alt1
- 4.3.51

* Wed Feb 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 4.3.42-alt1
- 4.3.42

* Tue Sep 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 4.3.3-alt1
- 4.3.3

* Wed Aug 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 4.3.2-alt1
- 4.3.2

* Thu Aug 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 4.3.0-alt1
- 4.3.0

* Tue Jul 15 2003 Yuri N. Sedunov <aris@altlinux.ru> 4.2.99-alt1
- 4.2.99

* Wed May 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 4.2.86-alt1
- new version.

* Sun May 18 2003 Yuri N. Sedunov <aris@altlinux.ru> 4.2.83-alt1
- First build for Sisyphus.

