%define rname kleopatra

%define kleopatraclientcore_sover 1
%define libkleopatraclientcore libkleopatraclientcore%kleopatraclientcore_sover
%define kleopatraclientgui_sover 1
%define libkleopatraclientgui libkleopatraclientgui%kleopatraclientgui_sover

Name: kde5-%rname
Version: 22.12.2
Release: alt1
%K5init no_appdata

Group: Graphical desktop/KDE
Summary: Certificate Manager for KDE
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Provides: kde5-pim-kleopatra = %EVR
Obsoletes: kde5-pim-kleopatra < %EVR
Requires: gnupg2 dirmngr pinentry-x11

Source: %rname-%version.tar
Patch1: alt-gpgme17.patch

# Automatically added by buildreq on Fri Apr 29 2016 (-bi)
# optimized out: boost-devel-headers cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ glibc-devel-static gtk-update-icon-cache kf5-kdoctools kf5-kdoctools-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libgpg-error-devel libjson-c libkf5gpgmepp-pthread libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs xml-common xml-utils
#BuildRequires: extra-cmake-modules kde5-gpgmepp-devel kde5-kmime-devel kde5-libkleo-devel kf5-kauth-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdoctools-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-knotifications-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-sonnet-devel libassuan-devel libgpgme-devel python-module-google python3-dev rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules boost-devel
BuildRequires: libassuan-devel libgpgme-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kdoctools-devel
BuildRequires: kf5-ki18n-devel kf5-kiconthemes-devel kf5-knotifications-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-sonnet-devel kf5-kitemmodels-devel
BuildRequires: kf5-kcrash-devel kf5-kwallet-devel
BuildRequires: kde5-kmime-devel kde5-libkleo-devel kf5-kauth-devel kf5-kcmutils-devel kf5-kcodecs-devel kf5-kconfig-devel
BuildRequires: kde5-kidentitymanagement-devel kde5-kmailtransport-devel kde5-kpimtextedit-devel kde5-akonadi-mime-devel kde5-akonadi-devel

%description
%summary


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

%package -n %libkleopatraclientcore
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libkleopatraclientcore
%name library

%package -n %libkleopatraclientgui
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libkleopatraclientgui
%name library

%prep
%setup -n %rname-%version
#%patch1 -p1

%build
%K5build

%install
%K5install
%K5install_move data kleopatra kwatchgnupg kconf_update kio locale

mv %buildroot/%_datadir/mime/packages/application-vnd-kde{,5}-kleopatra.xml

%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories5/*.*categories
%_datadir/mime/packages/*kleopatra*.xml

%files
%_K5bin/kleopatra
%_K5xdgapp/org.kde.kleopatra.desktop
%_K5xdgapp/kleopatra_import.desktop
%_K5data/kleopatra/
%_K5cf_upd/*kleopatra*
%_K5plug/pim5/kcms/kleopatra/kleopatra_config_gnupgsystem.so
%_K5icon/*/*/apps/kleopatra.*
%_K5data/kio/servicemenus/*.desktop
#
%_K5bin/kwatchgnupg
%_K5data/kwatchgnupg/

%files -n %libkleopatraclientcore
%_K5lib/libkleopatraclientcore.so.%kleopatraclientcore_sover
%_K5lib/libkleopatraclientcore.so.*
%files -n %libkleopatraclientgui
%_K5lib/libkleopatraclientgui.so.%kleopatraclientgui_sover
%_K5lib/libkleopatraclientgui.so.*

%changelog
* Fri Feb 03 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.2-alt1
- new version

* Wed Jan 11 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.1-alt1
- new version

* Mon Nov 07 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt1
- new version

* Tue Oct 18 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.2-alt1
- new version

* Thu Sep 08 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.1-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.3-alt1
- new version

* Fri Jun 10 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.2-alt1
- new version

* Fri May 13 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.1-alt1
- new version

* Fri Mar 04 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.3-alt1
- new version

* Mon Feb 21 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.2-alt1
- new version

* Thu Jan 13 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt1
- new version

* Mon Nov 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.3-alt1
- new version

* Fri Oct 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.2-alt1
- new version

* Thu Sep 02 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.1-alt1
- new version

* Thu Aug 19 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.0-alt1
- new version

* Thu Jul 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.3-alt1
- new version

* Thu Jun 10 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.2-alt1
- new version

* Mon May 17 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.1-alt1
- new version

* Wed Mar 10 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.3-alt1
- new version

* Fri Feb 05 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.2-alt1
- new version

* Tue Jan 12 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.1-alt1
- new version

* Wed Dec 16 2020 Sergey V Turchin <zerg@altlinux.org> 20.12.0-alt1
- new version

* Mon Nov 23 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.3-alt1
- new version

* Wed Oct 14 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.2-alt1
- new version

* Thu Sep 17 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.1-alt1
- new version

* Tue Jul 21 2020 Sergey V Turchin <zerg@altlinux.org> 20.04.3-alt1
- new version

* Thu Mar 12 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.3-alt1
- new version

* Thu Feb 13 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.2-alt1
- new version

* Thu Jan 16 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Fri Nov 08 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.3-alt1
- new version

* Wed Oct 23 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.2-alt1
- new version

* Mon Sep 09 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.1-alt1
- new version

* Fri Aug 16 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Tue Jul 16 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Fri Jun 07 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.2-alt1
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Tue Apr 30 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Thu Apr 11 2019 Sergey V Turchin <zerg@altlinux.org> 19.03.90-alt1
- new version

* Fri Mar 15 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Fri Feb 08 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Wed Jan 30 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.1-alt1
- new version

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Tue Jun 26 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Tue May 15 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Feb 13 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.2-alt1%ubt
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.2-alt1%ubt
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Mon May 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1%ubt
- new version

* Mon Apr 24 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1%ubt
- new version

* Wed Mar 15 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Thu Mar 09 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.2-alt1%ubt
- new version

* Mon Nov 28 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt0.M80P.1
- build for M80P

* Fri Nov 25 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.3-alt1
- new version

* Mon Sep 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Fri Aug 19 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.0-alt1
- new version

* Wed Jul 13 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.3-alt1
- new version

* Thu Jun 30 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Tue May 10 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Wed Apr 27 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.0-alt1
- initial build
