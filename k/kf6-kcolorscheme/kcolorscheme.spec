%define rname kcolorscheme

Name: kf6-%rname
Version: 6.5.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 widgets for configuration dialogs

Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: qt6-base-devel qt6-declarative-devel
BuildRequires: kf6-kconfig-devel kf6-kguiaddons-devel kf6-ki18n-devel

%description
KColorScheme provides easy-to-use classes to create configuration dialogs, as
well as a set of widgets which uses KConfig to store their settings.

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

%package -n libkf6colorscheme
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6colorscheme
KF6 library

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data locale
%find_lang %name --all-name --with-kde
%K6find_qtlang %name --all-name
rm -rf %buildroot%_libdir/*/*/*/__*


mkdir -p %buildroot/%_K6data/kcolorscheme/


%files common -f %name.lang
%doc LICENSES/* README.md
%dir %_K6data/kcolorscheme/
%_datadir/qlogging-categories6/*.*categories

%files devel
%_K6inc/KColorScheme/
%_K6link/lib*.so
%_K6lib/cmake/KF6ColorScheme
#%_K6plug/designer/*.so

%files -n libkf6colorscheme
%_K6lib/libKF6ColorScheme.so.*

%changelog
* Wed Sep 04 2024 Sergey V Turchin <zerg@altlinux.org> 6.5.0-alt1
- new version

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.4.0-alt1
- new version

* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build
