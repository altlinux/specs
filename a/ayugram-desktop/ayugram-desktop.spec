# TODO: build external, json11 separately
# Check https://github.com/EasyCoding/tgbuild for patches

%define oname ayugram

%define ffmpeg_version 4.0
# minimum required
%define tg_qt6_version 6.6.2

# AppID for Basealt build
# check https://core.telegram.org/api/obtaining_api_id
# this id from https://github.com/AyuGram/AyuGramDesktop/blob/dev/docs/building-linux.md#building-the-project
%define apiid 2040
%define apihash b18441a1ff607e10a989891a5462e627

# TODO: def_with clang
%def_with wayland
%def_with x11
%def_with rlottie
%def_with gsl
%def_without system_fonts
%def_without ninja
%def_without ffmpeg_static
%def_with scudo

Name: ayugram-desktop
Version: 5.2.2
Release: alt1

Summary: Desktop Telegram client with good customization and Ghost mode

License: GPLv3 with OpenSSL exception
Group: Networking/Instant messaging
Url: https://github.com/AyuGram/AyuGramDesktop

# Source-git: https://github.com/AyuGram/AyuGramDesktop.git
Source: %name-%version.tar

Source1: %name-postsubmodules-%version.tar

# Source2-url: https://github.com/desktop-app/GSL/archive/refs/heads/main.zip
#Source2: %name-gsl-%version.tar

Patch1: telegram-desktop-remove-tgvoip.patch
Patch2: telegram-desktop-set-native-window-frame.patch
#Patch5: telegram-desktop-fix-missed-cstdint.patch
#Patch7: telegram-desktop-fix-build-with-make.patch
Patch8: telegram-desktop-use-external-gsl.patch
#Patch9: telegram-desktop-try-fix-circular-deps.patch
Patch20: telegram-desktop-fix-protoc.patch

# lacks few build deps, still
# [ppc64le] E: Couldn't find package libdispatch-devel
# [ppc64le] /usr/bin/ld.default: /usr/lib64/libtg_owt.a: error adding symbols: file in wrong format
ExcludeArch: ppc64le
# [aarch64] error: cpio archive too big - 4103M
ExcludeArch: aarch64

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-compat >= 2.1.5
BuildRequires(pre): rpm-build-intro >= 2.1.5
%if_with ninja
BuildRequires(pre): rpm-macros-ninja-build
%endif

# use no more than system_memory/3000 build procs (see https://bugzilla.altlinux.org/show_bug.cgi?id=35112)
%_tune_parallel_build_by_procsize 3000

# error: cpio archive too big - 4133M
%define optflags_debug -g0

# minimalize memory using
%ifarch %ix86 armh
%define optflags_debug -g0
%define optflags_lto %nil
%endif

BuildRequires: gcc-c++ libstdc++-devel
# for -lstdc++fs
BuildRequires: libstdc++%__gcc_version-devel-static

BuildRequires: python3

# cmake 3.16 as in CMakeLists.txt
BuildRequires: cmake >= 3.16
BuildRequires: extra-cmake-modules

BuildRequires(pre): rpm-macros-qt6
BuildRequires: qt6-base-devel >= %tg_qt6_version
BuildRequires: qt6-svg-devel qt6-svg
BuildRequires: qt6-charts-devel qt6-charts
BuildRequires: qt6-5compat-devel
BuildRequires: qt6-imageformats
# WebView support: Quick QuickWidgets WaylandCompositor
BuildRequires: qt6-declarative-devel
%{?_with_wayland:BuildRequires: qt6-wayland-devel qt6-wayland}
# needs for smiles and emojicons
Requires: qt6-imageformats

BuildRequires: libenchant2-devel
BuildRequires: libhunspell-devel

# for autoupdater (included ever if disabled)
# TODO:
BuildRequires: liblzma-devel

# for SourceFiles/mtproto/connection.cpp
BuildRequires: libzip-devel

BuildRequires: zlib-devel >= 1.2.8
BuildRequires: libxxhash-devel
BuildRequires: liblz4-devel
BuildRequires: libcrc32c-devel
BuildRequires: libfmt-devel

BuildRequires: libminizip-devel libpcre2-devel libexpat-devel libssl-devel libselinux-devel bison

%if_with x11
#BuildRequires: libxcbutil-keysyms-devel
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-record)
BuildRequires: pkgconfig(xcb-screensaver)
%endif

#BuildRequires: libgtk+3-devel
BuildRequires: libglibmm2.68-devel >= 2.77
BuildRequires: gobject-introspection-devel

BuildRequires: libopus-devel
# TODO:
# libdee-devel

#BuildRequires: libopenal-devel >= 1.22.2
# p10
BuildRequires: libopenal-devel >= 1.21.1
# libportaudio2-devel libxcb-devel
# used by qt imageformats: libwebp-devel
BuildRequires: libva-devel libdrm-devel

# Telegram fork of OWT
BuildRequires: libowt-tg-devel >= 4.3.0.11
BuildRequires: librnnoise-devel
#BuildRequires: libvpx-devel
BuildRequires: libjpeg-devel

# No rule to make target '/usr/lib64/libopenh264.so', needed by 'telegram-desktop'
BuildRequires: libopenh264-devel

# No rule to make target '/usr/lib64/libXcomposite.so', needed by 'telegram-desktop'
BuildRequires: libXcomposite-devel

# No rule to make target '/usr/lib64/libXdamage.so', needed by 'telegram-desktop'
BuildRequires: libXdamage-devel
BuildRequires: libXrandr-devel libXext-devel libXfixes-devel libXrender-devel libXtst-devel


#see hack below (used directly in Telegram/ThirdParty/tgcalls/tgcalls/desktop_capturer/DesktopCaptureSourceHelper.cpp)
BuildRequires: libyuv-devel

# Just to disable noise like Package 'libffi', required by 'gobject-2.0', not found
# See https://bugzilla.altlinux.org/30001
BuildRequires: libffi-devel libmount-devel libXdmcp-devel libblkid-devel
BuildRequires: bzlib-devel libbrotli-devel gstreamer1.0-devel

BuildRequires: boost-program_options-devel

# uses forked version, tag e0ea6af518345c4a46195c4951e023e621a9eb8f
BuildRequires: librlottie-devel >= 0.1.1
BuildRequires: libqrcodegen-cpp-devel

# C++ sugar
%if_with gsl
BuildRequires: libmicrosoft-gsl-devel >= 1:4.0.0-alt2
%endif

# https://github.com/telegramdesktop/tdesktop/issues/8471
#BuildRequires: libvariant-devel
BuildRequires: libexpected-devel
BuildRequires: librange-v3-devel >= 0.11.0
BuildRequires: libdispatch-devel

# for bundled cldr3
BuildRequires: libprotobuf-devel libprotobuf-lite-devel protobuf-compiler

# need for /usr/lib64/cmake/Qt5XkbCommonSupport/Qt5XkbCommonSupportConfig.cmake
BuildRequires: libxkbcommon-devel

%if_with ninja
BuildRequires: ninja-build
%endif

# FIXME: libva need only for linking, extra deps?

Provides: telegram = %version-%release
Provides: tdesktop = %version-%release
Obsoletes: tdesktop


%if_with ffmpeg_static
BuildRequires: libffmpeg-devel-static >= %ffmpeg_version
%else
BuildRequires: libavfilter-devel >= %ffmpeg_version
BuildRequires: libavcodec-devel >= %ffmpeg_version
BuildRequires: libavformat-devel >= %ffmpeg_version
BuildRequires: libavutil-devel >= %ffmpeg_version
BuildRequires: libswscale-devel >= %ffmpeg_version
BuildRequires: libswresample-devel >= %ffmpeg_version
%endif

# Use the same Qt version as built with
# See https://bugzilla.altlinux.org/49495
# https://git.altlinux.org/gears/t/telegram-desktop.git?a=blob;f=tdesktop/Telegram/lib_ui/ui/rp_widget.cpp;h=41b24bc5cd896aadd6fc6c35fadfa00f5f4f4b8b#l25
Requires: libqt6-core = %_qt6_version

Requires: dbus

# instead of internal fonts OpenSans
# works with system fonts, see https://bugzilla.altlinux.org/show_bug.cgi?id=38986
#Requires: fonts-ttf-open-sans

# some problems with t_assert
%add_optflags -fpermissive -DNDEBUG

# disable some warnings
%add_optflags -Wno-strict-aliasing -Wno-unused-variable -Wno-sign-compare -Wno-switch

%add_optflags -fstack-protector-all -fstack-clash-protection -D_GLIBCXX_ASSERTIONS
%ifarch x86_64
%add_optflags -fcf-protection
%endif


%description
AyuGram is a Telegram client with a very pleasant features. 

Telegram is a messaging app with a focus on speed and security, it's super-fast, simple and free.
You can use Telegram on all your devices at the same time - your messages
sync seamlessly across any number of your phones, tablets or computers.

AyuGram pretends to be an official application to Telegram.
If you look at the list of sessions, you'll see yourself using a regular Telegram rather than AyuGram.
Generally, developer ToS apply only to developers, by restricting their application keys.
But since we're using official ones, Telegram can't block our client.
And since it's applied only to developers,
they can't ban you, except if you're doing bad things that violate user ToS. 

We are not responsible for the possible blocking of your account. Use the client at your own risk.

%prep
%setup -a1
%patch1 -p2
%patch2 -p2
%patch20 -p1

%if_without gsl
test -d /usr/share/cmake/Microsoft.GSL/ && echo "External Microsoft GSL is incompatible with buggy libstd++ (see https://gcc.gnu.org/bugzilla/show_bug.cgi?id=106547), remove libmicrosoft-gsl-devel to correct build" && exit 1
%else
%patch8 -p2
%endif

#patch9 -p1

# See https://github.com/desktop-app/tg_owt/pull/82
# TODO: there are incorrect using and linking libyuv
subst 's|third_party/libyuv/include/libyuv.h|libyuv.h|' Telegram/ThirdParty/tgcalls/tgcalls/desktop_capturer/*.cpp
# TODO: ld: lib_webview/liblib_webview.a(webview_linux_webkit_gtk.cpp.o): undefined reference to symbol 'dlclose@@GLIBC_2.2.5
# TODO: ld: /tmp/.private/lav/ccfxvz2E.ltrans115.ltrans.o: неопределённая ссылка на символ «ARGBScale»
#subst "s|\(desktop-app::external_rnnoise\)|\1 -lyuv|" Telegram/cmake/lib_tgcalls.cmake

# Unbundling libraries...
# TODO: minizip
for i in \
%if_with gsl
	Telegram/ThirdParty/GSL \
%endif
	Telegram/ThirdParty/QR \
	Telegram/ThirdParty/expected \
	Telegram/ThirdParty/fcitx5-qt \
	Telegram/ThirdParty/hime \
	Telegram/ThirdParty/hunspell \
	Telegram/ThirdParty/lz4 \
	Telegram/ThirdParty/nimf \
	Telegram/ThirdParty/range-v3 \
	Telegram/ThirdParty/xxHash \
%if_with rlottie
	Telegram/ThirdParty/rlottie \
%endif
	Telegram/ThirdParty/libtgvoip \
%if 0
	Telegram/ThirdParty/tgcalls/tgcalls/legacy \
%endif
	%nil ; do
	echo "Removing $i ..."
	rm -r $i
done

%if_with rlottie
# really ALT's rlottie is forked rlottie from desktop-app
subst 's|#ifndef LOTTIE_USE_PACKAGED_RLOTTIE|#ifdef LOTTIE_USE_PACKAGED_RLOTTIE|' \
	Telegram/lib_lottie/lottie/lottie_icon.cpp \
	Telegram/lib_lottie/lottie/details/lottie_frame_provider_direct.cpp
%endif

# https://github.com/telegramdesktop/tdesktop/issues/26489#issuecomment-1627535022
sed -i -e 's/find_package(Protobuf REQUIRED)/find_package(Protobuf REQUIRED CONFIG)/' \
	Telegram/ThirdParty/cld3/CMakeLists.txt

%build
%if_with ffmpeg_static
export PKG_CONFIG_PATH=%_libdir/ffmpeg-static/%_lib/pkgconfig/
%endif

%if_with clang
%remove_optflags -frecord-gcc-switches
export CC=clang
%endif

# due precompiled headers
export CCACHE_SLOPPINESS=pch_defines,time_macros

# CMAKE_BUILD_TYPE should always be Release due to some hardcoded checks.
#    -DCMAKE_BUILD_TYPE=RelWithDebInfo \

%cmake \
%if_with ninja
    -G Ninja \
%endif
    -DCMAKE_BUILD_TYPE=Release \
    -DTDESKTOP_API_ID=%apiid \
    -DTDESKTOP_API_HASH=%apihash \
    -DDESKTOP_APP_USE_PACKAGED:BOOL=ON \
    -DDESKTOP_APP_DISABLE_AUTOUPDATE=ON \
%if_with system_fonts
    -DDESKTOP_APP_USE_PACKAGED_FONTS:BOOL=ON \
%else
    -DDESKTOP_APP_USE_PACKAGED_FONTS:BOOL=OFF \
%endif
    -DDESKTOP_APP_DISABLE_CRASH_REPORTS:BOOL=ON \
    -DDESKTOP_APP_DISABLE_SPELLCHECK:BOOL=OFF \
    -DQT_VERSION_MAJOR=6 \
%if_without scudo
    -DDESKTOP_APP_DISABLE_SCUDO=ON \
%endif
%if_with wayland
    -DDESKTOP_APP_DISABLE_WAYLAND_INTEGRATION:BOOL=OFF \
%else
    -DDESKTOP_APP_DISABLE_WAYLAND_INTEGRATION:BOOL=ON \
%endif
%if_with x11
    -DDESKTOP_APP_DISABLE_X11_INTEGRATION:BOOL=OFF \
%else
    -DDESKTOP_APP_DISABLE_X11_INTEGRATION:BOOL=ON \
%endif
%if_with rlottie
    -DDESKTOP_APP_USE_PACKAGED_RLOTTIE=ON \
# FIXME: lottie_cache.h:9:10: fatal error: ffmpeg/ffmpeg_utility.h: No such file or directory
#    -DDESKTOP_APP_LOTTIE_USE_CACHE:BOOL=OFF \
%else
    -DDESKTOP_APP_USE_PACKAGED_RLOTTIE=OFF \
%endif
    %nil

%if_with ninja
%ninja_build
%else
%cmake_build
%endif

%install
%if_with ninja
%ninja_install
%else
%cmakeinstall_std
%endif
# XDG files
#install -m644 -D lib/xdg/tg.protocol %buildroot%_Kservices/tg.protocol

#ln -s %name %buildroot%_bindir/Telegram
ln -s %name %buildroot%_bindir/%oname
#ln -s %name %buildroot%_bindir/%{oname}desktop

%files
%_bindir/%name
#%_bindir/telegramdesktop
#%_bindir/Telegram
%_bindir/%oname
%_desktopdir/com.%oname.desktop.desktop
%_datadir/dbus-1/services/*.service
%_datadir/metainfo/*.metainfo.xml
%_iconsdir/hicolor/16x16/apps/%oname.png
%_iconsdir/hicolor/32x32/apps/%oname.png
%_iconsdir/hicolor/48x48/apps/%oname.png
%_iconsdir/hicolor/64x64/apps/%oname.png
%_iconsdir/hicolor/128x128/apps/%oname.png
%_iconsdir/hicolor/256x256/apps/%oname.png
%_iconsdir/hicolor/512x512/apps/%oname.png
%_iconsdir/hicolor/symbolic/apps/%oname-symbolic.svg
#_man1dir/*
%doc README.md

%changelog
* Wed Jul 03 2024 Vitaly Lipatov <lav@altlinux.ru> 5.2.2-alt1
- new version 5.2.2 (with rpmrb script)
- disable debuginfo (error: cpio archive too big - 4133M)

* Wed Jun 05 2024 Vitaly Lipatov <lav@altlinux.ru> 5.1.2-alt1
- new version 5.1.2 (with rpmrb script)
- disabled build on aarch64 (cpio archive too big - 4103M)

* Wed May 08 2024 Vitaly Lipatov <lav@altlinux.ru> 4.16.8-alt1
- new version 4.16.8 (with rpmrb script)

* Thu Apr 04 2024 Vitaly Lipatov <lav@altlinux.ru> 4.16-alt1
- new version 4.16 (with rpmrb script)

* Thu Mar 28 2024 Vitaly Lipatov <lav@altlinux.ru> 4.15.2-alt1
- initial build for ALT Sisyphus
