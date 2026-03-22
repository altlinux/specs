# git rev-parse --short=7 %version
%define git_descr e3cdadb

%define json_commit 54be9b04f0ec65d0bcfe0da54e7f01ea86fbfc3e
%define volk_commit e51c647181c7a8101454e69446079bc34100a320

Name: shadps4-qtlauncher
Version: 224
Release: alt1

Summary: Sony PlayStation 4 emulator (Qt GUI)
License: GPL-2.0
Group: Emulators

Url: http://shadps4.net/
Vcs: https://github.com/shadps4-emu/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64

# https://github.com/shadps4-emu/%name/archive/v%version/%name-%version.tar.gz
Source0: %name-%version.tar
# https://github.com/nlohmann/json/archive/%json_commit/json-%json_commit.tar.gz
Source1: json-%json_commit.tar
# https://github.com/zeux/volk/archive/%volk_commit/volk-%volk_commit.tar.gz
Source2: volk-%volk_commit.tar

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
%setup -b 1 -b 2

%__mv -Tf ../json-%json_commit externals/json
%__mv -Tf ../volk-%volk_commit externals/volk

# Enforce package versioning in GUI
sed -i \
-e 's|@APP_VERSION@|%version|g' \
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
%_datadir/metainfo/net.shadps4.%name.metainfo.xml
%_desktopdir/net.shadps4.%name.desktop
%_iconsdir/hicolor/512x512/apps/net.shadps4.shadPS4.png
%_iconsdir/hicolor/scalable/apps/net.shadps4.shadPS4.svg
%_libexecdir/%name

%changelog
* Sun Mar 22 2026 Nazarov Denis <nenderus@altlinux.org> 224-alt1
- Version 224

* Sat Nov 08 2025 Nazarov Denis <nenderus@altlinux.org> 151-alt1
- Initial build for ALT Linux
