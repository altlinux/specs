%define ver_major 0.8

Name: gupnp-tools
Version: %ver_major.15
Release: alt1

Summary: A collection of developer tools utilising GUPnP and GTK+3
Group: Development/Other
License: GPLv2+
Url: http://www.gupnp.org/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define gupnp_ver 0.20.14
%define gssdp_ver 0.13.3
%define soup_ver 2.42

BuildRequires(pre): meson
BuildRequires: desktop-file-utils
BuildRequires: libgupnp-devel >= %gupnp_ver libgupnp-av-devel libgssdp-devel >= %gssdp_ver
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
%_iconsdir/hicolor/*x*/*.png
%_datadir/%name/
%doc AUTHORS README* NEWS

%changelog
* Fri Dec 21 2018 Yuri N. Sedunov <aris@altlinux.org> 0.8.15-alt1
- 0.8.15

* Mon Oct 16 2017 Yuri N. Sedunov <aris@altlinux.org> 0.8.14-alt1
- first build for Sisyphus

