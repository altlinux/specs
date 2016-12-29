%add_findpackage_path %_kde4_bindir
%def_enable lcms2

%define rname libkdcraw
Name: libkdcraw4
Version: 15.08.0
Release: alt2

Group: System/Libraries
Summary: Decoding RAW pictures
Url: http://projects.kde.org/projects/kdegraphics/libs/libkdcraw
License: GPLv2 and LGPLv2 and GPLv3

Conflicts: libkdcraw <= 0.1.5-alt2
Provides: libkdcraw4-common = %version-%release
Obsoletes: libkdcraw4-common < %version-%release

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Sep 09 2011 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libgomp-devel libjpeg-devel liblcms-devel libqt3-devel rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4libs-devel libgomp-devel libjpeg-devel zlib-devel kde-common-devel
BuildRequires: libraw-devel
%if_enabled lcms2
BuildRequires: liblcms2-devel
%else
BuildRequires: liblcms-devel
%endif

%description
Libkdcraw is a C++ interface around LibRaw library used to decode RAW
picture files.

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: %name = %version-%release
Conflicts: libkdcraw-devel
%description devel
Development files for %name

%prep
%setup -qn %rname-%version


%build
%K4build \
    %{?_enable_lcms2:-DENABLE_LCMS2=ON}


%install
%K4install


%files
%doc README AUTHORS NEWS TODO
%_K4libdir/libkdcraw.so.*
%_K4iconsdir/hicolor/*/apps/kdcraw.*
%_K4apps/libkdcraw/

%files devel
%_K4includedir/libkdcraw/
%_K4link/lib*.so
%_pkgconfigdir/libkdcraw.pc


%changelog
* Thu Dec 29 2016 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt2
- rebuild with new libraw

* Tue Sep 15 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Wed Jan 28 2015 Sergey V Turchin <zerg@altlinux.org> 14.12.1-alt1
- new version

* Tue Apr 22 2014 Sergey V Turchin <zerg@altlinux.org> 4.13.0-alt1
- new version

* Thu Mar 13 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt0.M70P.1
- built for M70P

* Fri Jan 31 2014 Sergey V Turchin <zerg@altlinux.org> 4.12.2-alt1
- new version

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt0.M70P.1
- built for M70P

* Thu Sep 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Thu Jul 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.5-alt1
- new version

* Mon Jan 14 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.2
- update from 4.10 branch

* Wed Dec 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- new beta version

* Tue Oct 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt0.M60P.1
- built for M60P

* Mon Jan 23 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60P.1
- built for M60P

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60T.1
- built for M60T

* Fri Sep 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- initial build
