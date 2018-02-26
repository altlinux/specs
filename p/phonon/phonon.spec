%def_disable zeitgeist

Name: phonon
Version: 4.6.0
Release: alt2

Group: Graphical desktop/KDE
Summary: KDE4 Multimedia Framework
Url: http://phonon.kde.org/
License: LGPLv2+

#Source: ftp://ftp.kde.org/pub/kde/stable/%name/%version/%name-%version.tar.bz2
Source: %name-%version.tar.bz2
# FC
Patch1: phonon-4.4.4-no_rpath.patch
Patch2: phonon-4.6.0-phonon-allow-stop-empty-source.patch
# ALT
Patch100: phonon-4.6.0-alt-fix-install.patch

#BuildRequires: glib2-devel gstreamer-devel gst-plugins-devel
#BuildRequires: libbfd-devel libxml2-devel
BuildRequires(pre): libqt4-devel
BuildRequires: ImageMagick-tools automoc cmake gcc-c++
BuildRequires: libalsa-devel libpulseaudio-devel libxine-devel gst-plugins-devel
BuildRequires: kde-common-devel
%if_enabled zeitgeist
BuildRequires: libqzeitgeist-devel
%endif

%description
Phonon is the KDE4 Multimedia Framework

%package -n libphononexperimental
Group: System/Libraries
Summary: Phonon library
Requires: libphonon = %version-%release
Conflicts: kde4libs < 4.0.81
%description -n libphononexperimental
Phonon library.

%package -n libphonon
Group: System/Libraries
Summary: Phonon library
Conflicts: kde4libs < 4.0.81
Requires: libqt4-core >= %{get_version libqt4-core}
%description -n libphonon
Phonon library.

%package devel
Group: Development/KDE and QT
Summary: Header files and documentation for compiling KDE applications
#Requires: libphononexperimental = %version-%release
#Requires: libphonon = %version-%release
Conflicts: kde4libs-devel < 4.0.81
%description devel
This package includes the header files you will need to compile applications
for KDE. Also included is the KDE API documentation in HTML format for easy
browsing.


%prep
%setup -q
%patch1 -p1
%patch2 -p1
#
%patch100 -p1


%build
%Kcmake \
    -DINCLUDE_INSTALL_DIR:PATH=%_K4includedir \
    -DPLUGIN_INSTALL_DIR:PATH=%_qt4dir
%Kmake

%install
%Kinstall

mkdir -p %buildroot/%_qt4dir/plugins/phonon_backend


%files -n libphononexperimental
%_K4libdir/libphononexperimental.so.*

%files -n libphonon
%dir %_qt4dir/plugins/phonon_backend/
%_K4libdir/libphonon.so.*

%files devel
%_K4includedir/phonon
%_K4includedir/KDE
%_K4libdir/libphonon.so
%_K4libdir/libphononexperimental.so
%dir %_datadir/phonon/
%_datadir/phonon/buildsystem/
%_libdir/cmake/phonon/
#%_qt4dir/plugins/designer/libphononwidgets.so
%_datadir/qt4/mkspecs/modules/qt_phonon.pri
%_pkgconfigdir/phonon.pc
%_K4dbus_interfaces/org.kde.Phonon.AudioOutput.xml

%changelog
* Fri Jan 13 2012 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt2
- fix cmake files

* Fri Jan 13 2012 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Tue Jan 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1.M60P.1
- built for M60P

* Tue Jan 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt2
- built without zeitgeist

* Fri Dec 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt0.M60P.1
- built for M60P

* Wed Dec 07 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- new version

* Thu Sep 29 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt5
- fix find pulseaudio

* Wed Sep 14 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt3.M60P.1
- built for M60P

* Wed Sep 14 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt4
- built with zeitgeist support

* Mon Aug 08 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt3
- fix to build

* Wed Apr 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt2
- temporary don't package designer plugin

* Tue Apr 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt3
- fix to build

* Mon Feb 07 2011 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt2
- rebuilt

* Mon Jan 31 2011 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1
- new version

* Fri Dec 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt1
- new version

* Fri Oct 08 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt2
- rebuilt

* Thu Jun 17 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt0.M51.1
- built for M51

* Thu Jun 17 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- new version

* Wed May 12 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt0.M51.1
- build for M51

* Wed May 12 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt1
- new version

* Tue Apr 20 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt2.M51.1
- build for M51

* Wed Apr 14 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt3
- add fixes for pulseaudio support

* Thu Mar 25 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt2
- fix build requires (ALT#23225)

* Mon Mar 22 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- new version

* Fri Jan 15 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.80-alt1
- new beta

* Mon Jul 20 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt3
- patch to xine kequalizer effect

* Wed Mar 25 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt2
- add workaround for /etc/modprobe.d/alsa-modindex snd_pcsp index=10

* Fri Feb 27 2009 Sergey V Turchin <zerg at altlinux dot org> 4.3.1-alt1
- new version

* Wed Jan 28 2009 Sergey V Turchin <zerg at altlinux dot org> 4.3.0-alt1
- new version

* Tue Jan 13 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.96-alt1
- new beta
- removed deprecated macroses from specfile

* Wed Jul 30 2008 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt1
- initial spec

