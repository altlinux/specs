%define ver_major 3.26
%def_disable packagekit

Name: simple-scan
Version: %ver_major.3
Release: alt1

Summary: Simple scanning utility
License: GPLv3+
Group: Graphics
Url: http://launchpad.net/%name

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: sane xdg-utils gnome-icon-theme colord

BuildRequires: meson yelp-tools libappstream-glib-devel
BuildRequires: libgtk+3-devel libgudev-devel libcolord-devel
BuildRequires: libjpeg-devel libwebp-devel libsane-devel zlib-devel
BuildRequires: vala-tools libcolord-vala

%description
Simple Scan is an easy-to-use application, designed to let users connect their
scanner and quickly have the image/document in an appropriate format.

%prep
%setup
find ./ -name "*.stamp" -delete

%build
%meson %{?_disable_packagekit:-Denable-packagekit=false}
%meson_build

%install
%meson_install

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_datadir/%name/
%_desktopdir/*
%_datadir/glib-2.0/schemas/org.gnome.SimpleScan.gschema.xml
%_datadir/appdata/%name.appdata.xml
%_man1dir/*

%changelog
* Mon Jan 22 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.3-alt1
- 3.26.3

* Tue Oct 31 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Tue Oct 03 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Thu Apr 27 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Mon Sep 26 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0.1-alt1
- 3.22.0.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Nov 30 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Tue Oct 20 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Thu Sep 24 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Wed Jun 24 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Sun Apr 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1.1-alt1
- 3.16.1.1

* Thu Apr 16 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Tue Mar 31 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0.1-alt1
- 3.16.0.1

* Sat Mar 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Thu Feb 19 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.90-alt1
- 3.15.90

* Fri Jan 23 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.4-alt1
- 3.15.4

* Tue Jan 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.3-alt1
- 3.15.3

* Thu Dec 04 2014 Yuri N. Sedunov <aris@altlinux.org> 3.15.2-alt1
- 3.15.2

* Wed Nov 09 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Apr 25 2011 Victor Forsiuk <force@altlinux.org> 2.32.0.2-alt1
- 2.32.0.2

* Tue Mar 08 2011 Victor Forsiuk <force@altlinux.org> 2.32.0.1-alt2
- Refresh BuildRequires.

* Mon Dec 06 2010 Victor Forsiuk <force@altlinux.org> 2.32.0.1-alt1
- 2.32.0.1

* Wed Oct 20 2010 Victor Forsiuk <force@altlinux.org> 2.32.0-alt1
- 2.32.0

* Tue Sep 28 2010 Victor Forsiuk <force@altlinux.org> 2.31.91-alt1
- 2.31.91
- Patch to remove zlib detection by pkgconfig (no zlib.pc in our zlib-devel).

* Mon May 31 2010 Victor Forsiuk <force@altlinux.org> 2.31.1-alt1
- 2.31.1

* Tue Mar 16 2010 Victor Forsiuk <force@altlinux.org> 0.9.9-alt1
- 0.9.9

* Tue Mar 09 2010 Victor Forsiuk <force@altlinux.org> 0.9.7-alt1
- 0.9.7

* Mon Mar 01 2010 Victor Forsiuk <force@altlinux.org> 0.9.5-alt1
- Initial build.
