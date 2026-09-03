%define abiversion 4
Name: svt-av1
Version: 4.2.0
Release: alt2

Summary: Scalable Video Technology for AV1 Encoder

# Main library: BSD-3
# Source/Lib/Common/Codec/EbHmCode.c: BSD
# Source/App/EncApp/EbAppString.*
# Source/Lib/Common/Codec/EbString.*
# Source/Lib/Common/Codec/vector.*: MIT
# Source/Lib/Common/ASM_SSE2/x86inc.asm: ISC
# Source/App/DecApp/EbMD5Utility.*: PublicDomain
License: BSD-3-Clause and MIT and ISC and ALT-Public-Domain
Group: Video
Url: https://gitlab.com/AOMediaCodec/SVT-AV1

# Source-url:        %url/-/archive/v%version/%name-%version.tar.bz2
Source: %name-%version.tar


BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: yasm
BuildRequires: help2man



BuildRequires:  pkgconfig(libcpuinfo)

Requires: lib%name%abiversion = %EVR

%description
The Scalable Video Technology for AV1 Encoder (SVT-AV1 Encoder) is an
AV1-compliant encoder library core. The SVT-AV1 development is a
work-in-progress targeting performance levels applicable to both VOD and Live
encoding / transcoding video applications.

%package -n lib%name%abiversion
Group: Video
Summary: SVT-AV1 libraries
%description -n lib%name%abiversion
The Scalable Video Technology for AV1 Encoder (SVT-AV1 Encoder) is an
AV1-compliant encoder library core. The SVT-AV1 development is a
work-in-progress targeting performance levels applicable to both VOD and Live
encoding / transcoding video applications.

This package contains SVT-AV1 libraries.

%package -n lib%name-devel
Group: Development/C
Summary: Development files for SVT-AV1
Requires: lib%name%abiversion = %EVR

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

%prep
%setup

rm -rfv third_party/cpuinfo
rm -rfv third_party/googletest


%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DUSE_CPUINFO=SYSTEM \
    -DSVT_AV1_LTO=ON \
    -DSVT_AV1_PGO=ON \
    %nil

%cmake_build


%install
%cmake_install

install -d -m0755 %buildroot/%_man1dir
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%buildroot%_libdir
#help2man -N --help-option=-help --version-string=%version %buildroot%_bindir/SvtAv1DecApp > %buildroot%_man1dir/SvtAv1DecApp.1
help2man -N --help-option=-help --no-discard-stderr --version-string=%version %buildroot%_bindir/SvtAv1EncApp > %buildroot%_man1dir/SvtAv1EncApp.1


%files
#%_bindir/SvtAv1DecApp
%_bindir/SvtAv1EncApp
#%_man1dir/SvtAv1DecApp.1*
%_man1dir/SvtAv1EncApp.1*

%files -n lib%name%abiversion
%doc LICENSE.md PATENTS.md
%doc CHANGELOG.md CONTRIBUTING.md README.md
#%_libdir/libSvtAv1Dec.so.0*
%_libdir/libSvtAv1Enc.so.%{abiversion}
%_libdir/libSvtAv1Enc.so.%{abiversion}.*

%files -n lib%name-devel
%_includedir/%name/
#%_libdir/libSvtAv1Dec.so
%_libdir/libSvtAv1Enc.so
#%_pkgconfigdir/SvtAv1Dec.pc
%_pkgconfigdir/SvtAv1Enc.pc
%_libdir/cmake/SVT-AV1/

%files -n lib%name-devel-docs
%doc LICENSE.md PATENTS.md
%doc Docs

%changelog
* Wed Sep 02 2026 Vitaly Lipatov <lav@altlinux.ru> 4.2.0-alt2
- Remove obsolete conflict with the legacy libsvt-av1 package (ALT bug 60184).
- Fix the Public Domain license identifier.

* Fri Jul 17 2026 Vitaly Lipatov <lav@altlinux.ru> 4.2.0-alt1
- new version 4.2.0

* Fri Mar 13 2026 Vitaly Lipatov <lav@altlinux.ru> 4.0.1-alt2
- add Obsoletes: libsvt-av1 to libsvt-av14 (ALT bug 58214)

* Sun Mar 08 2026 Vitaly Lipatov <lav@altlinux.ru> 4.0.1-alt1
- new version 4.0.1
- rename libsvt-av1 to libsvt-av1-4 per Shared Libs Policy (soname 4)

* Wed Mar 12 2025 Vitaly Lipatov <lav@altlinux.ru> 3.0.1-alt1
- new version 3.0.1 (with rpmrb script)

* Mon Mar 10 2025 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- new version (3.0.0) with rpmgs script

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
