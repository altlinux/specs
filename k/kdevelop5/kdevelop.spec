#define _unpackaged_files_terminate_build 1
%ifarch %e2k ppc64le
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

Name: kdevelop5
Version: 5.6.1
Release: alt3
Summary: A cross-platform IDE for C, C++, Python, QML/JavaScript and PHP
Group: Development/Tools
License: GPLv2
Url: http://www.kdevelop.org/
Source: v%version.tar.gz

%add_python_req_skip lldb
%add_python_req_skip gdb
%add_python3_req_skip gdb

BuildRequires(pre): rpm-build-kf5 rpm-build-python3

# Automatically added by buildreq on Sun Jan 17 2021
# optimized out: clang11.0-devel clang11.0-libs clang11.0-libs-support cmake cmake-modules docbook-dtds docbook-style-xsl fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 gtk-update-icon-cache kf5-attica-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-ki18n-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-krunner-common kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-plasma-framework-devel kf5-solid-devel kf5-sonnet-devel libcairo-gobject libdbusmenu-qt52 libgdk-pixbuf libglvnd-devel libgpg-error libopencore-amrnb0 libopencore-amrwb0 libp11-kit libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-help libqt5-network libqt5-positioning libqt5-printsupport libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-quickwidgets libqt5-sql libqt5-svg libqt5-texttospeech libqt5-waylandclient libqt5-webchannel libqt5-webenginecore libqt5-webenginewidgets libqt5-widgets libqt5-x11extras libqt5-xml librabbitmq-c libsasl2-3 libssl-devel libstdc++-devel libwayland-client libwayland-cursor libx265-192 libxcbutil-keysyms llvm11.0-devel llvm11.0-libs pkg-config python-modules python-modules-logging python2-base python3 python3-base python3-module-pkg_resources qt5-base-common qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-tools qt5-webchannel-devel sh4 shared-mime-info xml-common xml-utils xz
BuildRequires: boost-devel-headers cppcheck extra-cmake-modules git-core grantlee5-devel kde5-libkomparediff2-devel kde5-okteta-devel kdevelop-pg-qt kf5-karchive-devel kf5-kcmutils-devel kf5-kcrash-devel kf5-kdeclarative-devel kf5-kdoctools-devel kf5-kguiaddons-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kitemmodels-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-knotifyconfig-devel kf5-kpackage-devel kf5-kparts-devel kf5-krunner-devel kf5-ktexteditor-devel kf5-ktextwidgets-devel kf5-purpose-devel kf5-threadweaver-devel libastyle-devel meson plasma5-libksysguard-devel python-modules-compiler python-modules-encodings python-tools-2to3 qt5-tools-devel time

BuildRequires: python-tools-2to3 libqt5-svg libqt5-webchannel libqt5-help kdevelop-pg-qt clang-devel >= 11 llvm-devel >= 11
%if_enabled qtwebengine
BuildRequires: qt5-webengine-devel
%else
BuildRequires: qt5-webkit-devel
%endif

%description
KDevelop is a free software integrated development environment (IDE)
developed under the KDE Umbrella. KDevelop provides support for a wide
variety of languages (such as C/C++, Python, PHP, Ruby, ...) via an
extensible plugin framework.

%prep
%setup  -n kdevelop-%version
sed -i '/.etc.bash[.]bashrc/s/^/#/' kdevplatform/util/kdevplatform_shell_environment.sh
2to3 -w plugins/gdb/printers/*.py

%build
%K5cmake
%K5make

%install
%K5install
%K5install_move data kdevelop kconf_update
%K5install_move bin 'kdevelop!' kdevplatform_shell_environment.sh
echo '#!/bin/sh
exec '%_K5bin/'kdevelop!'' "$@"
' > %buildroot/%_bindir/kdevelop!
chmod +x %buildroot/%_bindir/kdevelop!

echo '#!/bin/sh
exec '%_K5bin/'kdevelop'' "$@"
' > %buildroot/%_bindir/kdevelop5
chmod +x %buildroot/%_bindir/kdevelop5

%find_lang %name --with-kde --all-name

%files -f %name.lang
%_K5bin/*
%_bindir/*
%_K5data/kdevelop
%_datadir/metainfo/*
%_xdgmimedir/packages/*
%_datadir/plasma/plasmoids/*
#_datadir/plasma/services/*
%_K5notif/*
%_K5srv/*
%_K5srvtyp/*
%_datadir/kdev*
%_K5icon/hicolor/*/*/*
%_libdir/lib*.so.*
# ???
%_libdir/libKDevelopSessionsWatch.so
%_qt5_plugindir/*
%_K5qml/org/kde/*
%_kf5_xdgapp/*
%_libdir/cmake/KDevelop
%_includedir/kdevelop

%_datadir/knsrcfiles/*
%_datadir/qlogging-categories5/*

%_includedir/kdevplatform
%_libdir/cmake/KDevPlatform
%_K5link/*

%changelog
* Fri Jan 28 2022 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt3
- build wth qtwebkit instead of qtwebengine on e2k and ppc64le

* Thu Mar 25 2021 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt2
- Fix build requires for p9 compatibility.

* Sat Jan 16 2021 Fr. Br. George <george@altlinux.ru> 5.6.1-alt1
- Autobuild version bump to 5.6.1
- Build with clang11

* Tue Jun 16 2020 Fr. Br. George <george@altlinux.ru> 5.5.2-alt1
- Autobuild version bump to 5.5.2

* Mon Jun 01 2020 Andrey Cherepanov <cas at altlinux.org> 5.4.80-alt0.1.p9
- Backport new version to p9 branch.

* Thu Jan 23 2020 Fr. Br. George <george@altlinux.ru> 5.4.80-alt1
- Autobuild version bump to 5.4.80

* Mon Nov 18 2019 Fr. Br. George <george@altlinux.ru> 5.4.4-alt1
- Autobuild version bump to 5.4.4

* Mon Jun 17 2019 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt2
- Rebuild witn new okteta

* Mon Mar 18 2019 Fr. Br. George <george@altlinux.ru> 5.3.2-alt1
- Autobuild version bump to 5.3.2

* Thu Feb 07 2019 Fr. Br. George <george@altlinux.ru> 5.3.1-alt1
- Autobuild version bump to 5.3.1

* Tue Oct 09 2018 Fr. Br. George <george@altlinux.ru> 5.2.80-alt2
- Fix user binary

* Thu Oct 04 2018 Fr. Br. George <george@altlinux.ru> 5.2.80-alt1
- Autobuild version bump to 5.2.80

* Sun Aug 12 2018 Fr. Br. George <george@altlinux.ru> 5.2.3-alt1
- Autobuild version bump to 5.2.3

* Sun Aug 12 2018 Fr. Br. George <george@altlinux.ru> 5.2.1-alt1
- Initial build for ALT

