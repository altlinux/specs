%define optflags_lto -flto=thin
%define llvm_version 17.0

# git show -s --format=%ci upstream/pcsx2 | sed 's/[ :-]//g' | sed 's/\(.\{,14\}\).*/\1/'
%define svn_rev 20231218210658

%define gtest_version 1.12.1
%define zstd_version 1.5.5
%define vulkan_headers_version 1.3.272
%define glslang_version 11.7.1
%define rcheevos_commit 8afec6c55e3a0f72368a5a085203bab1b8828ffb
%define libwebp_version 1.3.2
%define fmt_commit 5cfd28d476c6859617878f951931b8ce7d36b9df
%define rapidyaml_version 0.4.1
%define c4core_commit d35c7c9bf370134595699d791e6ff8db018ddc8d
%define cmake_commit 371982300ff5a076d7c3199057ebed77bbe3472f
%define debugbreak_commit 5dcbe41d2bd4712c8014aa7e843723ad7b40fd74
%define lz4_commit b8fd2d15309dd4e605070bd4486e26b6ef814e29

Name: pcsx2
Version: 1.7.5312
Release: alt1

Summary: Playstation 2 console emulator
License: GPLv3 and LGPLv3
Group: Emulators

Url: http://%name.net/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64

BuildRequires(pre): at-spi2-atk-devel
BuildRequires(pre): bzlib-devel
BuildRequires(pre): expat-devel
BuildRequires(pre): libat-spi2-core-devel
BuildRequires(pre): libblkid-devel
BuildRequires(pre): libbrotli-devel
BuildRequires(pre): libdatrie-devel
BuildRequires(pre): libdbus-devel
BuildRequires(pre): libepoxy-devel
BuildRequires(pre): libffi-devel
BuildRequires(pre): libfribidi-devel
BuildRequires(pre): libjpeg-devel
BuildRequires(pre): libmount-devel
BuildRequires(pre): libpcre2-devel
BuildRequires(pre): libpixman-devel
BuildRequires(pre): libselinux-devel
BuildRequires(pre): libthai-devel
BuildRequires(pre): libtiff-devel
BuildRequires(pre): libuuid-devel
BuildRequires(pre): wayland-protocols

# https://github.com/PCSX2/%name/archive/v%version/%name-%version.tar.gz
Source0: %name-%version.tar
# https://github.com/google/googletest/archive/release-%gtest_version/googletest-release-%gtest_version.tar.gz
Source1: googletest-release-%gtest_version.tar
# https://github.com/facebook/zstd/archive/v%zstd_version/zstd-%zstd_version.tar.gz
Source2: zstd-%zstd_version.tar
# https://github.com/KhronosGroup/Vulkan-Headers/archive/v%vulkan_headers_version/Vulkan-Headers-%vulkan_headers_version.tar.gz
Source3: Vulkan-Headers-%vulkan_headers_version.tar
# https://github.com/KhronosGroup/glslang/archive/%glslang_version/glslang-%glslang_version.tar.gz
Source4: glslang-%glslang_version.tar
# https://github.com/RetroAchievements/rcheevos/archive/%rcheevos_commit/rcheevos-%rcheevos_commit.tar.gz
Source5: rcheevos-%rcheevos_commit.tar
# https://github.com/webmproject/libwebp/archive/v%libwebp_version/libwebp-%libwebp_version.tar.gz
Source6: libwebp-%libwebp_version.tar
# https://github.com/fmtlib/fmt/archive/%fmt_commit/fmt-%fmt_commit.tar.gz
Source7: fmt-%fmt_commit.tar
# https://github.com/biojppm/rapidyaml/archive/v%rapidyaml_version/rapidyaml-%rapidyaml_version.tar.gz
Source8: rapidyaml-%rapidyaml_version.tar
# https://github.com/biojppm/c4core/archive/%c4core_commit/c4core-%c4core_commit.tar.gz
Source9: c4core-%c4core_commit.tar
# https://github.com/biojppm/cmake/archive/%cmake_commit/cmake-%cmake_commit.tar.gz
Source10: cmake-%cmake_commit.tar
# https://github.com/biojppm/debugbreak/archive/%debugbreak_commit/debugbreak-%debugbreak_commit.tar.gz
Source11: debugbreak-%debugbreak_commit.tar
# https://github.com/lz4/lz4/archive/%lz4_commit/lz4-%lz4_commit.tar.gz
Source12: lz4-%lz4_commit.tar

BuildRequires: clang%llvm_version
BuildRequires: ctest
BuildRequires: extra-cmake-modules
BuildRequires: libGLU-devel
BuildRequires: libSDL2-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXcursor-devel
BuildRequires: libXdamage-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXft-devel
BuildRequires: libXinerama-devel
BuildRequires: libXmu-devel
BuildRequires: libXrandr-devel
BuildRequires: libXtst-devel
BuildRequires: libaio-devel
BuildRequires: libalsa-devel
BuildRequires: libavformat-devel
BuildRequires: libbacktrace-devel
BuildRequires: libcurl-devel
BuildRequires: libdbus-devel
BuildRequires: libfast_float-devel
BuildRequires: liblzma-devel
BuildRequires: libpcap-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libswresample-devel
BuildRequires: libswscale-devel
BuildRequires: libudev-devel
BuildRequires: libwayland-egl-devel
BuildRequires: lld%llvm_version
BuildRequires: llvm%llvm_version
BuildRequires: llvm%llvm_version-gold
BuildRequires: ninja-build
BuildRequires: qt6-tools-devel

%description
PCSX2 is an emulator for the playstation 2 video game console. It is written mostly in C++, some part are in C and x86 assembly.
There is still lot of on going work to improve compatibility & speed.

%prep
%setup -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8 -b 9 -b 10 -b 11 -b 12

%__mv -Tf ../googletest-release-%gtest_version 3rdparty/gtest
%__mv -Tf ../zstd-%zstd_version 3rdparty/zstd/zstd
%__mv -Tf ../Vulkan-Headers-%vulkan_headers_version 3rdparty/vulkan-headers
%__mv -Tf ../glslang-%glslang_version 3rdparty/glslang/glslang
%__mv -Tf ../rcheevos-%rcheevos_commit 3rdparty/rcheevos/rcheevos
%__mv -Tf ../libwebp-%libwebp_version 3rdparty/libwebp/libwebp
%__mv -Tf ../fmt-%fmt_commit 3rdparty/fmt/fmt
%__mv -Tf ../rapidyaml-%rapidyaml_version 3rdparty/rapidyaml/rapidyaml
%__mv -Tf ../c4core-%c4core_commit 3rdparty/rapidyaml/rapidyaml/ext/c4core
%__mv -Tf ../cmake-%cmake_commit 3rdparty/rapidyaml/rapidyaml/ext/c4core/cmake
%__mv -Tf ../debugbreak-%debugbreak_commit 3rdparty/rapidyaml/rapidyaml/ext/c4core/src/c4/ext/debugbreak
%__mv -Tf ../lz4-%lz4_commit 3rdparty/lz4/lz4

%build
export ALTWRAP_LLVM_VERSION=%llvm_version

%cmake \
	-DCMAKE_C_COMPILER:STRING=clang \
	-DCMAKE_CXX_COMPILER:STRING=clang++ \
	-DCMAKE_RANLIB:PATH=%_bindir/llvm-ranlib \
	-DCMAKE_AR:PATH=%_bindir/llvm-ar \
	-DCMAKE_NM:PATH=%_bindir/llvm-nm \
	-DCMAKE_EXE_LINKER_FLAGS:STRING="-fuse-ld=lld" \
	-DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" \
	-DCMAKE_DISABLE_PRECOMPILE_HEADERS:BOOL=TRUE \
	-DCMAKE_BUILD_PO:BOOL=TRUE \
	-DDISABLE_ADVANCE_SIMD:BOOL=TRUE \
	-DDISABLE_BUILD_DATE:BOOL=TRUE \
	-DLTO_PCSX2_CORE:BOOL=TRUE \
	-GNinja \
	-Wno-dev

echo "#define SVN_REV $(echo %svn_rev)ll 
#define GIT_TAG \"v$(echo %version)\"
#define GIT_TAGGED_COMMIT 1
#define GIT_REV \"\"" > %_cmake__builddir/common/include/svnrev.h

%cmake_build

%install
%__mkdir_p %buildroot%_bindir %buildroot%_libexecdir/%name
%__install -Dp -m0755 %_target_platform/bin/%name-qt %buildroot%_libexecdir/%name/%name-qt
%__ln_s %_libexecdir/%name/%name-qt %buildroot%_bindir/%name-qt
%__cp -r %_target_platform/bin/resources %buildroot%_libexecdir/%name
%__install -Dp -m0644 %_target_platform/bin/resources/icons/AppIconLarge.png %buildroot%_iconsdir/hicolor/256x256/apps/PCSX2.png
%__install -Dp -m0644 .github/workflows/scripts/linux/%name-qt.desktop %buildroot%_desktopdir/%name-qt.desktop

%check
%ctest

%files
%doc bin/docs/*.pdf
%_bindir/%name-qt
%_desktopdir/%name-qt.desktop
%_libexecdir/%name
%_iconsdir/hicolor/256x256/apps/PCSX2.png

%changelog
* Tue Dec 19 2023 Nazarov Denis <nenderus@altlinux.org> 1.7.5312-alt1
- Version 1.7.5312

* Wed Oct 18 2023 Nazarov Denis <nenderus@altlinux.org> 1.7.5107-alt1
- Version 1.7.5107

* Sat Jun 17 2023 Nazarov Denis <nenderus@altlinux.org> 1.7.4587-alt1
- Version 1.7.4587

* Sat May 13 2023 Nazarov Denis <nenderus@altlinux.org> 1.7.4500-alt1
- Version 1.7.4500

* Mon Apr 17 2023 Nazarov Denis <nenderus@altlinux.org> 1.7.4395-alt1
- Version 1.7.4395

* Sat Apr 15 2023 Nazarov Denis <nenderus@altlinux.org> 1.7.4383-alt1
- Version 1.7.4383

* Fri Apr 14 2023 Nazarov Denis <nenderus@altlinux.org> 1.7.4380-alt1
- Version 1.7.4380

* Thu Apr 06 2023 Nazarov Denis <nenderus@altlinux.org> 1.7.4342-alt1
- Version 1.7.4342

* Mon Dec 19 2022 Nazarov Denis <nenderus@altlinux.org> 1.7.3332-alt1.1
- Fix build

* Sat Sep 24 2022 Nazarov Denis <nenderus@altlinux.org> 1.7.3332-alt1
- Version 1.7.3332

* Sun May 29 2022 Nazarov Denis <nenderus@altlinux.org> 1.7.2828-alt1
- Version 1.7.2828

* Mon May 23 2022 Nazarov Denis <nenderus@altlinux.org> 1.7.2787-alt1
- Version 1.7.2787

* Fri Dec 10 2021 Nazarov Denis <nenderus@altlinux.org> 1.7.2116-alt1
- Version 1.7.2116

* Sat Nov 06 2021 Nazarov Denis <nenderus@altlinux.org> 1.7.2019-alt1
- Version 1.7.2019

* Fri Nov 05 2021 Nazarov Denis <nenderus@altlinux.org> 1.7.2016-alt1
- Version 1.7.2016

* Thu Nov 04 2021 Nazarov Denis <nenderus@altlinux.org> 1.7.2012-alt1
- Version 1.7.2012

* Wed Nov 03 2021 Nazarov Denis <nenderus@altlinux.org> 1.7.2006-alt1
- Version 1.7.2006

* Tue Nov 02 2021 Nazarov Denis <nenderus@altlinux.org> 1.7.2003-alt1
- Version 1.7.2003

* Sun Oct 11 2020 Anton Midyukov <antohami@altlinux.org> 1.6.0-alt6
- Rebuild with libwxGTK3.0

* Mon Jun 01 2020 Nazarov Denis <nenderus@altlinux.org> 1.6.0-alt5
- Use directory /usr/share/doc/PCSX2 for Configuration Guide and Readme / FAQ

* Sun May 24 2020 Nazarov Denis <nenderus@altlinux.org> 1.6.0-alt4
- Build GSdx plugin additionaly without AVX2 & SSE4 support
- Build GSdx legacy plugin
- Disable build date

* Sat May 23 2020 Nazarov Denis <nenderus@altlinux.org> 1.6.0-alt3
- Move localization files to separate subpackage
- Add requires to all plugin types

* Sat May 23 2020 Nazarov Denis <nenderus@altlinux.org> 1.6.0-alt2
- Add build pre requires
- Return XDG_STD option

* Fri May 08 2020 Nazarov Denis <nenderus@altlinux.org> 1.6.0-alt1
- Version 1.6.0

* Mon Jul 23 2018 Nazarov Denis <nenderus@altlinux.org> 1.4.0-alt2%ubt
- Rebuilt with new GLEW

* Sat Feb 20 2016 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1.1
- rebuilt against libSoundTouch.so.1

* Mon Jan 11 2016 Nazarov Denis <nenderus@altlinux.org> 1.4.0-alt1
- Version 1.4.0

* Tue Nov 18 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.2-alt2
- Rebuild with libsoundtouch 1.8.0

* Sun Feb 16 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.2-alt0.M70T.1
- Build for branch t7

* Sun Feb 16 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.2-alt1
- Version 1.2.2

* Tue Feb 11 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.1-alt1.M70P.1
- Build for branch p7

* Mon Feb 10 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.1-alt1.M70T.1
- Build for branch t7

* Sun Feb 09 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.1-alt2
- Fix language files for x64

* Sat Feb 08 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.1-alt0.M70T.1
- Build for branch t7

* Fri Feb 07 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.1-alt1
- Version 1.2.1

* Tue Feb 04 2014 Nazarov Denis <nenderus@altlinux.org> 1.2.0-alt1
- Version 1.2.0

* Thu Oct 17 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0-alt1.M70T.1
- Build for branch t7

* Sat Sep 28 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0-alt2
- Fix post-install unowned files
- Rebuild the ps2hw.dat file

* Fri Sep 27 2013 Nazarov Denis <nenderus@altlinux.org> 1.0.0-alt1
- Initial build for ALT Linux
