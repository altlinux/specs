%define oname KOceanSaver

Name: kde4-screensaver-koceansaver
Version: 0.8
Release: alt3
Epoch: 1

Summary: An under water screen saver for KDE4
Url: http://sourceforge.net/projects/koceansaver/
Group: Graphical desktop/KDE
License: GPL2+
Source0: %oname-%version.tar.gz

# Automatically added by buildreq on Mon May 13 2013
# optimized out: automoc cmake cmake-modules fontconfig fontconfig-devel kde4libs kde4libs-devel libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-svg libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: ctest gcc-c++ glib2-devel glibc-devel-static kde4base-workspace-devel libXxf86misc-devel libfreetype-devel libicu50 qt4-designer
BuildRequires: cmake gcc-c++ glib2-devel kde4base-workspace-devel libXxf86misc-devel libfreetype-devel libicu50 qt4-designer

%description
A KDE 4 screensaver that shows an underwater ocean seen
with sea creatures. In particular, swimming Baracudas and
sharks. A treasure chest lies on the sea floor with a ship
wrecked in the background.

%prep
%setup -n %oname

%build
%cmake_insource
%make_build VERBOSE=1

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS ChangeLog INSTALL
%_bindir/koceansaver.kss
%dir %_datadir/apps/koceansaver/data/
%_datadir/apps/koceansaver/data/*
%_datadir/kde4/services/ScreenSavers/koceansaver.desktop
%_man1dir/koceansaver.*

%changelog
* Thu Nov 14 2013 Igor Zubkov <icesik@altlinux.org> 1:0.8-alt3
- Add epoch for correct update

* Wed Nov 13 2013 Igor Zubkov <icesik@altlinux.org> 0.8-alt2
- Make build more verbose

* Wed Nov 13 2013 Igor Zubkov <icesik@altlinux.org> 0.8-alt1
- 0.8

* Mon May 13 2013 Igor Zubkov <icesik@altlinux.org> 0.71-alt1
- build for Sisyphus

