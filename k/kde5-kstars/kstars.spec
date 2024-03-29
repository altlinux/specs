%define rname kstars
%def_disable indi
#{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%define optflags_lto %nil

Name: kde5-%rname
Version: 3.6.5
Release: alt2
Epoch: 1
%K5init no_altplace appdata

Group: Education
Summary: Desktop Planetarium
Url: http://www.kde.org
License: GPL-2.0-or-later AND GPL-3.0-or-later

ExcludeArch: armh

Provides: kde4edu-kstars = %EVR
Obsoletes: kde4edu-kstars < %EVR
Provides: kdeedu-kstars = %EVR
Obsoletes: kdeedu-kstars < %EVR

%if_enabled indi
Requires: indi
%endif
Requires: xplanet

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Mar 18 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ gtk-update-icon-cache kf5-attica-devel kf5-kdoctools-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-multimedia libqt5-network libqt5-opengl libqt5-printsupport libqt5-qml libqt5-quick libqt5-sql libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms pkg-config python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel rpm-build-gir rpm-build-python3 xml-common xml-utils zlib-devel
#BuildRequires: eigen3 extra-cmake-modules kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-kparts-devel kf5-kplotting-devel kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libGLU-devel libcfitsio-devel libindi-devel python-module-google python3.3-site-packages qt5-multimedia-devel qt5-svg-devel ruby ruby-stdlibs wcslib-devel xplanet zlib-devel-static
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel qt5-declarative-devel qt5-multimedia-devel qt5-svg-devel qt5-websockets-devel
BuildRequires: qt5-datavis3d-devel
BuildRequires: libsecret-devel libqtkeychain-qt5-devel
BuildRequires: eigen3 libGLU-devel zlib-devel
BuildRequires: libcfitsio-devel wcslib-devel libraw-devel libgsl-devel
%if_enabled indi
BuildRequires: libindi-devel
%endif
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-kparts-devel kf5-kplotting-devel
BuildRequires: kf5-kservice-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel
BuildRequires: kf5-solid-devel kf5-sonnet-devel kf5-kcrash-devel kf5-knotifyconfig-devel

%description
KStars is a Desktop Planetarium for KDE. It provides an accurate graphical
simulation of the night sky, from any location on Earth, at any date and
time. The display includes 130,000 stars, 13,000 deep-sky objects,all 8
planets, the Sun and Moon, and thousands of comets and asteroids.

%prep
%setup -n %rname-%version
%define glibc_ver %{get_version glibc-core}
%_K5if_ver_lt %glibc_ver 2.34
# libpthread.so was removed from glibc-2.34
# ld: ../lib/libKStarsLib.a(supernovaecomponent.cpp.o): undefined reference to symbol 'pthread_create@@GLIBC_2.1'
# must be from QtConcurrent::run()
sed -i '1i string(APPEND CMAKE_EXE_LINKER_FLAGS " -lpthread")' CMakeLists.txt
%endif

%build
%K5build \
    -DOpenGL_GL_PREFERENCE="GLVND" \
    #

%install
%K5install
#K5install_move data kstars sounds
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5bin/kstars
#%_K5data/kstars/
%_datadir/kstars/
%_K5icon/*/*/apps/kstars.*
#%_K5snd/KDE-KStars-*.*
%_datadir/sounds/KDE-KStars-*.*
%_K5xdgapp/org.kde.kstars.desktop
%_K5notif/kstars.notifyrc
# kauth
#%_K5libexecdir/kauth/kauth_kstars_helper
#%_K5conf_dbus_sysd/*kstars*.conf
#%_K5dbus_sys_srv/*kstars*.service
#%_datadir/polkit-1/actions/*kstars*.policy
%_K5cfg/kstars.kcfg
%_datadir/metainfo/*kstars*

%changelog
* Tue Jul 04 2023 Sergey V Turchin <zerg@altlinux.org> 1:3.6.5-alt2
- allow to build with glibc < 2.34

* Tue Jul 04 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1:3.6.5-alt1.1
- fixed build for Elbrus

* Mon Jul 03 2023 Sergey V Turchin <zerg@altlinux.org> 1:3.6.5-alt1
- new version
- update code from stable-3.6.5 branch
- moved to standart place

* Wed Nov 16 2022 Sergey V Turchin <zerg@altlinux.org> 1:3.6.1-alt2
- update code from stable-3.6.1 branch

* Mon Oct 10 2022 Sergey V Turchin <zerg@altlinux.org> 1:3.6.1-alt1
- new version

* Thu Apr 14 2022 Sergey V Turchin <zerg@altlinux.org> 1:3.5.8-alt2
- require xplanet

* Wed Apr 13 2022 Sergey V Turchin <zerg@altlinux.org> 1:3.5.8-alt1
- new version

* Wed Oct 06 2021 Sergey V Turchin <zerg@altlinux.org> 1:3.5.5-alt1
- new version

* Wed Oct 06 2021 Sergey V Turchin <zerg@altlinux.org> 1:3.5.2-alt4
- disable LTO

* Tue Aug 31 2021 Sergey V Turchin <zerg@altlinux.org> 1:3.5.2-alt3
- enable LTO

* Mon Aug 30 2021 Sergey V Turchin <zerg@altlinux.org> 1:3.5.2-alt2
- build without LTO
- build without indi

* Mon Mar 01 2021 Sergey V Turchin <zerg@altlinux.org> 1:3.5.2-alt1
- new version

* Thu Sep 03 2020 Sergey V Turchin <zerg@altlinux.org> 1:3.4.3-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 1:3.3.6-alt1
- new version

* Thu Dec 27 2018 Sergey V Turchin <zerg@altlinux.org> 1:3.0.0-alt1
- new version

* Wed Aug 01 2018 Sergey V Turchin <zerg@altlinux.org> 1:2.9.7-alt2%ubt
- fix build requires

* Fri Jul 27 2018 Sergey V Turchin <zerg@altlinux.org> 1:2.9.7-alt1%ubt
- new version

* Fri Apr 13 2018 Sergey V Turchin <zerg@altlinux.org> 1:2.9.4-alt2%ubt
- fix build requires

* Thu Apr 12 2018 Sergey V Turchin <zerg@altlinux.org> 1:2.9.4-alt1%ubt
- new version

* Fri Jan 19 2018 Sergey V Turchin <zerg@altlinux.org> 1:2.9.1-alt1%ubt
- new version

* Mon Dec 25 2017 Sergey V Turchin <zerg@altlinux.org> 1:2.8.9-alt1%ubt
- new version

* Tue Nov 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Thu Jun 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Wed Jun 07 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1%ubt
- new version

* Thu Apr 06 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Thu Sep 22 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Mon Jul 04 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Mon Apr 04 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt4
- fix build requires

* Tue Mar 22 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt3
- rebuild with new wcslib

* Tue Mar 22 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt2
- rebuild with new cfitsio

* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- initial build
