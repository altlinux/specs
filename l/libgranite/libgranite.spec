%define _name granite
%define ver_major 0.5
%define api_ver 1.0

Name: libgranite
Version: %ver_major
Release: alt1

Summary: Extension of GTK+3 libraries
Group: System/Libraries
License: GPLv3+
Url: https://github.com/elementary/%_name

Source: %url/archive/%version/%_name-%version.tar.gz

BuildRequires: cmake rpm-build-gir vala libgtk+3-devel libgee0.8-devel
BuildRequires: libpixman-devel gobject-introspection-devel libXdmcp-devel
BuildRequires: libXdamage-devel libXxf86vm-devel libharfbuzz-devel libpng-devel
BuildRequires: libXinerama-devel libXi-devel libXrandr-devel libXcursor-devel
BuildRequires: libXcomposite-devel libxkbcommon-devel libwayland-cursor-devel
BuildRequires: at-spi2-atk-devel libgtk+3-gir-devel libgee0.8-gir-devel
BuildRequires: libexpat-devel

%description
Granite is an extension of GTK+. Among other things, it provides the
commonly-used widgets such as modeswitchers, welcome screens, AppMenus,
search bars, and more found in elementary apps.

This package contains the shared library.

%package devel
Summary: Extension of GTK+ libraries (development files)
Group: Development/GNOME and GTK+

Requires: %name = %version-%release

%description devel
Granite is an extension of GTK+. Among other things, it provides the
commonly-used widgets such as modeswitchers, welcome screens, AppMenus,
search bars, and more found in elementary apps.

This package contains header files.

%package vala
Summary: Vala language bindings for the granite library
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %version-%release

%description vala
This package provides Vala language bindings for the granite library.

%package -n granite-demo
Summary: Extension of GTK+ libraries (demo binary)
Group: Development/GNOME and GTK+

Requires: %name = %version-%release

%description -n granite-demo
Granite is an extension of GTK+. Among other things, it provides the
commonly-used widgets such as modeswitchers, welcome screens, AppMenus,
search bars, and more found in elementary apps.

This package contains a small demo application to show Granite Widgets.

%package gir
Summary: GObject introspection data for the granite library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the granite library.

%package gir-devel
Summary: GObject introspection devel data for the granite library.
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the granite library.

%prep
%setup -n %_name-%version

%build
%cmake_insource -DCMAKE_BUILD_TYPE:STRING="Release"
%make_build VERBOSE=1

%install
%makeinstall_std

%find_lang %_name

%files -f %_name.lang
%doc AUTHORS README*
%_libdir/*.so.*

%files devel
%_libdir/*.so
%dir %_includedir/%_name
%_includedir/%_name/*.h
%_pkgconfigdir/%_name.pc

%files -n %_name-demo
%_bindir/*
%_desktopdir/%_name-demo.desktop
%_datadir/icons/hicolor/*/*/*.svg

%files gir
%_typelibdir/Granite-%api_ver.typelib

%files gir-devel
%_girdir/Granite-%api_ver.gir

%files vala
%_datadir/vala/vapi/%_name.deps
%_datadir/vala/vapi/%_name.vapi

%changelog
* Mon Nov 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.5-alt1
- 0.5

* Wed May 10 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Fri Mar 31 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.0.1-alt2
- fixed build with vala-0.36

* Thu Sep 29 2016 Yuri N. Sedunov <aris@altlinux.org> 0.4.0.1-alt1
- 0.4.0.1

* Sun Sep 06 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Mon Mar 03 2014 Igor Zubkov <icesik@altlinux.org> 0.2.3-alt1
- 0.2.3

* Mon Nov 11 2013 Igor Zubkov <icesik@altlinux.org> 0.2.2-alt6
- Fix FTBFS with new cmake

* Mon Sep 16 2013 Igor Zubkov <icesik@altlinux.org> 0.2.2-alt5
- Fix typo in spec file

* Mon Sep 16 2013 Igor Zubkov <icesik@altlinux.org> 0.2.2-alt4
- Cleanup spec file
- Update build requires

* Thu Aug 22 2013 Igor Zubkov <icesik@altlinux.org> 0.2.2-alt3
- Cleanup build requires

* Tue Aug 20 2013 Igor Zubkov <icesik@altlinux.org> 0.2.2-alt2
- Fix summaries and descriptions

* Sun Aug 11 2013 Igor Zubkov <icesik@altlinux.org> 0.2.2-alt1
- 0.1.0 -> 0.2.2

* Sun Aug 11 2013 Igor Zubkov <icesik@altlinux.org> 0.1.0-alt1
- build for Sisyphus

