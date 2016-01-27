%define ver_major 3.18
%define _libexecdir %_prefix/libexec

Name: gnome-calculator
Version: %ver_major.3
Release: alt1

Summary: GTK+3 based desktop calculator
License: %gpl2plus
Group: Sciences/Mathematics
Url: https://wiki.gnome.org/Apps/Calculator

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

Obsoletes: gcalctool <= 6.6.2
Provides: gcalctool = 6.6.2

BuildPreReq: rpm-build-licenses rpm-build-gnome

BuildPreReq: intltool yelp-tools
BuildPreReq: libgtk+3-devel >= 3.12
BuildRequires: libgio-devel >= 2.40.0 libxml2-devel vala-tools >= 0.24
BuildRequires: libmpfr-devel libgtksourceview3-devel >= 3.16

%description
This package provides gcalctool, the calculator application that was
previously in the OpenWindows Deskset of the Solaris 8 operating system.

It incorporates a multiple precision arithmetic packages based on the work
of Professor Richard Brent.

A single graphics driver for GTK included with this package.

%prep
%setup

%build
%configure --disable-static \
    --disable-schemas-compile
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_libexecdir/%name-search-provider
%_libdir/%name/libcalculator.so
%_datadir/dbus-1/services/org.gnome.Calculator.SearchProvider.service
%_datadir/gnome-shell/search-providers/gnome-calculator-search-provider.ini
%_desktopdir/%name.desktop
%_man1dir/%name.1.*
%_man1dir/gcalccmd.1.*
%config %_datadir/glib-2.0/schemas/org.gnome.calculator.gschema.xml
%_datadir/appdata/%name.appdata.xml
%doc NEWS

%exclude %_libdir/%name/*.la

%changelog
* Wed Jan 27 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3

* Tue Nov 10 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Wed Jun 10 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Fri May 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Sun Oct 26 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Mon Sep 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.4-alt1
- 3.12.4

* Mon Jun 16 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.3-alt1
- 3.12.3

* Thu Apr 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Mon Nov 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Sat Oct 19 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Wed Sep 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Sun Apr 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Mon Feb 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.90-alt1
- gcalctool -> gnome-calculator

