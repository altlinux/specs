Name: obs-studio-plugin-multi-rtmp
Version: 0.5.0.1
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

ExclusiveArch: x86_64

%description
This is a plugin to streaming to multiple RTMP servers concurrently.
It's able to share encoders with main output of OBS to save CPU power.
It can also use standalone encoders with basic configuration (bitrate).

%prep
%setup

%build
%cmake_insource
%make

%install
mkdir -p %buildroot%_datadir/obs
mkdir -p %buildroot%_libdir/obs-plugins
mv rundir/RelWithDebInfo/data/obs-plugins %buildroot%_datadir/obs
mv rundir/RelWithDebInfo/obs-plugins/64bit/obs-multi-rtmp.so %buildroot%_libdir/obs-plugins/obs-multi-rtmp.so

%files
%doc Readme.md LICENSE
%_libdir/obs-plugins/obs-multi-rtmp.so
%_datadir/obs/obs-plugins/obs-multi-rtmp

%changelog
* Tue Oct 24 2023 Mikhail Tergoev <fidel@altlinux.org> 0.5.0.1-alt1
- initial build for ALT Sisyphus

