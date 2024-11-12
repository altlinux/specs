%define rname kgeography

Name: %rname
Version: 24.08.2
Release: alt1
%K6init

Group: Education
Summary: Geography learning program
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-kgeography = %EVR
Obsoletes: kde5-kgeography < %EVR

Source: %rname-%version.tar
Source2: data.tar
Patch: alt-fix-borders.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-kauth-devel kf6-kcodecs-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kdoctools-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kitemviews-devel
BuildRequires: kf6-kservice-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-kcrash-devel
BuildRequires: kf6-kcolorscheme-devel

%description
%summary.

%prep
%setup -n %rname-%version
tar -xvf %SOURCE2 data/
%patch -p2

mv data/flags/{ukraine/Crimea,russia/crimea}.png
mv data/flags/{ukraine/Donetsk,russia/donetsk}.png
mv data/flags/{ukraine/Lugansk,russia/lugansk}.png
mv data/flags/{ukraine/Zaporizhya,russia/zaporozhye}.png
mv data/flags/{ukraine/Kherson,russia/kherson}.png
mv data/flags/{ukraine/Sevastopol-city,russia/sevastopol}.png

%build
%K6build

%install
%K6install
%K6install_move data kgeography
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_datadir/locale/*/LC_SCRIPTS/kgeography/
%_K6bin/kgeography
%_K6data/kgeography/
%_K6icon/*/*/apps/kgeography.*
%_K6xdgapp/org.kde.kgeography.desktop
%_K6cfg/kgeography.kcfg
%_datadir/metainfo/*.xml

%changelog
* Thu Nov 07 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

