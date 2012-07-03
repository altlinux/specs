%def_disable okular_msits

%add_findpackage_path %_kde4_bindir

%define rname okular
Name: kde4-okular
Version: 4.8.4
Release: alt1

Group: Office
Summary: KDE document viewer
Url: http://projects.kde.org/projects/kdegraphics/okular
License: GPLv2

Requires: kde4-icon-theme

Provides: kde4graphics-okular = %version-%release
Obsoletes: kde4graphics-okular < %version-%release

Source: %rname-%version.tar

# Automatically added by buildreq on Mon Sep 12 2011 (-bi)
# optimized out: automoc cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgpg-error libpng-devel libpoppler3-qt4 libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-test libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libtiff-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: ebook-tools-devel gcc-c++ glib2-devel kde4libs-devel libchm-devel libdjvu-devel libpoppler-qt4-devel libqca2-devel libqimageblitz-devel libqt3-devel libspectre-devel rpm-build-ruby zlib-devel-static
BuildRequires: ebook-tools-devel gcc-c++ glib2-devel kde4libs-devel libdjvu-devel libpoppler-qt4-devel libqca2-devel libqimageblitz-devel libspectre-devel zlib-devel kde-common-devel
%if_enabled okular_msits
BuildRequires: libchm-devel
%endif

%description
Document viewer; support different kinds of documents.

%package -n libokularcore4
Summary: KDE 4 core library
Group: System/Libraries
%description -n libokularcore4
KDE 4 core library.

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
%doc AUTHORS TODO
%_K4bindir/okular
%_K4lib/okularGenerator_*
%_K4lib/okularpart.so
%if_enabled okular_msits
%_K4lib/kio_msits.so
%endif
%_K4xdg_apps/okular*
%_K4apps/okular
%_K4cfg/okular.kcfg
%_K4cfg/gssettings.kcfg
%_K4srv/libokularGenerator_*
%_K4srv/okular*
%if_enabled okular_msits
%_K4srv/msits*
%endif
%_K4srvtyp/okularGenerator.desktop
%_K4iconsdir/hicolor/*/apps/okular.*
%_K4doc/en/okular/

%files -n libokularcore4
%_K4libdir/libokularcore.so.*

%files devel
%_K4includedir/okular/
%_K4libdir/cmake/Okular/
%_K4link/lib*.so


%changelog
* Thu Jun 21 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- new version

* Thu May 31 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt0.M60P.1
- build for M60P

* Thu May 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Wed Apr 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt0.M60P.1
- built for M60P

* Wed Apr 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt0.M60P.1
- built for M60P

* Sun Mar 11 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Fri Feb 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt2
- fix requires

* Tue Jan 24 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt0.M60P.1
- build for M60P

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1
- new version

* Mon Nov 07 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt2
- rebuilt with poppler-0.18

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt0.M60P.1
- built for M60P

* Tue Nov 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1
- new version

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt0.M60T.1
- built for M60T

* Mon Oct 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- new version

* Fri Sep 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- initial build
