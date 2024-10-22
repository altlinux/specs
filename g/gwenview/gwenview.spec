%define rname gwenview

%define sover 5
%define libgwenview libgwenviewlib%sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Image viewer for KDE
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kde5-gwenview = %EVR
Obsoletes: kde5-gwenview < %EVR

Source: %rname-%version.tar
Source1: add-ru-gwenview.po

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-phonon-devel qt6-declarative-devel qt6-svg-devel
BuildRequires: libexiv2-devel libjpeg-devel liblcms2-devel libpng-devel zlib-devel libtiff-devel
#BuildRequires: libcfitsio-devel
BuildRequires: wayland-protocols qt6-wayland-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel
BuildRequires: kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kcrash-devel kf6-kdbusaddons-devel kf6-kdoctools kf6-kdoctools-devel 
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel
BuildRequires: kf6-kitemmodels-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knotifications-devel kf6-kparts-devel
BuildRequires: kf6-kservice-devel kf6-ktextwidgets-devel kf6-kunitconversion-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel
BuildRequires: kf6-baloo-devel kf6-kfilemetadata-devel
BuildRequires: kf6-purpose-devel
BuildRequires: kde6-kcolorpicker-devel kde6-kimageannotator-devel
BuildRequires: plasma6-activities-devel
BuildRequires: kde6-libkdcraw-devel


%description
Fast and easy to use image and video viewer for KDE.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: kde5-gwenview-common = %EVR
Obsoletes: kde5-gwenview-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libgwenview
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libgwenview
%name library


%prep
%setup -n %rname-%version

for f in lib/resize/resizeimagewidget.ui ; do
    sed -i 's|notr=\"true\"||' $f
done

msgcat --use-first po/ru/gwenview.po %SOURCE1 > po/ru/gwenview.po.tmp
cat po/ru/gwenview.po.tmp >po/ru/gwenview.po
rm -f po/ru/gwenview.po.tmp

%build
%K6build

%install
%K6install
%K6install_move data gwenview gvpart solid kconf_update
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%_K6icon/*/*/actions/document-share.*
%_datadir/qlogging-categories6/*.*categories

%files
%_K6bin/*
%_K6plug/kf6/parts/gvpart.so
%_K6plug/kf6/kfileitemaction/*.so
%_K6xdgapp/*.desktop
%_K6data/gwenview/
%_K6data/solid/actions/gwenview*.desktop
%_K6icon/*/*/apps/gwenview.*
%_datadir/metainfo/*.xml

%files devel
#%_K6inc/gwenview_version.h
#%_K6inc/Gwenview/
#%_K6link/lib*.so
#%_K6lib/cmake/Gwenview

%files -n %libgwenview
%_K6lib/libgwenviewlib.so.%sover
%_K6lib/libgwenviewlib.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

