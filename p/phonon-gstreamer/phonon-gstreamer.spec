
Name: phonon-gstreamer
Version: 4.6.0
Release: alt3

Group: System/Libraries
Summary: Gstreamer phonon backend
License: LGPLv2+
Url: http://phonon.kde.org/

Provides: phonon-backend = %{get_version phonon-devel}
Provides: phonon-backend-gstreamer = %version
Requires: gst-plugins-base gst-plugins-good

Source: %name-%version.tar
# FC
Patch1: phonon-4.3.50-gstreamer-fix-seekable-query-failed.patch
Patch2: phonon-4.4.3-flac_mimetype.patch

# Automatically added by buildreq on Wed Apr 20 2011 (-bi)
# optimized out: cmake-modules elfutils fontconfig glib2-devel gstreamer-devel libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libgst-plugins libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-xml libstdc++-devel libxkbfile-devel libxml2-devel pkg-config python-base ruby xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel
#BuildRequires: automoc cmake gcc-c++ glibc-devel-static gst-plugins-devel libXxf86misc-devel libalsa-devel libqt3-devel libqt4-opengl phonon-devel rpm-build-ruby
BuildRequires(pre): phonon-devel
BuildRequires: automoc cmake gcc-c++ glibc-devel gst-plugins-devel libXxf86misc-devel libalsa-devel phonon-devel
BuildRequires: kde-common-devel

%description
Gstreamer phonon backend

%prep
%setup -q
#%patch1 -p1
%patch2 -p1

%build
%K4cmake \
    -DINCLUDE_INSTALL_DIR=%_K4includedir \
    -DPLUGIN_INSTALL_DIR:PATH=%_qt4dir
%K4make

%install
%K4install

%files
%_qt4dir/plugins/phonon_backend/phonon_gstreamer.so
%_K4srv/phononbackends/gstreamer.desktop
%_iconsdir/hicolor/*/apps/phonon-gstreamer.*

%changelog
* Thu Apr 26 2012 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt3
- fix requires

* Tue Feb 28 2012 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1.M60P.1
- built for M60P

* Tue Feb 28 2012 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt2
- update code from 4.6 branch

* Fri Feb 24 2012 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt0.M60P.1
- built for M60P

* Fri Feb 24 2012 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Tue Feb 21 2012 Sergey V Turchin <zerg@altlinux.org> 4.5.90-alt0.M60P.1
- built for M60P

* Fri Jan 13 2012 Sergey V Turchin <zerg@altlinux.org> 4.5.90-alt1
- 4.6 RC1

* Mon Aug 08 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- new version

* Wed Apr 20 2011 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt3
- fix build requires

* Tue Feb 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt2
- fix requires

* Tue Feb 01 2011 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1
- initial build
