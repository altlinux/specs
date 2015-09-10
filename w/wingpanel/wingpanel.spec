%define ver_major 0.3

Name: wingpanel
Version: %ver_major.0.2
Release: alt1

Summary: A super sexy space-saving top panel
Group: Graphical desktop/Other
License: GPLv3+
Url: https://launchpad.net/wingpanel

Source: https://launchpad.net/%name/%{ver_major}.x/%version/+download/%name-%version.tar.xz

Packager: Igor Zubkov <icesik@altlinux.org>

BuildRequires: gcc-c++ cmake glib2-devel libindicator-gtk3-devel libgranite-devel
BuildRequires: libpixman-devel libexpat-devel libXdmcp-devel libXdamage-devel
BuildRequires: libXxf86vm-devel libharfbuzz-devel libpng-devel
BuildRequires: libXinerama-devel libXi-devel libXrandr-devel libXcursor-devel
BuildRequires: libXcomposite-devel libxkbcommon-devel libwayland-cursor-devel
BuildRequires: at-spi2-atk-devel libgranite-vala
BuildRequires: libwnck3-devel libido3-devel


%description
A replacement for the traditional GNOME Panel, designed to be a lightweight
container for system/application indicators and notification icons.
Designed by elementary Project.

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE:STRING="Release" \
		-DNO_INDICATOR_NG:BOOL=ON \
		-DOLD_LIB_IDO:BOOL=ON
%cmake_build VERBOSE=1

%install
%cmakeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/*
%_desktopdir/%name.desktop
%_datadir/glib-2.0/schemas/org.pantheon.desktop.wingpanel.gschema.xml
%_iconsdir/hicolor/scalable/apps/wingpanel.svg

%changelog
* Mon Sep 07 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.0.2-alt1
- 0.3.0.2

* Mon Oct 07 2013 Igor Zubkov <icesik@altlinux.org> 0.2.5-alt1
- 0.2.3 -> 0.2.5

* Sun Sep 15 2013 Igor Zubkov <icesik@altlinux.org> 0.2.3-alt1
- build for Sisyphus

