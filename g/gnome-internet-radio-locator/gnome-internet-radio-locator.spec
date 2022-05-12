%define ver_major 12.4
%define gst_api_ver 1.0
%def_with recording

Name: gnome-internet-radio-locator
Version: %ver_major.0
Release: alt1

Summary: GNOME Internet Radio Locator
License: GPLv2+
Group: Sound
Url: https://wiki.gnome.org/Apps/Girl

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: gst-plugins-base%gst_api_ver
Requires: gst-plugins-bad%gst_api_ver
Requires: gst-plugins-ugly%gst_api_ver
Requires: dconf geoclue2

%define gtk_ver 4.0.3

BuildRequires: gnome-common intltool yelp-tools gtk-doc
BuildRequires: libgtk4-devel >= %gtk_ver libxml2-devel libchamplain-gtk3-devel
BuildRequires: gst-plugins%gst_api_ver-devel gst-plugins-bad1.0-devel
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: libgeocode-glib-devel pkgconfig(libgeoclue-2.0) pkgconfig(geoclue-2.0)

%description
GNOME Internet Radio Locator is a Free Software program that allows
you to easily locate radio programs by broadcasters on the Internet
with the help of a map.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure \
	%{subst_with recording}
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name/
%_iconsdir/hicolor/*x*/apps/%name.png
%_datadir/metainfo/%name.appdata.xml
%_man1dir/%name.1.*
%doc AUTHORS NEWS README TODO HACKING


%changelog
* Thu May 12 2022 Yuri N. Sedunov <aris@altlinux.org> 12.4.0-alt1
- 12.4.0

* Thu Mar 10 2022 Yuri N. Sedunov <aris@altlinux.org> 12.0.8-alt1
- 12.0.8

* Mon Sep 27 2021 Yuri N. Sedunov <aris@altlinux.org> 12.0.4-alt1
- 12.0.4

* Mon Jun 28 2021 Yuri N. Sedunov <aris@altlinux.org> 12.0.0-alt1
- 12.0.0

* Thu Mar 25 2021 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- 4.0.0

* Tue Feb 16 2021 Yuri N. Sedunov <aris@altlinux.org> 3.9.1-alt1
- 3.9.1

* Thu Oct 29 2020 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Wed Sep 30 2020 Yuri N. Sedunov <aris@altlinux.org> 3.3.0-alt1
- 3.3.0

* Thu Jul 23 2020 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Mon Jul 13 2020 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Fri Jan 24 2020 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Wed Jan 15 2020 Yuri N. Sedunov <aris@altlinux.org> 2.8.0-alt1
- 2.8.0

* Thu Jan 09 2020 Yuri N. Sedunov <aris@altlinux.org> 2.6.0-alt1
- 2.6.0

* Tue Dec 24 2019 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Fri Dec 06 2019 Yuri N. Sedunov <aris@altlinux.org> 2.1.5-alt1
- 2.1.5

* Wed Nov 27 2019 Yuri N. Sedunov <aris@altlinux.org> 2.1.4-alt1
- 2.1.4

* Thu Oct 24 2019 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- 2.1.1

* Wed Oct 23 2019 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- 2.1.0

* Thu Oct 17 2019 Yuri N. Sedunov <aris@altlinux.org> 2.0.9-alt1
- 2.0.9

* Sun Sep 29 2019 Yuri N. Sedunov <aris@altlinux.org> 2.0.7-alt1
- 2.0.7

* Sat May 25 2019 Yuri N. Sedunov <aris@altlinux.org> 2.0.4-alt1
- 2.0.4

* Fri Apr 05 2019 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

* Wed Feb 20 2019 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0

* Mon Feb 04 2019 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Mon Jan 28 2019 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- 1.7.0

* Sun Jan 13 2019 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Sat May 26 2018 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Mon May 21 2018 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Sat May 19 2018 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Fri Apr 20 2018 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Mon Mar 26 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.5-alt1
- 1.0.5

* Sat Feb 17 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.4-alt1
- 1.0.4

* Sat Feb 17 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Sat Nov 25 2017 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Tue Oct 24 2017 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Sat Sep 16 2017 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Mon Aug 14 2017 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed Jul 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Tue Jul 18 2017 Yuri N. Sedunov <aris@altlinux.org> 0.5.3-alt1
- 0.5.3

* Mon Jul 17 2017 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Tue Jun 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0

* Fri Jun 16 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for Sisyphus

