%define git_date 2025-11-06
%define git_commit d0c3bd6491f07d11b5b6a334ed540b57d767d1c2

# git rev-list --count %git_commit
%define app_ver 151
# git rev-parse --short=7 %git_commit
%define git_descr d0c3bd6

%define vulkan_headers_version 1.4.329
%define json_commit 54be9b04f0ec65d0bcfe0da54e7f01ea86fbfc3e
%define volk_commit e51c647181c7a8101454e69446079bc34100a320

Name: shadps4-qtlauncher
Version: %app_ver
Release: alt1

Summary: Sony PlayStation 4 emulator (Qt GUI)
License: GPL-2.0
Group: Emulators

Url: http://shadps4.net/
Vcs: https://github.com/shadps4-emu/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64

# https://github.com/shadps4-emu/%name/archive/shadPS4QtLauncher-%git_date-%git_commit/%name-shadPS4QtLauncher-%git_date-%git_commit.tar.gz
Source0: %name-shadPS4QtLauncher-%git_date-%git_commit.tar
# https://github.com/KhronosGroup/Vulkan-Headers/archive/v%vulkan_headers_version/Vulkan-Headers-%vulkan_headers_version.tar.gz
Source1: Vulkan-Headers-%vulkan_headers_version.tar
# https://github.com/nlohmann/json/archive/%json_commit/json-%json_commit.tar.gz
Source2: json-%json_commit.tar
# https://github.com/zeux/volk/archive/%volk_commit/volk-%volk_commit.tar.gz
Source3: volk-%volk_commit.tar

Provides: shadps4-qt = %EVR
Obsoletes: shadps4-qt <= 0.2.0-alt1

BuildRequires: alt-os-release
BuildRequires: clang
BuildRequires: glslang
BuildRequires: libGLU-devel
BuildRequires: libSDL3-devel
BuildRequires: libfmt-devel
BuildRequires: libpugixml-devel
BuildRequires: libtoml11-devel
BuildRequires: lld
BuildRequires: llvm
BuildRequires: qt6-multimedia-devel
BuildRequires: qt6-tools-devel

%description
QtLauncher is the official launcher for shadPS4.

%prep
%setup -n %name-shadPS4QtLauncher-%git_date-%git_commit -b 1 -b 2 -b 3

%__mv -Tf ../Vulkan-Headers-%vulkan_headers_version externals/vulkan-headers
%__mv -Tf ../json-%json_commit externals/json
%__mv -Tf ../volk-%volk_commit externals/volk

# Enforce package versioning in GUI
sed -i \
-e 's|@APP_VERSION@|%app_ver|g' \
-e 's|@GIT_BRANCH@|main|g' \
-e 's|@GIT_DESC@|%git_descr|g' \
src/common/scm_rev.cpp.in

%build
export CC="clang"
export CXX="clang++"
export RANLIB="llvm-ranlib"
export AR="llvm-ar"
export NM="llvm-nm"
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
export LANG=C.UTF-8

%cmake \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DENABLE_UPDATER:BOOL=FALSE \
	-GNinja \
	-Wno-dev
%cmake_build

%install
%cmake_install

%__mkdir_p %buildroot%_libexecdir/%name

%__mv %buildroot%_bindir/shadPS4QtLauncher %buildroot%_libexecdir/%name/
%__ln_s -r %buildroot%_libexecdir/%name/shadPS4QtLauncher %buildroot%_bindir/shadPS4QtLauncher
%__cp -r %_target_platform/translations %buildroot%_libexecdir/%name

%files
%doc CONTRIBUTING.md README.md
%_bindir/shadPS4QtLauncher
%_datadir/metainfo/net.shadps4.shadPS4.metainfo.xml
%_desktopdir/net.shadps4.shadPS4.desktop
%_iconsdir/hicolor/512x512/apps/net.shadps4.shadPS4.png
%_iconsdir/hicolor/scalable/apps/net.shadps4.shadPS4.svg
%_libexecdir/%name

%changelog
* Sat Nov 08 2025 Nazarov Denis <nenderus@altlinux.org> 151-alt1
- Initial build for ALT Linux
