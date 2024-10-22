%define rname pim-sieve-editor

%define sover 6
%define libsieveeditor libsieveeditor%sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Sieve Editor
Url: http://www.kde.org
License: LGPL-2.0-or-later

ExcludeArch: %not_qt6_qtwebengine_arches

Provides: kde5-pim-sieve-editor = %EVR
Obsoletes: kde5-pim-sieve-editor < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-base-devel
BuildRequires: boost-devel libsasl2-devel
BuildRequires: libqtkeychain-qt6-devel
BuildRequires: akonadi-contacts-devel akonadi-devel akonadi-mime-devel kf6-kcontacts-devel kimap-devel kmailtransport-devel
BuildRequires: kmime-devel kpimtextedit-devel kde6-libksieve-devel messagelib-devel pimcommon-devel
BuildRequires: kf6-kcrash-devel kf6-kdbusaddons-devel  kf6-kdoctools-devel kf6-kiconthemes-devel kf6-kio-devel
BuildRequires: kf6-kitemmodels-devel kf6-ktextwidgets-devel kf6-kwallet-devel kf6-syntax-highlighting-devel

%description
Sieve Editor is an editor for Sieve scripts used for email filtering on a mail server.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
Provides: kde5-pim-sieve-editor-common = %EVR
Obsoletes: kde5-pim-sieve-editor-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libsieveeditor
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libsieveeditor5 < %EVR
%description -n %libsieveeditor
%name library

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data kconf_update
%find_lang %name --with-kde --all-name

%files common -f %name.lang

%files
%doc LICENSES/*
%_K6bin/*sieveeditor*
%_K6xdgapp/*sieveeditor*.desktop
%_K6cfg/*sieveeditor*
%_K6icon/*/*/apps/*sieveeditor*.*
%_datadir/qlogging-categories6/*.*categories
%_datadir/metainfo/*.xml

%files -n %libsieveeditor
%_K6lib/libsieveeditor.so.%sover
%_K6lib/libsieveeditor.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

