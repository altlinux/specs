%def_enable snapshot

%def_enable introspection
%def_enable hwdb
%def_enable gtk_doc
%def_enable man
%def_enable tests
%def_enable examples
%def_disable installed_tests

%def_enable check

%define _name gmobile
%define namespace Gm
%define ver_major 0.2
%define api_ver_major 0
%define api_ver 0
%define sover 0

Name: lib%_name
Version: %ver_major.1
Release: alt1

Summary: Classes and utilities for mobile devices
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://gitlab.gnome.org/World/Phosh/gmobile

Vcs: https://gitlab.gnome.org/World/Phosh/gmobile.git

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
%{?_enable_gtk_doc:BuildRequires: gi-docgen}
%{?_enable_man:BuildRequires: /usr/bin/rst2man}

%description
gmobile carries some helpers for glib based environments on mobile devices.
Some of those parts might move to glib or libgnome-desktop eventually. It can
be used as a shared library or git submodule. There aren't any API stability
guarantees at this point in time.

This package provides shared %_name library.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
This package provides development files for %_name library.

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the %_name library.

%package gir-devel
Summary: GObject introspection devel data for %name
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for the %_name library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
This package contains development documentation for %_name library.

%package examples
Summary: simple applications from %_name package
Group: Development/Other
Requires: %name = %EVR

%description examples
This package provides example programs that can be used to chek
the functionality of the %_name library.

%package tests
Summary: Tests for %name
Group: Development/Other
Requires: %name = %EVR

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed %_name library.

%prep
%setup -n %_name-%version
sed -i "s|\(udevdir = \)prefix / 'lib' / 'udev'|\1'%_udevdir'|" meson.build

%build
%meson \
    -Ddefault_library=shared \
    %{subst_enable_meson_bool introspection introspection} \
    %{subst_enable_meson_bool hwdb hwdb} \
    %{subst_enable_meson_bool gtk_doc gtk_doc} \
    %{subst_enable_meson_bool man man} \
    %{subst_enable_meson_bool tests tests} \
    %{subst_enable_meson_bool examples examples}
%nil
%meson_build

%install
%meson_install
rm %buildroot%_libdir/%name.a
%find_lang --output=%name.lang %_name-%api_ver

%check
%__meson_test

%files -f %name.lang
%_libdir/%name.so.*
%{?_enable_hwdb:
%_udevrulesdir/61-%_name.rules
%_udevhwdbdir/61-%_name-wakeup.hwdb}
%{?_enable_hwdb:%{?_enable_man:%_man5dir/%_name.udev.5*}}
%doc NEWS README*

%files devel
%_includedir/%_name
%_libdir/%name.so
%_pkgconfigdir/%_name.pc

%if_enabled introspection
%files gir
%_typelibdir/%namespace-%api_ver_major.typelib

%files gir-devel
%_girdir/%namespace-%api_ver_major.gir
%endif

%if_enabled gtk_doc
%files devel-doc
%_datadir/doc/%_name-%api_ver_major/
%endif

%if_enabled examples
%files examples
%_bindir/gm-display-panel-preview
%_bindir/gm-display-panel-run-phosh
%_bindir/gm-timeout
%endif

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%_name-%api_ver/
%_datadir/installed-tests/%_name-%api_ver/
%endif


%changelog
* Sun Jun 23 2024 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- 0.2.1

* Sat Jun 22 2024 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1.1
- rebuilt with new systemd macros

* Mon May 13 2024 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- 0.2.0

* Sat Apr 06 2024 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- first build for sisyphus (v0.1.0-5-g7d55bed)

