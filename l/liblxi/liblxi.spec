%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: liblxi
Version: 1.22
Release: alt1

Summary: LAN eXtensions for Instrumentation (LXI) software interface
License: BSD-3-Clause
Group: System/Libraries
Url: https://github.com/lxi/liblxi

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake

BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(avahi-client)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libtirpc)

%description
liblxi is an open source software library which offers a simple API for
communicating with LXI compatible instruments. The API allows
applications to easily discover instruments on networks and communicate
SCPI commands.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Group: Development/C

%description devel

LAN eXtensions for Instrumentation (LXI) software interface
liblxi is an open source software library which offers a simple API for
communicating with LXI compatible instruments. The API allows
applications to easily discover instruments on networks and communicate
SCPI commands.

This package contains development files for %name.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc AUTHORS LICENSE NEWS README.md
%_libdir/*.so.1*

%files devel
%_libdir/*.so
%_pkgconfigdir/*.pc
%_includedir/lxi.h
%_man3dir/lxi_*.3*

%changelog
* Sat Nov 29 2025 Nikolay Strelkov <snk@altlinux.org> 1.22-alt1
- Initial build for Sisyphus
