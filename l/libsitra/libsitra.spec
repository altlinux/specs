%define _unpackaged_files_terminate_build 1
%define sover 0
%define api_ver 0.1
%define libsitra libsitra%sover
%define namespace Libsitra

Name: libsitra
Version: 0.1.0
Release: alt1

Summary: A library to list, and manage online fonts on your system.
Group: System/Libraries
License: GPL-3.0-or-later
Url: https://github.com/sitraorg/libsitra
Vcs: https://github.com/sitraorg/libsitra

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(json-glib-1.0)

%description
A library to list, and manage online fonts on your system.

%package -n %libsitra
Summary: A library to list, and manage online fonts on your system.
Group: System/Libraries

%description -n %libsitra
A library to list, and manage online fonts on your system.

%package devel
Summary: Development files for libsitra.
Requires: %libsitra = %EVR
Group: System/Libraries

%description devel
This package contains the libraries and header files that are needed
for writing applications with libsitra.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files -n %libsitra
%_libdir/%name.so.%version
%_libdir/%name.so.%sover

%files devel
%_libdir/%name.so
%_includedir/%name.h
%_libdir/pkgconfig/%name-%api_ver.pc
%_datadir/vala/vapi/%name-%api_ver.vapi
%_girdir/%namespace-%api_ver.gir

%changelog
* Mon Feb 23 2026 Vladislav Petrukhin <vladp@altlinux.org> 0.1.0-alt1
- Initial build.

