%define rname mbox-importer

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: MBox Importer
Url: http://www.kde.org
License: GPL-2.0-or-later

ExcludeArch: %not_qt6_qtwebengine_arches

Provides: kde5-mbox-importer = %EVR
Obsoletes: kde5-mbox-importer < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-build-ubt rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: boost-devel libassuan-devel libdb4-devel libsasl2-devel
BuildRequires: libqtkeychain-qt6-devel
BuildRequires: kf6-kcrash-devel kf6-kio-devel kf6-kitemmodels-devel kf6-ktextwidgets-devel kf6-karchive-devel
BuildRequires: kf6-ktexttemplate-devel kf6-kcontacts-devel kf6-kiconthemes-devel
BuildRequires: kde6-libkleo-devel
BuildRequires: akonadi-contacts-devel akonadi-devel akonadi-mime-devel kidentitymanagement-devel
BuildRequires: kimap-devel kmime-devel kpimtextedit-devel mailcommon-devel mailimporter-devel messagelib-devel
BuildRequires: pimcommon-devel kde6-libkdepim-devel

%description
PIM Mailbox importer.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/*mboximporter*
%_K6xdgapp/*mboximporter*.desktop

%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

