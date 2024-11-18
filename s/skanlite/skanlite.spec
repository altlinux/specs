
%define rname skanlite

Name: %rname
Version: 24.08.3
Release: alt1
%K6init

Group: Graphics
Summary: Image scanning application
Url: http://www.kde.org
License: GPL-2.0-only or GPL-3.0-only

#Requires: hplip-sane
Provides:  kde5-skanlite = %EVR
Obsoletes: kde5-skanlite < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libpng-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kdoctools kf6-kdoctools-devel kf6-ki18n-devel kf6-kio-devel
BuildRequires: kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel
BuildRequires: kde6-libksane-devel

%description
Skanlite is a simple image scanning application that does nothing more
than scan and save images. It can open a save dialog for every image
scanned or save the images immediately in a specified directory
with auto-generated names and format.

%prep
%setup -n %rname-%version

%build
%K6build \
    -DQT_MAJOR_VERSION=6 \
    #

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/skanlite
%_K6xdgapp/*skanlite*.desktop
%_K6icon/hicolor/*/apps/*skanlite*
%_datadir/metainfo/*.xml


%changelog
* Mon Nov 18 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

