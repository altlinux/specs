%undefine __libtoolize
%define _optlevel s
%define _keep_libtool_files 1

%define qtdir %_qt3dir
%define unstable 0
%add_findpackage_path %_K3bindir
%add_findprov_lib_path %_libdir/kde3

Name: kdetoys
Version: 3.5.13
Release: alt2

Group: Graphical desktop/KDE
Summary: K Desktop Environment - Toys and Amusements
URL: http://www.kde.org/
License: GPL

Source: kdetoys-%version.tar
#
Patch10: kdetoys-3.1.0-kweather_start_hack.patch

Requires: %name-amor = %version-%release
Requires: %name-eyes = %version-%release
Requires: %name-fifteen = %version-%release
Requires: %name-kmoon = %version-%release
Requires: %name-kodo = %version-%release
Requires: %name-kteatime = %version-%release
Requires: %name-ktux = %version-%release
Requires: %name-kweather = %version-%release
Requires: %name-kworldclock = %version-%release

# Automatically added by buildreq on Tue Apr 09 2002
#BuildRequires: XFree86-devel XFree86-libs freetype2 gcc-c++ kde-common kdebase kdelibs-devel libarts-devel libjpeg-devel liblcms libmng libpng-devel libqt3-devel libstdc++-devel libtiff-devel zlib-devel

BuildRequires(pre): kdelibs-devel
BuildRequires: gcc-c++ kde-common
#BuildRequires: kdebase
BuildRequires: libjpeg-devel liblcms libmng libpng-devel libqt3-devel
BuildRequires: libstdc++-devel libtiff-devel zlib-devel libart_lgpl-devel
BuildRequires: libpcre-devel
BuildRequires: libacl-devel libattr-devel
#BuildRequires: kdelibs-devel-cxx = %__gcc_version_base
BuildRequires: kdelibs >= %version kdelibs-devel >= %version

%description
Toys for the K Desktop Environment.

Software included in this package are:
	- amor: Amusing Misuse Of Resources put's comic figures above your windows
	- eyes: a kicker applet similar to XEyes
	- fifteen: kicker applet, order 15 pieces in a 4x4 square by moving them
	- kmoon: system tray applet showing the moon phase
	- kodo: mouse movement meter
	- kteatime: system tray applet that makes sure your tea doesn't get too strong
	- ktux: Tux-in-a-Spaceship screen saver
	- kweather: kicker applet that will display the current weather outside
	- kworldwatch: application and kicker applet showing daylight area on the world globe

%package common
Summary: Common empty package for %name
Group: Graphical desktop/KDE
Requires: kde-common >= 3.2
Conflicts: kdetoys <= 3.1.0-alt2
#
%description common
Common empty package for %name

%package devel
Summary: Headers files for kdetoys
Group: Development/KDE and QT
Requires: %name-common = %version-%release
Requires: %name-amor = %version-%release

%description devel
Headers files for kdetoys.

%package amor
Summary: Put's comic figures above your windows
Group: Toys
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description amor
Amusing Misuse Of Resources put's comic figures above your windows

%package eyes
Summary: KDE kicker applet similar to XEyes
Group: Toys
Requires: kdebase-wm, %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description eyes
KDE kicker applet similar to XEyes

%package fifteen
Summary: KDE kicker applet, order 15 pieces in a 4x4 square by moving them
Group: Toys
Requires: kdebase-wm, %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description fifteen
KDE kicker applet, order 15 pieces in a 4x4 square by moving them

%package kmoon
Summary: KDE system tray applet showing the moon phase
Group: Toys
Requires: kdebase-wm, %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kmoon
KDE system tray applet showing the moon phase

%package kodo
Summary: Mouse movement meter
Group: Toys
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kodo
Mouse movement meter

%package kteatime
Summary: KDE applet that makes sure your tea doesn't get too strong
Group: Toys
Requires: kdebase-wm, %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kteatime
KDE system tray applet that makes sure your tea
doesn't get too strong

%package ktux
Summary: Tux-in-a-Spaceship screen saver for KDE
Group: Toys
Requires: kdebase-wm, %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description ktux
Tux-in-a-Spaceship screen saver for KDE

%package kweather
Summary: KDE kicker applet to display the current weather
Group: Toys
Requires: kdebase-wm, %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kweather
KDE kicker applet that will display the current weather outside

%package kworldclock
Summary: Showing daylight area on the world globe
Group: Toys
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kworldclock
Application and KDE kicker applet showing daylight area
on the world globe

%prep
%setup -q -n kdetoys-%version
cp -ar altlinux/admin ./
#%patch10 -p1

sed -i '\|\${kdeinit}_LDFLAGS[[:space:]]=[[:space:]].*-no-undefined|s|-no-undefined|-no-undefined -Wl,--warn-unresolved-symbols|' admin/am_edit
for f in `find $PWD -type f -name Makefile.am`
do
    sed -i -e '\|_la_LDFLAGS.*[[:space:]]-module[[:space:]]|s|-module|-module \$(KDE_PLUGIN)|' $f
    #sed -i -e '\|_la_LDFLAGS.*[[:space:]]-no-undefined|s|-no-undefined|-no-undefined -Wl,--allow-shlib-undefined|' $f
    grep -q -e 'lib.*SOURCES' $f || continue
    RPATH_LINK_OPTS+=" -Wl,-rpath-link,`dirname $f`/.libs"
done
sed -i "s|\(-Wl,--as-needed\)| $RPATH_LINK_OPTS \1|g" admin/acinclude.m4.in
sed -i -e 's|\$USER_INCLUDES|-I%_includedir/tqtinterface \$USER_INCLUDES|' admin/acinclude.m4.in

find ./ -type f -name Makefile.am | \
while read f
do
    sed -i -e 's|\(.*_la_LIBADD[[:space:]]*\)=\(.*\)|\1= -lDCOP -lkdefx \$(LIB_KUTILS) \$(LIB_KHTML) \$(LIB_KIO) \$(LIB_KDEUI) \$(LIB_KDECORE) \$(LIB_QT) \2|' $f
done

make -f admin/Makefile.common cvs ||:


%build
rm -rf %buildroot
export QTDIR=%qtdir
export KDEDIR=%prefix

export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

export LD_LIBRARY_PATH=$QTDIR/%_lib:$KDEDIR/%_lib:$LD_LIBRARY_PATH
export LDFLAGS="-L%buildroot/%_libdir -L%buildroot/%_libdir/kde3 -L%_libdir"
%K3configure \
    --disable-gcc-hidden-visibility \
%if %unstable
    --enable-debug=full \
%else
    --disable-debug \
%endif
    --enable-final

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%if %unstable
%set_strip_method none
%endif

%K3install


%files
%files common

%files amor
%_K3bindir/amor
%_K3apps/amor
%_kde3_iconsdir/hicolor/*/apps/amor.png
%doc %_K3doc/en/amor
%_K3xdg_apps/amor.desktop

%files eyes
%_K3lib/eyes_panelapplet.so*
%_K3apps/kicker/applets/eyesapplet.desktop

%files fifteen
%_K3lib/fifteen_panelapplet.so*
%_K3apps/kicker/applets/kfifteenapplet.desktop

%files kmoon
%_K3lib/kmoon_panelapplet.so*
%_K3apps/kmoon
%_kde3_iconsdir/hicolor/*/apps/kmoon.png
%_K3apps/kicker/applets/kmoonapplet.desktop
%doc %_K3doc/en/kmoon/

%files kodo
%_K3bindir/kodo
%_K3xdg_apps/kodo.desktop
%_K3apps/kodo
%_kde3_iconsdir/hicolor/*/apps/kodo.png
%doc %_K3doc/en/kodo/

%files kteatime
%_K3bindir/kteatime
%_K3xdg_apps/kteatime.desktop
%_K3apps/kteatime
%doc %_K3doc/en/kteatime/
%_kde3_iconsdir/hicolor/*/apps/kteatime.png

%files ktux
%_K3bindir/ktux
%_K3applnk/System/ScreenSavers/ktux.desktop
%_K3apps/ktux
%_kde3_iconsdir/hicolor/*/apps/ktux.png

%files kweather
%_K3bindir/kweatherservice
%_K3bindir/kweatherreport
%_K3libdir/libkdeinit_kweatherreport.so*
%_K3lib/weather_panelapplet.so*
%_K3lib/kcm_weather.so*
%_K3lib/kcm_weatherservice.so*
%_K3lib/kweatherreport.so*
%_K3apps/kicker/applets/kweather.desktop
%_K3apps/kweather
%_K3apps/kweatherservice
%_K3srv/k*weather*.desktop
%_kde3_iconsdir/hicolor/*/apps/kweather.png
%doc %_K3doc/en/kweather/

%files kworldclock
%_K3bindir/kworldclock
%_K3lib/ww_panelapplet.so*
%_K3xdg_apps/kworldclock.desktop
%_K3apps/kdesktop/programs/kdeworld.desktop
%_K3apps/kicker/applets/kwwapplet.desktop
%_K3apps/kworldclock
%_kde3_iconsdir/hicolor/*/apps/kworldclock.png
%doc %_K3doc/en/kworldclock/

%files devel
%if %_keep_libtool_files
#%_K3libdir/*.la
%endif
%_K3includedir/*.h


%changelog
* Fri Jun 15 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt2
- Automake version is fixed to 1.11.5 detect.

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt1
- TDE 3.5.13 release build

* Fri Feb 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.12-alt2.2
- Removed bad RPATH

* Wed Apr 20 2011 Andrey Cherepanov <cas@altlinux.org> 3.5.12-alt2.1
- remove xorg-x11-devel requirement

* Thu Mar 03 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt2
- move to alternate place

* Tue Dec 28 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt1
- new version

* Wed Mar 10 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt2
- fix to build with new autotools

* Wed Aug 27 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt1
- new version

* Tue Feb 26 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt1
- new version

* Wed Oct 17 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt1
- new version

* Thu May 24 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt1
- new version

* Mon Jan 29 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt1
- new version

* Tue Oct 17 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt1
- new version

* Tue Sep 05 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.4-alt1
- new version

* Wed Jun 07 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.3-alt1
- new version

* Thu Apr 06 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.2-alt1
- new version

* Thu Feb 02 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt1
- new version

* Thu Dec 08 2005 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt1
- new version

* Wed Jun 08 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt1
- new version

* Fri Apr 01 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.0-alt1
- new version

* Tue Jan 11 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt1
- rebuild

* Wed Jan 05 2005 ZerG <zerg@altlinux.ru> 3.3.2-alt0.0.M24
- new version

* Thu Oct 07 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt1
- new version

* Mon Oct 04 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.0-alt1
- new version

* Mon Jun 07 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt1
- new version

* Thu Apr 15 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt1
- new version

* Thu Mar 18 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt1
- update code from KDE_3_2_BRANCH

* Mon Mar 15 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.0-alt1
- new version
- update code from KDE_3_2_BRANCH

* Mon Sep 22 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt1
- update code from cvs

* Thu Aug 21 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt1
- update code from cvs

* Thu Jul 03 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt2
- update code from cvs

* Mon Jun 02 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.2-alt1
- update from cvs KDE_3_1_BRANCH

* Tue May 06 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.1-alt2
- update from cvs KDE_3_1_BRANCH

* Wed Apr 02 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt1
- update from cvs KDE_3_1_BRANCH

* Tue Feb 04 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt5
- update from cvs

* Wed Jan 15 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt4
- add losted kdetoys package

* Mon Jan 13 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt3
- split

* Thu Dec 26 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt2
- update from cvs
- fix kweather start

* Fri Nov 29 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt1
- update from cvs

* Sun Nov 10 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.20.rc2
- rc2

* Mon Nov 04 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.20.rc1
- rc1. Increase %release to easy check dependencies

* Mon Oct 21 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.10
- update from cvs

* Wed Sep 11 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt2
- rebuild with gcc 3.2 && objprelink
- sync patches with cooker

* Tue Aug 20 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt1
- update from cvs

* Mon Aug 12 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.2-alt1
- new version

* Wed May 29 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt1
- new version

* Tue Apr 30 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt2
- move to /usr

* Tue Apr 09 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt1
- build for ALT

* Thu Apr 04 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-2mdk
- Fix update menu

* Wed Mar 27 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-1mdk
- kde3.0

* Fri Mar 22 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.rc3.1mdk
- RC3

* Sat Mar 16 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.rc2.1mdk
- Rc2

* Sun Jan 27 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta2.1mdk
- beta2

* Tue Jan 15 2002 David BAUDENS <baudens@mandrakesoft.com> 3.0-0.beta1.5mdk
- Fix conflict with kdetoys2

* Sun Jan 13 2002 David BAUDENS <baudens@mandrakesoft.com> 3.0-0.beta1.4mdk
- Allow KDE 2 and KDE 3 to be installed in same time
- Don't build static libraries
- Remove KDE 2's changelogs (KDE 2 and KDE 3 spec files have a separate life
  now)
- Fix previous changelog
- Fix menu generation
- Fix ./configure

* Thu Dec 20 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta1.3mdk
- Rename to allow KDE 2 and KDE 3 to be installed in same time

* Sat Dec 08 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0beta1-3mdk
- kde 3.0 beta1

* Thu Nov 29 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-2mdk
- Improved spec file

* Fri Nov 23 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-1mdk
- kde 3.0 try
