%define qt6_version 6.7
%define kf6_version 6.5

Name: budgie-desktop-services
Version: 1.0.3
Release: alt1

Summary: Central hub and orchestrator for Budgie Desktop

License: MPL-2.0
Group: Graphical desktop/Other
Url: https://forge.moderndesktop.dev/BuddiesOfBudgie/budgie-desktop-services

ExcludeArch: %ix86

# Source-url: %url/archive/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake >= 3.20
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++

BuildRequires: pkgconfig(Qt6Core) >= %qt6_version
BuildRequires: pkgconfig(Qt6DBus) >= %qt6_version
BuildRequires: pkgconfig(Qt6WaylandClient) >= %qt6_version
BuildRequires: pkgconfig(wayland-client)
BuildRequires: qt6-wayland-devel

BuildRequires: plasma6-kwayland-devel >= %kf6_version
BuildRequires: libtoml11-devel

# Qt Wayland xdg-shell integration plugin, loaded at runtime
# (without it the service aborts: no Qt platform plugin could be initialized)
Requires: libqt6-wlshellintegration

%description
Central hub and orchestrator for Budgie Desktop with a focus on Budgie 11.
Presently delivers Wayland-native display configuration capabilities
for Budgie 10.10.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%doc COPYING
%_bindir/org.buddiesofbudgie.Services
%_datadir/dbus-1/system.d/org.buddiesofbudgie.Services.conf

%changelog
* Tue Oct 06 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt1
- new version 1.0.3
- update Url: upstream moved to forge.moderndesktop.dev
- require libqt6-wlshellintegration (Qt xdg-shell plugin for wayland)

* Fri Mar 06 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- new version 1.0.2

* Sun Jan 11 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Sisyphus
- add ExcludeArch: ix86
