%def_disable snapshot

%define _libexecdir %_prefix/libexec
%define ver_major 45
%define xdg_name org.gnome.NautilusPreviewer
%define api_ver 1.0
%define gst_api_ver 1.0

%def_enable introspection
%def_enable wayland
%def_enable x11
%define lo_bin %_bindir/libreoffice

Name: sushi
Version: %ver_major.0
Release: alt1

Summary: A quick previewer for Nautilus
Group: Graphical desktop/GNOME
License: GPLv2+
Url: https://gitlab.gnome.org/GNOME/sushi

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define gst_ver 1.0
%define webkit_api_ver 4.1
%define webkit_ver 2.38

Requires: gst-plugins-base%gst_api_ver gst-libav
Requires: %lo_bin
Requires: typelib(Gtk) = 3.0

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson %_bindir/appstream-util desktop-file-utils
BuildRequires: libgtksourceview4-devel libgjs-devel libharfbuzz-devel
BuildRequires: libevince-devel libepoxy-devel
BuildRequires: pkgconfig(webkit2gtk-%webkit_api_ver) >= %webkit_ver
BuildRequires: gstreamer%gst_api_ver-devel >= %gst_ver gst-plugins%gst_api_ver-devel
%if_enabled introspection
BuildRequires: libgtksourceview4-gir-devel libevince-gir-devel
BuildRequires: libgstreamer%gst_api_ver-gir-devel gst-plugins%gst_api_ver-gir-devel
%endif

%description
This is sushi, a quick previewer for Nautilus, the GNOME desktop file
manager.

%package -n lib%name
Summary: Library for the Sushi project
Group: System/Libraries

%description -n lib%name
Library for Sushi project.

%package -n lib%name-devel
Summary: Development files for Sushi library
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
This package contains libraries and header files for developing
applications that use Sushi library.

%package -n lib%name-gir
Summary: GObject introspection data for the Sushi library
Group: System/Libraries
Requires: lib%name = %EVR

%description -n lib%name-gir
GObject introspection data for the Sushi library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Sushi library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %EVR
Requires: lib%name-devel = %EVR

%description -n lib%name-gir-devel
GObject introspection devel data for the Sushi library.

%set_typelibdir %_libdir/%name/girepository-1.0

%prep
%setup

%build
%meson \
%{?_disable_wayland:-Dwayland=disabled} \
%{?_disable_x11:-DX11=disabled}
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_libexecdir/*
%dir %_libdir/%name
%_libdir/%name/*.so
%dir %_libdir/%name/girepository-1.0
%_libdir/%name/girepository-1.0/Sushi-%api_ver.typelib
%_datadir/%name/
%_datadir/dbus-1/services/*
%_datadir/metainfo/%xdg_name.appdata.xml
%doc README* AUTHORS NEWS TODO

%changelog
* Mon Sep 18 2023 Yuri N. Sedunov <aris@altlinux.org> 45.0-alt1
- 45.0

* Mon May 29 2023 Yuri N. Sedunov <aris@altlinux.org> 44.2-alt1
- 44.2

* Thu Sep 22 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Fri Jul 01 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Wed Apr 06 2022 Yuri N. Sedunov <aris@altlinux.org> 41.2-alt1
- 41.2

* Fri Apr 01 2022 Yuri N. Sedunov <aris@altlinux.org> 41.1-alt1
- 41.1

* Tue Sep 21 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Fri Jun 04 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Mon Oct 26 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Wed Jun 19 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Sun Mar 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Tue Sep 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Wed Aug 29 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.3-alt2
- requires %%_bindir/libreoffice

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.3-alt1
- 3.28.3

* Sat Apr 29 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Thu Mar 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.23.91-alt1
- 3.23.91

* Wed Aug 31 2016 Yuri N. Sedunov <aris@altlinux.org> 3.21.91-alt1
- 3.21.91

* Tue May 17 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Wed Mar 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.19.90-alt1
- 3.19.90

* Wed Sep 23 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Wed May 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Tue Mar 10 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.90-alt1
- 3.15.90

* Mon Dec 01 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt2
- rebuilt against libmusicbrainz5.so.1

* Wed Apr 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Thu Feb 20 2014 Yuri N. Sedunov <aris@altlinux.org> 3.11.90-alt1
- 3.11.90

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Tue Mar 20 2012 Yuri N. Sedunov <aris@altlinux.org> 0.3.92-alt1
- 0.3.92

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- first build for people/gnome

