%define rname kmail-account-wizard

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Networking/Other
Summary: Account Wizard
Url: http://www.kde.org
License: LGPL-2.0-or-later

Provides: kde5-kmail-account-wizard = %EVR
Obsoletes: kde5-kmail-account-wizard < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel qt6-tools-devel-static
BuildRequires: boost-devel libassuan-devel libldap-devel libsasl2-devel
BuildRequires: libqtkeychain-qt6-devel
BuildRequires: kf6-kdoctools-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kitemmodels-devel kf6-knewstuff-devel
BuildRequires: kf6-knotifications-devel kf6-knotifyconfig-devel kf6-kparts-devel kf6-ktexteditor-devel
BuildRequires: kf6-ktextwidgets-devel kf6-kwallet-devel kf6-syntax-highlighting-devel
BuildRequires: kf6-kcmutils-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kde6-libkleo-devel
BuildRequires: akonadi-contacts-devel akonadi-devel akonadi-mime-devel kf6-kcontacts-devel kidentitymanagement-devel
BuildRequires: kimap-devel kldap-devel kmailtransport-devel kmime-devel kpimtextedit-devel kde6-libkdepim-devel
BuildRequires: messagelib-devel pimcommon-devel

%description
Launch the account wizard to configure PIM accounts.

%prep
%setup -n %rname-%version

%build
%K6build \
    -DDATA_INSTALL_DIR=%_K6data \
    #

%install
%K6install
%K6install_move data knsrcfiles
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/accountwizard
%_K6xdgapp/*accountwizard*.desktop
%_datadir/metainfo/*accountwizard*.xml


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

