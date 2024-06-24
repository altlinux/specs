%define rname kpty

%def_enable utempter
%define helperpath %_libexecdir/utempter/utempter

Name: kf6-%rname
Version: 6.3.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 interfacing with pseudo terminal devices
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Feb 13 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libcloog-isl4 libqt6-core libqt6-test libstdc++-devel python-base ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ kf6-kcoreaddons-devel kf6-ki18n-devel libutempter-devel python-module-google qt6-base-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf6 rpm-build-ubt
%if_enabled utempter
BuildRequires: libutempter-devel
%endif
BuildRequires: extra-cmake-modules gcc-c++ kf6-kcoreaddons-devel kf6-ki18n-devel qt6-base-devel

%description
This library provides primitives to interface with pseudo terminal devices
as well as a KProcess derived class for running child processes and
communicating with them using a pty.

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

%package -n libkf6pty
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
Requires: utempter
%description -n libkf6pty
KF6 library


%prep
%setup -n %rname-%version

%if_disabled utempter
# disable to find utempter executable
sed -i '/find_file.*UTEMPTER_EXECUTABLE/s/UTEMPTER_EXECUTABLE/UTEMPTER_EXECUTABLE_DISABLE/' cmake/FindUTEMPTER.cmake
%endif

%build
%K6build \
%if_enabled utempter
    -DUTEMPTER_EXECUTABLE=%helperpath \
%endif
    #

%install
%K6install
%find_lang %name --all-name
%K6find_qtlang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories

%files devel
#%_K6inc/kpty_version.h
%_K6inc/KPty/
%_K6link/lib*.so
%_K6lib/cmake/KF6Pty

%files -n libkf6pty
%_K6lib/libKF6Pty.so.*


%changelog
* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

