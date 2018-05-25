%define ver_major 0.14
%define api_ver 0.14

Name: retro-gtk
Version: %ver_major.0
Release: alt1

Summary: Toolkit to write Gtk+3-based frontends to libretro
License: GPLv3
Group: System/Libraries
Url: https://git.gnome.org/browse/%name

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildRequires(pre): meson
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libpulse-simple)
BuildRequires: vala-tools
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel


%description
%name is a toolkit allowing to easily write GTK+3 based Libretro
frontends.

%package -n lib%name
Summary: Toolkit to write Gtk+3-based frontends to libretro
Group: System/Libraries

%description -n lib%name
%name is a toolkit allowing to easily write GTK+3 based Libretro
frontends.

This package provides shared %name library.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
%name is a toolkit allowing to easily write GTK+3 based Libretro
frontends.

This package provides headers and libraries to develop applications that
use lib%name.

%package -n lib%name-gir
Summary: GObject introspection data for lib%name
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the %name library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for lib%name
Group: Development/Other
BuildArch: noarch
Requires: lib%name-devel = %version-%release
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the %name library.


%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files -n lib%name
%_libdir/lib%name-%api_ver.so
%doc README* AUTHORS NEWS

%files -n lib%name-devel
%_includedir/%name/
%_pkgconfigdir/%name-%api_ver.pc
%_vapidir/%name-%api_ver.deps
%_vapidir/%name-%api_ver.vapi

%files -n lib%name-gir
%_typelibdir/Retro-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/Retro-%api_ver.gir

#%files demo
%exclude %_bindir/retro-demo


%changelog
* Fri May 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1
- first build for Sisyphus

