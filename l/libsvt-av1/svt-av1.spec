%define sover 2
%define oname svt-av1
Name: lib%oname
Version: 2.3.0
Release: alt3

Summary: Scalable Video Technology for AV1 Encoder (legacy)

# Main library: BSD-3
# Source/Lib/Common/Codec/EbHmCode.c: BSD
# Source/App/EncApp/EbAppString.*
# Source/Lib/Common/Codec/EbString.*
# Source/Lib/Common/Codec/vector.*: MIT
# Source/Lib/Common/ASM_SSE2/x86inc.asm: ISC
# Source/App/DecApp/EbMD5Utility.*: PublicDomain
License: BSD-3-Clause and MIT and ISC and Public Domain
Group: System/Legacy libraries
Url: https://gitlab.com/AOMediaCodec/SVT-AV1

# Source-url:        %url/-/archive/v%version/%oname-%version.tar.bz2
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake rpm-macros-meson
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: yasm
BuildRequires: help2man

BuildRequires:  meson
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)


BuildRequires:  pkgconfig(libcpuinfo)

Obsoletes: libSvtAv1Enc2

%description
Legacy shared library libSvtAv1Enc.so.2 for backward compatibility.

%package -n lib%name
Group: Video
Summary: SVT-AV1 libraries

%description -n lib%name
The Scalable Video Technology for AV1 Encoder (SVT-AV1 Encoder) is an
AV1-compliant encoder library core. The SVT-AV1 development is a
work-in-progress targeting performance levels applicable to both VOD and Live
encoding / transcoding video applications.

This package contains SVT-AV1 libraries.

%package -n lib%name-devel
Group: Development/C
Summary: Development files for SVT-AV1
Requires: lib%name = %EVR

%description -n lib%name-devel
The Scalable Video Technology for AV1 Encoder (SVT-AV1 Encoder) is an
AV1-compliant encoder library core. The SVT-AV1 development is a
work-in-progress targeting performance levels applicable to both VOD and Live
encoding / transcoding video applications.

This package contains the development files for SVT-AV1.

%package -n lib%name-devel-docs
Group: Development/Documentation
Summary: Development documentation for SVT-AV1
BuildArch: noarch

%description -n lib%name-devel-docs
The Scalable Video Technology for AV1 Encoder (SVT-AV1 Encoder) is an
AV1-compliant encoder library core. The SVT-AV1 development is a
work-in-progress targeting performance levels applicable to both VOD and Live
encoding / transcoding video applications.

This package contains the documentation for development of SVT-AV1.

%package -n gstreamer1-%oname
Group: Video
Summary: GStreamer 1.0 %oname-based plug-in
Requires: gst-plugins-base1.0

%description -n gstreamer1-%oname
This package provides %oname-based GStreamer plug-in.

%prep
%setup
rm -rfv third_party/cpuinfo
rm -rfv third_party/aom*
rm -rfv third_party/googletest

# Patch build gstreamer plugin
sed -e "s|install: true,|install: true, include_directories : [ include_directories('../Source/API') ], link_args : '-lSvtAv1Enc',|" \
-e "/svtav1enc_dep =/d" -e 's|, svtav1enc_dep||' -e "s|svtav1enc_dep.found()|true|" -i gstreamer-plugin/meson.build

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DUSE_EXTERNAL_CPUINFO=ON \
    -DSVT_AV1_LTO=ON \
    -DSVT_AV1_PGO=ON \
    %nil

%cmake_build

export LIBRARY_PATH="$LIBRARY_PATH:$(pwd)/Bin/RelWithDebInfo"
pushd gstreamer-plugin
%meson
%meson_build
popd

%install
%cmake_install

install -d -m0755 %buildroot/%_man1dir
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%buildroot%_libdir
#help2man -N --help-option=-help --version-string=%version %buildroot%_bindir/SvtAv1DecApp > %buildroot%_man1dir/SvtAv1DecApp.1
help2man -N --help-option=-help --no-discard-stderr --version-string=%version %buildroot%_bindir/SvtAv1EncApp > %buildroot%_man1dir/SvtAv1EncApp.1

pushd gstreamer-plugin
%meson_install
popd

rm -rf %buildroot%_bindir
rm -rf %buildroot%_includedir
rm -f %buildroot%_libdir/libSvtAv1Enc.so
rm -rf %buildroot%_libdir/cmake
rm -rf %buildroot%_pkgconfigdir
rm -rf %buildroot%_man1dir

%files
%_libdir/libSvtAv1Enc.so.%{sover}
%_libdir/libSvtAv1Enc.so.%{sover}.*

%files -n gstreamer1-%oname
%_libdir/gstreamer-1.0/libgstsvtav1enc.so

%changelog
* Sat Mar 14 2026 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt3
- rebuild as libsvt-av1 legacy package (replaces libSvtAv1Enc2)

* Mon Mar 10 2025 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt1
- new version (2.3.0) with rpmgs script

* Sun Feb 18 2024 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- new version 1.8.0 (with rpmrb script)

* Fri Jun 30 2023 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1
- new version 1.6.0 (with rpmrb script)

* Tue May 02 2023 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- new version 1.5.0 (with rpmrb script)

* Tue May 02 2023 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- initial build for Sisyphus (thanks, Fedora!)
