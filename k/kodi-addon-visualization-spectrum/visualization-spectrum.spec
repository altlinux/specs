Name: kodi-addon-visualization-spectrum
Version: 22.1.0
Release: alt1

Summary: Spectrum visualization for Kodi
License: GPLv2
Group: Video
Url: https://github.com/xbmc/visualization.spectrum

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
%_libdir/kodi/addons/visualization.spectrum
%_datadir/kodi/addons/visualization.spectrum

%changelog
* Tue Jun 23 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 22.1.0-alt1
- 22.1.0 released

* Thu Apr 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 22.0.3-alt1
- 22.0.3 released

* Mon Mar 24 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 21.0.2-alt1
- 21.0.2 released

