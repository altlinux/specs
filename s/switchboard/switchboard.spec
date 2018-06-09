%def_disable snapshot
%define ver_major 2.3
%define api_ver 2.0

Name: switchboard
%define xdg_name org.pantheon.%name
%define rdn_name io.elementary.%name
Version: %ver_major.1
Release: alt1

Summary: Modular Desktop Settings Hub for elementary OS
License: GPLv2.1+
Group: Graphical desktop/Other
Url: https://github.com/elementary/%name

%if_disabled snapshot
Source: %url/archive/%name-%version.tar.gz
%else
# VCS: https://github.com/elementary/switchboard.git
Source: %name-%version.tar
%endif

Provides: %rdn_name = %version-%release
Requires: lib%name = %version-%release

BuildRequires: cmake gcc-c++ intltool libappstream-glib-devel
BuildRequires: libgtk+3-devel >= 3.10
BuildRequires: libgranite-devel libclutter-gtk3-devel
BuildRequires: libgranite-vala vala-tools

%description
This project is about the container app only and its library. For plugins
that handle the settings, please refer to
https://launchpad.net/pantheon-plugs.

%package -n lib%name
Summary: Switchboard Library
Group: System/Libraries

%description -n lib%name
This package provides shared library needed for Switchboard to work.

%package -n lib%name-devel
Summary: Switchboard Library - development files
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains files that are needed to develop Switchboard plugins.

%prep
%setup
# fix pc-file
subst 's@\(\/include\)\/@\1@' lib/%name.pc.cmake

%build
%cmake -DCMAKE_BUILD_TYPE:STRING="Release" \
	-DUSE_UNITY:BOOL=OFF \
	-DGSETTINGS_COMPILE=OFF
%cmake_build V=1

%install
%cmakeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/metainfo/%rdn_name.appdata.xml

%files -n lib%name
%_libdir/lib%name-%api_ver.so.*

%files -n lib%name-devel
%_includedir/%name-%api_ver/
%_libdir/lib%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc
%_vapidir/%name-%api_ver.deps
%_vapidir/%name-%api_ver.vapi

%changelog
* Sat Jun 09 2018 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt1
- 2.3.1

* Sat Jan 06 2018 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt2
- rebuilt against libgranite.so.4

* Wed Aug 02 2017 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Tue Feb 07 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Fri Jan 13 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Wed Mar 30 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt2
- fixed pc-file

* Fri Sep 11 2015 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- first build for Sisyphus


