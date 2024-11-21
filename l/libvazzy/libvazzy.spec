%define _unpackaged_files_terminate_build 1

Name: libvazzy
Version: 0.1.0
Release: alt1

Summary: ALT Repo API library on Vala
License: GPL-3.0
Group: Development/Other
Url: https://github.com/Rirusha/libvazzy
VCS: https://github.com/Rirusha/libvazzy

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: gobject-introspection-devel

%description
%summary.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%_includedir/libvazzy.h
%_libdir/girepository-1.0/Vazzy-0.1.typelib
%_libdir/libalt-repo.*
%_libdir/pkgconfig/libvazzy-0.1.pc
%_datadir/gir-1.0/Vazzy-0.1.gir
%_datadir/vala/vapi/libvazzy-0.1.deps
%_datadir/vala/vapi/libvazzy-0.1.vapi

%changelog
* Thu Nov 21 2024 Alexey Volkov <qualimock@altlinux.org> 0.1.0-alt1
- Initial build for ALT
