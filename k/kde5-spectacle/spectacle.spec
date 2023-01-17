%define rname spectacle
%ifndef _unitdir_user
%define _unitdir_user %prefix/lib/systemd/user
%endif
%define service_name app-org.kde.spectacle

Name: kde5-%rname
Version: 22.12.1
Release: alt1
%K5init altplace no_appdata

Group: Graphical desktop/KDE
Summary: The KDE Screenshot Utility
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar
Patch1: alt-services-paths.patch
Patch2: alt-desktop-exec.patch
Patch3: alt-kimageannotator-tr.patch
Patch4: alt-def-capture-mode.patch

# Automatically added by buildreq on Wed May 11 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ gtk-update-icon-cache kf5-kdoctools kf5-kdoctools-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcb-devel libxcb-render-util libxcbutil-cursor libxcbutil-image libxcbutil-keysyms perl pkg-config python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 xml-common xml-utils
#BuildRequires: extra-cmake-modules kde5-libkipi-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdelibs4support kf5-kdoctools-devel kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kpackage-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-libkscreen-devel kf5-solid-devel libxcbutil-cursor-devel libxcbutil-devel libxcbutil-image-devel python-module-google python3-dev qt5-declarative-devel qt5-x11extras-devel ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-declarative-devel qt5-x11extras-devel qt5-svg-devel
BuildRequires: libxcbutil-cursor-devel libxcbutil-devel libxcbutil-image-devel
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdeclarative-devel kf5-kdelibs4support kf5-kdoctools-devel
BuildRequires: kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kpackage-devel
BuildRequires: kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel
BuildRequires: kf5-solid-devel kf5-knewstuff-devel kf5-kglobalaccel-devel kf5-kwayland-devel
BuildRequires: kf5-purpose-devel
BuildRequires: plasma5-libkscreen-devel
BuildRequires: kde5-kcolorpicker-devel kde5-kimageannotator-devel

%description
Spectacle is screenshot taking utility for the KDE desktop. Spectacle
can also be used in non-KDE X11 desktop environments.

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
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1
#%patch3 -p1
#%patch4 -p1

%build
%K5build \
    -DDATA_INSTALL_DIR=%_K5data \
    #

%install
%K5install
%K5install_move data kglobalaccel kconf_update locale
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5bin/spectacle
%_K5conf_bin/*spectacle*
%_K5conf_up/*spectacle*
%_K5xdgapp/org.kde.spectacle.desktop
%_K5icon/hicolor/*/apps/spectacle.*
%_K5notif/spectacle.notifyrc
%_K5data/kglobalaccel/*spectacle*.desktop
%_K5dbus_srv/org.kde.Spectacle.service
%_K5conf_up/*.upd
%_K5conf_up/*.py
%_datadir/qlogging-categories5/*.*categories
%_unitdir_user/%service_name.service

#%files devel
#%_K5dbus_iface/org.kde.Spectacle.xml

%changelog
* Wed Jan 11 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.1-alt1
- new version

* Mon Nov 07 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt1
- new version

* Tue Oct 18 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.2-alt1
- new version

* Thu Sep 15 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.1-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.3-alt1
- new version

* Fri Jun 10 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.2-alt1
- new version

* Fri May 13 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.1-alt1
- new version

* Fri Mar 04 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.3-alt1
- new version

* Mon Jan 17 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt1
- new version

* Mon Nov 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.3-alt1
- new version

* Fri Oct 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.2-alt1
- new version

* Thu Sep 02 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.1-alt1
- new version

* Mon Aug 23 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.0-alt1
- new version

* Thu Jul 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.3-alt1
- new version

* Thu Jun 10 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.2-alt1
- new version

* Mon Jun 07 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.1-alt2
- fix paths to binary in service files

* Wed May 19 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.1-alt1
- new version

* Thu Apr 01 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.3-alt2
- load kimageannotator translations

* Thu Mar 11 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.3-alt1
- new version

* Fri Feb 19 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.2-alt2
- build with kf5-purpose

* Fri Feb 05 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.2-alt1
- new version

* Thu Jan 14 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.1-alt1
- new version

* Fri Dec 18 2020 Sergey V Turchin <zerg@altlinux.org> 20.12.0-alt1
- new version

* Wed Nov 25 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.3-alt1
- new version

* Wed Oct 14 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.2-alt1
- new version

* Thu Sep 24 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.1-alt2
- fix startup from desktop-file

* Fri Sep 18 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.1-alt1
- new version

* Fri Aug 14 2020 Sergey V Turchin <zerg@altlinux.org> 20.04.3-alt1
- new version

* Thu Mar 12 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.3-alt1
- new version

* Fri Feb 14 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.2-alt1
- new version

* Tue Jan 21 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Fri Nov 08 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.3-alt1
- new version

* Fri Oct 25 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.2-alt1
- new version

* Tue Sep 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Tue Aug 27 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Thu Jul 18 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Mon Jun 10 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Mon May 06 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Wed Mar 20 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Tue Feb 19 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Wed Dec 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt4
- update russian translation

* Tue Nov 06 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt3
- build without purpose

* Fri Oct 26 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt2
- update russian translation

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Wed Jul 04 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Thu May 31 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt2%ubt
- update build requires

* Tue May 22 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Mar 06 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.2-alt1%ubt
- new version

* Mon Nov 13 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Tue May 02 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1%ubt
- new version

* Thu Mar 23 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Thu Nov 24 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt0.M80P.1
- build for M80P

* Wed Nov 23 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1
- new version

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Tue Sep 06 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.0-alt1
- new version

* Thu Jul 14 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.3-alt1
- new version

* Fri Jul 01 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Fri Apr 01 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.3-alt1
- new version

* Wed Mar 23 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt2
- rebuild wit new libkscreen

* Fri Feb 26 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Wed Jan 20 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Wed Sep 30 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- initial build
