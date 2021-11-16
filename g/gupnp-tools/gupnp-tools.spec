%def_disable snapshot
%define ver_major 0.10

Name: gupnp-tools
Version: %ver_major.2
Release: alt1

Summary: A collection of developer tools utilising GUPnP and GTK+3
Group: Development/Other
License: GPLv2+
Url: http://www.gupnp.org/

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define gupnp_api_ver 1.2
%define gssdp_api_ver 1.2
%define gupnp_ver 1.2
%define gssdp_ver 1.2
%define soup_ver 2.42

BuildRequires(pre): meson
BuildRequires: desktop-file-utils
BuildRequires: libgupnp%gupnp_api_ver-devel >= %gupnp_ver libgssdp%gssdp_api_ver-devel >= %gssdp_ver
BuildRequires: libgupnp-av-devel
BuildRequires: libgtk+3-devel libsoup-devel >= %soup_ver libxml2-devel libuuid-devel
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

