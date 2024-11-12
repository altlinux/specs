%define rname kturtle

Name: %rname
Version: 24.08.2
Release: alt1
%K6init

Group: Education
Summary: An educational programming environment
Url: http://www.kde.org
License: GPL-2.0-only or GPL-2.0-or-later

Provides:  kde5-kturtle = %EVR
Obsoletes: kde5-kturtle < %EVR

Source: %rname-%version.tar
Patch1: alt-def-language.patch
Patch2: alt-fix-lang-change.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-svg-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel  kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-ki18n-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knewstuff-devel kf6-kservice-devel
BuildRequires: kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel

%description
KTurtle is an educational programming environment for the KDE Desktop.
KTurtle aims to make programming as easy and touchable as possible, and
therefore can be used to teach kids the basics of math, geometry
and... programming.

%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1

%build
%K6build

%install
%K6install
%K6install_move data katepart kturtle
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/kturtle
%_K6icon/*/*/apps/kturtle.*
%_K6xdgapp/org.kde.kturtle.desktop
%_K6data/knsrcfiles/kturtle.knsrc
%_datadir/metainfo/*.xml


%changelog
* Thu Nov 07 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

