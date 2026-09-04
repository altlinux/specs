Name: kodi-addon-visualization-goom
Version: 22.1.0
Release: alt1

Summary: GOOM visualization for Kodi
License: GPLv2
Group: Video
Url: https://github.com/xbmc/visualization.goom

ExcludeArch: i586

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
* Mon Jun 22 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 22.1.0-alt1
- 22.1.0 released

* Mon Mar 24 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 21.0.0-alt1
- 21.0.0 released

