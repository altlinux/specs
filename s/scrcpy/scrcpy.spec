# Switch which helps to rebuild server jar with
# nonfree Android SDK.  Don't forget to enable
# newtwork sharing in hasher-priv.
%def_disable build_server

Name: scrcpy
Version: 2.3.1
Release: alt1
Summary: Display and control your Android device screen
License: Apache-2.0
Group: Networking/Remote access
Url: https://github.com/Genymobile/scrcpy
# Repacked: https://github.com/Genymobile/scrcpy/archive/v%version/%name-%version.tar.gz
Source0: %name-%version.tar

# Prebuilt .jar with --enable build_server .
Source1: scrcpy-server.jar

%if_enabled build_server
# Android SDK is not free and its license doesn't permit redistribution.
# If you want to (re)build the server application download it here:
# https://developer.android.com/studio#downloads
# SHA256 (commandlinetools-linux-10406996_latest.zip) = 8919e8752979db73d8321e9babe2caedcc393750817c1a5f56c128ec442fb540
Source2: commandlinetools-linux-10406996_latest.zip

BuildPreReq: java-devel unzip
%endif

BuildRequires(pre): meson
# Automatically added by buildreq on Tue Jul 18 2023
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libavcodec-devel libavformat-devel libavutil-devel libcairo-gobject libcdio-paranoia libdc1394-22 libgdk-pixbuf libgpg-error libopencore-amrnb0 libopencore-amrwb0 libp11-kit librabbitmq-c4 libraw1394-11 libx265-199 ninja-build pkg-config python3 python3-base sh4 xz
BuildRequires: libSDL2-devel libavdevice-devel libswresample-devel libusb-devel meson python2-base

Requires: android-tools

%description
This application provides display and control of Android devices connected to
USB (or over TCP/IP).  It does not require any root access.

%prep
%setup
%if_enabled build_server
mkdir -p android-sdk
cd android-sdk
unzip %SOURCE2
%endif

%build
%if_enabled build_server
export ANDROID_SDK_ROOT="$PWD"/android-sdk
yes | "$ANDROID_SDK_ROOT"/cmdline-tools/bin/sdkmanager --sdk_root="$ANDROID_SDK_ROOT" --licenses
%else
set -- -Dprebuilt_server=%SOURCE1
%endif

%meson \
	"$@" \
	#
%meson_build

%install
%if_enabled build_server
export ANDROID_SDK_ROOT=$PWD/android-sdk
%endif
%meson_install

rm %buildroot%_desktopdir/*.desktop

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%files
%doc README.md FAQ.md LICENSE
%_bindir/scrcpy
%_man1dir/scrcpy.1.*
%_datadir/scrcpy

%_iconsdir/hicolor/256x256/apps/scrcpy.png
%_datadir/zsh/site-functions/_scrcpy
%_datadir/bash-completion/completions/scrcpy

%changelog
* Wed Dec 20 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.3.1-alt1
- Updated to v2.3.1.

* Tue Jul 18 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.1.1-alt1
- Updated to v2.1.1.

* Thu Jan 20 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.21-alt1
- Updated to v1.21.

* Tue Sep 14 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.19-alt1
- Updated to v1.19.

* Mon Oct 12 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.16-alt1
- Updated to v1.16.
- Fixed package summary and description.

* Fri May 29 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.14-alt1
- Initial build.
