%define rname kmenuedit

Name: %rname
Version: 6.1.4
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Frameworks 6 Menu Editor
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: plasma5-kmenuedit = %EVR
Obsoletes: plasma5-kmenuedit < %EVR

Source: %rname-%version.tar
Patch1: alt-menueditor.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-kglobalaccel-devel kf6-kguiaddons-devel kf6-kxmlgui-devel kf6-kio-devel
BuildRequires: kf6-ki18n-devel kf6-kiconthemes-devel  kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel kf6-knotifications-devel kf6-kparts-devel kf6-kservice-devel kf6-ktextwidgets-devel
BuildRequires: kf6-kunitconversion-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel

%description
Menu Editor


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build

%install
%K6install
%K6install_move data kmenuedit
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories
%_K6bin/*
%_K6data/kmenuedit/
%_K6xdgapp/*.desktop
%_K6icon/*/*/apps/kmenuedit.*
%_datadir/metainfo/*.xml


%changelog
* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

