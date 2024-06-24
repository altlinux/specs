%define rname kglobalaccel
%ifndef _unitdir_user
%define _unitdir_user %prefix/lib/systemd/user
%endif
%define service_name plasma-kglobalaccel

Name: kf6-%rname
Version: 6.3.0
Release: alt1
%K6init

Group: System/Libraries
Summary: KDE Frameworks 6 global desktop keyboard shortcuts
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-tools-devel
BuildRequires: libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel
BuildRequires: libXdmcp-devel libXft-devel libXinerama-devel libXmu-devel libXpm-devel
BuildRequires: libXrandr-devel libXtst-devel libXv-devel libXxf86misc-devel
BuildRequires: libXxf86vm-devel libxcbutil-keysyms-devel libxkbfile-devel
#BuildRequires: kf6-kconfig-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
#BuildRequires: kf6-ki18n-devel kf6-kwindowsystem-devel kf6-kservice-devel

%description
KGlobalAccel allows you to have global accelerators that are independent of
the focused window.  Unlike regular shortcuts, the application's window does not
need focus for them to be activated.

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

%package -n libkf6globalaccel
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6globalaccel
KF6 library

%package -n libkf6globalaccelprivate
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6globalaccelprivate
KF6 library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data locale
mkdir -p %buildroot/%_K6data/kglobalaccel/
%find_lang %name --all-name
%K6find_qtlang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories
%dir %_K6data/kglobalaccel/

#%files
#%_bindir/*6
#%_K6bin/kglobalaccel6
#%_K6srv/kglobalaccel6.desktop
#%_K6dbus_srv/org.kde.kglobalaccel.service
#%_K6plug/org.kde.kglobalaccel6*/
#%_unitdir_user/%service_name.service

%files devel
%_K6inc/KGlobalAccel/
%_K6link/lib*.so
%_K6lib/cmake/KF6GlobalAccel/
%_K6dbus_iface/kf6_org.kde.??lobal?ccel*

%files -n libkf6globalaccel
%_K6lib/libKF6GlobalAccel.so.*
#%files -n libkf6globalaccelprivate
#%_K6lib/libKF6GlobalAccelPrivate.so.*


%changelog
* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

