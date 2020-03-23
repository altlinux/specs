Name: opusfile
Version: 0.11
Release: alt0.5.gd2577d7

Summary: Library for encoding .opus audio files and live streams
License: BSD
Group: System/Libraries
Url: http://opus-codec.org/
# http://downloads.xiph.org/releases/opus/%name-%version.tar.gz
Source0: %name-%version.tar
Source1: package_version

BuildRequires: libssl-devel libogg-devel libopus-devel

%def_disable static

%description
Stand-alone decoder library for .opus streams

%package -n lib%{name}0
Summary: Stand-alone decoder library for .opus streams
License: BSD
Group: System/Libraries

%description -n lib%{name}0
Stand-alone decoder library for .opus streams

%package devel
Summary: Development files for %name
Group: Development/C
PreReq: lib%{name}0 = %EVR
BuildRequires: doxygen

%description devel
This package contains the header files and documentation needed
to develop applications with %name.

%package devel-static
Summary: Static libraries for %name
Group: Development/C
PreReq: %name-devel = %EVR

%description devel-static
This package contains development libraries required for packaging
statically linked libopus-based software.

%package -n libopusurl0
Summary: High-level Opus decoding library, URL support
License: BSD
Group: System/Libraries

%description -n libopusurl0
High-level Opus decoding library, URL support.

%package -n opusurl-devel
Summary: Development files for opusurl
Group: Development/C
PreReq: libopusurl0 = %EVR
BuildRequires: libssl-devel

%description -n opusurl-devel
This package contains the header files and documentation needed
to develop applications with opusurl.

%package -n opusurl-devel-static
Summary: Static libraries for opusurl
Group: Development/C
PreReq: %name-devel = %EVR

%description -n opusurl-devel-static
This package contains development libraries required for packaging
statically linked libopus-based software.

%prep
%setup

%build
cp %SOURCE1 .
%autoreconf
%configure \
	%{subst_enable static}
%make_build

%install
%makeinstall_std

%check
%make check

%files -n lib%{name}0
%_libdir/lib%{name}.so.*
%doc AUTHORS README.md COPYING

%files devel
%_libdir/lib%{name}.so
%_includedir/*
%_pkgconfigdir/%name.pc
%dir %_docdir/%name/
%_docdir/%name/*

%if_enabled static
%files devel-static
%_libdir/lib%{name}.a
%endif

%files -n libopusurl0
%_libdir/libopusurl.so.*

%files -n opusurl-devel
%_libdir/libopusurl.so
%_pkgconfigdir/opusurl.pc

%if_enabled static
%files devel-static
%_libdir/libopusurl.a
%endif

%changelog
* Sat Mar 21 2020 L.A. Kostis <lakostis@altlinux.ru> 0.11-alt0.5.gd2577d7
- initial build for ALTLinux.

