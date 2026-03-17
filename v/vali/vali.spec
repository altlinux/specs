%define _unpackaged_files_terminate_build 1
%define soversion 1

Name: vali
Version: 0.1.1
Release: alt1

Summary: A C library and code generator for Varlink
License: MIT
Group: Development/C

Url: https://gitlab.freedesktop.org/emersion/vali
VCS: https://gitlab.freedesktop.org/emersion/vali

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: meson ninja-build
BuildRequires: libjson-c-devel libaml-devel

%description
A Varlink C implementation and code generator.

%package -n libvali%soversion
Summary: A C library for Varlink
Group: Development/C

%description -n libvali%soversion
%summary.

%package -n libvali-devel
Summary: Development files for library.
Group: Development/C
Requires: libvali%soversion = %EVR

%description -n libvali-devel
%summary.

%prep
%setup
%patch0 -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%_bindir/vali

%files -n libvali-devel
%_includedir/vali.h
%_libdir/libvali.so
%_pkgconfigdir/vali.pc

%files -n libvali%soversion
%_libdir/libvali.so.%version
%_libdir/libvali.so.%soversion

%changelog
* Tue Mar 17 2026 Andrey Kovalev <ded@altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus.
