%define rname ktextwidgets

Name: kf6-%rname
Version: 6.2.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 text editing widgets
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules gcc-c++ qt6-base-devel qt6-speech-devel qt6-tools-devel qt6-declarative-devel
BuildRequires: kf6-kauth-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kguiaddons-devel
BuildRequires: kf6-ki18n-devel kf6-kiconthemes-devel kf6-kitemviews-devel kf6-kservice-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-sonnet-devel kf6-kcolorscheme-devel

%description
KTextWidgets provides widgets for displaying and editing text. It supports
rich text as well as plain text.

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
Requires: kf6-sonnet-devel kf6-ki18n-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf6textwidgets
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6textwidgets
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

%files devel
%_K6plug/designer/*.so
%_K6inc/KTextWidgets/
%_K6link/lib*.so
%_K6lib/cmake/KF6TextWidgets

%files -n libkf6textwidgets
%_K6lib/libKF6TextWidgets.so.*


%changelog
* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

