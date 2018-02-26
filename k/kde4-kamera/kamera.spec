%add_findpackage_path %_kde4_bindir

%define rname kamera
Name: kde4-kamera
Version: 4.8.0
Release: alt1

Group: Graphics
Summary: KDE support for digital cameras
Url: http://projects.kde.org/projects/kdegraphics/kamera
License: GPLv2

Provides: kde4graphics-kamera = %version-%release
Obsoletes: kde4graphics-kamera < %version-%release

Source: %rname-%version.tar


# Automatically added by buildreq on Mon Sep 12 2011 (-bi)
# optimized out: automoc cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgpg-error libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-qt3support libqt4-sql libqt4-svg libqt4-xml libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libgphoto2-devel libqt3-devel rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4libs-devel zlib-devel kde-common-devel libgphoto2-devel

%description
Digital camera io_slave for Konqueror. Together gPhoto this allows you
to access your camera's picture with the URL camera:/

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
%description devel
Development files for %name

%prep
%setup -qn %rname-%version


%build
%K4build


%install
%K4install


%files

%doc AUTHORS README
%_K4lib/kcm_kamera.so
%_K4lib/kio_kamera.so
%_K4apps//solid/actions/solid_camera.desktop
%_K4srv/kamera.desktop
%_K4srv/camera.protocol
%_K4doc/en/kcontrol/kamera/

#%files devel
#%_K4includedir/kamera/
#%_K4link/lib*.so


%changelog
* Tue Jan 24 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60P.1
- built for M60P

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60T.1
- built for M60T

* Fri Sep 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- initial build
