%add_findpackage_path %_kde4_bindir
%def_disable marble
%def_enable baloo
%define rname digikam
%define label digiKam
Name: kde4-%rname
%define lname lib%name
Version: 4.14.0
Release: alt3

Summary: digiKam is an advanced digital photo management application for linux
License: %gpl2plus
Group: Graphics
Url: http://www.digikam.org/

Conflicts: digikam <= 0.9.6-alt3
Requires: libqt4-sql-sqlite kde4base-runtime libkipi4 libqt4-sql-mysql
Requires: %lname = %version-%release
Requires: %name-i18n = %version-%release
Requires: %name-data = %version-%release
%if_enabled marble
Requires: %name-marble = %version-%release
%endif

BuildRequires(pre): rpm-build-licenses kde-common-devel
BuildPreReq: libpng-devel
# Automatically added by buildreq on Wed Sep 01 2010
BuildRequires: doxygen gcc-c++ graphviz kde4graphics-devel kde4pimlibs-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libgphoto2-devel libjasper-devel libjpeg-devel liblensfun-devel liblqr-devel libxkbfile-devel libtiff-devel
BuildRequires: libpgf-devel libclapack-devel libusb-compat-devel liblcms2-devel
BuildRequires: kde4libs-devel libkface-devel libkgeomap-devel boost-devel
BuildRequires: libopencv-devel libsqlite-devel eigen3
%if_enabled baloo
BuildRequires: kde4-baloo-devel
%endif
%if_enabled marble
BuildRequires: kde4edu-devel
%endif

Source0: %rname-%version.tar
Source1: %rname-po-%version.tar
Source2: %rname-doc-%version.tar
Source3: %rname-doc-translated-%version.tar
Patch1: alt-build-without-mysql.patch
Patch2: alt-fix-build.patch
Patch3: alt-lensfun0.3.2.patch

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
%setup -q -n %rname-%version  -a1 -a2 -a3
%patch1 -p2
%patch2 -p1
%patch3 -p1

# change double to qreal for casting on arm
find -type f -name \*.cpp | \
while read f ; do
    sed -i 's|<double>|<qreal>|g' $f
done
find -type f -name \*.h | \
while read f ; do
    sed -i 's|<double>|<qreal>|g' $f
done

mv %rname-po-%version po
mv %rname-doc-%version doc
mv %rname-doc-translated-%version doc-translated
sed -i 's|add_subdirectory|macro_optional_add_subdirectory|' doc-translated/CMakeLists.txt

cat >> CMakeLists.txt <<__EOF__
find_package(Msgfmt REQUIRED)
find_package(Gettext REQUIRED)
add_subdirectory( po )
add_subdirectory( doc )
add_subdirectory( doc-translated )
__EOF__


%build
%K4build \
    -DENABLE_INTERNALMYSQL=OFF \
    -DENABLE_MYSQLSUPPORT=OFF \
    -DENABLE_BALOOSUPPORT=%{?_enable_baloo:ON}%{!?_enable_baloo:OFF} \
    -DENABLE_LCMS2=ON \
    -DKDE4_BUILD_TESTS=OFF \
    #

%install
%K4install

rm -rf %buildroot%_man1dir

rm -f %buildroot/%_K4i18n/*/*/kipiplugin*
rm -f %buildroot/%_K4i18n/*/*/libkipi.*
rm -f %buildroot/%_K4i18n/*/*/libkgeomap*
%K4find_lang --with-kde %rname
%K4find_lang --with-kde --append --output=%rname.lang showfoto

%files
%_K4bindir/%rname
%_K4bindir/showfoto

%files utils
%_K4bindir/cleanup_digikamdb
%_K4bindir/digitaglinktree

%files -n %lname
%_K4libdir/lib%{rname}*.so*
%_K4lib/kio_%{rname}*.so

%if_enabled marble
%files marble
%_K4plug/marble
%endif

%files data
%doc AUTHORS ChangeLog DESIGN HACKING NEWS README TODO
%_K4xdg_apps/*.desktop
%_K4apps/%rname
%exclude %_K4apps/%rname/%{rname}imageplugin_*_ui.rc
%_K4apps/showfoto
%_K4apps/solid/actions/%{rname}-opencamera.desktop
%_K4srv/%{rname}*.protocol
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
* Thu Jan 21 2016 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt3
- fix to build with liblensfun-0.3.2

* Thu Jan 21 2016 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt2
- rebuild with new liblensfun

* Tue Oct 20 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt1
- new version

* Fri Sep 11 2015 Sergey V Turchin <zerg@altlinux.org> 4.13.0-alt1
- new version

* Mon Jun 22 2015 Sergey V Turchin <zerg@altlinux.org> 4.11.0-alt1
- new version

* Thu Feb 26 2015 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Tue Feb 10 2015 Sergey V Turchin <zerg@altlinux.org> 4.7.0-alt1
- new version

* Wed Jan 28 2015 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt2
- rebuild with new gphoto

* Tue Dec 23 2014 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Thu Nov 20 2014 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Fri Oct 10 2014 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- new version

* Wed Oct 01 2014 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt2
- add fix against KDE bug 325580

* Tue Sep 23 2014 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- new version

* Mon Sep 15 2014 Sergey V Turchin <zerg@altlinux.org> 4.2.0-alt1
- new version

* Mon May 19 2014 Sergey V Turchin <zerg@altlinux.org> 4.0.0-alt1
- new version

* Fri Mar 14 2014 Sergey V Turchin <zerg@altlinux.org> 3.5.0-alt1.M70P.1
- built for M70P

* Tue Feb 04 2014 Sergey V Turchin <zerg@altlinux.org> 3.5.0-alt2
- rebuilt

* Mon Oct 14 2013 Sergey V Turchin <zerg@altlinux.org> 3.5.0-alt0.M70P.1
- built for M70P

* Fri Oct 11 2013 Sergey V Turchin <zerg@altlinux.org> 3.5.0-alt1
- new version

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 3.4.0-alt0.M70P.1
- built for M70P

* Wed Sep 11 2013 Sergey V Turchin <zerg@altlinux.org> 3.4.0-alt1
- new version

* Tue May 21 2013 Sergey V Turchin <zerg@altlinux.org> 3.2.0-alt1
- new version

* Thu Apr 18 2013 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt1
- 3.1.0 release

* Thu Dec 13 2012 Sergey V Turchin <zerg@altlinux.org> 3.0.0-alt0.1
- 3.0.0-beta3

* Fri Oct 12 2012 Sergey V Turchin <zerg@altlinux.org> 2.9.0-alt3
- fix to build with gphoto

* Fri Oct 05 2012 Sergey V Turchin <zerg@altlinux.org> 2.9.0-alt2
- rebuilt with new kde

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9.0-alt1.1
- Rebuilt with libpng15

* Wed Sep 12 2012 Aeliya Grevnyov <gray_graff@altlinux.org> 2.9.0-alt1
- 2.9.0

* Wed Sep 12 2012 Aeliya Grevnyov <gray_graff@altlinux.org> 2.7.0-alt2
- fix build

* Tue Jul 10 2012 Aeliya Grevnyov <gray_graff@altlinux.org> 2.7.0-alt1
- 2.7.0

* Sat Jul 07 2012 Aeliya Grevnyov <gray_graff@altlinux.org> 2.6.0-alt1
- 2.6.0

* Mon May 07 2012 Sergey V Turchin <zerg@altlinux.org> 2.5.0-alt1.M60P.1
- build for M60P

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
