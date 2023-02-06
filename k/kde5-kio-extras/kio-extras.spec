%define rname kio-extras

%define molletnetwork_sover 21
%define libmolletnetwork libmolletnetwork5%molletnetwork_sover
%define kioarchive_sover 5
%define libkioarchive libkioarchive%kioarchive_sover

%def_enable exiv2

Name: kde5-%rname
Version: 22.12.2
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: KDE Workspace 5 additional kio-slaves
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Requires: %name-common = %version-%release
Requires: kf5-kio
Provides: kf5-kio-extras = %EVR
Obsoletes: kf5-kio-extras < %EVR

# djvu thumbnailer
Requires: /usr/bin/ddjvu
# ico thumbnailer: /usr/bin/wrestool
# comic thumbnailer: /usr/bin/unrar

Source: %rname-%version.tar
Patch11: alt-smb-share.patch
Patch12: alt-fix-permissions.patch
Patch13: alt-find-samba.patch

# Automatically added by buildreq on Sat Mar 21 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils glibc-devel-static ilmbase-devel kf5-attica-devel kf5-kdoctools-devel libEGL-devel libGL-devel libcloog-isl4 libdbusmenu-qt52 libgpg-error libjson-c libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libstdc++-devel libxcbutil-keysyms pkg-config python-base qt5-base-devel ruby ruby-stdlibs samba-libs shared-mime-info xml-common xml-utils
#BuildRequires: extra-cmake-modules gcc-c++ kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdelibs4support-devel kf5-kdesignerplugin-devel kf5-kdnssd-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-khtml-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kjs-devel kf5-knotifications-devel kf5-kparts-devel kf5-kpty-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libexiv2-devel libjpeg-devel libmtp-devel libopenslp-devel libsmbclient-devel libssh-devel openexr-devel python-module-google qt5-phonon-devel qt5-svg-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++ qt5-phonon-devel qt5-svg-devel
%if_enabled exiv2
BuildRequires: libexiv2-devel
%endif
BuildRequires: libjpeg-devel libmtp-devel libopenslp-devel libsmbclient-devel libssh-devel openexr-devel
BuildRequires: libtirpc-devel
BuildRequires: gperf libtag-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kactivities-devel
BuildRequires: kf5-kdesignerplugin-devel kf5-kdnssd-devel
BuildRequires: kf5-kdoctools kf5-kdoctools-devel
BuildRequires: kf5-kemoticons-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-khtml-devel kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel kf5-kjs-devel kf5-knotifications-devel kf5-kparts-devel kf5-kpty-devel kf5-kservice-devel
BuildRequires: kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwallet-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel
BuildRequires: kf5-syntax-highlighting-devel kf5-kactivities-stats-devel
BuildRequires: kde5-kdsoap-devel kde5-libkexiv2-devel

%description
Additional kio-slaves.

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

%package -n %libmolletnetwork
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libmolletnetwork
KF5 library

%package -n %libkioarchive
Group: System/Libraries
Summary: KF5 library
Requires: %name-common = %version-%release
%description -n %libkioarchive
KF5 library


%prep
%setup -n %rname-%version
%patch11 -p1
%patch12 -p1
%patch13 -p1

%build
%K5build

%install
%K5install

%K5install_move data kio_bookmarks kio_desktop kio_docfilter kio_info konqueror remoteview
%K5install_move data doc solid dbus-1/services

# workaround against man compressor
rm -rf %buildroot/%_K5doc/*/kioslave5/man

%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories5/*.*categories
%_K5xdgmime/*.xml

%files
%_K5exec/smbnotifier
%_K5plug/kf5/*/*.so
%_K5plug/*.so
%_K5data/kio_*/
#%_K5data/konqsidebartng
%_K5data/konqueror
%_K5data/remoteview
%_K5srv/*.desktop
#%_K5srv/*.protocol
%_K5srvtyp/*.desktop
%_K5data/solid/actions/*.desktop
%_K5cfg/*.kcfg
%_K5dbus_srv/*.service

%files devel
%_K5inc/*kio*archive*.h
#%_K5inc/KIO*/
#%_K5inc/kio/
#%_K5link/lib*.so
%_K5lib/cmake/Kio*/
#%_K5archdata/mkspecs/modules/qt_KIO*.pri
#%_K5dbus_iface/*.xml

#%files -n %libmolletnetwork
#%_K5lib/libmolletnetwork5.so.*
#%_K5lib/libmolletnetwork5.so.%molletnetwork_sover

%files -n %libkioarchive
%_K5lib/libkioarchive.so.*
%_K5lib/libkioarchive.so.%kioarchive_sover

%changelog
* Mon Feb 06 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.2-alt1
- new version

* Wed Jan 11 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.1-alt1
- new version

* Mon Nov 07 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt1
- new version

* Tue Oct 18 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.2-alt1
- new version

* Thu Sep 15 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.1-alt1
- new version

* Tue Aug 30 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.3-alt2
- fix connect to samba-4.16 (closes: 43616)

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

* Tue Dec 21 2021 Oleg Solovyov <mcpain@altlinux.org> 21.08.3-alt2
- Fix SMB tree view in Dolphin (Closes: #41527)

* Mon Nov 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.3-alt1
- new version

* Fri Oct 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.2-alt1
- new version

* Wed Sep 29 2021 Oleg Solovyov <mcpain@altlinux.org> 21.08.1-alt2
- require ddjvu (Closes: #40997)

* Thu Sep 02 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.1-alt1
- new version

* Mon Aug 23 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.0-alt1
- new version

* Thu Jul 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.3-alt1
- new version

* Thu Jun 10 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.2-alt1
- new version

* Wed May 19 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.1-alt1
- new version

* Thu Mar 11 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.3-alt1
- new version

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

* Fri Sep 18 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.1-alt1
- new version

* Fri Aug 14 2020 Sergey V Turchin <zerg@altlinux.org> 20.04.3-alt1
- new version

* Tue May 12 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.3-alt2
- don't store unasked fish:/ passwords (Fixes: CVE-2020-12755)

* Thu Mar 12 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.3-alt1
- new version

* Fri Feb 14 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.2-alt1
- new version

* Tue Jan 21 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Tue Nov 26 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.3-alt2
- fix to compile with libssh-0.9.2

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

* Thu Jan 10 2019 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt4
- add fix to avoid crash by not checking free space for smb://

* Wed Jan 09 2019 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt3
- rebuild

* Tue Nov 13 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt2
- don't package htmlthumbnail plugin
- security fixes: CVE-2018-19120

* Tue Jul 24 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1%ubt
- new version

* Wed Jul 04 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1%ubt
- new version

* Tue May 22 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1%ubt
- new version

* Wed Mar 14 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1%ubt
- new version

* Tue Mar 06 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.2-alt1%ubt
- new version

* Mon Nov 13 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1%ubt
- new version

* Mon Aug 14 2017 Oleg Solovyov <mcpain@altlinux.org> 17.04.3-alt2%ubt
- fix changing file permissions (ALT#33502)

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1%ubt
- new version

* Wed Jun 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1%ubt
- new version

* Thu May 04 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt2%ubt
- update icon for smb:/ shares

* Tue May 02 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.0-alt1%ubt
- new version

* Tue May 02 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt2%ubt
- add application/x-smb-share for smb:/ shares

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

* Fri Feb 26 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- new version

* Wed Jan 20 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Tue Dec 22 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- new version

* Wed Dec 09 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt2
- fix to build

* Thu Nov 12 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.3-alt1
- new version

* Wed Oct 14 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.2-alt1
- new version

* Wed Sep 16 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.1-alt1
- new version

* Thu Aug 20 2015 Sergey V Turchin <zerg@altlinux.org> 15.08.0-alt1
- new version

* Wed Jul 01 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri May 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Thu Apr 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Tue Apr 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt0.1
- test

* Thu Apr 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt1
- new version

* Mon Mar 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt0.1
- test

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.1
- initial build
