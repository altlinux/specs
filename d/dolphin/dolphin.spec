%define rname dolphin

%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif
%define service_name plasma-dolphin

%def_enable baloo

%define sover 6
%define libdolphinprivate libdolphinprivate%sover
%define libdolphinvcs libdolphinvcs%sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: File tools
Summary: The file manager for KDE
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kde5-dolphin = %EVR
Obsoletes: kde5-dolphin < %EVR

Requires: kf6-kio
#Requires: kf6-kio-extras

Source: %rname-%version.tar
Patch2: alt-def-general.patch
Patch3: alt-def-toolbar.patch
Patch4: alt-fix-unmounting-during-preview-generation.patch
Patch5: upstream-8d7e600f.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-phonon-devel 
BuildRequires: libxapian-devel desktop-file-utils
BuildRequires: packagekit-qt6-devel
BuildRequires: kf6-kfilemetadata-devel
%if_enabled baloo
BuildRequires: kf6-baloo-devel baloo-widgets-devel
%endif
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcmutils-devel
BuildRequires: kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel kf6-kguiaddons-devel
BuildRequires: kf6-ki18n-devel kf6-kiconthemes-devel  kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel kf6-knewstuff-devel kf6-knotifications-devel kf6-kparts-devel kf6-kservice-devel
BuildRequires: kf6-ktexteditor-devel kf6-ktextwidgets-devel kf6-kunitconversion-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel
BuildRequires: plasma6-activities-devel

%description
Dolphin is a file manager for KDE focusing on usability.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: kde5-dolphin-common = %EVR
Obsoletes: kde5-dolphin-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libdolphinprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libdolphinprivate5 < %EVR
%description -n %libdolphinprivate
%name library

%package -n %libdolphinvcs
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libdolphinvcs5 < %EVR
%description -n %libdolphinvcs
%name library


%prep
%setup -n %rname-%version
%patch2 -p1
%patch3 -p1
#%patch4 -p2
%patch5 -R -p1

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    -DDATA_INSTALL_DIR=%_K6data \
    #

%install
%K6install
%K6install_move data kglobalaccel knsrcfiles kconf_update
%find_lang %name --with-kde --all-name

desktop-file-install --mode=0755 --dir %buildroot/%_K6xdgapp \
    --add-mime-type=x-scheme-handler/ftp \
    --add-mime-type=x-scheme-handler/smb \
    --add-mime-type=x-scheme-handler/nfs \
    --add-mime-type=x-scheme-handler/trash \
    %buildroot/%_K6xdgapp/org.kde.dolphin.desktop
# kf6-kio-extras
#    --add-mime-type=x-scheme-handler/network \
# kf6-plasma-workspace
#    --add-mime-type=x-scheme-handler/desktop \
#    --add-mime-type=x-scheme-handler/remote \
#    --add-mime-type=x-scheme-handler/programs \
#    --add-mime-type=x-scheme-handler/applications \

%files common -f %name.lang
%doc LICENSES/*
#%_datadir/locale/*/LC_SCRIPTS/dolphin/
%_datadir/qlogging-categories6/*.*categories

%files
%_K6bin/*
%_K6plug/dolphin/
%_K6plug/kf6/parts/*dolphin*.so
%_K6plug/kf6/kfileitemaction/*action*.so
%_K6xdgapp/*dolphin*.desktop
%_K6icon/*/*/apps/*dolphin*.*
%_K6cfg/dolphin*
%_K6conf_up/*dolphin*
%_K6data/dolphin/
%_K6data/kglobalaccel/*dolphin*
%_K6data/knsrcfiles/*
%_K6dbus_srv/org.kde.dolphin.FileManager1.service
%_userunitdir/%service_name.service
%_datadir/metainfo/*.xml
%_datadir/zsh/site-functions/*dolphin*

%files devel
%_K6inc/?olphin*
%_K6link/lib*.so
%_K6lib/cmake/DolphinVcs/
%_K6dbus_iface/org.freedesktop.FileManager1.xml

%files -n %libdolphinprivate
%_K6lib/libdolphinprivate.so.*
%_K6lib/libdolphinprivate.so.%sover
%files -n %libdolphinvcs
%_K6lib/libdolphinvcs.so.*
%_K6lib/libdolphinvcs.so.%sover


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

