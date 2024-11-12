%define rname kmplot

Name: %rname
Version: 24.08.2
Release: alt1
%K6init

Group: Education
Summary: Mathematical Function Plotter
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-kmplot = %EVR
Obsoletes: kde5-kmplot < %EVR

Source: %rname-%version.tar
Patch0: alt-fix-saving-softimage-pic.patch
Patch1: alt-fix-hiding-statusbar.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-svg-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel  kf6-kio-devel kf6-kitemmodels-devel
BuildRequires: kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knotifications-devel kf6-kparts-devel kf6-kservice-devel
BuildRequires: kf6-ktextwidgets-devel kf6-kunitconversion-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel
BuildRequires: kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel

%description
KmPlot is a program to plot graphs of functions, their integrals or derivatives.

%prep
%setup -n %rname-%version
%patch0 -p1
%patch1 -p1

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/kmplot
%_K6plug/kf6/parts/*kmplot*.so
%_K6icon/*/*/apps/kmplot.*
%_K6xdgapp/org.kde.kmplot.desktop
%_K6cfg/kmplot.kcfg
%_datadir/metainfo/*.xml


%changelog
* Thu Nov 07 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

