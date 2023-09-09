%define optflags_lto -flto=thin
%define llvm_version 17.0

# git describe mainline-0-%version
%define git_descr mainline-636-12601-g84f0a23ff11

%define sirit_commit ab75463999f4f3291976b079d42d52ee91eebf3f
%define mbedtls_commit 8c88150ca139e06aa2aae8349df8292a88148ea1
%define tzdb_to_nx_date 220816

Name: yuzu
Version: 1553
Release: alt1

Summary: Nintendo Switch emulator/debugger
License: GPLv3+
Group: Emulators

Url: https://%name-emu.org/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): libavfilter-devel

# https://github.com/%name-emu/%name-mainline/archive/mainline-0-%version/%name-mainline-mainline-0-%version.tar.gz
Source0: %name-mainline-mainline-0-%version.tar
# https://github.com/ReinUsesLisp/sirit/archive/%sirit_commit/sirit-%sirit_commit.tar.gz
Source1: sirit-%sirit_commit.tar
# https://github.com/yuzu-emu/mbedtls/archive/%mbedtls_commit/mbedtls-%mbedtls_commit.tar.gz
Source2: mbedtls-%mbedtls_commit.tar

Source3: https://github.com/lat9nq/tzdb_to_nx/releases/download/%tzdb_to_nx_date/%tzdb_to_nx_date.zip

Patch0: %name-cpp-jwt-version-alt.patch
Patch1: %name-vulkan-version-alt.patch

BuildRequires: /proc
BuildRequires: boost-asio-devel
BuildRequires: boost-filesystem-devel
BuildRequires: catch-devel
BuildRequires: clang-tools
BuildRequires: clang%llvm_version
BuildRequires: glslang
BuildRequires: libSDL2-devel
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
BuildRequires: libinih-devel
BuildRequires: liblz4-devel
BuildRequires: libopus-devel
BuildRequires: libpolly%llvm_version-devel
BuildRequires: libswscale-devel
BuildRequires: libusb-devel
BuildRequires: libvulkan-memory-allocator-devel
BuildRequires: libxml2-devel
BuildRequires: libzstd-devel
BuildRequires: lld%llvm_version
BuildRequires: llvm%llvm_version-devel
BuildRequires: llvm%llvm_version-gold
BuildRequires: mlir%llvm_version-tools
BuildRequires: ninja-build
BuildRequires: nlohmann-json-devel
BuildRequires: python-modules-encodings
BuildRequires: python3-dev
BuildRequires: python3-module-mpl_toolkits
BuildRequires: qt6-tools-devel
BuildRequires: spirv-headers
BuildRequires: zlib-devel

%description
%name is an open source Nintendo Switch emulator/debugger.

%prep
%setup -n %name-mainline-mainline-0-%version -b 1 -b 2

%patch0 -p1
%patch1 -p1

%__mv -Tf ../sirit-%sirit_commit externals/sirit
%__mv -Tf ../mbedtls-%mbedtls_commit externals/mbedtls

# Enforce package versioning in GUI
sed -i \
-e 's|@GIT_BRANCH@|HEAD|g' \
-e 's|@GIT_DESC@|%git_descr|g' \
-e 's|@TITLE_BAR_FORMAT_IDLE@|%name %version|g' \
-e 's|@TITLE_BAR_FORMAT_RUNNING@|%name %version|g' \
src/common/scm_rev.cpp.in

%__rm .gitmodules

%build
export ALTWRAP_LLVM_VERSION=%llvm_version

sed -i -e 's/-Werror=shadow-uncaptured-local/-Wno-error=shadow-uncaptured-local/' src/CMakeLists.txt

%__mkdir_p %_target_platform/externals/nx_tzdb
%__cp %SOURCE3 %_target_platform/externals/nx_tzdb

%cmake \
	-DCMAKE_C_COMPILER:STRING=clang \
	-DCMAKE_CXX_COMPILER:STRING=clang++ \
	-DCMAKE_RANLIB:PATH=%_bindir/llvm-ranlib \
	-DCMAKE_AR:PATH=%_bindir/llvm-ar \
	-DCMAKE_NM:PATH=%_bindir/llvm-nm \
	-DCMAKE_EXE_LINKER_FLAGS:STRING="-fuse-ld=lld" \
	-DENABLE_QT6:BOOL=TRUE \
	-DENABLE_QT_TRANSLATION:BOOL=TRUE \
	-DYUZU_USE_EXTERNAL_SDL2:BOOL=FALSE \
	-DYUZU_USE_EXTERNAL_VULKAN_HEADERS:BOOL=FALSE \
	-DYUZU_ENABLE_LTO:BOOL=TRUE \
	-DYUZU_DOWNLOAD_TIME_ZONE_DATA:BOOL=TRUE \
	-DSIRIT_USE_SYSTEM_SPIRV_HEADERS:BOOL=TRUE \
	-DLLVM_DIR:PATH=%_libexecdir/llvm-%llvm_version/%_lib/cmake/llvm \
	-GNinja \
	-Wno-dev
%cmake_build

%install
%cmake_install

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
