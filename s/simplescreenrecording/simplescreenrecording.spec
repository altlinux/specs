Name: simplescreenrecording
Version: 0.0.7
Release: alt1
Summary: Simple Screen Recording with OpenGL capture

Group: Video
License: GPLv3
Url: http://www.maartenbaert.be/simplescreenrecorder/
Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar

BuildRequires: gcc-c++ glibc-devel-static libalsa-devel libavformat-devel libswscale-devel fontconfig gnu-config libGL-devel libGLU-devel libX11-devel libXext-devel libXfixes-devel libavcodec-devel libavutil-devel libopencore-amrnb0 libopencore-amrwb0 libqt4-core libqt4-devel libqt4-gui libstdc++-devel pkg-config xorg-fixesproto-devel xorg-xextproto-devel xorg-xproto-devel

%description
%summary

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall

%files
%_bindir/simplescreenrecorder
%_libdir/libssr-glinject.so
%_desktopdir/simplescreenrecorder.desktop
%_iconsdir/hicolor/256x256/apps/simplescreenrecorder.png

%changelog
* Wed Sep 04 2013 Denis Smirnov <mithraen@altlinux.ru> 0.0.7-alt1
- initial build for ALT Linux Sisyphus
