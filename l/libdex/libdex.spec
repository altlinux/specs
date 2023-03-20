%def_disable snapshot
%define ver_major 0.2
%define beta %nil
%define api_ver 1

%def_enable introspection
%def_enable vala
%def_enable docs
# not installable
%def_disable examples
%def_enable check

Name: libdex
Version: %ver_major.0
Release: alt1%beta

Summary: Dex provides Future-based programming for GLib-based applications
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://gitlab.gnome.org/GNOME/%name

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
#Source: %url/-/archive/%version/%name-%version.tar.bz2
%else
Vcs: https://gitlab.gnome.org/GNOME/libdex.git
Source: %name-%version.tar
%endif

%define meson_ver 0.62
%define glib_ver 2.68
%define uring_ver 0.7

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson >= %meson_ver
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: liburing-devel >= %uring_ver
%{?_enable_introspection:BuildRequires(pre): rpm-build-gir
BuildRequires: pkgconfig(gobject-introspection-1.0)}
%{?_enable_vala:BuildRequires(pre): rpm-build-vala
BuildRequires: vala-tools}
%{?_enable_examples:BuildRequires: libsoup3.0-devel}
%{?_enable_docs:BuildRequires: gi-docgen}

%description
%summary

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use Dex library.

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for Dex library.

%package gir-devel
Summary: GObject introspection devel data for %name
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for Dex library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %EVR

%description devel-doc
This package contains development documentation for Dex library.

%package demo
Summary: Dex example programs
Group: Development/Other
Requires: %name = %EVR

%description demo
This package contains Dex example programs.

%prep
%setup -n %name-%version%beta

%build
%meson \
    %{?_enable_docs:-Ddocs=true} \
    %{?_disable_examples:-Dexamples=false}
%nil
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_libdir/%name-%api_ver.so.*
%doc README* TODO* NEWS

%files devel
%_includedir/%name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc
%{?_enable_vala:%_vapidir/%name.*}

%if_enabled introspection
%files gir
%_typelibdir/Dex-%api_ver.typelib

%files gir-devel
%_girdir/Dex-%api_ver.gir
%endif

%if_enabled docs
%files devel-doc
%_datadir/doc/%name-%api_ver/
%endif

%if_enabled examples
%files demo
%_bindir/%name-*
%endif

%changelog
* Sat Mar 18 2023 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for Sisyphus

