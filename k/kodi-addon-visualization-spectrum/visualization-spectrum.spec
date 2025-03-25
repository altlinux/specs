Name: kodi-addon-visualization-spectrum
Version: 21.0.2
Release: alt1

Summary: Spectrum visualization for Kodi
License: GPLv2
Group: Video
Url: https://github.com/xbmc/visualization.spectrum

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
%_libdir/kodi/addons/visualization.spectrum
%_datadir/kodi/addons/visualization.spectrum

%changelog
* Mon Mar 24 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 21.0.2-alt1
- 21.0.2 released

