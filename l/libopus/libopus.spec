Name: libopus
Version: 0.9.14
Release: alt1

Summary: Opus Audio Codec library
License: BSD-style
Group: System/Libraries
Url: http://opus-codec.org/
# http://downloads.xiph.org/releases/opus/%name-%version.tar.xz
Source: opus-%version.tar

%def_disable static

%description
The Opus codec is designed for interactive speech and audio transmission
over the Internet. It is designed by the IETF Codec Working Group and
incorporates technology from Skype's SILK codec and Xiph.Org's CELT codec. 

%package devel
Summary: Development files for libopus
Group: Development/C
PreReq: %name = %version-%release
BuildRequires: doxygen

%description devel
This package contains the header files and documentation needed
to develop applications with libopus.

%package devel-static
Summary: Static libraries for libopus
Group: Development/C
PreReq: %name-devel = %version-%release

%description devel-static
This package contains development libraries required for packaging
statically linked libopus-based software.

%prep
%setup -n opus-%version

%build
%configure %{subst_enable static}
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*
%doc AUTHORS README COPYING

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Mon Jul 23 2012 L.A. Kostis <lakostis@altlinux.ru> 0.9.14-alt1
- Updated to 0.9.14;
- initial build for ALTLinux.

