%define _name slingshot
%define ver_major 0.8
%define api_ver 0.8

Name: %_name-launcher
Version: %ver_major.1.1
Release: alt1

Summary: The lightweight and stylish app launcher from elementary
License: GPLv2.1+
Group: Graphical desktop/Other
Url: https://launchpad.net/%_name

Source: https://launchpad.net/%_name/freya/%version/+download/%name-%version.tar.xz

Requires: zeitgeist

BuildRequires: rpm-build-xdg cmake gcc-c++ libgtk+3-devel >= 3.12.0 libsoup-devel libjson-glib-devel
BuildRequires: libgee0.8-devel libgranite-devel libzeitgeist2.0-devel libplank-devel
BuildRequires: libgnome-menus-devel libgranite-vala libplank-vala vala-tools

%description
Slingshot is a lightweight and stylish app launcher from elementary OS.

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE:STRING="Release" \
	-DUSE_UNITY:BOOL=OFF
%cmake_build V=1

%install
%cmakeinstall_std

%find_lang %_name

%files -f %_name.lang
%_xdgmenusdir/pantheon-applications.menu
%_bindir/%name
%_datadir/glib-2.0/schemas/org.pantheon.desktop.%_name.gschema.xml


%changelog
* Fri Sep 11 2015 Yuri N. Sedunov <aris@altlinux.org> 0.8.1.1-alt1
- first build for Sisyphus


