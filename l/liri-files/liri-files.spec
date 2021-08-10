Name: liri-files
Version: 0.2.0
Release: alt2

Summary: Liri file manager
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/lirios/files

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ cmake cmake-modules-liri qt5-tools-devel
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5QuickControls2)
BuildRequires: pkgconfig(taglib)
BuildRequires: qml(Fluid.Controls)

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
%_bindir/liri-files
%_libdir/qt5/qml/Liri/Files
%_datadir/applications/io.liri.Files.desktop
%_datadir/metainfo/*.xml
%_datadir/liri-files

%changelog
* Tue Aug 10 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.0-alt2
- v0.1.0-135-gc48f01d

* Mon Oct 14 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.0-alt1
- initial
