%define rname kbookmarks

Name: kf6-%rname
Version: 6.2.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 access and manipulate bookmarks
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules gcc-c++ qt6-tools-devel qt6-declarative-devel
BuildRequires: kf6-kauth-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kglobalaccel-devel kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel
BuildRequires: kf6-kitemviews-devel kf6-kservice-devel kf6-ktextwidgets-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel
BuildRequires: kf6-kcolorscheme-devel
#BuildRequires: kf6-sonnet-devel kf6-attica-devel

%description
KBookmarks lets you access and manipulate bookmarks stored using the
XBEL format.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf6bookmarks
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6bookmarks
KF6 library

%package -n libkf6bookmarkswidgets
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6bookmarkswidgets
KF6 library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --all-name
%K6find_qtlang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories

%files devel
%_K6inc/KBookmarks*/
%_K6link/lib*.so
%_K6lib/cmake/KF6Bookmarks

%files -n libkf6bookmarks
%_K6lib/libKF6Bookmarks.so.*

%files -n libkf6bookmarkswidgets
%_K6lib/libKF6BookmarksWidgets.so.*


%changelog
* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

