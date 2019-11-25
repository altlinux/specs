%def_disable snapshot
%define ver_major 3.34
%define xdg_name org.gnome.SimpleScan

%def_enable packagekit

Name: simple-scan
Version: %ver_major.2
Release: alt1

Summary: Simple scanning utility
License: GPLv3+
Group: Graphics
Url: http://launchpad.net/%name

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

Requires: sane xdg-utils gnome-icon-theme colord
%{?_enable_packagekit:Requires: packagekit}

%define gtk_ver 3.22
%define gusb_ver 0.2.7

BuildRequires(pre): meson
BuildRequires: yelp-tools libappstream-glib-devel
BuildRequires: libgtk+3-devel >= %gtk_ver libgusb-devel >= %gusb_ver
BuildRequires: libsane-devel zlib-devel
BuildRequires: vala-tools libcolord-vala
BuildRequires: libcolord-devel libwebp-devel
%{?_enable_packagekit:BuildRequires: libpackagekit-glib-devel}

%description
Simple Scan is an easy-to-use application, designed to let users connect their
scanner and quickly have the image/document in an appropriate format.

%prep
%setup
find ./ -name "*.stamp" -delete

%build
%meson %{?_disable_packagekit:-Dpackagekit=false}
%meson_build

%install
%meson_install

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_desktopdir/*
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%_datadir/metainfo/%name.appdata.xml
%_man1dir/*

%changelog
* Mon Nov 25 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.2-alt1
- 3.34.2

* Sun Oct 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- updated to 3.34.0-6-g14fe1c4

* Mon May 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2.1-alt1
- 3.32.2.1

* Wed Apr 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Tue Oct 23 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Fri Sep 28 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1.1-alt1
- 3.30.1.1

* Tue Sep 25 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Mon Apr 09 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

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
