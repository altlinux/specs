%define ver_major 3.10
%def_without newtranslations

Name: gnome-calculator
Version: %ver_major.1
Release: alt1

Summary: GTK+3 based desktop calculator
License: %gpl2plus
Group: Sciences/Mathematics

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
%if_with newtranslations
Source1: %name-0.4.16.ru.po.bz2
%endif

Obsoletes: gcalctool <= 6.6.2
Provides: gcalctool = 6.6.2

BuildPreReq: rpm-build-licenses rpm-build-gnome

# Taken from configure.in
BuildPreReq: intltool yelp-tools itstool
BuildPreReq: libgtk+3-devel >= 3.0.7
BuildRequires: libgio-devel >= 2.31.0 libxml2-devel vala-tools >= 0.18

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
%_desktopdir/*
%_man1dir/*
%config %_datadir/glib-2.0/schemas/org.gnome.calculator.gschema.xml
%_datadir/appdata/%name.appdata.xml
%doc NEWS

%changelog
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

