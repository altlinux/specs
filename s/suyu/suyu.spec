%define optflags_lto -flto=thin
%define llvm_version 17.0

# git describe v%version --long
%define git_descr v0.0.4-0-g433bcabb72

%define sirit_commit ab75463999f4f3291976b079d42d52ee91eebf3f
%define mbedtls_commit 8c88150ca139e06aa2aae8349df8292a88148ea1
%define simpleini_version 4.20
%define tzdb_to_nx_date 221202

Name: suyu
Version: 0.0.4
Release: alt1
Epoch: 1

Summary: Fully open-source Switch emulator
License: GPLv3+
Group: Emulators

Url: https://%name.dev/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64

BuildRequires(pre): libavfilter-devel

# https://git.%name.dev/%name/%name/archive/v%version.tar.gz
Source0: %name-v%version.tar
# https://github.com/ReinUsesLisp/sirit/archive/%sirit_commit/sirit-%sirit_commit.tar.gz
Source1: sirit-%sirit_commit.tar
# https://github.com/yuzu-emu/mbedtls/archive/%mbedtls_commit/mbedtls-%mbedtls_commit.tar.gz
Source2: mbedtls-%mbedtls_commit.tar
# https://github.com/brofield/simpleini/archive/v%simpleini_version/simpleini-%simpleini_version.tar.gz
Source3: simpleini-%simpleini_version.tar

Source4: https://github.com/lat9nq/tzdb_to_nx/releases/download/%tzdb_to_nx_date/%tzdb_to_nx_date.zip

Patch0: %name-cpp-jwt-version-alt.patch
Patch1: %name-cmake-externals-alt.patch

BuildRequires: /proc
BuildRequires: boost-asio-devel
BuildRequires: boost-filesystem-devel
BuildRequires: catch-devel
BuildRequires: clang%llvm_version
BuildRequires: clang%llvm_version-tools
BuildRequires: ctest
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
BuildRequires: libopus-devel
BuildRequires: libstb-devel
BuildRequires: libswscale-devel
BuildRequires: libusb-devel
BuildRequires: libvulkan-memory-allocator-devel
BuildRequires: libxml2-devel
BuildRequires: libzstd-devel
BuildRequires: lld%llvm_version
BuildRequires: llvm%llvm_version-devel
BuildRequires: llvm%llvm_version-gold
BuildRequires: ninja-build
BuildRequires: nlohmann-json-devel
BuildRequires: python-modules-encodings
BuildRequires: python3-dev
BuildRequires: python3-module-mpl_toolkits
BuildRequires: qt6-tools-devel
BuildRequires: renderdoc-devel
BuildRequires: spirv-headers
BuildRequires: unzip
BuildRequires: zlib-devel

%description
%name is a familiar C++ based Switch emulator with a focus on compatibility. Completely free and open-source, forever.

%prep
%setup -n %name-v%version -b 1 -b 2 -b 3

%patch0 -p1
%patch1 -p1

%__mv -Tf ../sirit-%sirit_commit externals/sirit
%__mv -Tf ../mbedtls-%mbedtls_commit externals/mbedtls
%__mv -Tf ../simpleini-%simpleini_version externals/simpleini

# Enforce package versioning in GUI
sed -i \
-e 's|@GIT_BRANCH@|dev|g' \
-e 's|@GIT_DESC@|%git_descr|g' \
src/common/scm_rev.cpp.in

%build
export ALTWRAP_LLVM_VERSION=%llvm_version

%__mkdir_p %_target_platform/externals/nx_tzdb/nx_tzdb
unzip %SOURCE4 -d %_target_platform/externals/nx_tzdb/nx_tzdb

%cmake \
	-DCMAKE_C_COMPILER:STRING=clang \
	-DCMAKE_CXX_COMPILER:STRING=clang++ \
	-DCMAKE_RANLIB:PATH=%_bindir/llvm-ranlib \
	-DCMAKE_AR:PATH=%_bindir/llvm-ar \
	-DCMAKE_NM:PATH=%_bindir/llvm-nm \
	-DCMAKE_EXE_LINKER_FLAGS:STRING="-fuse-ld=lld" \
	-DENABLE_QT6:BOOL=TRUE \
	-DENABLE_QT_TRANSLATION:BOOL=TRUE \
	-DSUYU_USE_EXTERNAL_SDL2:BOOL=FALSE \
	-DSUYU_USE_EXTERNAL_VULKAN_HEADERS:BOOL=FALSE \
	-DSUYU_USE_EXTERNAL_VULKAN_UTILITY_LIBRARIES:BOOL=FALSE \
	-DSUYU_TESTS:BOOL=TRUE \
	-DSUYU_USE_PRECOMPILED_HEADERS:BOOL=FALSE \
	-DSUYU_CHECK_SUBMODULES:BOOL=FALSE \
	-DSUYU_ENABLE_LTO:BOOL=TRUE \
	-DSIRIT_USE_SYSTEM_SPIRV_HEADERS:BOOL=TRUE \
	-DLLVM_DIR:PATH=$(llvm-config --cmakedir) \
	-GNinja \
	-Wno-dev
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc CONTRIBUTING.md README.md
%_bindir/%name
%_bindir/%name-cmd
%_bindir/%name-room
%_desktopdir/dev.%{name}_emu.%name.desktop
%_datadir/metainfo/dev.%{name}_emu.%name.metainfo.xml
%_datadir/mime/packages/dev.%{name}_emu.%name.xml
%_iconsdir/hicolor/scalable/apps/dev.%{name}_emu.%name.svg

%changelog
* Mon Jun 24 2024 Nazarov Denis <nenderus@altlinux.org> 1:0.0.4-alt1
- Version 0.0.4 (ALT #50715)

* Mon Mar 25 2024 Nazarov Denis <nenderus@altlinux.org> 1:0.0.1-alt1
- Version 0.0.1
  + upstream reset the versioning scheme
- Build with RenderDoc

* Thu Mar 21 2024 Nazarov Denis <nenderus@altlinux.org> 0.0.2-alt1
- Initial build for ALT Linux
