%ifarch %ix86
%global optflags_lto %nil
%endif

Name: boca
Version: 1.0.7
Release: alt4.git8ffdb685

Summary: A component library used by the fre:ac audio converter

License: GPL-2.0
Group: System/Libraries
URL: https://www.freac.org
VCS: https://github.com/enzo1982/BoCA

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

%package -n lib%name
Summary: A component library used by the fre:ac audio converter
Group: System/Libraries

%description -n lib%name
BoCA is the component framework behind the fre:ac audio converter.
It provides unified interfaces for components like encoders,
decoders, taggers and extensions as well as code to support
communication between the application and its components.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C++

%description -n lib%name-devel
This package contains header files for lib%name.

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

%files -n lib%name
%doc *.md COPYING
%_libdir/%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Sun Sep 27 2026 Alexander Kovalev <alexvk@altlinux.org> 1.0.7-alt4.git8ffdb685
- Update to git 8ffdb685.
- Rename source package according to upstream name.

* Sun Jul 26 2026 Alexander Kovalev <alexvk@altlinux.org> 1.0.7-alt3.git5d0de9f4
- Update to git 5d0de9f4.

* Sun Jan 25 2026 Alexander Kovalev <alexvk@altlinux.org> 1.0.7-alt2.gitd98a4875
- Update to git d98a4875.

* Tue Oct 14 2025 Alexander Kovalev <alexvk@altlinux.org> 1.0.7-alt1.git1f120b87
- Initial build for ALT.
