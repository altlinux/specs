%define _kde_alternate_placement 1

%define rname kffmpegthumbnailer
Name: kde4-kffmpegthumbnailer
Version: 1.1.0
Release: alt2

Group: Video
Summary: A video thumbnailer for kde based on ffmpegthumbnailer
License: GPLv2+
Url: http://code.google.com/p/ffmpegthumbnailer/

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Mar 21 2013 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libavcodec-devel libavformat-devel libavutil-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libopencore-amrnb0 libopencore-amrwb0 libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libswscale-devel libxkbfile-devel phonon-devel pkg-config python-base ruby ruby-stdlibs xorg-kbproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libffmpegthumbnailer-devel libicu libqt3-devel python-module-distribute rpm-build-ruby xorg-xf86miscproto-devel zlib-devel-static
BuildRequires: gcc-c++ libffmpegthumbnailer-devel kde4libs-devel kde-common-devel

%description
This video thumbnailer can be used to create thumbnails for your video files.
The thumbnailer uses ffmpeg to decode frames from the video files.

%prep
%setup -qn %rname-%version

%build
%K4build

%install
%K4install

%files
%doc README Changelog
%_K4srv/kffmpegthumbnailer.desktop
%_K4lib/kffmpegthumbnailer.so

%changelog
* Wed Dec 09 2015 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt2
- rebuild with gcc5

* Thu Mar 21 2013 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt1
- initial build
