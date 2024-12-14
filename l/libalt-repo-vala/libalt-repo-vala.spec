%define _unpackaged_files_terminate_build 1

%define apiver 1
%define namever %name-%apiver

Name: libalt-repo-vala
Version: 1.19.20
Release: alt1

Summary: ALT Repo API library on Vala
License: GPL-3.0-or-later
Group: Development/Other
Url: https://github.com/alt-gnome/libalt-repo-vala.git
VCS: https://github.com/alt-gnome/libalt-repo-vala.git

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: gobject-introspection-devel
BuildRequires: gir(Gee) = 0.8
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libapi-base-1)
BuildRequires: pkgconfig(libvazzy-1)

%description
%summary.

%package -n %namever
Summary: %{summary %name}
Group: System/Libraries

%description -n %namever
%{description %name}.

%package -n %namever-devel
Group: Development/Other
Summary: Headers files and library symbolic links for %name
Requires: %namever = %EVR

%description -n %namever-devel
%summary.
This package contains headers and libs
required for building programs with %name.

%package -n %namever-gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %namever = %EVR

%description -n %namever-gir
%{summary %apiver-gir}.

%package -n %namever-gir-devel
Summary: GObject introspection devel data for %name
Group: System/Libraries
BuildArch: noarch
Requires: %namever-gir = %EVR
Requires: %namever-devel = %EVR

%description -n %namever-gir-devel
%{summary %apiver-gir-devel}.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -n %namever
%_libdir/libalt-repo-%apiver.so.*

%files -n %namever-devel
%_includedir/libalt-repo-%apiver.h
%_libdir/libalt-repo-%apiver.so
%_pkgconfigdir/libalt-repo-%apiver.pc
%_datadir/vala/vapi/libalt-repo-%apiver.deps
%_datadir/vala/vapi/libalt-repo-%apiver.vapi

%files -n %namever-gir
%_typelibdir/AltRepo-%apiver.typelib

%files -n %namever-gir-devel
%_girdir/AltRepo-%apiver.gir

%changelog
* Sat Dec 14 2024 Alexey Volkov <qualimock@altlinux.org> 1.19.20-alt1
- Initial build for ALT
