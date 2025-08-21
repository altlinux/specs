# git describe mainline-0-%version
%define git_descr mainline-636-14434-g537296095ab

%define sirit_commit ab75463999f4f3291976b079d42d52ee91eebf3f
%define tzdb_to_nx_commit 97929690234f2b4add36b33657fe3fe09bd57dfd

Name: yuzu
Version: 1734
Release: alt7

Summary: Nintendo Switch emulator/debugger
License: GPLv3+
Group: Emulators

Url: https://%name-emu.org/
Vcs: https://github.com/%name-emu/%name-mainline
Packager: Nazarov Denis <nenderus@altlinux.org>

ExcludeArch: %ix86

# https://github.com/%name-emu/%name-mainline/archive/mainline-0-%version/%name-mainline-mainline-0-%version.tar.gz
Source0: %name-mainline-mainline-0-%version.tar
# https://github.com/ReinUsesLisp/sirit/archive/%sirit_commit/sirit-%sirit_commit.tar.gz
Source1: sirit-%sirit_commit.tar
# https://github.com/lat9nq/tzdb_to_nx/archive/%tzdb_to_nx_commit/tzdb_to_nx-%tzdb_to_nx_commit.tar.gz
Source2: tzdb_to_nx-%tzdb_to_nx_commit.tar

Patch0: %name-cpp-jwt-version-alt.patch
Patch1: %name-xbyak-version-alt.patch
Patch2: %name-fmt11-alt.patch
Patch3: %name-dynarmic-6.7-debian.patch
Patch4: %name-llvm-version-debian.patch
Patch5: %name-httplib-version-alt.patch
Patch6: %name-mcl-find-alt.patch
Patch7: %name-simpleini-system-alt.patch
Patch8: %name-mbedtls-system-debian.patch

BuildRequires: /proc
BuildRequires: alt-os-release
BuildRequires: boost-asio-devel
BuildRequires: boost-filesystem-devel
BuildRequires: catch-devel
BuildRequires: clang
BuildRequires: clang-tools
BuildRequires: ctest
BuildRequires: git-core
BuildRequires: glslang
BuildRequires: libSDL2-devel
BuildRequires: libVulkanUtilityLibraries-devel
BuildRequires: libavcodec-devel
BuildRequires: libavfilter-devel
BuildRequires: libbrotli-devel
BuildRequires: libcpp-httplib-devel
BuildRequires: libcpp-jwt-devel
BuildRequires: libcubeb-devel
BuildRequires: libdynarmic-devel
BuildRequires: libedit-devel
BuildRequires: libenet-devel
BuildRequires: libffi-devel
BuildRequires: libgamemode-devel
BuildRequires: liblz4-devel
BuildRequires: libmbedtls-devel
BuildRequires: libopus-devel
BuildRequires: libsimpleini-devel
BuildRequires: libstb-devel
BuildRequires: libswscale-devel
BuildRequires: libusb-devel
BuildRequires: libvulkan-memory-allocator-devel
BuildRequires: libxml2-devel
BuildRequires: libzstd-devel
BuildRequires: lld
BuildRequires: llvm
BuildRequires: llvm-devel
BuildRequires: nlohmann-json-devel
BuildRequires: python-modules-encodings
BuildRequires: python3-dev
BuildRequires: qt6-tools-devel
BuildRequires: renderdoc-devel
BuildRequires: spirv-headers
BuildRequires: zlib-devel

%description
%name is an open source Nintendo Switch emulator/debugger.

%prep
%setup -n %name-mainline-mainline-0-%version -b 1 -b 2

%autopatch -p1

%__mv -Tf ../sirit-%sirit_commit externals/sirit
%__mv -Tf ../tzdb_to_nx-%tzdb_to_nx_commit externals/nx_tzdb/tzdb_to_nx

# Enforce package versioning in GUI
sed -i \
-e 's|@GIT_BRANCH@|HEAD|g' \
-e 's|@GIT_DESC@|%git_descr|g' \
-e 's|@TITLE_BAR_FORMAT_IDLE@|%name %version|g' \
-e 's|@TITLE_BAR_FORMAT_RUNNING@|%name %version|g' \
src/common/scm_rev.cpp.in

%__rm .gitmodules

%build
sed -i -e 's/-Werror=shadow-uncaptured-local/-Wno-error=shadow-uncaptured-local/' src/CMakeLists.txt
sed -i -e 's/-Werror=conversion/-Wno-error=conversion/' src/input_common/CMakeLists.txt

%add_optflags -Wno-error=conversion -I%_includedir/SimpleIni -DXBYAK_STRICT_CHECK_MEM_REG_SIZE=0

export CC="clang"
export CXX="clang++"
export RANLIB="llvm-ranlib"
export AR="llvm-ar"
export NM="llvm-nm"
export LDFLAGS="-fuse-ld=lld $LDFLAGS"

%cmake \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DENABLE_QT6:BOOL=TRUE \
	-DENABLE_QT_TRANSLATION:BOOL=TRUE \
	-DYUZU_USE_EXTERNAL_SDL2:BOOL=FALSE \
	-DYUZU_USE_EXTERNAL_VULKAN_HEADERS:BOOL=FALSE \
	-DYUZU_USE_EXTERNAL_VULKAN_UTILITY_LIBRARIES:BOOL=FALSE \
	-DYUZU_ENABLE_LTO:BOOL=TRUE \
	-DYUZU_TESTS:BOOL=TRUE \
	-DSIRIT_USE_SYSTEM_SPIRV_HEADERS:BOOL=TRUE \
	-DLLVM_DIR:PATH=$(llvm-config --cmakedir) \
	-DTZDB2NX_ZONEINFO_DIR:PATH=%_datadir/zoneinfo \
	-DTZDB2NX_VERSION:STRING=$(stat -c '%y' /usr/share/zoneinfo/tzdata.zi | sed 's/\(....-..-..\).*/\1/' | tr -dc '[:digit:]') \
	-GNinja \
	-Wno-dev
%cmake_build

%install
%cmake_install

%check
%ctest || :

%files
%doc CONTRIBUTING.md README.md
%_bindir/%name
%_bindir/%name-cmd
%_bindir/%name-room
%_desktopdir/org.%{name}_emu.%name.desktop
%_datadir/metainfo/org.%{name}_emu.%name.metainfo.xml
%_datadir/mime/packages/org.%{name}_emu.%name.xml
%_iconsdir/hicolor/scalable/apps/org.%{name}_emu.%name.svg

%changelog
* Thu Aug 21 2025 Nazarov Denis <nenderus@altlinux.org> 1734-alt7
- Add optflag -DXBYAK_STRICT_CHECK_MEM_REG_SIZE=0 (ALT #55675)

* Mon Aug 11 2025 Nazarov Denis <nenderus@altlinux.org> 1734-alt6
- Build on AArch64

* Sat Aug 09 2025 Nazarov Denis <nenderus@altlinux.org> 1734-alt5
- Build tests
- Build tzdb_to_nx

* Wed Aug 06 2025 Nazarov Denis <nenderus@altlinux.org> 1734-alt4
- Build with latest LLVM
- Build with system httplib
- Build without mcl
- Build with system SimpleIni
- Build with system Mbed TLS

* Mon Aug 04 2025 Nazarov Denis <nenderus@altlinux.org> 1734-alt3
- Build with dynarmic 6.7

* Fri Dec 13 2024 Nazarov Denis <nenderus@altlinux.org> 1734-alt2.1
- Fix FTBFS

* Sat Mar 09 2024 Nazarov Denis <nenderus@altlinux.org> 1734-alt2
- Remove vulkan version patch

* Fri Mar 08 2024 Nazarov Denis <nenderus@altlinux.org> 1734-alt1
- Version 1734

* Thu Feb 08 2024 Nazarov Denis <nenderus@altlinux.org> 1563-alt1.1
- Fix FTBFS

* Tue Sep 19 2023 Nazarov Denis <nenderus@altlinux.org> 1563-alt1
- Version 1563

* Sun Sep 10 2023 Nazarov Denis <nenderus@altlinux.org> 1553-alt1
- Version 1553

* Thu Sep 07 2023 Nazarov Denis <nenderus@altlinux.org> 1550-alt1
- Version 1550

* Tue Sep 05 2023 Nazarov Denis <nenderus@altlinux.org> 1546-alt1
- Version 1546 (ALT #47009)

* Mon Sep 04 2023 Nazarov Denis <nenderus@altlinux.org> 1487-alt1
- Version 1487

* Thu Jul 27 2023 Nazarov Denis <nenderus@altlinux.org> 1452-alt3.1
- Fix FTBFS

* Wed May 31 2023 Nazarov Denis <nenderus@altlinux.org> 1452-alt3
- Build with Clang

* Tue May 30 2023 Nazarov Denis <nenderus@altlinux.org> 1452-alt2
- Build on AArch64
- Enable link-time optimization

* Tue May 30 2023 Nazarov Denis <nenderus@altlinux.org> 1452-alt1
- Version 1452

* Sun May 28 2023 Nazarov Denis <nenderus@altlinux.org> 1448-alt1
- Version 1448

* Thu Apr 13 2023 Nazarov Denis <nenderus@altlinux.org> 1139-alt1.1
- Add zstd patch

* Sun Aug 21 2022 Nazarov Denis <nenderus@altlinux.org> 1139-alt1
- Version 1139

* Thu Jun 02 2022 Nazarov Denis <nenderus@altlinux.org> 1040-alt1
- Version 1040

* Mon Jan 10 2022 Nazarov Denis <nenderus@altlinux.org> 875-alt1
- Version 875

* Wed Jan 05 2022 Nazarov Denis <nenderus@altlinux.org> 869-alt1
- Version 869

* Tue Jan 04 2022 Nazarov Denis <nenderus@altlinux.org> 868-alt1
- Version 868

* Sat Nov 06 2021 Nazarov Denis <nenderus@altlinux.org> 801-alt1
- Version 801

* Sat Nov 06 2021 Nazarov Denis <nenderus@altlinux.org> 800-alt1
- Version 800

* Mon May 31 2021 Arseny Maslennikov <arseny@altlinux.org> 620-alt1.1
- NMU: spec: adapted to new cmake macros.

* Thu May 13 2021 Nazarov Denis <nenderus@altlinux.org> 620-alt1
- Version 620

* Fri Mar 19 2021 Nazarov Denis <nenderus@altlinux.org> 567-alt1
- Version 567

* Thu Mar 11 2021 Nazarov Denis <nenderus@altlinux.org> 0.559-alt3
- Enable translations

* Thu Mar 11 2021 Nazarov Denis <nenderus@altlinux.org> 0.559-alt2
- Enforce package versioning in GUI

* Wed Mar 10 2021 Nazarov Denis <nenderus@altlinux.org> 0.559-alt1
- Initial build for ALT Linux
