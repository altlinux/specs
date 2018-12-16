Name: retroshare
Version: 0.6.4
Release: alt5

Summary: Secure communication with friends

License: GPLv3
Group: Networking/File transfer
Url: http://retroshare.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/RetroShare/RetroShare/archive/v%version.tar.gz
Source: %name-%version.tar
# backported upstream patch from master
Patch100:retroshare-0.6.4-qt-5.11.patch
patch101:retroshare-0.6.4-gcc8.patch

# manually removed: ruby ruby-stdlibs selinux-policy i586-libxcb  python-module-google python-module-mwlib python3-dev python3-module-yieldfrom python3-module-zope
# Automatically added by buildreq on Tue Jan 03 2017
# optimized out: gcc-c++ glib2-devel libGL-devel libX11-devel libXScrnSaver-devel libavutil-devel libcom_err-devel libgnome-keyring libgpg-error libjson-c libkrb5-devel libp11-kit libqt5-core libqt5-gui libqt5-multimedia libqt5-network libqt5-printsupport libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxml2-devel qt5-base-devel qt5-declarative-devel qt5-script-devel qt5-tools-devel qt5-xmlpatterns-devel xorg-scrnsaverproto-devel xorg-xproto-devel zlib-devel
BuildRequires: bzlib-devel libavcodec-devel libcurl-devel libgnome-keyring-devel libmicrohttpd-devel libqtav-devel  libsqlcipher-devel libssl-devel libupnp-devel libxslt-devel
BuildRequires: qt5-connectivity-devel qt5-location-devel qt5-multimedia-devel qt5-phonon-devel qt5-quick1-devel qt5-sensors-devel qt5-serialport-devel qt5-svg-devel qt5-tools-devel-static qt5-wayland-devel qt5-webkit-devel qt5-websockets-devel qt5-x11extras-devel
BuildRequires: zlib-devel
# VOIP extension
BuildRequires: libspeex-devel libspeexdsp-devel libopencv-devel qt5-multimedia-devel
#libhighgui-dev - part of opencv


BuildRequires: gcc-c++ desktop-file-utils

Requires: %name-common = %version-%release

%description
RetroShare is a decentralized, private and secure commmunication
and sharing platform.
RetroShare provides filesharing, chat, messages, forums and channels.

Authors:
see http://retroshare.sourceforge.net/team.html

%package nogui
Summary: RetroShare cli client
Group: Networking/File transfer
Requires: %name-common = %version-%release

%description nogui
This is the command-line client for RetroShare network.
This client can be contacted and talked-to using SSL.
Clients exist for portable devices running e.g. Android.

%package common
Summary: RetroShare common files
Group: Networking/File transfer
BuildArch: noarch

%description common
This is the common files package for RetroShare network.

%package voip-plugin
Summary: RetroShare VOIP plugin
Group: Networking/File transfer
Requires: %name = %version-%release

%description voip-plugin
This package provides a plugin for RetroShare,
a secured Friend-to-Friend communication platform.
The plugin adds voice-over-IP functionality to the private chat window.
Both friends chatting together need the plugin installed to be able to talk together.

%package feedreader-plugin
Summary: RetroShare FeedReader plugin
Group: Networking/File transfer
Requires: %name = %version-%release

%description feedreader-plugin
This package provides a plugin for RetroShare, a secured Friend-to-Friend communication platform. The plugin adds a RSS feed reader tab to retroshare.

%prep
%setup
%patch100 -p1
%patch101 -p1

# https://svnweb.freebsd.org/ports?view=revision&revision=468858
# fix build with ffmpeg 4.0 (replace CODEC_, skip CODEC_ID)
%__subst "s| \(CODEC_[^I]\)| AV_\1|g" plugins/VOIP/gui/VideoProcessor.cpp

%build
qmake-qt5 "CONFIG-=debug" "CONFIG+=release" "CONFIG+=retroshare_plugins" PREFIX=%prefix LIB_DIR=%_libdir RetroShare.pro
%make_build

%install
make INSTALL_ROOT=%buildroot install
ln -s %name-nogui %buildroot%_bindir/%name-cli
desktop-file-validate %buildroot%_desktopdir/retroshare.desktop

%files
%_bindir/%name
%_pixmapsdir/retroshare.xpm
%_iconsdir/hicolor/*/apps/*.png
%_desktopdir/retroshare.desktop

%files common
%_datadir/%name/

%files nogui
%_bindir/%name-cli
%_bindir/%name-nogui

%files voip-plugin
%_libdir/retroshare/extensions6/libVOIP.so*

%files feedreader-plugin
%_libdir/retroshare/extensions6/libFeedReader.so*

%changelog
* Sun Dec 16 2018 Vitaly Lipatov <lav@altlinux.ru> 0.6.4-alt5
- fix build with gcc8

* Wed Sep 19 2018 Alexey Shabalin <shaba@altlinux.org> 0.6.4-alt4
- fixed build

* Thu Sep 13 2018 Vitaly Lipatov <lav@altlinux.ru> 0.6.4-alt3
- rebuild with openssl 1.1

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 0.6.4-alt2
- rebuild with ffmpeg 4.0

* Sat May 26 2018 Vitaly Lipatov <lav@altlinux.ru> 0.6.4-alt1
- new version 0.6.4 (with rpmrb script)

* Sat Oct 21 2017 Vitaly Lipatov <lav@altlinux.ru> 0.6.3-alt1
- new version 0.6.3 (with rpmrb script)

* Thu Jun 08 2017 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt2
- rebuild with ffmpeg

* Tue Mar 14 2017 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt1
- new version 0.6.2 (with rpmrb script)

* Tue Jan 03 2017 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- initial build for ALT Linux Sisyphus

* Sat Apr  4 2015 Heini <noreply@nowhere.net> - 
- Initial build.

