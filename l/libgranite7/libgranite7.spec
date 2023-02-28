%def_disable snapshot
%def_disable docs
%def_enable check

%define _name granite
%define rdn_name io.elementary.%_name-%api_ver_major
%define ver_major 7.2
%define api_ver_major 7
%define api_ver 7.0
%define sover 7

Name: lib%_name%api_ver_major
Version: %ver_major.0
Release: alt1

Summary: Extension of GTK4 libraries
Group: System/Libraries
License: LGPL-3.0
Url: https://github.com/elementary/%_name

%if_disabled snapshot
Source: %url/archive/%version/%_name-%version.tar.gz
%else
Vcs: https://github.com/elementary/granite.git
Source: %_name-%version.tar
%endif

%define glib_ver 2.50
%define gtk4_ver 4.4
%define vala_ver 0.40

Requires: elementary-icon-theme >= %ver_major

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson vala-tools >= %vala_ver libgio-devel >= %glib_ver
BuildRequires: libgio-devel >= %glib_ver libgtk4-devel >= %gtk4_ver
BuildRequires: libgee0.8-devel gobject-introspection-devel
BuildRequires: libgtk4-gir-devel libgee0.8-gir-devel
%{?_enable_docs:BuildRequires: gtk-doc valadoc}

%description
Granite is a companion library for GTK4 and GLib that provides complex
widgets and convenience methods designed for use in apps built for
elementary OS.

This package contains the shared library.

%package devel
Summary: Extension of GTK+ libraries (development files)
Group: Development/GNOME and GTK+
Requires: %name = %EVR
Provides: %name-vala = %EVR

%description devel
Granite is a companion library for GTK4 and GLib that provides complex
widgets and convenience methods designed for use in apps built for
elementary OS.

This package contains header files.

%package -n %_name%api_ver_major-demo
Summary: Extension of GTK4 libraries (demo binary)
Group: Development/GNOME and GTK+
Requires: %name = %EVR

%description -n %_name%api_ver_major-demo
Granite is a companion library for GTK4 and GLib that provides complex
widgets and convenience methods designed for use in apps built for
elementary OS.

This package contains a small demo application to show Granite Widgets.

%package gir
Summary: GObject introspection data for the Granite library
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the Granite library.

%package gir-devel
Summary: GObject introspection devel data for the Granite library.
Group: System/Libraries
BuildArch: noarch
Requires: %name-devel = %EVR
Requires: %name-gir = %EVR

%description gir-devel
GObject introspection devel data for the Granite library.

%prep
%setup -n %_name-%version

%build
%meson %{?_enable_docs:-Ddocumentation=true}
%meson_build

%install
%meson_install
%find_lang %_name-%api_ver_major

%check
%__meson_test

%files -f %_name-%api_ver_major.lang
%_libdir/*.so.%{sover}*
%_iconsdir/hicolor/*/*/*.svg
%_datadir/metainfo/%_name-%api_ver_major.appdata.xml
%doc README*

%files devel
%_includedir/%_name-%api_ver_major/
%_libdir/*.so
%_pkgconfigdir/%_name-%api_ver_major.pc
%_datadir/vala/vapi/%_name-%api_ver_major.deps
%_datadir/vala/vapi/%_name-%api_ver_major.vapi

%files -n %_name%api_ver_major-demo
%_bindir/*
%_desktopdir/%rdn_name.demo.desktop

%files gir
%_typelibdir/Granite-%api_ver.typelib

%files gir-devel
%_girdir/Granite-%api_ver.gir


%changelog
* Tue Feb 28 2023 Yuri N. Sedunov <aris@altlinux.org> 7.2.0-alt1
- 7.2.0

* Tue Oct 11 2022 Yuri N. Sedunov <aris@altlinux.org> 7.1.0-alt1
- 7.1.0

* Wed May 04 2022 Yuri N. Sedunov <aris@altlinux.org> 7.0.0-alt1
- 7.0.0 (ported to GTK4)

* Wed Nov 24 2021 Yuri N. Sedunov <aris@altlinux.org> 6.2.0-alt1
- 6.2.0

* Fri Oct 29 2021 Yuri N. Sedunov <aris@altlinux.org> 6.1.2-alt1
- 6.1.2

* Fri Aug 27 2021 Yuri N. Sedunov <aris@altlinux.org> 6.1.1-alt1
- 6.1.1

* Mon Jul 19 2021 Yuri N. Sedunov <aris@altlinux.org> 6.1.0-alt1
- 6.1.0

* Sun Mar 28 2021 Yuri N. Sedunov <aris@altlinux.org> 6.0.0-alt1
- 6.0.0

* Thu Jul 02 2020 Yuri N. Sedunov <aris@altlinux.org> 5.5.0-alt1
- updated to 5.5.0-2-g5bab90be

* Fri May 01 2020 Yuri N. Sedunov <aris@altlinux.org> 5.4.0-alt1
- 5.4.0

* Thu Apr 02 2020 Yuri N. Sedunov <aris@altlinux.org> 5.3.1-alt1
- 5.3.1

* Wed Jan 08 2020 Yuri N. Sedunov <aris@altlinux.org> 5.3.0-alt1
- 5.3.0

* Sun Sep 08 2019 Yuri N. Sedunov <aris@altlinux.org> 5.2.5-alt1
- 5.2.5

* Mon Jul 08 2019 Yuri N. Sedunov <aris@altlinux.org> 5.2.4-alt1
- 5.2.4

* Fri Feb 15 2019 Yuri N. Sedunov <aris@altlinux.org> 5.2.3-alt1
- 5.2.3 (ported to Meson build system)

* Thu Dec 20 2018 Yuri N. Sedunov <aris@altlinux.org> 5.2.2-alt1
- 5.2.2

* Fri Nov 09 2018 Yuri N. Sedunov <aris@altlinux.org> 5.2.1-alt1
- 5.2.1

* Sun Nov 04 2018 Yuri N. Sedunov <aris@altlinux.org> 5.2.0-alt1
- 5.2.0

* Thu Aug 30 2018 Yuri N. Sedunov <aris@altlinux.org> 5.1.0-alt1
- 5.1.0

* Mon Jun 25 2018 Yuri N. Sedunov <aris@altlinux.org> 5.0-alt1
- updated to 5.0-21-g4e84fc7

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

