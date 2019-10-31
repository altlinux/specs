Name: liri-platformtheme
Version: 1.0.0
Release: alt1

Summary: Qt platform theme plugin for apps integration
License: GPL
Group: Graphical desktop/Other
Url: https://github.com/lirios/platformtheme

Source: %name-%version-%release.tar

BuildRequires: cmake cmake-modules-liri
BuildRequires: pkgconfig(Qt5Core)
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
%_libdir/qt5/plugins/platformthemes/libliritheme.so

%changelog
* Mon Oct 14 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- initial
