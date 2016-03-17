%define rname kamerka
Name: kde4-kamerka
Version: 0.12
Release: alt1

Group: Video
Summary: Take photos using your webcam and shiny interface
Url: http://dos1.github.com/kamerka/
License: GPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Fri May 30 2014 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libcloog-isl4 libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql libqt4-sql-sqlite libqt4-svg libqt4-xml libqt4-xmlpatterns libsoprano-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libXxf86misc-devel libicu50 libqt3-devel libv4l-devel qt4-designer ruby ruby-stdlibs zlib-devel-static
BuildRequires: gcc-c++ libqimageblitz-devel kde4libs-devel libv4l-devel

%description
Kamerka is a KDE application which uses Video4Linux to get image from
webcam, with ability to save photos. It features easy to use, animated
and well-integrated user interface.

%prep
%setup -qn %rname-%version

%build
%K4build


%install
%K4install

%find_lang --with-kde %rname

%files -f %rname.lang
%doc AUTHORS README
%_K4bindir/%rname
%_K4cfg/%rname.kcfg
%_K4xdg_apps/%rname.desktop
%_K4apps/%rname/
%_pixmapsdir/%rname.png
%_man1dir/%rname.*

%changelog
* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 0.12-alt1
- new version

* Fri May 30 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.5-alt0.M70P.1
- built for M70P

* Fri May 30 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.5-alt1
- initial build

