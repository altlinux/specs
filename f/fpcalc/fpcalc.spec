%define _name chromaprint

Name: fpcalc
Version: 1.5.1
Release: alt1
Summary: fpcalc tool from Chromaprint package

Group: Sound
License: LGPLv2+
Url: http://www.acoustid.org/chromaprint

Source: %_name-%version.tar

BuildRequires: rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libchromaprint-devel
BuildRequires: libfftw3-devel libtag-devel
BuildRequires: libavdevice-devel libavformat-devel
BuildRequires: libavutil-devel libswresample-devel

%description
Chromaprint library is the core component of the AcoustID project. It's a
client-side library that implements a custom algorithm for extracting
fingerprints from raw audio sources.

This package provides command-line tool from Chromaprint.

%prep
%setup -n %_name-%version

%build
%cmake \
    -DBUILD_SHARED_LIBS=OFF \
    -DBUILD_TOOLS=ON \
    -DBUILD_EXAMPLES=OFF \
    -DBUILD_TESTS=OFF
%cmake_build

%install
%cmake_install
rm -f %buildroot%_libdir/*.a

%files
%_bindir/fpcalc

%changelog
* Mon Jul 03 2023 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- first build for Sisyphus

