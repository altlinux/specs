Name: liri-terminal
Version: 0.2.0
Release: alt2

Summary: A Material Design terminal
License: GPLv3
Group: Terminals
Url: https://github.com/lirios/terminal

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ cmake cmake-modules-liri qt5-tools-devel
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5QuickControls2)
BuildRequires: pkgconfig(Qt5GSettings)

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
%_bindir/liri-terminal
%_libdir/qt5/qml/Liri/Terminal
%_datadir/applications/io.liri.Terminal.desktop
%_datadir/glib-2.0/schemas/io.liri.Terminal.gschema.xml
%_datadir/metainfo/*.xml
%_datadir/liri-terminal

%changelog
* Tue Aug 10 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.0-alt2
- v0.2.0-114-g8efb3e0

* Mon Oct 14 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.0-alt1
- initial
