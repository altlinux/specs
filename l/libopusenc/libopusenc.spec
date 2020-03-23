Name: libopusenc
Version: 0.2.1
Release: alt2.g9cb17c6

Summary: Library for encoding .opus audio files and live streams
License: BSD
Group: System/Libraries
Url: http://opus-codec.org/
# http://downloads.xiph.org/releases/opus/%name-%version.tar.gz
Source0: %name-%version.tar
Source1: package_version

BuildRequires: libopus-devel

%def_disable static

%description
The libopusenc libraries provide a high-level API for encoding .opus files. libopusenc depends only on libopus.

%package -n %{name}0
Summary: Library for encoding .opus audio files and live streams
License: BSD
Group: System/Libraries

%description -n %{name}0
The libopusenc libraries provide a high-level API for encoding .opus files. libopusenc depends only on libopus.

%package devel
Summary: Development files for %name
Group: Development/C
PreReq: %{name}0 = %EVR
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

%files -n %{name}0
%_libdir/*.so.*
%doc AUTHORS README.md COPYING

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc
%dir %_docdir/%name/
%_docdir/%name/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Mon Mar 23 2020 L.A. Kostis <lakostis@altlinux.ru> 0.2.1-alt2.g9cb17c6
- Bump release.

* Sat Mar 21 2020 L.A. Kostis <lakostis@altlinux.ru> 0.2.1-alt0.2.g9cb17c6
- initial build for ALTLinux.
