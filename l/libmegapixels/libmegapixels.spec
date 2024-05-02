Name:    libmegapixels
Version: 0.1.0
Release: alt1.git3669b8a

Summary: The device abstraction for the Megapixels application
License: GPL
Group:   System/Libraries
Url:     https://gitlab.com/megapixels-org/libmegapixels

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch0: megapixels-pinephone-pro-conf-syntax.patch

BuildRequires(pre): meson
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: libconfig-devel

%description
%summary

%package devel
Summary: Development files for %name
Group: Development/C

%description devel
%summary

%package utils
Summary: Utilities for %name
Group: Other

%description utils
%summary

%prep
%setup
%patch0 -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%doc docs/index.rst docs/overview.rst
%_libdir/%name.so.*
%_datadir/megapixels/config

%files devel
%_includedir/%name.h
%_libdir/%name.so
%_libdir/pkgconfig/%name.pc

%files utils
%_bindir/*

%changelog
* Tue Apr 30 2024 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt1.git3669b8a
- Initial build for Sisyphus.
