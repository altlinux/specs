%define rname ktexteditor

Name: kf6-%rname
Version: 6.3.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 full text editor component
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-speech-devel
BuildRequires: libgit2-devel
BuildRequires: libeditorconfig-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kglobalaccel-devel kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel
BuildRequires: kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knotifications-devel kf6-kparts-devel
BuildRequires: kf6-kservice-devel kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel
BuildRequires: kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel
BuildRequires: kf6-syntax-highlighting-devel kf6-ki18n-devel

%description
KTextEditor provides a powerful text editor component that you can embed in your
application.

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
Requires: kf6-syntax-highlighting-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf6texteditor
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6texteditor
KF6 library


%prep
%setup -n %rname-%version

%build
%K6build \
    -DKDE_INSTALL_DATADIR:PATH=%_K6data \
    #

%install
%K6install
%K6install_move data kdevappwizard
mkdir -p %buildroot/%_datadir/katepart6/syntax/

%find_lang %name --all-name
%K6find_qtlang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories
%_datadir/katepart6/
%_K6dbus/system.d/*ktexteditor*.conf

%files devel
%_K6inc/KTextEditor/
%_K6link/lib*.so
%_K6lib/cmake/KF6TextEditor
%_K6data/kdevappwizard/templates/*ktexteditor*

%files -n libkf6texteditor
%_K6exec/kauth/*ktexteditor*
%_K6dbus_sys_srv/*ktexteditor*.service
%_datadir/polkit-1/actions/*ktexteditor*.policy
#
%_K6lib/libKF6TextEditor.so.*
%_K6plug/kf6/parts/katepart.so
#%_K6srv/*
#%_K6srvtyp/*


%changelog
* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

