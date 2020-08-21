%define _unpackaged_files_terminate_build 1
%define GIT_COMMIT_HASH 361b52b
%define GIT_BRANCH master
%define GIT_REVISION_NUMBER 112

Name: airsane
Version: 0.0.0
Release: alt1.20200805.git361b52b
Summary: A SANE WebScan frontend that supports Apple's AirScan protocol.
License: GPLv3
Group: Graphics

Url: https://github.com/SimulPiscator/AirSane.git
#Git: https://github.com/SimulPiscator/AirSane.git
Source: %name-%version.tar

BuildRequires: ccmake
BuildRequires: gcc-c++
BuildRequires: sane-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libavahi-devel
BuildRequires: libusb-devel

%description
A SANE WebScan frontend that supports Apple's AirScan protocol.
Scanners are detected automatically, and published through mDNS.
Though images may be acquired and transferred in JPEG, PNG, and
PDF/raster format through a simple web interface, AirSane's intended
purpose is to be used with AirScan/eSCL clients such as Apple's Image
Capture.

Images are encoded on-the-fly during acquisition, keeping memory/storage
demands low. Thus, AirSane will run fine on a Raspberry Pi or similar
device.

Authentication and secure communication are not supported.

If you are looking for a powerful SANE web frontend, AirSane may not be
for you. You may be interested in phpSANE instead.

%prep
%setup

# fix build with our libpng
sed -i 's|libpng\/png\.h|png.h|' imageformats/pngencoder.cpp
# change systemd unit-file settings
sed -i 's|\/usr\/local\/bin\/airsaned|/usr/bin/airsaned|' systemd/airsaned.service
sed -i 's|^Group=saned|Group=scanner|' systemd/airsaned.service
sed -i 's|^User=saned|User=_saned|' systemd/airsaned.service
#  look for an icon in a more suitable FS path
sed -i 's|^icon \/etc\/airsane\/Gnome-scanner.png|icon %_iconsdir/hicolor/512x512/apps/Gnome-scanner.png|' etc/options.conf
# provide git version info to build scripts
sed -i 's|git rev-parse --abbrev-ref HEAD|echo "%GIT_BRANCH"|' version.cmake
sed -i 's|git log -1 --format=\%h|echo "%GIT_COMMIT_HASH"|' version.cmake
sed -i 's|git rev-list --count --first-parent HEAD|echo "%GIT_REVISION_NUMBER"|' version.cmake
sed -i 's|sh -c \"git diff --quiet --exit-code \|\| echo +\"|echo ""|' version.cmake

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

# store the icon in a more suitable FS path
mkdir -p %buildroot/%_iconsdir/hicolor/512x512/apps
mv %buildroot/%_sysconfdir/%name/*.png %buildroot/%_iconsdir/hicolor/512x512/apps

%post
%post_service airsaned

%preun
%preun_service airsaned

%files
%doc LICENSE README.md
%_bindir/*
%_unitdir/*
%config(noreplace) %_sysconfdir/%name/*.conf
%config(noreplace) %_sysconfdir/default/%name
%_iconsdir/hicolor/512x512/apps/*.png

%changelog
* Fri Aug 21 2020 Nikolai Kostrigin <nickel@altlinux.org> 0.0.0-alt1.20200805.git361b52b
- Initial build for Sisyphus
