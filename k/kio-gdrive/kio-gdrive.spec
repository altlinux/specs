
%def_disable qtkeychain

%define rname kio-gdrive

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group:     Networking/File transfer
Summary:   KIO-client for Google Drive
URL:       https://cgit.kde.org/kio-gdrive.git/
License:   GPL-2.0-or-later

Provides: kde5-kio-gdrive = %EVR
Obsoletes: kde5-kio-gdrive < %EVR
Requires: kaccounts-providers signon-plugin-oauth2

Source: %rname-%version.tar
Source10: kio5_gdrive_ru.po

BuildRequires(pre): rpm-build-kf6

BuildRequires: extra-cmake-modules gettext-tools qt6-svg-devel qt6-wayland-devel
BuildRequires: libvulkan-devel
%if_enabled qtkeychain
BuildRequires: libqtkeychain-qt6-devel
%else
BuildRequires: intltool signon-devel accounts-qt6-devel kaccounts-integration-devel
%endif
BuildRequires: kf6-kdoctools-devel kf6-kio-devel kf6-purpose-devel
BuildRequires: kf6-ki18n-devel kf6-kio-devel kf6-knotifications-devel
BuildRequires: kde6-libkgapi-devel

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
%K6build \
    -DQT_MAJOR_VERSION=6 \
    #

%install
%K6install
%K6install_move data remoteview purpose
%find_lang --with-kde --all-name %rname

%files -f %rname.lang
%doc LICENSES/*
%_K6data/remoteview/*drive*.desktop
%_K6plug/kf6/*/*drive*.so
%_datadir/metainfo/*drive*.xml
%if_enabled qtkeychain
%else
%_K6plug/kaccounts/daemonplugins/*drive*.so
%_K6plug/kf6/kfileitemaction/*.so
%_datadir/accounts/services/kde/*drive*.service
%_K6notif/*drive*.notifyrc
%_K6data/purpose/*gdrive*
%endif


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

