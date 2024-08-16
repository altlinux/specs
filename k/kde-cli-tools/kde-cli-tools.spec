%define rname kde-cli-tools

%def_enable bootstrap

%add_findreq_skiplist %_K6exec/kdeeject

Name: %rname
Version: 6.1.4
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Frameworks 6 common cli tools
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: qt6-dbus
%if_disabled bootstrap
Requires: kdialog
%endif

Provides: plasma5-kde-cli-tools = %EVR
Obsoletes: plasma5-kde-cli-tools < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-svg-devel
BuildRequires: zlib-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcmutils-devel kf6-kcodecs-devel
BuildRequires: kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel
BuildRequires: kf6-kdbusaddons-devel
BuildRequires: kf6-kdesu-devel kf6-kdoctools kf6-kdoctools-devel kf6-kglobalaccel-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel  kf6-kio-devel kf6-kitemmodels-devel
BuildRequires: kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knotifications-devel kf6-kparts-devel kf6-kpty-devel
BuildRequires: kf6-kservice-devel kf6-ktextwidgets-devel kf6-kunitconversion-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel
BuildRequires: kf6-kdeclarative-devel kf6-kpackage-devel
BuildRequires: plasma-workspace-devel
%description
KDE common command line tools.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/*
%_K6exec/*
%_K6plug/plasma/kcms/systemsettings_qwidgets/*.so
%_K6xdgapp/*.desktop
%_datadir/zsh/site-functions/*kde*


%changelog
* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build
