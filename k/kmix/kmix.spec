%define rname kmix

%define sover 5
%define libkmixcore libkmixcore%sover

Name: %rname
Version: 24.08.2
Release: alt1
%K5init

Group: Sound
Summary: KDE sound mixer
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-kmix = %EVR
Obsoletes: kde5-kmix < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-declarative-devel
BuildRequires: libalsa-devel libcanberra-devel libpulseaudio-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdesignerplugin-devel
BuildRequires: kf5-kdoctools kf5-kdoctools-devel kf5-kglobalaccel-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel
BuildRequires: kf5-kinit-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kpackage-devel
BuildRequires: kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel kf5-plasma-framework-devel kf5-solid-devel kf5-sonnet-devel

%description
A sound mixer applet for KDE.
It allows you to control the volumes of your
sound card from a KDE panel applet.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
Provides:  kde5-kmix-common = %EVR
Obsoletes: kde5-kmix-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkmixcore
Group: System/Libraries
Summary: KF5 library
Requires: %name-common >= %EVR
%description -n %libkmixcore
KF5 library


%prep
%setup -n %rname-%version

%build
%K5build \
    -DKMIX_KF5_BUILD:BOOL=ON \
    #

%install
%K5install
%K5install_move data kmix
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%_datadir/qlogging-categories5/*.*categories

%files
%_K5bin/*
%_K5plug/kf5/kded/*kmix*.so
%_K5start/*.desktop
%_K5data/kmix/
%_K5cfg/*kmix*.kcfg
%_K5xmlgui/kmix/
%_K5xdgapp/*kmix.desktop
%_K5srv/*.desktop
%_K5notif/*kmix*.notifyrc
%_K5icon/*/*/actions/kmix.*
%_datadir/metainfo/*.xml

%files devel
%_K5dbus_iface/*.xml

%files -n %libkmixcore
%_K5lib/libkmixcore.so.*
%_K5lib/libkmixcore.so.%sover

%changelog
* Mon Oct 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build
