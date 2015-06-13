Name: qtox
Version: 1.1
Release: alt1

Summary: Powerful Tox client that follows the Tox design guidelines

License: GPL+
Group: Networking/Instant messaging
Url: https://github.com/tux3/qTox

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/tux3/qTox
Source: %name-%version.tar

BuildPreReq: rpm-macros-qt5

# manually removed: i586-libxcb ruby ruby-stdlibs 
# Automatically added by buildreq on Sat Jun 13 2015
# optimized out: fontconfig glib2-devel glibc-devel-static libGL-devel libX11-devel libatk-devel libavcodec-devel libavutil-devel libcairo-devel libcloog-isl4 libdc1394-22 libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libjson-c libopencore-amrnb0 libopencore-amrwb0 libp11-kit libpango-devel libqt5-core libqt5-gui libqt5-network libqt5-opengl libqt5-sql libqt5-svg libqt5-widgets libqt5-xml libraw1394-11 libsodium-devel libstdc++-devel libswscale-devel libvpx-devel libwayland-client libwayland-server python3-base qt5-base-devel qt5-declarative-devel qt5-script-devel qt5-tools xorg-scrnsaverproto-devel xorg-xproto-devel
BuildRequires: gcc-c++ git-core libXScrnSaver-devel libavdevice-devel libavformat-devel libdb4-devel libfilteraudio-devel libgtk+2-devel libopenal-devel libqrencode-devel libswscale-devel-static python3 qt5-connectivity-devel qt5-location-devel qt5-multimedia-devel qt5-phonon-devel qt5-quick1-devel qt5-sensors-devel qt5-serialport-devel qt5-svg-devel qt5-tools-devel qt5-wayland-devel qt5-webkit-devel qt5-websockets-devel toxcore-devel

%description
Powerful Tox Qt5 client that follows the Tox design guidelines.

%prep
%setup

%build
%qmake_qt5
%make_build

%install
mkdir -p %buildroot%_bindir/
install -m 0755 %name %buildroot%_bindir/%name
mkdir -p %buildroot%_desktopdir/
install -m 0644 qTox.desktop %buildroot%_desktopdir/%name.desktop

# create icons tree
mkdir -p %buildroot%_iconsdir/hicolor/scalable/apps/
install -m 0644 img/icons/qtox.svg %buildroot%_iconsdir/hicolor/scalable/apps/

for i in img/icons/*.png ; do
    DNAME=$(echo $(basename $i) | sed "s|.*-\([0-9]\+x[0-9]\+\).*|\1|g")
    install -D -m 0644 $i %buildroot%_iconsdir/hicolor/$DNAME/apps/%name.png
done

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
* Sat Jun 13 2015 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- initial build for ALT Linux Sisyphus
