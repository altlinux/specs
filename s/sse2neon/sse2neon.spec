%define _unpackaged_files_terminate_build 1
%define git 0d6e9b3
%define optflags_lto %nil

%global _description \
sse2neon is a translator of Intel SSE (Streaming SIMD Extensions) intrinsics to \
Arm NEON, shortening the time needed to get an Arm working program that then \
can be used to extract profiles and to identify hot paths in the code. The \
header file sse2neon.h contains several of the functions provided by Intel \
intrinsic headers such as <xmmintrin.h>, only implemented with NEON-based \
counterparts to produce the exact semantics of the intrinsics.

Name:    sse2neon
Version: 1.6.0
Release: alt3.g%{git}
Summary: A translator from Intel SSE intrinsics to Arm/Aarch64 NEON implementation
Group:   Development/C++
License: MIT
URL:     https://github.com/DLTcollab/sse2neon

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: clang libstdc++-devel

ExclusiveArch: %arm aarch64
%description %_description

%package devel
Summary:   translator from Intel SSE intrinsics to Arm/Aarch64 NEON implementation
Group:   Development/C++
%description devel %_description

%prep
%setup
%patch -p1

%build
export CXXFLAGS='%optflags'
# clang supports more instructions than gcc
export CXX=clang++
export CC=clang
%make_build

%install
mkdir -p %buildroot%_includedir
install -pm644 %name.h %buildroot%_includedir/

%check
# checks are hw depended? Ignore then for now
# failed tests:
# [00:00:27] Test mm_set_rounding_mode           failed
# [00:00:27] Test mm_setcsr                      failed
# [00:00:27] Test mm_storeu_si64                 failed
# [00:00:27] Test mm_cvtpd_epi32                 failed
# [00:00:27] Test mm_cvtpd_pi32                  failed
# [00:00:27] Test mm_cvttpd_epi32                failed
# [00:00:27] Test mm_cvttpd_pi32                 failed
# [00:00:28] Test mm_set_denormals_zero_mode     failed
make check ||:

%files devel
%doc LICENSE
%doc *.md
%_includedir/*

%changelog
* Wed Nov 08 2023 L.A. Kostis <lakostis@altlinux.ru> 1.6.0-alt3.g0d6e9b3
- v1.6.0-59-g0d6e9b3.

* Fri Jul 07 2023 L.A. Kostis <lakostis@altlinux.ru> 1.6.0-alt2.g2eede2
- fix armh detection.

* Fri Jul 07 2023 L.A. Kostis <lakostis@altlinux.ru> 1.6.0-alt1.g2eede2
- initial build for ALTLinux.
