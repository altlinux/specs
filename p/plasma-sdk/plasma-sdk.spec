%define rname plasma-sdk
%filter_from_requires /inkscape/d

Name: plasma-sdk
Version: 6.1.2
Release: alt1
%K6init

Group: Development/KDE and QT
Summary: KDE Frameworks 6 Applications useful for Plasma Development
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: kf6-kirigami
Provides: plasma5-sdk = %EVR
Obsoletes: plasma5-sdk < %EVR

Source: %rname-%version.tar
Patch1: alt-fix-lnf-double-create.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-svg-devel qt6-5compat-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kdeclarative-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel
BuildRequires: kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knewstuff-devel kf6-kpackage-devel kf6-kparts-devel kf6-kservice-devel
BuildRequires: kf6-ktexteditor-devel kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel
BuildRequires: kf6-solid-devel kf6-sonnet-devel kf6-kdbusaddons-devel kf6-kitemmodels-devel
BuildRequires: kf6-kdoctools-devel kf6-syntax-highlighting-devel kf6-ksvg-devel kf6-kirigami-devel
BuildRequires: plasma6-lib-devel plasma6-plasma5support-devel

%description
Applications useful for Plasma Development.


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build \
    #
#    -DPLASMATE_BUILD_WITH_KDEVPLATFORM=ON \

%install
%K6install
%K6install_move data kpackage
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/*
%_K6xdgapp/*.desktop
%_K6plug/ktexteditor/
%_K6data/plasma/shells/*/
%_K6data/kpackage/
%_datadir/zsh/site-functions/_*
%_datadir/metainfo/*.xml



%changelog
* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

