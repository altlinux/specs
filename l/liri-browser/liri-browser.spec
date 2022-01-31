Name: liri-browser
Version: 0.0.20210809
Release: alt2

Summary: A cross-platform Material Design web browser
License: GPLv3
Group: Networking/WWW
Url: https://github.com/lirios/browser

# no qtwebengine
ExcludeArch: ppc64le

Source0: %name-%version-%release.tar

BuildRequires: gcc-c++ cmake cmake-modules-liri qt5-tools-devel
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5QuickControls2)
BuildRequires: pkgconfig(Qt5WebEngine)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: qml(QtGraphicalEffects)

%description
%summary

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/liri-browser
%_datadir/applications/io.liri.Browser.desktop
%_iconsdir/*/*/*/*.png
%_iconsdir/*/*/*/*.svg

%changelog
* Mon Jan 31 2022 Sergey V Turchin <zerg@altlinux.org> 0.0.20210809-alt2
- exclude ppc64le from build

* Tue Aug 10 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20210809-alt1
- updated from git.a1d14aa

* Fri Nov 01 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20190816-alt1
- initial
