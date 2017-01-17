%def_disable snapshot

%define _name slingshot
%define ver_major 2.0
%define api_ver 0.8

Name: %_name-launcher
Version: %ver_major.1
Release: alt1

Summary: The lightweight and stylish app launcher from elementary
License: GPLv2.1+
Group: Graphical desktop/Other
Url: https://launchpad.net/%_name

%if_disabled snapshot
Source: https://launchpad.net/%_name/loki/%version/+download/%name-%version.tar.xz
%else
# rev. 642
Source: %name-%version.tar
%endif

Requires: zeitgeist

BuildRequires: rpm-build-xdg cmake gcc-c++ libgtk+3-devel >= 3.12.0 libsoup-devel libjson-glib-devel
BuildRequires: libgee0.8-devel libgranite-devel libzeitgeist2.0-devel libplank-devel
BuildRequires: libgnome-menus-devel libgranite-vala libplank-vala vala-tools
BuildRequires: libwingpanel-devel libwingpanel-vala libswitchboard-devel

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
%_libdir/wingpanel/lib%_name.so
%_xdgmenusdir/pantheon-applications.menu
%_datadir/glib-2.0/schemas/org.pantheon.desktop.%_name.gschema.xml


%changelog
* Tue Jan 17 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

* Wed Mar 30 2016 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt0.1
- update to rev642
- built against libplank.so.1

* Fri Sep 11 2015 Yuri N. Sedunov <aris@altlinux.org> 0.8.1.1-alt1
- first build for Sisyphus


