%define sover 0
%define libchromaprint libchromaprint%sover

Name: chromaprint
Version: 0.6
Release: alt1
Summary: Library implementing the AcoustID fingerprinting

Group: Sound
License: LGPLv2+
Url: http://www.acoustid.org/chromaprint/
Source: %name-%version.tar

# Automatically added by buildreq on Mon May 21 2012 (-bi)
# optimized out: boost-devel cmake-modules elfutils libavcodec-devel libavutil-devel libopencore-amrnb0 libopencore-amrwb0 libstdc++-devel pkg-config python-base
#BuildRequires: boost-devel-headers cmake gcc-c++ libavdevice-devel libavformat-devel libfftw3-devel libswscale-devel libtag-devel
BuildRequires: boost-devel cmake gcc-c++ libavdevice-devel libavformat-devel libfftw3-devel libswscale-devel libtag-devel
BuildRequires: cmake kde-common-devel

%description
Chromaprint library is the core component of the AcoustID project. It's a
client-side library that implements a custom algorithm for extracting
fingerprints from raw audio sources.

The library exposes a simple C API. The documentation for the C API can be
found in the main header file.

%package -n %libchromaprint
Summary: Library implementing the AcoustID fingerprinting
Group: System/Libraries
#Obsoletes: python-chromaprint < 0.6-alt1
%description -n %libchromaprint
Chromaprint library is the core component of the AcoustID project. It's a
client-side library that implements a custom algorithm for extracting
fingerprints from raw audio sources.

The library exposes a simple C API. The documentation for the C API can be
found in the main header file.

%package -n libchromaprint-devel
Summary: Headers for developing programs that will use %name
Group: Development/C
Requires: %libchromaprint = %version-%release
%description -n libchromaprint-devel
This package contains the headers that programmers will need to develop
applications which will use %name.

%prep
%setup


%build
%Kbuild \
    -DBUILD_TOOLS=ON \
    -DBUILD_EXAMPLES=OFF \
    -DBUILD_TESTS=OFF

%install
%Kinstall
mkdir -p %buildroot/%_bindir
[ -x %buildroot/%_bindir/fpcollect ] || install -m 0755 BUILD*/tools/fpcollect  %buildroot/%_bindir/

%files
%_bindir/*

%files -n %libchromaprint
%doc CHANGES.txt NEWS.txt README.txt
%_libdir/libchromaprint.so.%sover
%_libdir/libchromaprint.so.%sover.*

%files -n libchromaprint-devel
%_includedir/chromaprint.h
%_libdir/lib*.so
%_libdir/pkgconfig/*.pc

%changelog
* Mon May 21 2012 Sergey V Turchin <zerg@altlinux.org> 0.6-alt1
- initial build
