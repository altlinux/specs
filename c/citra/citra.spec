# git describe --always upstream/citra
%define git_desc 19617f7edb

Name: citra
Version: 1724
Release: alt1

Summary: Nintendo 3DS emulator
License: GPLv2
Group: Emulators

Url: https://%name-emu.org/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64 aarch64

# https://github.com/%name-emu/%name-nightly/archive/nightly-%version/%name-nightly-nightly-%version.tar.gz
Source0: %name-nightly-nightly-%version.tar
# https://github.com/citra-emu/ext-boost.git
Source1: boost.tar
# https://github.com/neobrain/nihstro.git
Source2: nihstro.tar
# https://github.com/citra-emu/ext-soundtouch.git
Source3: soundtouch.tar
# https://github.com/philsquared/Catch.git
Source4: catch.tar
# https://github.com/citra-emu/dynarmic.git
Source5: dynarmic.tar
# https://github.com/herumi/xbyak.git
Source6: xbyak.tar
# https://github.com/weidai11/cryptopp.git
Source7: cryptopp.tar
# https://github.com/fmtlib/fmt.git
Source8: fmt.tar
# https://github.com/lsalzman/enet.git
Source9: enet.tar
# https://github.com/benhoyt/inih.git
Source10: inih.tar
# https://github.com/citra-emu/ext-libressl-portable.git
Source11: libressl.tar
# https://github.com/libusb/libusb.git
Source12: libusb.tar
# https://github.com/kinetiknz/cubeb.git
Source13: cubeb.tar
# https://github.com/discordapp/discord-rpc.git
Source14: discord-rpc.tar
# https://github.com/arun11299/cpp-jwt.git
Source15: cpp-jwt.tar
# https://github.com/wwylele/teakra.git
Source16: teakra.tar
# https://github.com/lvandeve/lodepng.git
Source17: lodepng.tar
# https://github.com/facebook/zstd.git
Source18: zstd.tar
# https://github.com/arsenm/sanitizers-cmake.git
Source19: sanitizers-cmake.tar

BuildRequires: boost-asio-devel
BuildRequires: ctest
BuildRequires: doxygen
BuildRequires: git-core
BuildRequires: graphviz
BuildRequires: libSDL2-devel
BuildRequires: libavformat-devel
BuildRequires: libswresample-devel
BuildRequires: libswscale-devel
BuildRequires: libusb-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-tools-devel

%description
Citra is an open-source Nintendo 3DS emulator and debugger, written with portability in mind.

%prep
%setup -n %name-nightly-nightly-%version -b 1 -b 2 -b 3 -b 4 -b 5 -b 6 -b 7 -b 8 -b 9 -b 10 -b 11 -b 12 -b 13 -b 14 -b 15 -b 16 -b 17 -b 18 -b 19

%__mv -Tf ../boost externals/boost
%__mv -Tf ../nihstro externals/nihstro
%__mv -Tf ../soundtouch externals/soundtouch
%__mv -Tf ../catch externals/catch
%__mv -Tf ../dynarmic externals/dynarmic
%__mv -Tf ../xbyak externals/xbyak
%__mv -Tf ../cryptopp externals/cryptopp/cryptopp
%__mv -Tf ../fmt externals/fmt
%__mv -Tf ../enet externals/enet
%__mv -Tf ../inih externals/inih/inih
%__mv -Tf ../libressl externals/libressl
%__mv -Tf ../libusb externals/libusb/libusb
%__mv -Tf ../cubeb externals/cubeb
%__mv -Tf ../discord-rpc externals/discord-rpc
%__mv -Tf ../cpp-jwt externals/cpp-jwt
%__mv -Tf ../teakra externals/teakra
%__mv -Tf ../lodepng externals/lodepng/lodepng
%__mv -Tf ../zstd externals/zstd
%__mv -Tf ../sanitizers-cmake externals/cubeb/cmake/sanitizers-cmake

%__mkdir externals/boost/.git
%__mkdir externals/nihstro/.git
%__mkdir externals/soundtouch/.git
%__mkdir externals/catch/.git
%__mkdir externals/dynarmic/.git
%__mkdir externals/xbyak/.git
%__mkdir externals/cryptopp/cryptopp/.git
%__mkdir externals/fmt/.git
%__mkdir externals/enet/.git
%__mkdir externals/inih/inih/.git
%__mkdir externals/libressl/.git
%__mkdir externals/libusb/libusb/.git
%__mkdir externals/cubeb/.git
%__mkdir externals/discord-rpc/.git
%__mkdir externals/cpp-jwt/.git
%__mkdir externals/teakra/.git
%__mkdir externals/lodepng/lodepng/.git
%__mkdir externals/zstd/.git

# Enforce package versioning in GUI
sed -i \
-e 's|@GIT_BRANCH@|HEAD|g' \
-e 's|@GIT_DESC@|%git_desc|g' \
-e 's|@BUILD_FULLNAME@|Nightly %version|g' \
src/common/scm_rev.cpp.in

%build
%add_optflags -Wno-error=return-type

%cmake \
	-DENABLE_QT_TRANSLATION:BOOL=ON \
	-DENABLE_FFMPEG_AUDIO_DECODER:BOOL=ON \
	-DENABLE_FFMPEG_VIDEO_DUMPER:BOOL=ON \
	-DUSE_SYSTEM_BOOST:BOOL=TRUE \
	-Wno-dev

%cmake_build

%install
%cmakeinstall_std

%check
cd %_cmake__builddir
ctest

%files
%_bindir/%name
%_bindir/%name-qt
%_bindir/%name-room
%_desktopdir/%name.desktop
%_datadir/mime/packages/%name.xml
%_iconsdir/hicolor/scalable/apps/%name.svg
%_man6dir/%name.6*
%_man6dir/%name-qt.6*

%changelog
* Sat Sep 25 2021 Nazarov Denis <nenderus@altlinux.org> 1724-alt1
- Version Nightly 1724

* Sun May 02 2021 Arseny Maslennikov <arseny@altlinux.org> 1704-alt1.1
- NMU: spec: adapted to new cmake macros.

* Thu Apr 29 2021 Nazarov Denis <nenderus@altlinux.org> 1704-alt1
- Version Nightly 1704

* Sat Apr 24 2021 Nazarov Denis <nenderus@altlinux.org> 1703-alt1
- Version Nightly 1703

* Sat Apr 03 2021 Nazarov Denis <nenderus@altlinux.org> 1697-alt1
- Version Nightly 1697

* Fri Mar 19 2021 Nazarov Denis <nenderus@altlinux.org> 1696-alt1
- Initial build for ALT Linux
