%ifarch x86_64
%define barch %_arch
%endif
%ifarch %ix86
%define barch x86
# due asm code in code/asm/snd_mixa.s
%set_verify_elf_method textrel=relaxed
%endif

Name: realrtcw
Version: 5.1
Release: alt1
Summary: RealRTCW is a community single-player overhaul project for Return to Castle Wolfenstein
License: GPL-3.0-only AND RTCW SP Additions
Group: Games/Arcade
Url: https://github.com/wolfetplayer/RealRTCW

Source0: %name-%version.tar
Source1: %name.desktop

Patch0: gcc14-compile-fix.patch
Patch1: fix-steam-typo.patch
Patch2: unbundle-zlib.patch

BuildRequires: gcc-c++
BuildRequires: pkg-config
BuildRequires: libSDL2-devel
BuildRequires: libcurl-devel
BuildRequires: libopenal-devel
BuildRequires: libfreetype-devel
BuildRequires: libopus-devel
BuildRequires: libvorbis-devel
BuildRequires: libopusfile-devel
BuildRequires: zlib-devel
BuildRequires: libminizip-devel
BuildRequires: libjpeg-devel

# TODO - need to check aarch64/ppc64le
ExclusiveArch: %ix86 x86_64

%description
RealRTCW is a community single-player overhaul project for Return to Castle
Wolfenstein based on the iortcw and rtcw-sp source code.

Features:
* All iortcw features including proper widescreen support
* Steam integration support using Steamshim by Ryan C. Gordon
* Support for 99%% of community made maps
* Expanded .weap files system from Enemy Territory
* Reworked difficulty levels
* Automatic AI attributes system
* Greatly expanded arsenal of weapons
* Overhauled recoil system
* Atmospheric effects support
* Foliage tech support
* Subtitles support
* New inventory items
* Increased engine limits
* Improved controller support
* Extended scripting functionality
* Custom BSPC and BSPCUI included in sdk folder
* A lot of bug fixes and QOL improvements

For full experience you also need files from
https://www.moddb.com/mods/realrtcw-realism-mod

Place "main" folder from the Wolfenstein installation to:
%_gamesdatadir/%name/
or
$HOME/.realrtcw/

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
CFLAGS="%optflags" \
USE_INTERNAL_LIBS=0 \
ARCH=%barch \
%make_build V=1

%install
mkdir -p %buildroot%_gamesbindir/
mkdir -p %buildroot%_gamesdatadir/%name
mkdir -p %buildroot%_libdir/%name/main
install -m 0755 build/release-linux-%barch/RealRTCW.%barch %buildroot%_gamesbindir/
cat > %buildroot%_gamesbindir/%name << EOF
cd %_libdir/%name
RealRTCW.%barch "$@"
cd -
EOF
chmod 755 %buildroot%_gamesbindir/%name
install -m 0644 build/release-linux-%barch/renderer_sp_opengl1_*.so %buildroot%_libdir/%name/
install -m 0644 build/release-linux-%barch/main/*.so %buildroot%_libdir/%name/main

# install menu entry
mkdir -p %buildroot%_desktopdir
install -m 0644 %SOURCE1 %buildroot%_desktopdir/

# install menu icons
mkdir -p %buildroot%_iconsdir/hicolor/scalable/apps
install -m 0644 misc/wolf.svg %buildroot%_iconsdir/hicolor/scalable/apps/

%files
%doc COPYING.txt README* rend2-readme.md voip-readme.txt
%_gamesbindir/*
%_gamesdatadir/%name
%_libdir/%name
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*.svg

%changelog
* Thu Feb 27 2025 L.A. Kostis <lakostis@altlinux.ru> 5.1-alt1
- Initial build for ALTLinux.

