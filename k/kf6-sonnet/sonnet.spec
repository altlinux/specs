%define rname sonnet

Name: kf6-%rname
Version: 6.4.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 multi-language spell checker
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Dec 26 2014 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libcloog-isl4 libqt6-core libqt6-gui libqt6-test libqt6-widgets libqt6-xml libstdc++-devel python-base qt6-base-devel qt6-tools ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ libhunspell-devel python-module-google qt6-tools-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf6 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++ qt6-tools-devel qt6-declarative-devel
BuildRequires: libhunspell-devel

%description
Sonnet is a plugin-based spell checking library for Qt-based
applications. It supports several different plugins.

%package common
Summary: %name common package
Group: System/Configuration/Other
#BuildArch: noarch
Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf6sonnetcore
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6sonnetcore
KF6 library

%package -n libkf6sonnetui
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6sonnetui
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
%dir %_K6plug/kf6/sonnet/

%files devel
%_K6bin/parsetrigrams6
%_bindir/parsetrigrams6
%_K6inc/Sonnet*/
%_K6link/lib*.so
%_K6lib/cmake/KF6Sonnet

%files -n libkf6sonnetcore
%_K6plug/designer/*.so
%_K6lib/libKF6SonnetCore.so.*
%_K6plug/kf6/sonnet/sonnet_hunspell.so
%files -n libkf6sonnetui
%_K6lib/libKF6SonnetUi.so.*
%_K6qml/org/kde/sonnet/


%changelog
* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.4.0-alt1
- new version

* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

