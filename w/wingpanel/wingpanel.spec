%define ver_major 2.0
%define api_ver %ver_major
%define rev 93

Name: wingpanel
Version: %ver_major.1
Release: alt1

Summary: A super sexy space-saving top panel
Group: Graphical desktop/Other
License: GPLv3+
Url: https://launchpad.net/wingpanel

# rev 93
Source: https://launchpad.net/%name/2.x/%version/+download/%name-%version.tar.xz

%define gtk_ver 3.14

Requires: dconf

BuildRequires: gcc-c++ cmake libgtk+3-devel >= %gtk_ver
BuildRequires: libgranite-devel libnotify-devel libgala-devel
BuildRequires: vala-tools libgranite-vala libgala-vala

%description
A replacement for the traditional GNOME Panel, designed to be a lightweight
container for system/application indicators and notification icons.
Designed by elementary Project.

%package -n lib%name
Summary: Shared library for Wingpanel
Group: System/Libraries

%description -n lib%name
This package contains shared library needed to run Wingpanel.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains headers and development libraries for lib%name

%package -n lib%name-vala
Summary: Vala language bindings for the Wingpanel library
Group: Development/Other
BuildArch: noarch
Requires: lib%name-devel = %version-%release

%description -n lib%name-vala
This package provides Vala language bindings for the Wingpanel library.


%prep
%setup
# fix pc-file
subst 's@\(\/include\)\/@\1@' lib/%name.pc.cmake

%build
%cmake -DCMAKE_BUILD_TYPE:STRING="Release" \
%cmake_build V=1

%install
%cmakeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_libdir/gala/plugins/libwingpanel-interface.so
%_desktopdir/%name.desktop
%_datadir/glib-2.0/schemas/org.pantheon.desktop.wingpanel.gschema.xml

%files -n lib%name
%_libdir/lib%name-%api_ver.so.*

%files -n lib%name-devel
%_includedir/%name-%api_ver/
%_libdir/lib%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc

%files -n lib%name-vala
%_vapidir/%name-%api_ver.deps
%_vapidir/%name-%api_ver.vapi

%changelog
* Fri Jan 13 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1 release

* Sun Sep 13 2015 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1.93
- 2.0.0_rev93

* Mon Sep 07 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.0.2-alt1
- 0.3.0.2

* Mon Oct 07 2013 Igor Zubkov <icesik@altlinux.org> 0.2.5-alt1
- 0.2.3 -> 0.2.5

* Sun Sep 15 2013 Igor Zubkov <icesik@altlinux.org> 0.2.3-alt1
- build for Sisyphus

