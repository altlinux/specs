Name:    libdng
Version: 0.1.1
Release: alt1.git9c7b18e

Summary: Interface library between libtiff and the world to make sure the output is valid DNG
License: MIT
Group:   System/Libraries
Url:     https://gitlab.com/megapixels-org/libdng

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: libtiff-devel
BuildRequires: scdoc

%description
%summary

%package devel
Summary: Development files for %name
Group: Development/C

%description devel
%summary

%package utils
Summary: Utility for %name
Group: Other

%description utils
%summary

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc docs/index.rst docs/overview.rst
%_libdir/%name.so.*

%files devel
%_includedir/%name.h
%_libdir/%name.so
%_libdir/pkgconfig/%name.pc

%files utils
%_bindir/makedng
%_man1dir/makedng.1*

%changelog
* Tue Apr 30 2024 Andrey Cherepanov <cas@altlinux.org> 0.1.1-alt1.git9c7b18e
- Initial build for Sisyphus.
