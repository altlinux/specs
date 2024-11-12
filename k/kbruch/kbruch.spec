%define rname kbruch

Name: %rname
Version: 24.08.2
Release: alt1
%K6init

Group: Education
Summary: Exercise Fractions
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-kbruch = %EVR
Obsoletes: kde5-kbruch < %EVR

Source: %rname-%version.tar
Patch: Fix-incorrect-display-of-user-interface-elements-alt.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-kauth-devel kf6-kcodecs-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel
BuildRequires: kf6-kdoctools-devel kf6-ki18n-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-kcolorscheme-devel

%description
KBruch is a small program to practice calculating with fractions and percentages.
Different exercises are provided for this purpose and you can use the learning mode
to practice with fractions. The program checks the user's input and gives feedback.

%prep
%setup -n %rname-%version
%patch -p1

%build
%K6build

%install
%K6install
%K6install_move data kbruch
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/kbruch
%_K6data/kbruch/
%_K6icon/*/*/apps/kbruch.*
%_K6xdgapp/org.kde.kbruch.desktop
%_K6cfg/kbruch.kcfg
%_datadir/metainfo/*.xml

%changelog
* Thu Nov 07 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

