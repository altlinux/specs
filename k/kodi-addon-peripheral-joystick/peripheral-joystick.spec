Name: kodi-addon-peripheral-joystick
Version: 21.1.22
Release: alt1

Summary: Joystick support for Kodi
License: GPLv2
Group: Video
Url: https://github.com/xbmc/peripheral.joystick

Source: %name-%version.tar

BuildRequires: cmake gcc-c++ kodi-devel tinyxml-devel libudev-devel

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
%_libdir/kodi/addons/peripheral.joystick
%_datadir/kodi/addons/peripheral.joystick

%changelog
* Mon Mar 24 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 21.1.22-alt1
- 21.1.22 released

