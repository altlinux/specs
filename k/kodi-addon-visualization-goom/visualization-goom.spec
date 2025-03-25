Name: kodi-addon-visualization-goom
Version: 21.0.0
Release: alt1

Summary: GOOM visualization for Kodi
License: GPLv2
Group: Video
Url: https://github.com/xbmc/visualization.goom

Source: %name-%version.tar

BuildRequires: cmake gcc-c++ kodi-devel libglm-devel
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
%_libdir/kodi/addons/visualization.goom
%_datadir/kodi/addons/visualization.goom

%changelog
* Mon Mar 24 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 21.0.0-alt1
- 21.0.0 released

