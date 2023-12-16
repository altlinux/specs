%def_enable snapshot
%define ver_major 0.12

Name: gupnp-tools
Version: %ver_major.1
Release: alt2

Summary: GUPnP Tools
Group: Development/Other
License: GPLv2+
Url: http://www.gupnp.org/

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.68
%define gssdp_api_ver 1.6
%define gupnp_api_ver 1.6
%define gssdp_ver 1.6
%define gupnp_ver 1.6
%define gtk_ver 3.10
%define soup_api_ver 3.0
%define soup_ver 3.0

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson desktop-file-utils
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgssdp%gssdp_api_ver-devel >= %gssdp_ver
BuildRequires: libgupnp%gupnp_api_ver-devel >= %gupnp_ver
BuildRequires: libgupnp-av-devel
BuildRequires: libgtk+3-devel >= %gtk_ver libsoup%soup_api_ver-devel >= %soup_ver
BuildRequires: libxml2-devel libuuid-devel
BuildRequires: libgtksourceview4-devel

%description
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup. The
GUPnP API is intended to be easy to use, efficient and flexible.

GUPnP Tools are free replacements of Intel UPnP tools that use GUPnP.
They provides client and server side tools which enable one to easily
test and debug one's UPnP devices and control points.


%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%meson_test

%files -f %name.lang
%_bindir/gssdp-discover
%_bindir/gupnp-event-dumper
%_bindir/gupnp-network-light
%_bindir/gupnp-universal-cp
%_bindir/gupnp-av-cp
%_bindir/gupnp-upload
%_desktopdir/gupnp-av-cp.desktop
%_desktopdir/gupnp-network-light.desktop
%_desktopdir/gupnp-universal-cp.desktop
%_iconsdir/hicolor/*x*/*/*.png
%_datadir/%name/
%doc AUTHORS README* NEWS

%changelog
* Sat Dec 16 2023 Yuri N. Sedunov <aris@altlinux.org> 0.12.1-alt2
- updated to 0.12.1-9-g88a441f (fixed build with libxml2-2.12.x)

* Wed Aug 02 2023 Yuri N. Sedunov <aris@altlinux.org> 0.12.1-alt1
- 0.12.1

* Wed Oct 12 2022 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0 (ported to GUPnP-1.6/Libsoup-3.0)

* Fri May 20 2022 Yuri N. Sedunov <aris@altlinux.org> 0.10.3-alt1
- 0.10.3

* Tue Nov 16 2021 Yuri N. Sedunov <aris@altlinux.org> 0.10.2-alt1
- 0.10.2

* Tue Jun 22 2021 Yuri N. Sedunov <aris@altlinux.org> 0.10.1-alt1
- 0.10.1

* Fri Mar 29 2019 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0 (ported to gssdp/gupnp-1.2)

* Fri Dec 21 2018 Yuri N. Sedunov <aris@altlinux.org> 0.8.15-alt1
- 0.8.15

* Mon Oct 16 2017 Yuri N. Sedunov <aris@altlinux.org> 0.8.14-alt1
- first build for Sisyphus

