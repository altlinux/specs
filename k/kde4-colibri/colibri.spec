%define _kde_alternate_placement 1

%define rname colibri
Name: kde4-colibri
Version: 0.2.2
Release: alt1

Group: Graphical desktop/KDE
Summary: Light notification system for KDE
Url: http://gitorious.org/colibri/
License: LGPLv2+


Source: %rname-%version.tar

# Automatically added by buildreq on Thu Dec 15 2011 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde-common-devel kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-script libqt4-sql libqt4-svg libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xextproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libqt3-devel python-module-distribute rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ kde4libs-devel kde-common-devel

%description
Light notification system for KDE


%prep
%setup -qn %rname-%version


%build
%K4build


%install
%K4install
%K4find_lang --with-kde %rname


%files -f %rname.lang
%_kde4_bindir/colibri
%_K4lib/kcm_colibri.so
%_K4start/colibri_autostart.desktop
%_K4srv/colibri.desktop


%changelog
* Thu Dec 15 2011 Sergey V Turchin <zerg@altlinux.org> 0.2.2-alt1
- initial build
