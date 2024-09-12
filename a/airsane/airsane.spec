%define _unpackaged_files_terminate_build 1

Name: airsane
Version: 0.4.2
Release: alt1
Summary: A SANE WebScan frontend that supports Apple's AirScan protocol.
License: GPLv3
Group: Graphics

Url: https://github.com/SimulPiscator/AirSane.git
VCS: https://github.com/SimulPiscator/AirSane.git

Source: %name-%version.tar

Provides: AirSane = %EVR
# user "_saned" in sane-server, group "scanner" in libsane
Requires: sane-server libsane
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake >= 3.5 ninja-build
BuildRequires: gcc-c++
BuildRequires: libsane-devel
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
#%%autopatch -p1

# fix build with our libpng
sed -i 's|libpng/png.h|png.h|' imageformats/pngencoder.cpp
#  look for an icon in a more suitable FS path
sed -i 's|^icon /etc/airsane/Gnome-scanner.png|icon %_iconsdir/hicolor/512x512/apps/Gnome-scanner.png|' etc/options.conf
# fix systemd unit
sed -i 's|/lib/systemd/system|%_unitdir|' CMakeLists.txt
sed -i 's|/etc/default|%_sysconfdir/sysconfig|' CMakeLists.txt
sed -i 's|/etc/default/airsane|%_sysconfdir/sysconfig/airsane|' systemd/airsaned.service.in
sed -i 's|^Group=saned|Group=scanner|' systemd/airsaned.service.in
sed -i 's|^User=saned|User=_saned|' systemd/airsaned.service.in


%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -GNinja
%cmake_build

%install
%cmake_install

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
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*.conf
%config(noreplace) %_sysconfdir/sysconfig/%name
%_iconsdir/hicolor/*

%changelog
* Thu Sep 12 2024 Alexey Shabalin <shaba@altlinux.org> 0.4.2-alt1
- 0.4.2 (NMU)
- add requires to sane-server and libsane for add user "_saned" and add group "scaner"
- move config to /etc/sysconfig
- fixed path systemd unit

* Fri Aug 4 2023 Vasiliy Kovalev <kovalev@altlinux.org> 0.3.5-alt1
- 0.3.4 -> 0.3.5

* Mon Jul 10 2023 Artyom Bystrov <arbars@altlinux.org> 0.3.4-alt2
- Fix build on GCC13

* Mon Jul 4 2022 Vasiliy Kovalev <kovalev@altlinux.org> 0.3.4-alt1
- Updated to 0.3.4
- Add patches
  + airsane-0.3.4-alt-strerror-fix.patch to fix error undeclared function
  + airsane-0.3.4-alt-mPort-fix.patch to fix warning incorrect initialization
    sequence of class members

* Fri Aug 21 2020 Nikolai Kostrigin <nickel@altlinux.org> 0.0.0-alt1.20200805.git361b52b
- Initial build for Sisyphus
