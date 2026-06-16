%define _unpackaged_files_terminate_build 1

Name: obs-studio-plugin-multi-rtmp
Version: 0.7.4
Release: alt1

Summary: This is a plugin to streaming to multiple RTMP servers concurrently

License: GPLv2
Group: Video
Url: https://github.com/sorayuki/obs-multi-rtmp

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: pkgconfig(libobs)
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Network)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6Xml)
BuildRequires: pkgconfig(vulkan)

Requires: obs-studio

ExcludeArch: %ix86 %arm %mips

%description
This is a plugin to streaming to multiple RTMP servers concurrently.
It's able to share encoders with main output of OBS to save CPU power.
It can also use standalone encoders with basic configuration (bitrate).

%prep
%setup

%build
%add_optflags -Wno-reorder
%cmake -DENABLE_QT=ON
%cmake_build

%install
%cmake_install

%files
%doc README.md LICENSE
%_libdir/obs-plugins/obs-multi-rtmp.so
%_datadir/obs/obs-plugins/obs-multi-rtmp

%changelog
* Tue Jun 16 2026 Mikhail Tergoev <fidel@altlinux.org> 0.7.4-alt1
- 0.7.4

* Sun Dec 28 2025 Mikhail Tergoev <fidel@altlinux.org> 0.7.3.2-alt1
- 0.7.3.2

* Wed Feb 28 2024 Ivan A. Melnikov <iv@altlinux.org> 0.5.0.1-alt1.1
- NMU: Build on all 64-bit architectures

* Tue Oct 24 2023 Mikhail Tergoev <fidel@altlinux.org> 0.5.0.1-alt1
- initial build for ALT Sisyphus

