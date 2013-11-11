%define origname granite

Name: libgranite
Version: 0.2.2
Release: alt6

Summary: Extension of GTK+ libraries
Group: System/Libraries
License: GPLv3+
Url: https://launchpad.net/granite

Source0: %origname-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.org>

BuildRequires: cmake rpm-build-gir vala libgtk+3-devel libgee-devel
BuildRequires: libpixman-devel gobject-introspection-devel libXdmcp-devel
BuildRequires: libXdamage-devel libXxf86vm-devel libharfbuzz-devel libpng-devel
BuildRequires: libXinerama-devel libXi-devel libXrandr-devel libXcursor-devel
BuildRequires: libXcomposite-devel libxkbcommon-devel libwayland-cursor-devel
BuildRequires: at-spi2-atk-devel libgtk+3-gir-devel libgee-gir-devel
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
Requires: %name = %version-%release

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
%setup -q -n %origname-%version

%build
%cmake_insource
%make_build VERBOSE=1

%install
%makeinstall_std

%find_lang %origname

%files -f %origname.lang
%doc AUTHORS INSTALL README
%_libdir/*.so.*

%files devel
%_libdir/*.so
%dir %_includedir/granite
%_includedir/granite/*.h
%_pkgconfigdir/granite.pc

%files -n granite-demo
%_bindir/*
%_datadir/icons/hicolor/*/*/*.svg

%files gir
%_typelibdir/Granite-1.0.typelib

%files gir-devel
%_girdir/Granite-1.0.gir

%files vala
%_datadir/vala/vapi/granite.deps
%_datadir/vala/vapi/granite.vapi

%changelog
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

