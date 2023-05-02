Name: svt-av1
Version: 1.5.0
Release: alt1

Summary: Scalable Video Technology for AV1 Encoder

# Main library: BSD-3
# Source/Lib/Common/Codec/EbHmCode.c: BSD
# Source/App/EncApp/EbAppString.*
# Source/Lib/Common/Codec/EbString.*
# Source/Lib/Common/Codec/vector.*: MIT
# Source/Lib/Common/ASM_SSE2/x86inc.asm: ISC
# Source/App/DecApp/EbMD5Utility.*: PublicDomain
License: BSD-3-Clause and MIT and ISC and Public Domain
Group: Video
Url: https://gitlab.com/AOMediaCodec/SVT-AV1

# Source-url:        %url/-/archive/v%version/%name-%version.tar.bz2
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake rpm-macros-meson
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: meson
BuildRequires: yasm
BuildRequires: help2man
BuildRequires: gstreamer1.0-devel
BuildRequires: gst-plugins1.0-devel

Requires: lib%name = %EVR

%description
The Scalable Video Technology for AV1 Encoder (SVT-AV1 Encoder) is an
AV1-compliant encoder library core. The SVT-AV1 development is a
work-in-progress targeting performance levels applicable to both VOD and Live
encoding / transcoding video applications.

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

%package -n gstreamer1-%name
Group: Video
Summary: GStreamer 1.0 %name-based plug-in
Requires: gst-plugins-base1.0
Requires: lib%name = %EVR

%description -n gstreamer1-%name
This package provides %name-based GStreamer plug-in.

%prep
%setup
# Patch build gstreamer plugin
sed -e "s|install: true,|install: true, include_directories : [ include_directories('../Source/API') ], link_args : '-lSvtAv1Enc',|" \
-e "/svtav1enc_dep =/d" -e 's|, svtav1enc_dep||' -e "s|svtav1enc_dep.found()|true|" -i gstreamer-plugin/meson.build

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo
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
help2man -N --help-option=-help --version-string=%version %buildroot%_bindir/SvtAv1DecApp > %buildroot%_man1dir/SvtAv1DecApp.1
help2man -N --help-option=-help --no-discard-stderr --version-string=%version %buildroot%_bindir/SvtAv1EncApp > %buildroot%_man1dir/SvtAv1EncApp.1

pushd gstreamer-plugin
%meson_install
popd

%files
%_bindir/SvtAv1DecApp
%_bindir/SvtAv1EncApp
%_man1dir/SvtAv1DecApp.1*
%_man1dir/SvtAv1EncApp.1*

%files -n lib%name
%doc LICENSE.md PATENTS.md
%doc CHANGELOG.md CONTRIBUTING.md README.md
%_libdir/libSvtAv1Dec.so.0*
%_libdir/libSvtAv1Enc.so.1*

%files -n lib%name-devel
%_includedir/%name/
%_libdir/libSvtAv1Dec.so
%_libdir/libSvtAv1Enc.so
%_pkgconfigdir/SvtAv1Dec.pc
%_pkgconfigdir/SvtAv1Enc.pc

%files -n lib%name-devel-docs
%doc LICENSE.md PATENTS.md
%doc Docs

%files -n gstreamer1-%name
%_libdir/gstreamer-1.0/libgstsvtav1enc.so

%changelog
* Tue May 02 2023 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- new version 1.5.0 (with rpmrb script)

* Tue May 02 2023 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- initial build for Sisyphus (thanks, Fedora!)
