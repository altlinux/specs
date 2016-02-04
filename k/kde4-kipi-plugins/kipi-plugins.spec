%define libsover 4
%define libkipiplugins libkipiplugins%libsover

%define rname kipi-plugins
Name: kde4-%rname
%define beta %nil
Version: 4.14.0
Release: alt2

Group: Graphics
Summary: KDE image Interface Plugins
License: GPLv2, ADOBE DNG SDK
Url: http://www.kipi-plugins.org/
Packager: Sergey V Turchin <zerg@altlinux.org>

Source0: %rname-%version.tar
Source1: %rname-po-%version.tar
Source2: %rname-doc-%version.tar
Source10: FindOpenCV.cmake
Source11: FindKSane.cmake
Source12: FindKipi.cmake
Patch1: alt-arm-cast-to-qreal.patch
Patch2: alt-lib-version.patch
Patch3: alt-find-qtsoap.patch
Patch4: alt-fix-build.patch

Requires: %name-core
Requires: %name-expoblending
Requires: %name-panorama
Conflicts: kipi-plugins <= 3:0.1.6-alt5

# Automatically added by buildreq on Thu Apr 16 2009 (-bi)
#BuildRequires: gcc-c++ kde4graphics-devel kde4pimlibs-devel libGL-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXdmcp-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libexpat-devel libgio-devel libgpod-devel libgtk+2-common-devel libnss-fallback libopencv-devel libqt3-devel libsane-devel libxkbfile-devel libxslt-devel nvidia_glx_180.44 subversion xorg-xf86vidmodeproto-devel xsltproc
BuildRequires(pre): kde4libs-devel kde4graphics-devel
BuildRequires: gcc-c++ kde4pimlibs-devel libgomp-devel libkgeomap-devel qjson-devel libqca2-devel
BuildRequires: libgio-devel libgpod-devel libgtk+2-devel boost-devel
BuildRequires: libopencv-devel libsane-devel libxslt-devel xsltproc libexpat-devel libxml2-devel libjpeg-devel
BuildRequires: qoauth-devel libkqoauth-devel qjson-devel herqq-devel qtsoap-devel
BuildRequires: qt-gstreamer1-devel libImageMagick-devel ImageMagick-tools
BuildRequires: libkvkontakte-devel libmediawiki-devel libtiff-devel flex

%description
The library of the KDE Image Plugin Interface used by digiKam and Gwenview

%package common
Summary: %name common package
Group: System/Configuration/Other
Requires: kde-common
Conflicts: kde4-kipi-plugins <= 1.1.0-alt1
%description common
%name common package

%package core
Group: Graphics
Summary: Core files for %name
Requires: %name-common = %version-%release
Requires: icc-profiles /usr/bin/convert
%description core
Core files for %name

%package expoblending
Group: Graphics
Summary: A tool to blend bracketed images
Requires: %name-common = %version-%release
Requires: hugin enblend
%description expoblending
A tool to blend bracketed images

%package panorama
Group: Graphics
Summary: A tool to assemble images as a panorama
Requires: %name-common = %version-%release
Requires: hugin enblend
%description panorama
A tool to assemble images as a panorama

%package -n %libkipiplugins
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n %libkipiplugins
KDE 4 library.

%prep
%setup -q -n %rname-%version -a1 -a2
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
mv %rname-po-%version po
mv %rname-doc-%version doc
#install -m 0644 %SOURCE10 cmake/modules
install -m 0644 %SOURCE11 cmake/modules
install -m 0644 %SOURCE12 cmake/modules

if ! grep -qe '^add_subdirectory([[:space:]]*po[[:space:]]*)' CMakeLists.txt
then
cat >> CMakeLists.txt <<__EOF__
find_package(Msgfmt REQUIRED)
find_package(Gettext REQUIRED)
add_subdirectory( po )
__EOF__
fi

if ! grep -qe '^add_subdirectory([[:space:]]*doc[[:space:]]*)' CMakeLists.txt
then
cat >> CMakeLists.txt <<__EOF__
add_subdirectory( doc )
__EOF__
fi

%build
%K4cmake -DImageMagick_INCLUDE_DIRS=%_includedir/ImageMagick-6
%K4make

%install
%K4install

rm -f %buildroot/%_K4i18n/*/*/digikam*
rm -f %buildroot/%_K4i18n/*/*/libkipi.*
rm -f %buildroot/%_K4i18n/*/*/libkgeomap*
%K4find_lang --with-kde %rname
find %buildroot/%_K4i18n -type f -name kipiplugin\*.mo | sed "s|\.mo$||" | \
while read f; do echo `basename "$f"`; done | sort -u | \
while read n
do
    %K4find_lang --with-kde --append --output=%rname.lang "$n"
done

%files
%files common

%files core -f %rname.lang
%doc AUTHORS ChangeLog README TODO NEWS COPYING-*
#%_K4bindir/dnginfo
%_K4bindir/dngconverter
#%_K4bindir/multithread
%_K4bindir/photolayoutseditor
%_K4bindir/scangui
%_K4lib/kipiplugin_*.so
#%_K4lib/photolayoutseditor*plugin_*.so
%_K4apps/kipi/
%_K4apps/kipiplugin_*/
%_K4apps/gpssync/
%_K4apps/photolayoutseditor/
%_K4cfg/photolayoutseditor.kcfg
%_K4srv/kipiplugin_*
#%_K4srv/photolayoutseditor*plugin_*.desktop
%_K4srvtyp/photolayoutseditor*plugin.desktop
%_K4iconsdir/oxygen/*/*/*.*
%_K4iconsdir/hicolor/*/*/*.*
%_K4xdg_apps/dngconverter.desktop
%_K4xdg_apps/kipiplugins.desktop
%_K4xdg_apps/photolayoutseditor.desktop
%_K4xdg_apps/scangui.desktop
%_K4tmpl/kipiplugins_photolayoutseditor/
# exclude expoblending
%exclude %_K4lib/kipiplugin_expoblending.so
%exclude %_K4srv/kipiplugin_expoblending.desktop
%exclude %_K4apps/kipiplugin_expoblending
# exclude panorama
%exclude %_K4lib/kipiplugin_panorama.so
%exclude %_K4apps/kipi/kipiplugin_panoramaui.rc
%exclude %_K4apps/kipiplugin_panorama/
%exclude %_K4srv/kipiplugin_panorama.desktop

%files expoblending
%_K4bindir/expoblending
%_K4lib/kipiplugin_expoblending.so
%_K4apps/kipiplugin_expoblending
%_K4srv/kipiplugin_expoblending.desktop
%_K4xdg_apps/expoblending.desktop

%files panorama
%_K4bindir/panoramagui
%_K4lib/kipiplugin_panorama.so
%_K4apps/kipi/kipiplugin_panoramaui.rc
%_K4apps/kipiplugin_panorama/
%_K4srv/kipiplugin_panorama.desktop
%_K4xdg_apps/panoramagui.desktop

%files -n %libkipiplugins
%_K4libdir/libkipiplugins.so.%libsover
%_K4libdir/libkipiplugins.so.%libsover.*

%changelog
* Thu Feb 04 2016 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt2
- split panorama to separate subpackage

* Tue Oct 20 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt1
- new version

* Fri Sep 11 2015 Sergey V Turchin <zerg@altlinux.org> 4.13.0-alt1
- new version

* Mon Jun 22 2015 Sergey V Turchin <zerg@altlinux.org> 4.11.0-alt1
- new version

* Tue Dec 23 2014 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Thu Dec 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt0.M70P.1
- built for M70P

* Thu Nov 20 2014 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Fri Oct 10 2014 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- new version

* Mon Sep 29 2014 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt2
- build with qt-gstreamer1

* Tue Sep 23 2014 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- new version

* Mon Sep 15 2014 Sergey V Turchin <zerg@altlinux.org> 4.2.0-alt1
- new version

* Mon May 19 2014 Sergey V Turchin <zerg@altlinux.org> 4.0.0-alt1
- new version

* Wed Apr 02 2014 Sergey V Turchin <zerg@altlinux.org> 3.5.0-alt4
- rebuilt with new ImageMagick

* Fri Mar 14 2014 Sergey V Turchin <zerg@altlinux.org> 3.5.0-alt2.M70P.1
- built for M70P

* Tue Feb 04 2014 Sergey V Turchin <zerg@altlinux.org> 3.5.0-alt3
- rebuilt

* Mon Oct 14 2013 Sergey V Turchin <zerg@altlinux.org> 3.5.0-alt1.M70P.1
- built for M70P

* Mon Oct 14 2013 Sergey V Turchin <zerg@altlinux.org> 3.5.0-alt2
- fix requires

* Fri Oct 11 2013 Sergey V Turchin <zerg@altlinux.org> 3.5.0-alt1
- new version

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 3.4.0-alt0.M70P.1
- built for M70P

* Tue Sep 10 2013 Sergey V Turchin <zerg@altlinux.org> 3.4.0-alt1
- new version

* Thu May 30 2013 Sergey V Turchin <zerg@altlinux.org> 3.2.0-alt2
- fix to build with new ImageMagick

* Tue May 21 2013 Sergey V Turchin <zerg@altlinux.org> 3.2.0-alt1
- new version

* Thu Apr 18 2013 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt2
- rebuild with new ImageMagick

* Thu Apr 18 2013 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt1
- 3.1.0 release

* Mon Feb 11 2013 Sergey V Turchin <zerg@altlinux.org> 3.0.0-alt1
- 3.0.0 release

* Wed Jan 16 2013 Sergey V Turchin <zerg@altlinux.org> 3.0.0-alt0.4
- fix to build VideoSlideshow plugin

* Fri Jan 11 2013 Sergey V Turchin <zerg@altlinux.org> 3.0.0-alt0.3
- 3.0.0-rc

* Fri Dec 21 2012 Sergey V Turchin <zerg@altlinux.org> 3.0.0-alt0.2
- fix desktop files X-KIPI-BinaryVersion

* Thu Dec 13 2012 Sergey V Turchin <zerg@altlinux.org> 3.0.0-alt0.1
- 3.0.0-beta3

* Fri Oct 05 2012 Sergey V Turchin <zerg@altlinux.org> 2.9.0-alt2
- rebuild with new kde

* Tue Oct 02 2012 Sergey V Turchin <zerg@altlinux.org> 2.9.0-alt1
- new version

* Tue Oct 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.1
- Rebuilt with libopencv2.4

* Wed Jul 11 2012 Sergey V Turchin <zerg@altlinux.org> 2.7.0-alt0.M60P.1
- built for M60P

* Wed Jul 11 2012 Sergey V Turchin <zerg@altlinux.org> 2.7.0-alt1
- new version

* Thu Jun 28 2012 Sergey V Turchin <zerg@altlinux.org> 2.6.0-alt0.M60P.1
- built for M60P

* Thu Jun 14 2012 Sergey V Turchin <zerg@altlinux.org> 2.6.0-alt1
- new version

* Fri May 04 2012 Sergey V Turchin <zerg@altlinux.org> 2.5.0-alt4
- fix compile on arm; thanks sbolshakov@alt

* Sat Apr 21 2012 Sergey V Turchin <zerg@altlinux.org> 2.5.0-alt3
- fix to build mediawiki plugin

* Thu Apr 19 2012 Sergey V Turchin <zerg@altlinux.org> 2.5.0-alt1.M60P.1
- build for M60P

* Thu Apr 19 2012 Sergey V Turchin <zerg@altlinux.org> 2.5.0-alt2
- build vkontakte and mediawiki plugins

* Tue Jan 10 2012 Sergey V Turchin <zerg@altlinux.org> 2.5.0-alt0.M60P.1
- built for M60P

* Tue Jan 10 2012 Sergey V Turchin <zerg@altlinux.org> 2.5.0-alt1
- new version

* Tue Dec 27 2011 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt0.M60P.1
- built for M60P

* Mon Nov 07 2011 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 2.2.0-alt1.M60P.1
- built for M60P

* Mon Oct 24 2011 Sergey V Turchin <zerg@altlinux.org> 2.2.0-alt2
- fix to build Shwup and YandexFotki plugins

* Wed Oct 19 2011 Sergey V Turchin <zerg@altlinux.org> 2.2.0-alt1
- new version

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 1.9.0-alt2.M60T.1
- built for M60T

* Wed Sep 21 2011 Sergey V Turchin <zerg@altlinux.org> 1.9.0-alt3
- rebuilt with kde-4.7

* Fri Apr 22 2011 Sergey V Turchin <zerg@altlinux.org> 1.9.0-alt2
- fix build requires

* Fri Mar 11 2011 Sergey V Turchin <zerg@altlinux.org> 1.9.0-alt1
- new version
- fix conflict with kipi-plugins

* Tue Feb 22 2011 Sergey V Turchin <zerg@altlinux.org> 1.8.0-alt1
- new version

* Tue Feb 22 2011 Sergey V Turchin <zerg@altlinux.org> 1.7.0-alt3
- move to stantart place

* Thu Feb 03 2011 Sergey V Turchin <zerg@altlinux.org> 1.7.0-alt2
- rebuilt with kde-4.6

* Thu Dec 23 2010 Sergey V Turchin <zerg@altlinux.org> 1.7.0-alt1
- new version

* Tue Dec 14 2010 Sergey V Turchin <zerg@altlinux.org> 1.6.0-alt2
- fix link with new opencv2 (thanks real@alt)

* Tue Nov 23 2010 Sergey V Turchin <zerg@altlinux.org> 1.6.0-alt1
- new version
- built with opencv2 (thanks real@alt)

* Tue Oct 12 2010 Sergey V Turchin <zerg@altlinux.org> 1.5.0-alt1
- new version

* Fri Aug 13 2010 Sergey V Turchin <zerg@altlinux.org> 1.3.0-alt1
- new version

* Thu Apr 22 2010 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt0.M51.3
- rebuilt with new KDE

* Mon Mar 29 2010 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt0.M51.1
- built for M51

* Mon Mar 29 2010 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt1
- new version

* Fri Mar 12 2010 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt3
- rebuilt with new opencv

* Tue Mar 09 2010 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt1.M51.1
- built for M51

* Tue Mar 09 2010 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt2
- split expoblending to separate package (able only with kde-4.4) (ALT#23087)

* Thu Mar 04 2010 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt0.M51.1
- built for M51

* Thu Mar 04 2010 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt1
- new version

* Thu Jan 28 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt3
- rebuilt with kde-4.4

* Tue Dec 29 2009 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt1.M51.1
- built for M51

* Tue Dec 29 2009 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt2
- require ImageMagick-tools(convert)

* Thu Dec 24 2009 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt0.M51.1
- built for M51

* Thu Dec 24 2009 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt1
- new version

* Wed Dec 09 2009 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt0.M51.1
- built for M51

* Tue Dec 08 2009 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt1
- new version

* Thu Nov 12 2009 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt0.M51.1
- built for M51

* Thu Nov 12 2009 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt1
- new version

* Tue Sep 29 2009 Sergey V Turchin <zerg@altlinux.org> 0.7.0-alt1
- new version

* Tue Sep 01 2009 Sergey V Turchin <zerg@altlinux.org> 0.6.0-alt1
- new version

* Fri Aug 07 2009 Sergey V Turchin <zerg@altlinux.org> 0.5.0-alt0.M50.1
- built for M50

* Fri Aug 07 2009 Sergey V Turchin <zerg@altlinux.org> 0.5.0-alt1
- new version

* Thu Jul 23 2009 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt2
- update to svn r1001493

* Tue Jul 14 2009 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt0.M50.1
- built for M50

* Tue Jul 14 2009 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- new version

* Tue Jun 23 2009 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt2
- rebuilt

* Wed May 13 2009 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt1
- new version

* Thu Apr 16 2009 Sergey V Turchin <zerg at altlinux dot org> 0.2.0-alt1
- initial specfile
