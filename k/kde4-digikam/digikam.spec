%add_findpackage_path %_kde4_bindir
%def_disable marble
%define rname digikam
%define label digiKam
Name: kde4-%rname
%define lname lib%name
Version: 2.7.0
Release: alt1

Summary: digiKam is an advanced digital photo management application for linux
License: %gpl2plus
Group: Graphics
Url: http://www.digikam.org/

Packager: Aeliya Grevnyov <gray_graff@altlinux.org>
Conflicts: digikam <= 0.9.6-alt3

BuildRequires(pre): rpm-build-licenses kde-common-devel

# Automatically added by buildreq on Wed Sep 01 2010
BuildRequires: doxygen gcc-c++ graphviz kde4graphics-devel kde4pimlibs-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libgphoto2-devel libjasper-devel libjpeg-devel liblcms-devel liblensfun-devel liblqr-devel libxkbfile-devel soprano
             
%if_enabled marble
BuildRequires: kde4edu-devel
%endif

# buildreq sucks
BuildRequires: kde4libs-devel soprano-backend-virtuoso soprano-backend-redland libkface-devel libkgeomap-devel boost-geometry-devel

Requires: libqt4-sql-sqlite kde4base-runtime libkipi4 libqt4-sql-mysql
Requires: %lname = %version-%release
Requires: %name-i18n = %version-%release
Requires: %name-data = %version-%release
%if_enabled marble
Requires: %name-marble = %version-%release
%endif
Source0: %rname-%version.tar
Patch1: build-without-mysql.patch
Patch2: i18n.patch
Patch3: digikam-boost-1.48.patch
Patch4: digikam-old-libkipi.patch
Patch5: digikam-arm-cast-to-qreal.patch
                                                 
%description
DigiKam is an advanced digital photo management application for KDE.
Photos can be collected into albums which can be sorted chronologically,
by directory layout or by custom collections.
DigiKam also provides tagging functionality. Images can be tagged despite of
their position and digiKam provides fast and intuitive ways to browse them.
User comments and customized meta-information added to images, are stored
into a database and retrieved to make them available into the user interface.
As soon as the camera is plugged in digikam allows you to preview, download,
upload and delete images.
DigiKam also includes tools like Image Editor, to modify photos using plugins
such as red eye correction or Gamma correction, exif management,...
Light Table to make artistic photos and an external image editor such
as Showfoto.
DigiKam also uses KIPI plugins (KDE Image Plugin Interface) to increase
its functionalities.

%package utils
Group: Graphics
Summary: %label utils
Requires: %name = %version-%release

%description utils
Utilities for %label data.

%package -n %lname
Group: System/Libraries
Summary: %label library

%description -n %lname
%label library.

%package data
Group: Graphics
Summary: A Photo Management Application for KDE
Requires: %name = %version-%release
BuildArch: noarch
Conflicts: digikam-data <= 0.9.6-alt3

%description data
DigiKam is an advanced digital photo management application for KDE.
Photos can be collected into albums which can be sorted chronologically,
by directory layout or by custom collections.
DigiKam also provides tagging functionality. Images can be tagged despite of
their position and digiKam provides fast and intuitive ways to browse them.
User comments and customized meta-information added to images, are stored
into a database and retrieved to make them available into the user interface.
As soon as the camera is plugged in digikam allows you to preview, download,
upload and delete images.
DigiKam also includes tools like Image Editor, to modify photos using plugins
such as red eye correction or Gamma correction, exif management,...
Light Table to make artistic photos and an external image editor such
as Showfoto.
DigiKam also uses KIPI plugins (KDE Image Plugin Interface) to increase
its functionalities.

%package i18n
Group: Graphics
Summary: Languages support for %label
Requires: %name = %version-%release
BuildArch: noarch

%description i18n
Languages support for %label.

%package image-plugins
Group: Graphics
Summary: %label image plugins
Requires: %name = %version-%release

%description image-plugins
%label plugins for additional functionalities in ImageEditor and
Showfoto.

%package -n %lname-devel
Group: Development/KDE and QT
Summary: Development files for %label
Requires: %lname = %version-%release

%description -n %lname-devel
Development files for %label.

%if_enabled marble
%package marble
Group: Graphics
Summary: %label support
Requires: %name = %version-%release
Requires: kde4edu-core kde4edu-marble

%description marble
Marble support for %lname.
%endif


%prep
%setup -q -n %rname-%version
%patch1 -p2
%patch2 -p2
#%%patch3 -p0
#%%patch4 -p1
%patch5 -p2

%build
%K4build -DENABLE_INTERNALMYSQL=no

%install
%K4install
rm -rf %buildroot%_man1dir
%K4find_lang --with-kde %rname

%files
%_K4bindir/%rname
%_K4bindir/showfoto

%files utils
%_K4bindir/cleanup_digikamdb
%_K4bindir/digitaglinktree

%files -n %lname
%_K4libdir/lib%{rname}*.so*
%_K4lib/kio_%{rname}*.so
%_K4lib/%{rname}nepomukservice.so

%if_enabled marble
%files marble
%_K4plug/marble
%endif

%files data
%doc AUTHORS ChangeLog DESIGN HACKING NEWS README TODO
%_K4xdg_apps/*.desktop
%dir %_K4apps/%rname
%_K4apps/%rname/%{rname}imagewindowui.rc
%_K4apps/%rname/%{rname}ui.rc
%_K4apps/%rname/queuemgrwindowui.rc
%_K4apps/%rname/about
%_K4apps/%rname/cameraui.rc
%_K4apps/%rname/data
%_K4apps/%rname/icons
%_K4apps/%rname/lighttablewindowui.rc
%_K4apps/%rname/tips
%_K4apps/%rname/utils
%_K4apps/%rname/digikam.notifyrc
%_K4apps/%rname/database
%_K4apps/%rname/lensfun
%_K4apps/showfoto
%_K4apps/solid/actions/%{rname}-opencamera.desktop
%_K4srv/%{rname}*.protocol
%_K4srv/digikamnepomukservice.desktop
%_K4iconsdir/hicolor/*/apps/%rname.*
%_K4iconsdir/hicolor/*/apps/showfoto.*
%_K4conf_update/*

%files i18n -f %rname.lang

%files image-plugins
%_K4lib/%{rname}imageplugin_*.so
%_K4apps/%rname/%{rname}imageplugin_*_ui.rc
%_K4srv/%{rname}imageplugin_*.desktop
%_K4srvtyp/*.desktop

%files -n %lname-devel
%_K4link/*.so

%changelog
* Tue Jul 10 2012 Aeliya Grevnyov <gray_graff@altlinux.org> 2.7.0-alt1
- 2.7.0

* Sat Jul 07 2012 Aeliya Grevnyov <gray_graff@altlinux.org> 2.6.0-alt1
- 2.6.0

* Fri May 04 2012 Sergey V Turchin <zerg@altlinux.org> 2.5.0-alt2
- fix compile on arm; thanks sbolshakov@alt

* Thu Jan 05 2012 Aeliya Grevnyov <gray_graff@altlinux.org> 2.5.0-alt1
- 2.5.0

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 2.2.0-alt1.M60P.1
- built for M60P

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 2.2.0-alt0.M60T.1
- built for M60T

* Fri Oct 07 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.0-alt2
- Missing l18n files have been added

* Tue Oct 04 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.2.0-alt1
- 2.2.0

* Wed Sep 21 2011 Sergey V Turchin <zerg@altlinux.org> 1.9.0-alt4
- rebuilt with kde-4.7

* Thu Aug 25 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 1.9.0-alt3
- Fix build with new libjpeg

* Tue Jul 05 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 1.9.0-alt2
- Disable Marble (Fix build)

* Sun Mar 13 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 1.9.0-alt1
- Release 1.9.0

* Tue Feb 22 2011 Sergey V Turchin <zerg@altlinux.org> 1.8.0-alt3
- move to standart place

* Thu Feb 03 2011 Sergey V Turchin <zerg@altlinux.org> 1.8.0-alt1.1
- rebuilt with kde-4.6

* Mon Jan 24 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 1.8.0-alt1
- Release 1.8.0

* Thu Dec 23 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 1.7.0-alt1
- Release 1.7.0

* Fri Nov 26 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 1.6.0-alt2
- Missing ru l18n files have been added (from 1.5.0)

* Thu Nov 25 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 1.6.0-alt1
- Release 1.6.0
- Remove MySQL-server from requires

* Tue Oct 12 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 1.5.0-alt1
- Release 1.5.0

* Mon Aug 30 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 1.4.0-alt1
- Release 1.4.0

* Thu Aug 12 2010 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt1.1
- rebuilt with kde-4.5

* Tue Mar 30 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 1.2.0-alt1
- Release 1.2.0


* Tue Feb 02 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 1.1.0-alt1
- Release 1.1.0
- Remove deprecate macroses

* Thu Jan 28 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt1.1
- rebuilt with kde-4.4

* Tue Dec 22 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 1.0.0-alt1
- Release 1.0.0

* Mon Dec 07 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 1.0.0-alt0.5.rc1
- New version 1.0.0-rc1

* Sun Nov 01 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 1.0.0-alt0.4.beta5
- Move marble support to subpackage
- Fix requires (ALT #21821)

* Wed Oct 07 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 1.0.0-alt0.3.beta5
- New version 1.0.0-beta5

* Mon Sep 14 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 1.0.0-alt0.3.beta4
- Build with MarbleWidget support

* Thu Sep 03 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 1.0.0-alt0.2.beta4
- New version 1.0.0-beta4

* Wed Aug 12 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 1.0.0-alt0.2.beta3
- Missing l10n files have been added

* Tue Aug 11 2009 Aeliya Grevnyov <gray_graff@altlinux.org> 1.0.0-alt0.1.beta3
- New version 1.0.0-beta3
- Drop kde3-digikam require (ALT #20975)

* Thu Mar 19 2009 Konstantin Baev <kipruss@altlinux.org> 0.10.0-alt1
- Release 0.10.0

* Wed Mar 11 2009 Konstantin Baev <kipruss@altlinux.org> 0.10.0-alt0.rc2.1
- New version 0.10.0-rc2

* Mon Feb 16 2009 Konstantin Baev <kipruss@altlinux.org> 0.10.0-alt0.rc1.3
- Remove manpages, whose conflicts with digikam-utils package

* Fri Feb 13 2009 Konstantin Baev <kipruss@altlinux.org> 0.10.0-alt0.rc1.2
- Back to manual BuildRequires

* Fri Feb 13 2009 Konstantin Baev <kipruss@altlinux.org> 0.10.0-alt0.rc1.1
- initial build for KDE4
