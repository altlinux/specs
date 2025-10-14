%define oname boca

Name: lib%oname
Version: 1.0.7
Release: alt1.git1f120b87

Summary: A component library used by the fre:ac audio converter

License: GPL-2.0
Group: System/Libraries
URL: https://www.freac.org
VCS: https://github.com/enzo1982/BoCA

Packager: Alexander Kovalev <alexvk@altlinux.org>

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires: gcc-c++
BuildRequires: libcdio-paranoia-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libsmooth-devel
BuildRequires: liburiparser-devel
BuildRequires: libxspf-devel

%description
BoCA is the component framework behind the fre:ac audio converter.
It provides unified interfaces for components like encoders,
decoders, taggers and extensions as well as code to support
communication between the application and its components.

%package devel
Summary: Development files for %name
Group: Development/C++

%description devel
This package contains header files for %name.

%prep
%setup
%autopatch -p1
find . -type f -exec sed -i 's|/usr/local|%_prefix|g' {} \;
sed -i 's|^LIBDIR = lib$|LIBDIR = %_lib|;
	s|(prefix)/lib$|(prefix)/%_lib|' Makefile-options
sed -i 's|(prefix)/lib |(prefix)/%_lib |' Makefile-commands runtime/Makefile
sed -i 's|/lib/boca|/%_lib/boca|g' runtime/common/utilities.cpp

%build
export CFLAGS="%optflags"
export CXXFLAGS="$CFLAGS"
export OBJCFLAGS="$CFLAGS"
export OBJCXXFLAGS="$CFLAGS"
%make_build config=systemlibxspf

%install
%makeinstall_std

%files
%doc *.md COPYING
%_libdir/%oname
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so

%changelog
* Tue Oct 14 2025 Alexander Kovalev <alexvk@altlinux.org> 1.0.7-alt1.git1f120b87
- Initial build for ALT.
