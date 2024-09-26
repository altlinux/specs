%define rname print-manager

%def_disable installer

%define sover 6
%define libkcupslib libkcupslib%sover

Name: %rname
Version: 6.1.5
Release: alt1
%K6init

Group: System/Configuration/Printing
Summary: Printer management for KDE
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kde5-print-manager = 1:%version-%release
Obsoletes: kde5-print-manager < 1:%version-%release

Requires: cups
Requires: /usr/lib/cups/backend/smb
#Requires: printer-drivers-X11
Requires: system-config-printer-lib
Requires: system-config-printer-udev

Source: %rname-%version.tar
Source10: add-ppdtranslations-ru.po
Patch1: alt-lib-sover.patch
Patch2: alt-queue-window.patch
Patch3: alt-remove-help-button.patch
Patch4: alt-print-opts-i18n.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: /usr/bin/msgcat
BuildRequires: libvulkan-devel
BuildRequires: libcups-devel
%if_enabled installer
BuildRequires: packagekit-qt6-devel
%endif
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcmutils-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-knotifications-devel kf6-kpackage-devel kf6-kservice-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel
BuildRequires: kf6-solid-devel kf6-kirigami-devel
BuildRequires: plasma6-lib-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
Provides: kde5-print-manager-common = 1:%version-%release
Obsoletes: kde5-print-manager-common < 1:%version-%release
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkcupslib
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
Obsoletes: libkcupslib0.2 < 1:%version-%release
%description -n %libkcupslib
KF6 library


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

tmp_file=`mktemp`
msgcat --use-first po/ru/print-manager.po %SOURCE10 >"$tmp_file"
cat "$tmp_file" >po/ru/print-manager.po
msgcat --use-first po/ru/plasma_applet_org.kde.plasma.printmanager.po %SOURCE10 >"$tmp_file"
cat "$tmp_file" >po/ru/plasma_applet_org.kde.plasma.printmanager.po
rm -f "$tmp_file"

%build
%K6build \
%if_enabled installer
    DSCP_PACKAGE_NAME=system-config-printer \
%else
    -DSCP_INSTALL:BOOL=OFF \
%endif
    #

%install
%K6install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*

%files
%_K6bin/configure-printer
%_K6bin/kde-add-printer
%_K6bin/kde-print-queue
%_K6plug/plasma/kcms/systemsettings/*printer*.so
%_K6plug/kf6/kded/*print*.so
%_K6xdgapp/*rint*.desktop
%_K6data/plasma/plasmoids/org.kde.plasma.printmanager/
%_K6qml/org/kde/plasma/printmanager/
%_K6notif/printmanager.notifyrc
%_datadir/qlogging-categories6/*.*categories
%_datadir/metainfo/*print*.xml

%files -n %libkcupslib
%_K6lib/libkcupslib.so.%sover
%_K6lib/libkcupslib.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- initial build
