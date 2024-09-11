%define rname sddm-kcm

Name: %rname
Version: 6.1.5
Release: alt1
#Epoch: 1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Frameworks 6 SDDM configuration module
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: plasma5-sddm-kcm = 1:%version-%release
Obsoletes: plasma5-sddm-kcm < 1:%version-%release
Requires: systemsettings
Requires: sddm

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: libvulkan-devel
BuildRequires: qt6-declarative-devel qt6-tools-devel
BuildRequires: libxcbutil-image-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kglobalaccel-devel kf6-kguiaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-kservice-devel kf6-ktextwidgets-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel
BuildRequires: kf6-karchive-devel kf6-knewstuff-devel kf6-kdeclarative-devel kf6-kcmutils-devel kf6-kpackage-devel

%description
SDDM configuration module.

%prep
%setup -n %rname-%version

%build
%K6build \
    -DSDDM_CONFIG_FILE=/etc/X11/sddm/sddm.conf \
    -DSDDM_SYSTEM_CONFIG_DIR=%_datadir/sddm/conf.d \
    #

%install
%K6install
%K6install_move data sddm-kcm knsrcfiles kpackage
%find_lang %name --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6data/knsrcfiles/*.knsrc
%_K6dbus/system.d/*.conf
%_K6bin/sddmthemeinstaller
%_K6plug/plasma/kcms/systemsettings/*.so
%_K6xdgapp/*.desktop
%_K6exec/kauth/*
#%_K6data/kpackage/kcms/kcm_sddm/
%_K6dbus_sys_srv/*.service
%_datadir/polkit-1/actions/*



%changelog
* Tue Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- new version

* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

