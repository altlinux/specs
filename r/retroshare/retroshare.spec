Name: retroshare
Version: 0.6.2
Release: alt1

Summary: Secure communication with friends

License: GPLv3
Group: Networking/File transfer
Url: http://retroshare.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/RetroShare/RetroShare/archive/v%version.tar.gz
Source: %name-%version.tar

# manually removed: ruby ruby-stdlibs selinux-policy i586-libxcb  python-module-google python-module-mwlib python3-dev python3-module-yieldfrom python3-module-zope
# Automatically added by buildreq on Tue Jan 03 2017
# optimized out: gcc-c++ glib2-devel libGL-devel libX11-devel libXScrnSaver-devel libavutil-devel libcom_err-devel libgnome-keyring libgpg-error libjson-c libkrb5-devel libp11-kit libqt5-core libqt5-gui libqt5-multimedia libqt5-network libqt5-printsupport libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxml2-devel pkg-config python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel qt5-script-devel qt5-tools-devel qt5-xmlpatterns-devel xorg-scrnsaverproto-devel xorg-xproto-devel zlib-devel
BuildRequires: bzlib-devel libavcodec-devel libcurl-devel libgnome-keyring-devel libmicrohttpd-devel libopencv-devel libqtav-devel libspeex-devel libspeexdsp-devel libsqlcipher-devel libssl-devel libupnp-devel libxslt-devel
BuildRequires: qt5-connectivity-devel qt5-location-devel qt5-multimedia-devel qt5-phonon-devel qt5-quick1-devel qt5-sensors-devel qt5-serialport-devel qt5-svg-devel qt5-tools-devel-static qt5-wayland-devel qt5-webkit-devel qt5-websockets-devel qt5-x11extras-devel

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

%build
qmake-qt5 "CONFIG-=debug" "CONFIG+=release" PREFIX=%prefix LIB_DIR=%_libdir RetroShare.pro
%make_build

%install
make INSTALL_ROOT=%buildroot install
#menu
desktop-file-validate %buildroot%_desktopdir/retroshare06.desktop
ln -s RetroShare06 %buildroot%_bindir/%name
ln -s RetroShare06-nogui %buildroot%_bindir/%name-cli

%files
%_bindir/%name
%_bindir/RetroShare06
%_pixmapsdir/retroshare06.xpm
%_iconsdir/hicolor/*/apps/*.png
%_desktopdir/retroshare06.desktop

%files common
%_datadir/RetroShare06/

%files nogui
%_bindir/%name-cli
%_bindir/RetroShare06-nogui

%files voip-plugin
%_libdir/retroshare/extensions6/libVOIP.so*

%files feedreader-plugin
%_libdir/retroshare/extensions6/libFeedReader.so*

%changelog
* Tue Mar 14 2017 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt1
- new version 0.6.2 (with rpmrb script)

* Tue Jan 03 2017 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- initial build for ALT Linux Sisyphus

* Sat Apr  4 2015 Heini <noreply@nowhere.net> - 
- Initial build.

