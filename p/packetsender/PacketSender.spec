%define NAME PacketSender
Name: packetsender
Version: 8.7.1
Release: alt1
Url: https://packetsender.com
Source: %NAME-%version.tar.gz
License: GPLv2+

Group: Networking/Other
Summary: Sending and receiving custom network packages

# Automatically added by buildreq on Wed Jul 24 2024
# optimized out: bash5 gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libdouble-conversion3 libglvnd-devel libgpg-error libp11-kit libqt6-core libqt6-dbus libqt6-gui libqt6-network libqt6-widgets libsasl2-3 libstdc++-devel python3 python3-base qt6-base-devel qt6-declarative-devel qt6-multimedia-devel qt6-positioning-devel qt6-serialport-devel qt6-webchannel-devel sh5
BuildRequires: qt6-3d-devel qt6-charts-devel qt6-connectivity-devel qt6-datavis3d-devel qt6-networkauth-devel qt6-quicktimeline-devel qt6-remoteobjects-devel qt6-scxml-devel qt6-sensors-devel qt6-serialbus-devel qt6-shadertools-devel qt6-speech-devel qt6-svg-devel qt6-tools-devel qt6-virtualkeyboard-devel qt6-wayland-devel qt6-websockets-devel

%description
Packet Sender is an open source utility to allow sending and receiving
TCP, UDP, and SSL (encrypted TCP) packets as well as HTTP/HTTPS requests
and panel generation. The mainline branch officially supports Windows,
Mac, and Desktop Linux (with Qt). Other places may recompile and
redistribute Packet Sender. Packet Sender is free and licensed GPL v2 or
later.

%prep
%setup -n %NAME-%version

%build
%qmake_qt6 src/%NAME.pro
%make_build

%install
install -D %name %buildroot%_bindir/%name
install -D src/%name.desktop %buildroot%_desktopdir/%name.desktop
install -D src/pslogo.png %buildroot%_iconsdir/hicolor/64x64/apps/%name.png
install -D src/%name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.png
for W in 128 192 256; do
        install -D src/pslogo$W.png %buildroot%_iconsdir/hicolor/${W}x${W}/apps/%name.png
done

%files
%doc README*
%_bindir/%name
%_iconsdir/*/*/*/%name.*
%_desktopdir/%name.desktop

%changelog
* Wed Jul 24 2024 Fr. Br. George <george@altlinux.org> 8.7.1-alt1
- Autobuild version bump to 8.7.1

