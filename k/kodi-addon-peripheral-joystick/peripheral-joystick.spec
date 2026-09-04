Name: kodi-addon-peripheral-joystick
Version: 22.0.11
Release: alt1

Summary: Joystick support for Kodi
License: GPLv2
Group: Video
URL: https://github.com/xbmc/peripheral.joystick
VCS: https://github.com/xbmc/peripheral.joystick

ExcludeArch: i586

Source: %name-%version.tar

BuildRequires: cmake gcc-c++ kodi-devel libtinyxml2-devel libudev-devel

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
* Fri Sep 04 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 22.0.11-alt1
- 22.0.11 released

* Thu Apr 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 22.0.6-alt1
- 22.0.6 released

* Sat Nov 01 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 21.1.23-alt1
- 21.1.23 released

* Mon Mar 24 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 21.1.22-alt1
- 21.1.22 released

