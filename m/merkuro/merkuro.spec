%define rname merkuro

%define sover 6
%define libmerkuro_contact libmerkuro_contact%sover
%define libmerkurocomponents libmerkurocomponents%sover


Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Calendar and task management
Url: http://www.kde.org
License: GPL-3.0-or-later

ExcludeArch: %not_qt6_qtwebengine_arches
Provides: kde5-merkuro = %EVR
Obsoletes: kde5-merkuro < %EVR

Requires: qml(QtLocation)
Requires: akonadi
Requires: akonadi-calendar
Requires: kmail-account-wizard

Source: %rname-%version.tar
Patch0: fix-menubar-display.patch

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-wayland-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-kcalendarcore-devel kf6-kcontacts-devel kf6-kiconthemes-devel kf6-kio-devel
BuildRequires: kf6-kirigami-devel kf6-kitemmodels-devel kf6-kpackage-devel kf6-ktextwidgets-devel
BuildRequires: kf6-qqc2-desktop-style-devel kf6-knotifications-devel kf6-ktexttemplate-devel
BuildRequires: kf6-kirigami-addons-devel
BuildRequires: plasma6-lib-devel
BuildRequires: akonadi-calendar-devel akonadi-contacts-devel akonadi-devel akonadi-mime-devel
BuildRequires: kcalutils-devel kidentitymanagement-devel kimap-devel kmime-devel
BuildRequires: kpimtextedit-devel kde6-libkdepim-devel kde6-libkleo-devel mailcommon-devel
BuildRequires: messagelib-devel pimcommon-devel kmailtransport-devel mimetreeparser-devel
BuildRequires: kmbox-devel

%description
Kirigami-based calendar and task management application that uses Akonadi.
It lets you add, edit and delete events and tasks from local and remote accounts of your choice,
while keeping changes synchronised across your Plasma desktop or phone.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
%description common
%name common package

%package -n %libmerkurocomponents
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libmerkurocomponents5 < %EVR
%description -n %libmerkurocomponents
%name library

%package -n %libmerkuro_contact
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libmerkuro_contact5 < %EVR
%description -n %libmerkuro_contact
%name library

%prep
%setup -n %rname-%version
#%patch0 -p1

%build
%K6build

%install
%K6install
%K6install_move data locale
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*

%files
%_datadir/qlogging-categories6/*.*categories
%_K6bin/merkuro-*
%_K6qml/org/kde/merkuro/
%_K6qml/org/kde/akonadi/
%_K6data/plasma/plasmoids/org.kde.merkuro.contact/
%_K6xdgapp/org.kde.merkuro*.desktop
%_K6icon/*/*/apps/*merkuro*.*
%_K6notif/*merkuro*
%_datadir/metainfo/*.xml

%files -n %libmerkurocomponents
%_K6lib/libMerkuroComponents.so.%sover
%_K6lib/libMerkuroComponents.so.*
%files -n %libmerkuro_contact
%_K6lib/libmerkuro_contact.so.%sover
%_K6lib/libmerkuro_contact.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

