%def_enable snapshot
%define _name chromaprint

Name: fpcalc
Version: 1.6.0
Release: alt1
Summary: fpcalc tool from Chromaprint package

Group: Sound
License: MIT
Url: https://www.acoustid.org/chromaprint

Vcs: https://github.com/acoustid/chromaprint.git

%if_disabled snapshot
Source: https://github.com/acoustid/chromaprint/releases/download/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

# to avoind conflict with libchromaprint1-debuginfo
%add_debuginfo_skiplist %_bindir/%name

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
#BuildRequires: libchromaprint-devel
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
* Sat Dec 27 2025 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- updated chromaprint to v1.6.0-2-g9b6a0c6 (ready for FFmpeg-8.0)

* Thu Sep 07 2023 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt2
- updated chromaprint to v1.5.1-12-gaa67c95
- built against ffmpeg-6.0 libraries

* Mon Jul 03 2023 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- first build for Sisyphus

