%define _unpackaged_files_terminate_build 1

# These come from meson.build.
%define apiversion 0.4
%define soversion 0

Name: wireplumber
Version: 0.3.60.63.g24a260030bab
Release: alt1

Summary: a modular session/policy manager for PipeWire

License: MIT
Group: Sound
URL: https://pipewire.pages.freedesktop.org/wireplumber/

BuildRequires(pre): meson
BuildRequires: pkgconfig(gobject-2.0) >= 2.58
BuildRequires: pkgconfig(gmodule-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(libpipewire-0.3) >= 0.3.20
BuildRequires: liblua5.3-devel
# TODO: How do we package gobject-introspection data?
# BuildRequires: gobject-introspection-devel

Source: %name-%version.tar
Patch1: alt-0001-meson.build-relax-version-requirements-on-dependenci.patch

%package -n lib%name
Summary: the client library for WirePlumber
Group: System/Libraries

%package -n lib%name-devel
Summary: development files of the client library for WirePlumber
Group: Development/C

%description
WirePlumber is a modular session / policy manager for PipeWire and a
GObject-based high-level library that wraps PipeWire's API, providing
convenience for writing the daemon's modules as well as external tools
for managing PipeWire.

%description -n lib%name
WirePlumber is a modular session / policy manager for PipeWire and a
GObject-based high-level library that wraps PipeWire's API, providing
convenience for writing the daemon's modules as well as external tools
for managing PipeWire.

This package contains the client library.

%description -n lib%name-devel
WirePlumber is a modular session / policy manager for PipeWire and a
GObject-based high-level library that wraps PipeWire's API, providing
convenience for writing the daemon's modules as well as external tools
for managing PipeWire.

This package contains the development files for the client library.

%prep
%setup
%patch1 -p1

%build
%meson \
    -Dsystem-lua=true \
    #

%meson_build

%install
%meson_install

%files
%doc NEWS.md README.md
%_sysconfdir/wireplumber
%_bindir/wireplumber
%_bindir/wpctl
%_datadir/wireplumber

%files -n lib%name
%_libdir/libwireplumber-%apiversion.so.%soversion.*
%_libdir/libwireplumber-%apiversion.so.%soversion
# plugins
%_libdir/wireplumber-%apiversion

%files -n lib%name-devel
# TODO: How do we package gobject-introspection data?
# /usr/lib64/girepository-1.0/Wp-%apiversion.typelib
%_pkgconfigdir/wireplumber-%apiversion.pc
%_libdir/libwireplumber-%apiversion.so
%_includedir/wireplumber-%apiversion
# /usr/share/gir-1.0/Wp-%apiversion.gir

%changelog
* Sun Feb 21 2021 Arseny Maslennikov <arseny@altlinux.org> 0.3.60.63.g24a260030bab-alt1
- Initial build for ALT Sisyphus.
