%define rname kstars
%def_disable indi
%define optflags_lto %nil

Name: %rname
Version: 3.8.2
Release: alt2
Epoch: 1
%K6init no_altplace appdata

Group: Education
Summary: Desktop Planetarium
Url: http://www.kde.org
License: GPL-2.0-or-later AND GPL-3.0-or-later

ExcludeArch: armh

Provides: kde5-kstars = %EVR
Obsoletes: kde5-kstars < %EVR

%if_enabled indi
Requires: indi
%endif
Requires: xplanet

Source: %rname-%version.tar
Source1: docs-ru.tar
Patch1: alt-check-indiless.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-multimedia-devel qt6-svg-devel qt6-websockets-devel
BuildRequires: qt6-datavis3d-devel
BuildRequires: /usr/bin/sqlite3
BuildRequires: libsecret-devel libqtkeychain-qt6-devel
BuildRequires: eigen3 libGLU-devel zlib-devel libcurl-devel libcups-devel
BuildRequires: libcfitsio-devel stellarsolver-devel wcslib-devel libraw0-devel libgsl-devel
BuildRequires: libopencv-devel
%if_enabled indi
BuildRequires: libindi-devel
%endif
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel  kf6-kio-devel kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel kf6-knewstuff-devel kf6-knotifications-devel kf6-kparts-devel kf6-kplotting-devel
BuildRequires: kf6-kservice-devel kf6-ktexteditor-devel kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel
BuildRequires: kf6-solid-devel kf6-sonnet-devel kf6-kcrash-devel kf6-knotifyconfig-devel

%description
KStars is a Desktop Planetarium for KDE. It provides an accurate graphical
simulation of the night sky, from any location on Earth, at any date and
time. The display includes 130,000 stars, 13,000 deep-sky objects,all 8
planets, the Sun and Moon, and thousands of comets and asteroids.

%prep
%setup -n %rname-%version -a1
%patch1 -p1
mv docs-ru po/ru/docs
sed -i 's|type="bool"|type="b"|' kstars/*.xml
echo "BEGIN TRANSACTION; UPDATE city SET Country = '' WHERE Country = 'Ukraine'; COMMIT;" | sqlite3 kstars/data/citydb.sqlite

%build
%add_optflags -I%_K6inc
%K6build \
    -DOpenGL_GL_PREFERENCE="GLVND" \
    -DBUILD_QT5:BOOL=OFF \
    -DBUILD_WITH_QT6:BOOL=ON \
    #

%install
%add_optflags -I%_K6inc
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/kstars
#%_K6data/kstars/
%_datadir/kstars/
%_K6icon/*/*/apps/kstars.*
#%_K6snd/KDE-KStars-*.*
%_datadir/sounds/KDE-KStars-*.*
%_K6xdgapp/org.kde.kstars.desktop
%_K6notif/kstars.notifyrc
# kauth
#%_K6libexecdir/kauth/kauth_kstars_helper
#%_K6conf_dbus_sysd/*kstars*.conf
#%_K6dbus_sys_srv/*kstars*.service
#%_datadir/polkit-1/actions/*kstars*.policy
%_K6cfg/kstars.kcfg
%_datadir/metainfo/*kstars*


%changelog
* Thu Apr 30 2026 Sergey V Turchin <zerg@altlinux.org> 1:3.8.2-alt2
- build with libraw0-devel

* Wed Apr 29 2026 Sergey V Turchin <zerg@altlinux.org> 1:3.8.2-alt1
- new version

* Thu Dec 04 2025 Sergey V Turchin <zerg@altlinux.org> 1:3.8.0-alt1
- new version

* Thu Dec 04 2025 Sergey V Turchin <zerg@altlinux.org> 1:3.7.9-alt2
- new version

* Thu Jul 31 2025 Sergey V Turchin <zerg@altlinux.org> 1:3.7.7-alt2
- cleanup citydb

* Thu Jul 03 2025 Sergey V Turchin <zerg@altlinux.org> 1:3.7.7-alt1
- new version

* Fri Nov 08 2024 Sergey V Turchin <zerg@altlinux.org> 3.7.3-alt1
- initial build

