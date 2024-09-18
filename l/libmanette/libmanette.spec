%define _name manette
%define ver_major 0.2
%define api_ver 0.2
%define namespace Manette
%define _libexecdir %_prefix/libexec

%def_enable introspection
%def_enable vala
%def_enable check

Name: lib%_name
Version: %ver_major.9
Release: alt1

Summary: A simple GObject game controller library
Group: System/Libraries
License: LGPL-2.1
Url: https://gnome.pages.gitlab.gnome.org/libmanette

Vcs: https://gitlab.gnome.org/GNOME/libmanette.git
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define meson_ver 0.53
%define glib_ver 2.50
%define evdev_ver 1.4.5

BuildRequires(pre): meson >= %meson_ver rpm-build-gir
BuildRequires: libgio-devel >= %glib_ver libevdev-devel >= %evdev_ver
BuildRequires: libgudev-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgudev-gir-devel}
%{?_enable_vala:BuildRequires: vala-tools}

%description
%name is a small GObject library for simple access to game
controllers.

%package devel
Summary: libinput development package
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains development libraries and header files
that are needed to write applications that use %name.

%package gir
Summary: GObject introspection data for the Manette library
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the Manette library.

%package gir-devel
Summary: GObject introspection devel data for the Manette library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for the Manette library.

%package tools
Summary: tools for %name
Group: Development/Tools
Requires: %name = %EVR

%description tools
This package contains commandline tools from %name package.

%prep
%setup

%build
%meson \
    %{subst_enable_meson_bool introspection introspection} \
    %{subst_enable_meson_bool vala vapi}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_libdir/%name-%api_ver.so.*
%doc README* NEWS

%files devel
%_includedir/%name/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
%{?_enable_vala:%_vapidir/%_name-%api_ver.*}

%if_enabled introspection
%files gir
%_typelibdir/%namespace-%api_ver.typelib

%files gir-devel
%_girdir/%namespace-%api_ver.gir
%endif

%files tools
%_bindir/%_name-test

%changelog
* Fri Sep 13 2024 Yuri N. Sedunov <aris@altlinux.org> 0.2.9-alt1
- 0.2.9

* Fri Feb 09 2024 Yuri N. Sedunov <aris@altlinux.org> 0.2.7-alt1
- 0.2.7

* Sat Nov 28 2020 Yuri N. Sedunov <aris@altlinux.org> 0.2.6-alt1
- 0.2.6

* Sat Sep 12 2020 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt1
- 0.2.5

* Sun Apr 05 2020 Yuri N. Sedunov <aris@altlinux.org> 0.2.4-alt1
- 0.2.4
- enabled %%check

* Wed Sep 11 2019 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- 0.2.3

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt1
- 0.2.2

* Mon Jul 30 2018 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- 0.2.1

* Thu Mar 01 2018 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- 0.2.0

* Sat Oct 28 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- first build for Sisyphus


