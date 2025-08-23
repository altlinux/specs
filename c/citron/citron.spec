%define mbedtls_commit 8c88150ca139e06aa2aae8349df8292a88148ea1
%define sirit_commit ab75463999f4f3291976b079d42d52ee91eebf3f
%define tzdb_to_nx_commit 97929690234f2b4add36b33657fe3fe09bd57dfd

Name: citron
Version: 0.6.1
Release: alt1

Summary: Nintendo Homebrew Emulator
License: GPLv3+
Group: Emulators

Url: https://%name-emu.org/
Vcs: https://git.%name-emu.org/%name/emu
Packager: Nazarov Denis <nenderus@altlinux.org>

ExcludeArch: %ix86

Source0: https://git.%name-emu.org/%name/emu/-/archive/v%version-canary-refresh/emu-v%version-canary-refresh.tar
Source1: https://git.%name-emu.org/Citron/mbedtls/-/archive/%mbedtls_commit/mbedtls-%mbedtls_commit.tar
Source2: https://git.%name-emu.org/Citron/sirit//-/archive/%sirit_commit/sirit-%sirit_commit.tar
# https://github.com/lat9nq/tzdb_to_nx/archive/%tzdb_to_nx_commit/tzdb_to_nx-%tzdb_to_nx_commit.tar.gz
Source3: tzdb_to_nx-%tzdb_to_nx_commit.tar

Patch0: %name-cmake-externals-alt.patch
Patch1: %name-dynarmic-6.7-alt.patch
Patch2: %name-simpleini-system-alt.patch
Patch3: %name-mcl-find-alt.patch

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
BuildRequires: libsimpleini-devel
BuildRequires: libstb-devel
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
BuildRequires: qt6-multimedia-devel
BuildRequires: qt6-tools-devel
BuildRequires: renderdoc-devel
BuildRequires: spirv-headers
BuildRequires: zlib-devel

%description
Citron, a cutting-edge Nintendo Homebrew emulator designed to deliver an optimized experience for playing your favorite games and exploring new ones. Citron is a high-performance and easy-to-use emulator, tailored for enthusiasts and developers alike.

Features

   - High Performance: Optimized for speed and smooth gameplay.
   - User-Friendly: Clean and intuitive interface.
   - Cross-Platform: Available on multiple platforms.
   - Homebrew Support: Fully supports legal homebrew games and applications.
   - Ongoing Development: Stay tuned for frequent updates as Citron evolves!

%prep
%setup -n emu-v%version-canary-refresh -b 1 -b 2 -b 3

%autopatch -p1

%__mv -Tf ../mbedtls-%mbedtls_commit externals/mbedtls
%__mv -Tf ../sirit-%sirit_commit externals/sirit
%__mv -Tf ../tzdb_to_nx-%tzdb_to_nx_commit externals/nx_tzdb/tzdb_to_nx

# Enforce package versioning in GUI
sed -i \
-e 's|@GIT_BRANCH@|HEAD|g' \
-e 's|@GIT_DESC@|v%version-canary-refresh|g' \
-e 's|@TITLE_BAR_FORMAT_IDLE@|%name %version|g' \
-e 's|@TITLE_BAR_FORMAT_RUNNING@|%name %version|g' \
src/common/scm_rev.cpp.in

%build
sed -i -e 's/-Werror=conversion/-Wno-error=conversion/' src/input_common/CMakeLists.txt

%add_optflags -I%_includedir/SimpleIni -DXBYAK_STRICT_CHECK_MEM_REG_SIZE=0

export CC="clang"
export CXX="clang++"
export RANLIB="llvm-ranlib"
export AR="llvm-ar"
export NM="llvm-nm"
export LDFLAGS="-fuse-ld=lld $LDFLAGS"

%cmake \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DENABLE_QT6:BOOL=ON \
	-DENABLE_QT_TRANSLATION:BOOL=ON \
	-DCITRON_USE_BUNDLED_QT:BOOL=OFF \
	-DUSE_SYSTEM_QT:BOOL=ON \
	-DCITRON_USE_EXTERNAL_SDL2:BOOL=OFF \
	-DCITRON_USE_BUNDLED_SDL2:BOOL=OFF \
	-DCITRON_USE_EXTERNAL_VULKAN_HEADERS:BOOL=OFF \
	-DCITRON_USE_EXTERNAL_VULKAN_UTILITY_LIBRARIES:BOOL=OFF \
	-DCITRON_USE_BUNDLED_FFMPEG:BOOL=OFF \
	-DCITRON_CHECK_SUBMODULES:BOOL=OFF \
	-DCITRON_ENABLE_LTO:BOOL=ON \
	-DCITRON_TESTS:BOOL=ON \
	-DSIRIT_USE_SYSTEM_SPIRV_HEADERS:BOOL=ON \
	-DTZDB2NX_ZONEINFO_DIR:PATH=%_datadir/zoneinfo \
	-DTZDB2NX_VERSION:STRING=$(stat -c '%y' %_datadir/zoneinfo/tzdata.zi | sed 's/\(....-..-..\).*/\1/' | tr -dc '[:digit:]') \
	-GNinja \
	-Wno-dev
%cmake_build

%install
%cmake_install

%check
%ctest || :

%files
%doc README.md
%_bindir/%name
%_bindir/%name-cmd
%_bindir/%name-room
%_desktopdir/org.%{name}_emu.%name.desktop
%_datadir/metainfo/org.%{name}_emu.%name.metainfo.xml
%_datadir/mime/packages/org.%{name}_emu.%name.xml
%_iconsdir/hicolor/scalable/apps/org.%{name}_emu.%name.svg

%changelog
* Sat Aug 23 2025 Nazarov Denis <nenderus@altlinux.org> 0.6.1-alt1
- Initial build for ALT Linux
