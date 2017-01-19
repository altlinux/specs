%define ver_major 9.7
%define gst_api_ver 1.0
%def_with recording

Name: girl
Version: %ver_major.1
Release: alt1

Summary: GNOME Internet Radio Locator
License: LGPLv2+
Group: Sound
Url: https://wiki.gnome.org/Apps/Girl

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: gst-plugins-base%gst_api_ver
Requires: gst-plugins-bad%gst_api_ver
Requires: gst-plugins-ugly%gst_api_ver

%define gtk_ver 3.6.0

BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: gnome-common intltool yelp-tools gtk-doc
BuildRequires: libgnomeui-devel libxml2-devel
BuildRequires: gst-plugins%gst_api_ver-devel

%description
GIRL is a GNOME Internet Radio Locator program that allows the user
to easily find and record live radio programs on radio broadcasters
on the Internet.

%prep
%setup
#echo "girl_LDADD=\$(GIRL_LIBS)" >> src/Makefile.am

%build
%autoreconf
%configure \
	%{subst_with recording}
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/%name/
%_iconsdir/hicolor/*x*/apps/%name.png
%_datadir/appdata/%name.appdata.xml
%_man1dir/%name.1.*
%doc AUTHORS NEWS README TODO LETTER HACKING


%changelog
* Thu Jan 19 2017 Yuri N. Sedunov <aris@altlinux.org> 9.7.1-alt1
- 9.7.1

* Mon Sep 26 2016 Yuri N. Sedunov <aris@altlinux.org> 9.5.2-alt1
- 9.5.2

* Sat Aug 27 2016 Yuri N. Sedunov <aris@altlinux.org> 9.5.1-alt1
- 9.5.1

* Sun Aug 14 2016 Yuri N. Sedunov <aris@altlinux.org> 9.5.0-alt1
- 9.5.0

* Mon Jul 11 2016 Yuri N. Sedunov <aris@altlinux.org> 9.4.0-alt1
- 9.4.0

* Sat Jul 02 2016 Yuri N. Sedunov <aris@altlinux.org> 9.3.0-alt1
- 9.3.0

* Sat Jun 11 2016 Yuri N. Sedunov <aris@altlinux.org> 9.2.0-alt1
- 9.2.0

* Tue Jun 07 2016 Yuri N. Sedunov <aris@altlinux.org> 9.1.0-alt1
- 9.1.0

* Tue May 31 2016 Yuri N. Sedunov <aris@altlinux.org> 9.0.1-alt1
- 9.0.1

* Fri May 06 2016 Yuri N. Sedunov <aris@altlinux.org> 8.4.2-alt1
- 8.4.2

* Sun Apr 03 2016 Yuri N. Sedunov <aris@altlinux.org> 8.4.0-alt1
- 8.4.0

* Sun Jan 17 2016 Yuri N. Sedunov <aris@altlinux.org> 8.0.0-alt1
- 8.0.0

* Thu Jan 07 2016 Yuri N. Sedunov <aris@altlinux.org> 7.0.0-alt1
- 7.0.0

* Thu Nov 12 2015 Yuri N. Sedunov <aris@altlinux.org> 6.1.0-alt1
- 6.1.0

* Wed Jul 01 2015 Yuri N. Sedunov <aris@altlinux.org> 6.0.0-alt1
- 6.0.0

* Sun May 03 2015 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- 4.0.0

* Sat Apr 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Tue Mar 31 2015 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0

* Sun Feb 22 2015 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Sat Jan 24 2015 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Thu Jan 08 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Mon Dec 29 2014 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt1
- first build for Sisyphus

