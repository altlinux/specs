# other variant: Debug
%define buildmode Release
# build with ffmpeg or libav (not yet supported)
%def_without ffmpeg

Name: tdesktop
Version: 0.10.19
Release: alt3

Summary: Telegram is a messaging app with a focus on speed and security
License: %gpl3only
Group: Networking/Instant messaging
Url: https://telegram.org/

# Source-url: https://github.com/telegramdesktop/tdesktop/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses rpm-macros-qt5 rpm-macros-cmake
BuildRequires(pre): rpm-macros-kde-common-devel

BuildRequires: gcc-c++ libstdc++-devel gyp cmake

BuildRequires: qt5-base-devel libqt5-network libqt5-gui qt5-imageformats
# for -lQt5PlatformSupport
BuildRequires: qt5-base-devel-static

BuildRequires: liblzma-devel libz3-devel libzip-devel libpcre-devel libexpat-devel libssl-devel bison
BuildRequires: libexif-devel libopus-devel libportaudio2-devel
BuildRequires: libxkbcommon-devel libxkbcommon-x11-devel libxcb-devel libappindicator-devel
BuildRequires: libXi-devel libSM-devel libICE-devel libdbus-devel libXfixes-devel
BuildRequires: libwebp-devel libva-devel libdrm-devel

BuildRequires: libopenal-devel >= 1.17.2

# FIXME: libva need only for linking, extra deps?

# QtAV has AVCompat.h header
BuildRequires: libqtav-devel

%if_with ffmpeg
%add_optflags -DQTAV_HAVE_SWRESAMPLE=1
BuildRequires: ffmpeg-devel
%else
# build with libav, not ffpeg
%add_optflags -DQTAV_HAVE_AVRESAMPLE=1
BuildRequires: libavcodec-devel libavresample-devel libavformat-devel libswscale-devel libavutil-devel
%endif

Requires: dbus

# some problems with t_assert
%add_optflags -fpermissive

# disable some warnings
%add_optflags -Wno-strict-aliasing


%description
Telegram is a messaging app with a focus on speed and security, it's super-fast, simple and free.
You can use Telegram on all your devices at the same time - your messages
sync seamlessly across any number of your phones, tablets or computers.

With Telegram, you can send messages, photos, videos and files of any type (doc, zip, mp3, etc),
as well as create groups for up to 1000 people or channels for broadcasting to unlimited audiences.
You can write to your phone contacts and find people by their usernames.
As a result, Telegram is like SMS and email combined - and can take care of all your personal
or business messaging needs.

Workround for error cannot register existing type 'GdkDisplayManager':
$ XDG_CURRENT_DESKTOP=NONE tdesktop

%prep
%setup
#patch1 -p1

%build
cd Telegram/gyp

# Note! real build instructions are only in .travis/build.sh
# TDESKTOP_DISABLE_CRASH_REPORTS disables BreakPad require
gyp -Dtravis_defines=TDESKTOP_DISABLE_CRASH_REPORTS,TDESKTOP_DISABLE_AUTOUPDATE,TDESKTOP_DISABLE_UNITY_INTEGRATION \
	-Dlinux_lib_ssl=-lssl \
	-Dlinux_lib_crypto=-lcrypto \
	-Dlinux_path_qt=%_qt5_datadir \
	--no-parallel \
	--check --depth=. --generator-output=../.. -Goutput_dir=out Telegram.gyp --format=cmake
# FIXME: --no-parallel due gyp related /dev/shm hasher issue:
#    sl = self._semlock = _multiprocessing.SemLock(kind, value, maxvalue)
#OSError: [Errno 38] Function not implemented

cd - && cd out/%buildmode

# Hack part

%if_without ffmpeg
%__subst "s|libswresample|libavresample|g" CMakeLists.txt
%endif

# drop plugin static linking
for i in qxcb qconnmanbearer qgenericbearer qnmbearer qwebp ; do
    %__subst "s|\"lib$i.a\"||g" CMakeLists.txt
done

# only dynamic linking
%__subst "s|lib\([a-zA-Z0-9-]*\)\.a|\1|g" CMakeLists.txt
%__subst "s|-static-libstdc++||g" CMakeLists.txt
# TODO: Telegram/gyp/settings_linux.gypi
%__subst "s|;QT_STATICPLUGIN||g" CMakeLists.txt

# disable BreakPad here too
%__subst "s|\"breakpad_client\"||g" CMakeLists.txt
# drop strange fcitx plugin
%__subst "s|\"fcitxplatforminputcontextplugin\"||g" CMakeLists.txt

# TODO configure, build static or dynamic xcb and xkb
#	-Dlinux_path_xkbcommon=%_libdir
%__subst "s|\"/usr/local/lib/|\"|g" CMakeLists.txt
%__subst "s|\"/usr/lib/|\"|g" CMakeLists.txt
%__subst "s|xcb-static|xcb|g" CMakeLists.txt

# TODO: need we have Qt built with it?
%__subst "s|qtpcre|pcre|g" CMakeLists.txt
%__subst "s|qtharfbuzzng|harfbuzz|g" CMakeLists.txt

# due   The CMAKE_ASM_COMPILER:    gcc  is not a full path and was not found in the PATH.
export ASM="gcc"
%cmake_insource
# Note: make VERBOSE=1 if needed
# double make due RCC Parse Error: '../Resources/telegram.qrc' Line: 1 Column: 0 [Premature end of document.]
%make_build || %make_build

%install
# XDG files
install -m644 -D lib/xdg/telegramdesktop.desktop %buildroot%_desktopdir/%name.desktop
install -m644 -D lib/xdg/tg.protocol %buildroot%_Kservices/tg.protocol
for i in 16 32 48 64 128 256; do
    install -m644 -D Telegram/Resources/art/icon$i.png %buildroot%_iconsdir/hicolor/${i}x${i}/apps/%name.png
done

cd out/%buildmode
#makeinstall_std
install -D Telegram %buildroot%_bindir/%name
ln -s %name %buildroot%_bindir/Telegram


%files
%_bindir/%name
%_bindir/Telegram
%_desktopdir/%name.desktop
%_Kservices/tg.protocol
%_iconsdir/hicolor/16x16/apps/%name.png
%_iconsdir/hicolor/32x32/apps/%name.png
%_iconsdir/hicolor/48x48/apps/%name.png
%_iconsdir/hicolor/64x64/apps/%name.png
%_iconsdir/hicolor/128x128/apps/%name.png
%_iconsdir/hicolor/256x256/apps/%name.png
#_man1dir/*
%doc README.md

%changelog
* Wed Dec 21 2016 Vitaly Lipatov <lav@altlinux.ru> 0.10.19-alt3
- add Belarusian Russian Ukrainian French Turkish Czech languages

* Mon Dec 19 2016 Vitaly Lipatov <lav@altlinux.ru> 0.10.19-alt2
- add desktop file, icons
- cleanup spec

* Sat Dec 17 2016 Vitaly Lipatov <lav@altlinux.ru> 0.10.19-alt1
- new version 0.10.19 (with rpmrb script)

* Sun Dec 20 2015 Hihin Ruslan <ruslandh@altlinux.ru> 0.9.15-alt1
- initial build for ALT Linux Sisyphus
