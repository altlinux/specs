%def_enable snapshot
%define ver_major 1.0
%define api_ver 1
%define _libexecdir %_prefix/libexec

%def_enable pulseaudio
%def_enable vala
%def_disable check

Name: retro-gtk
Version: %ver_major.2
Release: alt2

Summary: Toolkit to write Gtk+3-based frontends to libretro
License: GPLv3
Group: System/Libraries
Url: https://gnome.pages.gitlab.gnome.org/retro-gtk

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif
Patch: %name-1.0.2-alt-meson-0.60.patch

%define meson_ver 0.50
%define glib_ver 2.68
%define gtk_ver 3.22

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson >= %meson_ver
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(gtk+-3.0) >= %gtk_ver
%{?_enable_pulseaudio:BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libpulse-simple)
BuildRequires: pkgconfig(samplerate)}
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
%{?_enable_vala:BuildRequires(pre): rpm-build-vala
BuildRequires: vala-tools}
%{?_enable_check:BuildRequires: xvfb-run}

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
%patch

%build
%meson \
%{?_disable_vala:-Dvapi=false}
%nil
%meson_build

%install
%meson_install

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
xvfb-run %meson_test

%files -n lib%name
%_libdir/lib%name-%api_ver.so.*
%_libexecdir/retro-runner
%doc README* AUTHORS NEWS

%files -n lib%name-devel
%_libdir/lib%name-%api_ver.so
%_includedir/%name/
%_pkgconfigdir/%name-%api_ver.pc
%{?_enable_vala:%_vapidir/%name-%api_ver.deps
%_vapidir/%name-%api_ver.vapi}

%files -n lib%name-gir
%_typelibdir/Retro-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/Retro-%api_ver.gir

#%files demo
%exclude %_bindir/retro-demo


%changelog
* Thu Dec 16 2021 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt2
- updated to 1.0.2-26-gf71c48a
- fixed build with meson-0.60

* Mon Mar 22 2021 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Sun Nov 29 2020 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1
- enabled %%check

* Sat Sep 12 2020 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Sun Jan 19 2020 Yuri N. Sedunov <aris@altlinux.org> 0.18.1-alt1
- 0.18.1

* Wed Sep 11 2019 Yuri N. Sedunov <aris@altlinux.org> 0.18.0-alt1
- 0.18.0

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 0.16.1-alt1
- 0.16.1

* Sat Sep 01 2018 Yuri N. Sedunov <aris@altlinux.org> 0.16.0-alt1
- 0.16.0

* Fri May 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1
- first build for Sisyphus

