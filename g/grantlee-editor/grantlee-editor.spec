%define rname grantlee-editor

%define pim_sover 6
%define libgrantleethemeeditor libgrantleethemeeditor%pim_sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Mail Header and Contact Theme Editor
Url: http://www.kde.org
License: GPL-2.0-or-later

ExcludeArch: %not_qt6_qtwebengine_arches

Provides: kde5-grantlee-editor = %EVR
Obsoletes: kde5-grantlee-editor < %EVR

Source: %rname-%version.tar
Patch0: alt-fix-display-theme-content.patch

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-base-devel qt6-webengine-devel
BuildRequires: boost-devel libassuan-devel libsasl2-devel
BuildRequires: kf6-karchive-devel kf6-kcrash-devel kf6-kdbusaddons-devel  kf6-kdoctools-devel
BuildRequires: kf6-kio-devel kf6-kitemmodels-devel kf6-knewstuff-devel kf6-kparts-devel kf6-ktexteditor-devel
BuildRequires: kf6-ktextwidgets-devel kf6-kwallet-devel kf6-syntax-highlighting-devel kf6-kcontacts-devel
BuildRequires: kf6-ktexttemplate-devel
BuildRequires: kde6-libkleo-devel
BuildRequires: akonadi-contacts-devel akonadi-devel akonadi-mime-devel grantleetheme-devel
BuildRequires: kimap-devel kmime-devel kpimtextedit-devel kde6-libkdepim-devel messagelib-devel
BuildRequires: pimcommon-devel

%description
KMail Header and KAddressbook Contact Theme Editor.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
Provides: kde5-grantlee-editor-common = %EVR
Obsoletes: kde5-grantlee-editor-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libgrantleethemeeditor
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libgrantleethemeeditor5 < %EVR
%description -n %libgrantleethemeeditor
%name library


%prep
%setup -n %rname-%version
%patch0 -p1

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files
%_K6bin/*editor*
%_K6xdgapp/*editor*.desktop
%_K6cfg/*editor*

#%files devel
#%_K6inc/grantlee-editor_version.h
#%_K6inc/grantlee-editor/
#%_K6link/lib*.so
#%_K6lib/cmake/grantlee-editor
#%_K6archdata/mkspecs/modules/qt_grantlee-editor.pri

%files -n %libgrantleethemeeditor
%_K6lib/libgrantleethemeeditor.so.%pim_sover
%_K6lib/libgrantleethemeeditor.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build
