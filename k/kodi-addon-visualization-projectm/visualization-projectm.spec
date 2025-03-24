Name: kodi-addon-visualization-projectm
Version: 21.0.3
Release: alt1

Summary: ProjectM visualization for Kodi
License: GPLv2
Group: Video
Url: https://github.com/xbmc/visualization.projectm

Source: %name-%version.tar

BuildRequires: cmake gcc-c++ kodi-devel projectm-devel
BuildRequires: pkgconfig(gl)

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
%_libdir/kodi/addons/visualization.projectm
%_datadir/kodi/addons/visualization.projectm

%changelog
* Mon Mar 24 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 21.0.3-alt1
- 21.0.3 released

