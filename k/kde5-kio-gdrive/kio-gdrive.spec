
%def_disable qtkeychain

%define rname kio-gdrive
%define sover 16
%define libktcore libktcore%sover

Name: kde5-%rname
Version: 22.12.2
Release: alt1
%K5init altplace appdata

Group:     Networking/File transfer
Summary:   KIO-client for Google Drive
License:   GPLv2 / GPLv3
URL:       https://cgit.kde.org/kio-gdrive.git/

Requires: kde5-kaccounts-providers signon-plugin-oauth2

Source: %rname-%version.tar
Source10: kio5_gdrive_ru.po

BuildRequires(pre): rpm-build-kf5

# Automatically added by buildreq on Fri Sep 18 2020 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kauth-devel kf5-kbookmarks-devel kf5-kcalcore-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcontacts-devel kf5-kcoreaddons-devel kf5-kdoctools kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel libaccounts-glib libaccounts-qt51 libcairo-gobject libdbusmenu-qt52 libgdk-pixbuf libglvnd-devel libgpg-error libopencore-amrnb0 libopencore-amrwb0 libp11-kit libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-positioning libqt5-printsupport libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-quickwidgets libqt5-svg libqt5-test libqt5-texttospeech libqt5-webchannel libqt5-webenginecore libqt5-webenginewidgets libqt5-widgets libqt5-x11extras libqt5-xml librabbitmq-c libsasl2-3 libsignon-qt51 libssl-devel libstdc++-devel libx265-192 libxcbutil-keysyms perl perl-Encode perl-XML-Parser perl-parent pkg-config python-modules python2-base python3 python3-base python3-dev python3-module-paste qt5-base-devel rpm-build-python3 sh4 xml-common xml-utils
#BuildRequires: accounts-qt5-devel appstream extra-cmake-modules intltool kde5-kaccounts-integration-devel kde5-libkgapi-devel kf5-kdoctools-devel kf5-ki18n-devel kf5-kio-devel kf5-knotifications-devel python-modules-compiler python3-module-mpl_toolkits qt5-svg-devel qt5-wayland-devel qt5-webengine-devel signon-devel
BuildRequires: extra-cmake-modules gettext-tools qt5-svg-devel qt5-wayland-devel
%if_enabled qtkeychain
BuildRequires: libqtkeychain-qt5-devel
%else
BuildRequires: intltool signon-devel accounts-qt5-devel kde5-kaccounts-integration-devel
%endif
BuildRequires: kf5-kdoctools-devel kf5-kio-devel kf5-libkgapi-devel kf5-purpose-devel
BuildRequires: kf5-ki18n-devel kf5-kio-devel kf5-knotifications-devel

%description
Now you are ready to use the slave. Either click on "Google Drive File Manager"
in the application launcher (which will open Dolphin with the `gdrive:/` URL) or run:
    $ kioclient5 exec gdrive:/

%prep
%setup -q -n %rname-%version

tmp_file=`mktemp`
msgcat --use-first po/ru/kio5_gdrive.po %SOURCE10 >"$tmp_file"
cat "$tmp_file" >po/ru/kio5_gdrive.po
rm -f "$tmp_file"

%build
%K5build

%install
%K5install
%K5install_move data remoteview purpose
%find_lang --with-kde --all-name %rname

%files -f %rname.lang
%doc LICENSES/*
%_K5data/remoteview/*drive*.desktop
%_K5plug/kf5/*/*drive*.so
%_datadir/metainfo/*drive*.xml
%if_enabled qtkeychain
%else
%_K5plug/kaccounts/daemonplugins/*drive*.so
%_K5plug/kf5/kfileitemaction/*.so
%_datadir/accounts/services/kde/*drive*.service
%_K5notif/*drive*.notifyrc
%_K5data/purpose/*gdrive*
%endif

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

* Fri Sep 18 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.1-alt1
- new version

* Mon Apr 27 2020 Sergey V Turchin <zerg@altlinux.org> 1.3.0-alt1
- new version

* Thu Nov 28 2019 Sergey V Turchin <zerg@altlinux.org> 1.2.7-alt1
- new version

* Wed Aug 21 2019 Sergey V Turchin <zerg@altlinux.org> 1.2.5-alt2
- fix compile with new libkgapi

* Tue Dec 04 2018 Sergey V Turchin <zerg@altlinux.org> 1.2.5-alt1
- new version

* Tue May 08 2018 Sergey V Turchin <zerg@altlinux.org> 1.2.3-alt1
- new version

* Thu Apr 12 2018 Sergey V Turchin <zerg@altlinux.org> 1.2.2-alt1
- new version

* Tue Mar 06 2018 Sergey V Turchin <zerg@altlinux.org> 1.2.1-alt1
- new version

* Fri Jun 23 2017 Sergey V Turchin <zerg@altlinux.org> 1.2.0.1-alt3
- build with kaccounts again

* Wed Jun 21 2017 Sergey V Turchin <zerg@altlinux.org> 1.2.0.1-alt2
- build without kaccounts and with qtkeychain

* Mon Jun 19 2017 Sergey V Turchin <zerg@altlinux.org> 1.2.0.1-alt1
- new version

* Tue May 02 2017 Sergey V Turchin <zerg@altlinux.org> 1.1.1-alt2
- rebuild with new libkgapi

* Thu Mar 23 2017 Sergey V Turchin <zerg@altlinux.org> 1.1.1-alt1
- new version

* Mon Jan 09 2017 Sergey V Turchin <zerg@altlinux.org> 1.0.4-alt1
- new version

* Mon Nov 07 2016 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt0.M80P.1
- build for M80P

* Wed Nov 02 2016 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt1
- initial build
