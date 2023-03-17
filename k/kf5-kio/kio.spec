%define rname kio

%def_enable streebog

Name: kf5-%rname
Version: 5.104.0
Release: alt1
%K5init altplace

Group: System/Libraries
Summary: KDE Frameworks 5 network transparent access to files and data
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar
Source10: add-ru.po
Patch1: alt-def-trash.patch
Patch2: alt-kio-help-fallback-kde4.patch
Patch10: alt-streebog-support.patch

# Automatically added by buildreq on Tue Feb 17 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds elfutils kf5-kdoctools-devel libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libXrender-devel libXt-devel libcloog-isl4 libcom_err-devel libgpg-error libjson-c libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-script libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms libxml2-devel pkg-config python-base qt5-base-devel ruby ruby-stdlibs xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: docbook-style-xsl extra-cmake-modules gcc-c++ kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdoctools kf5-kdoctools-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libacl-devel libattr-devel libkrb5-devel libxkbfile-devel libxslt-devel python-module-google qt5-script-devel qt5-x11extras-devel rpm-build-ruby xsltproc zlib-devel-static
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: qt5-script-devel qt5-x11extras-devel qt5-tools-devel qt5-declarative-devel
BuildRequires: docbook-style-xsl extra-cmake-modules
BuildRequires: libxslt-devel xsltproc zlib-devel
BuildRequires: libacl-devel libattr-devel libkrb5-devel
BuildRequires: libmount-devel libblkid-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel
BuildRequires: kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel
BuildRequires: kf5-kdbusaddons-devel kf5-kdoctools kf5-kdoctools-devel kf5-kglobalaccel-devel
BuildRequires: kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kservice-devel kf5-ktextwidgets-devel
BuildRequires: kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel
BuildRequires: kf5-solid-devel kf5-sonnet-devel kf5-attica-devel kf5-kcrash-devel

%description
This framework implements almost all the file management functions you
will ever need. In fact, the KDE file manager (Dolphin) and the KDE
file dialog also uses this to provide its network-enabled file management.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: qt5-base-devel
Requires: kf5-kbookmarks-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kcoreaddons-devel
Requires: kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kxmlgui-devel kf5-solid-devel
Requires: kf5-kwindowsystem-devel kf5-kcrash-devel kf5-kdbusaddons-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5kiocore
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5kiocore
KF5 library

%package -n libkf5kiogui
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5kiogui
KF5 library

%package -n libkf5kiowidgets
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5kiowidgets
KF5 library

%package -n libkf5kiofilewidgets
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5kiofilewidgets
KF5 library

%package -n libkf5kiontlm
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n libkf5kiontlm
KF5 library

%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1

%if_enabled streebog
%patch10 -p2 -b .streebog
%endif

msgcat --use-first %SOURCE10 po/ru/kio5.po > po/ru/kio5.po.tmp
cat po/ru/kio5.po.tmp >po/ru/kio5.po
rm -f po/ru/kio5.po.tmp

# don't install kcm desktops
sed -i '/install.*desktop.*DESTINATION.*KDE_INSTALL_KSERVICESDIR/d' src/kcms/*/CMakeLists.txt


%build
%K5build \
%if_enabled streebog
	-DEXTRA_CRYPTO:BOOL=ON \
%endif
	#

%install
%K5install
%K5install_move data doc kconf_update kdevappwizard kdevfiletemplates
%find_lang %name --with-kde --all-name
%K5find_qtlang %name --all-name
mkdir -p %buildroot/%_K5data/kio/servicemenus/

%files common -f %name.lang
%doc LICENSES/* README.md
%dir %_K5data/kio/
%dir %_K5data/kio/servicemenus/
%_K5srvtyp/*
%_datadir/qlogging-categories5/*.*categories

%files
%config(noreplace) %_K5xdgconf/*
%_bindir/*5
%_K5bin/*
%_K5exec/*
%_K5plug/kf5/*
%_K5plug/plasma/kcms/systemsettings*
%_K5data/kcookiejar/
%_K5notif/*
%_K5plug/*.so
%_K5xdgapp/*.desktop
%_K5conf_up/*.upd
%_K5srv/*
%_K5dbus_srv/*.service
%_datadir/dbus-1/services/*.service
#
#%_K5libexecdir/kauth/*
#%_K5dbus_sys_srv/*.service
#%_datadir/polkit-1/actions/*.policy

%files devel
%_K5plug/designer/*.so
#%_K5inc/kio_version.h
%_K5inc/KIO*/
%_K5inc/kio/
%_K5link/lib*.so
%_K5lib/cmake/KF5KIO
%_K5archdata/mkspecs/modules/qt_KIO*.pri
%_K5archdata/mkspecs/modules/qt_KNTLM.pri
%_K5dbus_iface/*.xml
%_K5data/kdevappwizard/templates/*io*

%files -n libkf5kiocore
%_K5lib/libKF5KIOCore.so.*
%files -n libkf5kiogui
%_K5lib/libKF5KIOGui.so.*
%files -n libkf5kiowidgets
%_K5lib/libKF5KIOWidgets.so.*
%files -n libkf5kiofilewidgets
%_K5lib/libKF5KIOFileWidgets.so.*
%files -n libkf5kiontlm
%_K5lib/libKF5KIONTLM.so.*

%changelog
* Tue Mar 14 2023 Sergey V Turchin <zerg@altlinux.org> 5.104.0-alt1
- new version

* Mon Feb 13 2023 Sergey V Turchin <zerg@altlinux.org> 5.103.0-alt1
- new version

* Wed Feb 08 2023 Sergey V Turchin <zerg@altlinux.org> 5.102.0-alt2
- fix russian translation

* Mon Jan 16 2023 Sergey V Turchin <zerg@altlinux.org> 5.102.0-alt1
- new version

* Fri Dec 16 2022 Sergey V Turchin <zerg@altlinux.org> 5.101.0-alt1
- new version

* Fri Nov 18 2022 Sergey V Turchin <zerg@altlinux.org> 5.100.0-alt3
- update russian translation

* Thu Nov 17 2022 Michael Shigorin <mike@altlinux.org> 5.100.0-alt2
- E2K: revert 5.91.0-alt2 change, looks fixed upstream (mcst#7002)

* Mon Nov 14 2022 Sergey V Turchin <zerg@altlinux.org> 5.100.0-alt1
- new version

* Tue Oct 11 2022 Sergey V Turchin <zerg@altlinux.org> 5.99.0-alt1
- new version

* Mon Sep 12 2022 Sergey V Turchin <zerg@altlinux.org> 5.98.0-alt1
- new version

* Wed Aug 17 2022 Sergey V Turchin <zerg@altlinux.org> 5.97.0-alt2
- exclude extra config modules info

* Mon Aug 15 2022 Sergey V Turchin <zerg@altlinux.org> 5.97.0-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 5.96.0-alt1
- new version

* Mon Jul 04 2022 Sergey V Turchin <zerg@altlinux.org> 5.95.0-alt2
- don't change default proxy type

* Tue Jun 14 2022 Sergey V Turchin <zerg@altlinux.org> 5.95.0-alt1
- new version

* Mon May 16 2022 Sergey V Turchin <zerg@altlinux.org> 5.94.0-alt1
- new version

* Wed Apr 20 2022 Sergey V Turchin <zerg@altlinux.org> 5.93.0-alt2
- set default proxy type to automatic

* Mon Apr 11 2022 Sergey V Turchin <zerg@altlinux.org> 5.93.0-alt1
- new version

* Tue Mar 29 2022 Sergey V Turchin <zerg@altlinux.org> 5.92.0-alt2
- small russian translation fix

* Tue Mar 15 2022 Sergey V Turchin <zerg@altlinux.org> 5.92.0-alt1
- new version

* Tue Mar 15 2022 Michael Shigorin <mike@altlinux.org> 5.91.0-alt2
- E2K: lcc 1.25 ftbfs workaround by ilyakurdyukov (mcst#7002)

* Mon Feb 14 2022 Sergey V Turchin <zerg@altlinux.org> 5.91.0-alt1
- new version

* Mon Jan 10 2022 Sergey V Turchin <zerg@altlinux.org> 5.90.0-alt1
- new version

* Thu Dec 16 2021 Sergey V Turchin <zerg@altlinux.org> 5.89.0-alt1
- new version

* Mon Nov 15 2021 Sergey V Turchin <zerg@altlinux.org> 5.88.0-alt1
- new version

* Wed Oct 13 2021 Sergey V Turchin <zerg@altlinux.org> 5.87.0-alt2
- fix requires

* Mon Oct 11 2021 Sergey V Turchin <zerg@altlinux.org> 5.87.0-alt1
- new version

* Mon Sep 13 2021 Sergey V Turchin <zerg@altlinux.org> 5.86.0-alt1
- new version

* Mon Aug 16 2021 Sergey V Turchin <zerg@altlinux.org> 5.85.0-alt1
- new version

* Tue Jul 13 2021 Sergey V Turchin <zerg@altlinux.org> 5.84.0-alt1
- new version

* Thu Jul 01 2021 Sergey V Turchin <zerg@altlinux.org> 5.83.0-alt1
- new version

* Wed May 12 2021 Sergey V Turchin <zerg@altlinux.org> 5.82.0-alt1
- new version

* Mon Apr 12 2021 Sergey V Turchin <zerg@altlinux.org> 5.81.0-alt1
- new version

* Tue Mar 23 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 5.80.0-alt2
- Re-enabled streebog support.

* Thu Mar 18 2021 Sergey V Turchin <zerg@altlinux.org> 5.80.0-alt1
- new version

* Mon Feb 15 2021 Sergey V Turchin <zerg@altlinux.org> 5.79.0-alt1
- new version

* Sun Jan 10 2021 Sergey V Turchin <zerg@altlinux.org> 5.78.0-alt1
- new version

* Mon Dec 14 2020 Sergey V Turchin <zerg@altlinux.org> 5.77.0-alt1
- new version

* Mon Nov 16 2020 Sergey V Turchin <zerg@altlinux.org> 5.76.0-alt1
- new version

* Tue Oct 13 2020 Sergey V Turchin <zerg@altlinux.org> 5.75.0-alt1
- new version

* Mon Sep 28 2020 Sergey V Turchin <zerg@altlinux.org> 5.74.0-alt2
- fix checksum widgets layout

* Mon Sep 14 2020 Sergey V Turchin <zerg@altlinux.org> 5.74.0-alt1
- new version

* Thu Aug 13 2020 Sergey V Turchin <zerg@altlinux.org> 5.73.0-alt3
- ship to repository

* Thu Aug 13 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 5.73.0-alt2
- Re-enabled streebog support.

* Tue Aug 11 2020 Sergey V Turchin <zerg@altlinux.org> 5.73.0-alt1
- new version

* Thu Jul 23 2020 Sergey V Turchin <zerg@altlinux.org> 5.72.0-alt1
- new version

* Tue May 19 2020 Sergey V Turchin <zerg@altlinux.org> 5.70.1-alt2
- fix find executables

* Tue May 19 2020 Sergey V Turchin <zerg@altlinux.org> 5.70.1-alt1
- new version

* Tue May 12 2020 Sergey V Turchin <zerg@altlinux.org> 5.70.0-alt1
- new version

* Mon Apr 20 2020 Sergey V Turchin <zerg@altlinux.org> 5.69.0-alt2
- fix requires

* Wed Apr 15 2020 Sergey V Turchin <zerg@altlinux.org> 5.69.0-alt1
- new version

* Mon Mar 16 2020 Sergey V Turchin <zerg@altlinux.org> 5.68.0-alt1
- new version

* Mon Feb 10 2020 Sergey V Turchin <zerg@altlinux.org> 5.67.0-alt1
- new version

* Mon Jan 13 2020 Sergey V Turchin <zerg@altlinux.org> 5.66.0-alt1
- new version

* Mon Dec 16 2019 Sergey V Turchin <zerg@altlinux.org> 5.65.0-alt1
- new version

* Mon Nov 11 2019 Sergey V Turchin <zerg@altlinux.org> 5.64.0-alt1
- new version

* Fri Oct 25 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 5.63.0-alt2
- Added support for GOST R 34.11-2012 (Streebog) hash function.

* Tue Oct 15 2019 Sergey V Turchin <zerg@altlinux.org> 5.63.0-alt1
- new version

* Mon Sep 16 2019 Sergey V Turchin <zerg@altlinux.org> 5.62.0-alt1
- new version

* Mon Aug 12 2019 Sergey V Turchin <zerg@altlinux.org> 5.61.0-alt1
- new version

* Mon Jul 15 2019 Sergey V Turchin <zerg@altlinux.org> 5.60.0-alt1
- new version

* Tue Jun 11 2019 Sergey V Turchin <zerg@altlinux.org> 5.59.0-alt1
- new version

* Mon Jun 03 2019 Sergey V Turchin <zerg@altlinux.org> 5.58.0-alt1
- new version

* Mon Apr 15 2019 Sergey V Turchin <zerg@altlinux.org> 5.57.0-alt1
- new version

* Fri Mar 15 2019 Sergey V Turchin <zerg@altlinux.org> 5.56.0-alt1
- new version

* Mon Feb 11 2019 Sergey V Turchin <zerg@altlinux.org> 5.55.0-alt1
- new version

* Thu Jan 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.54.0-alt2
- new version

* Tue Jan 15 2019 Sergey V Turchin <zerg@altlinux.org> 5.54.0-alt1
- new version

* Tue Dec 11 2018 Sergey V Turchin <zerg@altlinux.org> 5.53.0-alt1
- new version

* Mon Nov 12 2018 Sergey V Turchin <zerg@altlinux.org> 5.52.0-alt1
- new version

* Wed Oct 17 2018 Sergey V Turchin <zerg@altlinux.org> 5.51.0-alt1
- new version

* Mon Sep 10 2018 Sergey V Turchin <zerg@altlinux.org> 5.50.0-alt1%ubt
- new version

* Tue Aug 21 2018 Sergey V Turchin <zerg@altlinux.org> 5.49.0-alt1%ubt
- new version

* Wed Aug 15 2018 Sergey V Turchin <zerg@altlinux.org> 5.48.0-alt2%ubt
- update russian translation

* Thu Jul 19 2018 Sergey V Turchin <zerg@altlinux.org> 5.48.0-alt1%ubt
- new version

* Fri Jun 15 2018 Sergey V Turchin <zerg@altlinux.org> 5.47.0-alt1%ubt
- new version

* Mon May 14 2018 Sergey V Turchin <zerg@altlinux.org> 5.46.0-alt1%ubt
- new version

* Fri May 04 2018 Sergey V Turchin <zerg@altlinux.org> 5.45.0-alt1%ubt
- new version

* Tue Mar 20 2018 Sergey V Turchin <zerg@altlinux.org> 5.44.0-alt1%ubt
- new version

* Thu Jan 18 2018 Sergey V Turchin <zerg@altlinux.org> 5.42.0-alt1%ubt
- new version

* Tue Dec 12 2017 Sergey V Turchin <zerg@altlinux.org> 5.41.0-alt1%ubt
- new version

* Tue Nov 21 2017 Sergey V Turchin <zerg@altlinux.org> 5.40.0-alt1%ubt
- new version

* Tue Oct 24 2017 Sergey V Turchin <zerg@altlinux.org> 5.39.0-alt1%ubt
- new version

* Tue Sep 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.38.0-alt1%ubt
- new version

* Wed Aug 16 2017 Sergey V Turchin <zerg@altlinux.org> 5.37.0-alt1%ubt
- new version

* Mon Jul 10 2017 Sergey V Turchin <zerg@altlinux.org> 5.36.0-alt1%ubt
- new version

* Thu Jun 29 2017 Sergey V Turchin <zerg@altlinux.org> 5.35.0-alt1%ubt
- new version

* Fri May 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.34.0-alt1%ubt
- new version

* Mon Apr 17 2017 Sergey V Turchin <zerg@altlinux.org> 5.33.0-alt1%ubt
- new version

* Wed Mar 29 2017 Sergey V Turchin <zerg@altlinux.org> 5.32.0-alt1%ubt
- new version

* Mon Feb 13 2017 Sergey V Turchin <zerg@altlinux.org> 5.31.0-alt1%ubt
- new version

* Wed Feb 08 2017 Sergey V Turchin <zerg@altlinux.org> 5.30.0-alt1%ubt
- new version

* Tue Dec 13 2016 Sergey V Turchin <zerg@altlinux.org> 5.29.0-alt1%ubt
- new version

* Fri Nov 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.28.0-alt0.M80P.1
- build for M80P

* Wed Nov 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.28.0-alt1
- new version

* Tue Nov 01 2016 Sergey V Turchin <zerg@altlinux.org> 5.27.0-alt2.M80P.1
- build for M80P

* Tue Nov 01 2016 Sergey V Turchin <zerg@altlinux.org> 5.27.0-alt3
- add Downloads to default user places

* Tue Nov 01 2016 Sergey V Turchin <zerg@altlinux.org> 5.27.0-alt1.M80P.1
- build for M80P

* Tue Nov 01 2016 Sergey V Turchin <zerg@altlinux.org> 5.27.0-alt2
- add Documents to default user places

* Thu Oct 13 2016 Sergey V Turchin <zerg@altlinux.org> 5.27.0-alt0.M80P.1
- build for M80P

* Tue Oct 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.27.0-alt1
- new version

* Mon Sep 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.26.0-alt1
- new version

* Mon Aug 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.25.0-alt1
- new version

* Thu Jul 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.24.0-alt2
- update requires

* Mon Jul 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.24.0-alt1
- new version

* Tue Jun 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.23.0-alt1
- new version

* Fri May 20 2016 Sergey V Turchin <zerg@altlinux.org> 5.22.0-alt1
- new version

* Mon Apr 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.21.0-alt1
- new version

* Tue Mar 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.20.0-alt1
- new version

* Tue Feb 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.19.0-alt1
- new version

* Wed Jan 20 2016 Sergey V Turchin <zerg@altlinux.org> 5.18.0-alt2
- add fallback to KDE4 docs to kio-help

* Mon Jan 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.18.0-alt1
- new version

* Fri Dec 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.17.0-alt1
- new version

* Wed Nov 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.16.0-alt1
- new version

* Wed Oct 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt2
- fix trash config dialog defaults

* Mon Oct 12 2015 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt1
- new version

* Tue Sep 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.14.0-alt2
- set trash defaults

* Mon Sep 14 2015 Sergey V Turchin <zerg@altlinux.org> 5.14.0-alt1
- new version

* Wed Aug 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.13.0-alt1
- new version

* Fri Jul 31 2015 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt2
- move dbus service to standatd place

* Fri Jul 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1
- new version

* Tue Jun 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.11.0-alt1
- new version

* Mon May 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.10.0-alt1
- new version

* Fri Apr 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.9.0-alt1
- new version

* Mon Apr 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Wed Mar 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt0.1
- test

* Mon Feb 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt0.1
- initial build
