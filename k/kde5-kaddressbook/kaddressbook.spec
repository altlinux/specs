%define rname kaddressbook

Name: kde5-%rname
Version: 22.12.1
Release: alt1
%K5init no_appdata

%define sover 5
%define libkaddressbookprivate libkaddressbookprivate%sover
%define libkpimaddressbookimportexport libkpimaddressbookimportexport%sover

Group: Graphical desktop/KDE
Summary: Addressbook
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Provides: kde5-pim-kaddressbook = %EVR
Obsoletes: kde5-pim-kaddressbook < %EVR
Requires: kde5-akonadi kde5-pim-runtime kde5-akonadi-search

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Mar 16 2017 (-bi)
# optimized out: cmake cmake-modules elfutils fontconfig gcc-c++ grantlee5-devel gtk-update-icon-cache kde5-libkleo-devel kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libgpg-error libgpg-error-devel libgpgme-devel libical-devel libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-script libqt5-sql libqt5-svg libqt5-test libqt5-webchannel libqt5-webenginecore libqt5-webenginewidgets libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms perl pkg-config python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: boost-devel-headers extra-cmake-modules kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-akonadi-search-devel kde5-grantleetheme-devel kde5-kcalcore-devel kde5-kcontacts-devel kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kmime-devel kde5-kontactinterface-devel kde5-kpimtextedit-devel kde5-libkdepim-devel kde5-mailcommon-devel kde5-messagelib-devel  kde5-pimcommon-devel kf5-kcmutils-devel kf5-kdelibs4support-devel kf5-kdoctools-devel kf5-kio-devel libassuan-devel libsasl2-devel python-module-google python3-dev rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: boost-devel libassuan-devel libsasl2-devel
BuildRequires: libqtkeychain-qt5-devel
BuildRequires: kde5-libkleo-devel
BuildRequires: kde5-akonadi-contacts-devel kde5-akonadi-devel kde5-akonadi-mime-devel kde5-akonadi-search-devel kde5-grantleetheme-devel
BuildRequires: kde5-kcalcore-devel kde5-kcontacts-devel kde5-kidentitymanagement-devel kde5-kimap-devel kde5-kmime-devel
BuildRequires: kde5-kontactinterface-devel kde5-kpimtextedit-devel kde5-libkdepim-devel kde5-messagelib-devel
BuildRequires:  kde5-pimcommon-devel
BuildRequires: kf5-kcmutils-devel kf5-kdelibs4support-devel kf5-kdoctools-devel kf5-kio-devel kf5-prison-devel

%description
Contact manager.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
Conflicts: kde5-pim-common < 16.12
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkaddressbookprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkaddressbookprivate
%name library

%package -n %libkpimaddressbookimportexport
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkpimaddressbookimportexport
%name library

%prep
%setup -n %rname-%version

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    #

%install
%K5install
%K5install_move data kaddressbook kconf_update kontact
for f in %buildroot/%_libdir/cmake/*/*.cmake ; do
    sed -i 's|%_K5inc/KF5|%_K5inc|g' $f
done
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories5/*.*categories

%files
%_K5bin/kaddressbook
%_K5plug/pim5/kcms/kaddressbook/
%_K5plug/*kaddressbook*.so
%_K5plug/pim5/kontact/*kaddressbook*.so
%_K5xdgapp/*kaddressbook*.desktop
%_K5data/kaddressbook/
#%_K5srv/kontact/kaddressbookplugin.desktop
#%_K5srv/*kaddressbook*.desktop
%_K5icon/*/*/apps/kaddressbook.*
#
#%_K5data/kontact/ksettingsdialog/*kaddressbook*

%files devel
%_K5inc/KPim/KAddressBookImportExport/
%_K5inc/KPim/kaddressbookimportexport/
%_K5inc/KPim/*.h
%_K5link/lib*.so
%_K5lib/cmake/KPimAddressbookImportExport/
%_K5archdata/mkspecs/modules/qt_K*.pri

%files -n %libkaddressbookprivate
%_K5lib/libkaddressbookprivate.so.%sover
%_K5lib/libkaddressbookprivate.so.*

%files -n %libkpimaddressbookimportexport
%_K5lib/libKPimAddressbookImportExport.so.%sover
%_K5lib/libKPimAddressbookImportExport.so.*

%changelog
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

* Tue Mar 26 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt2
- fix build requires

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

* Thu Mar 16 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1%ubt
- new version

* Wed Mar 15 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.2-alt1%ubt
- initial build
