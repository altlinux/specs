Name: phosphor-led-sysfs
Version: 1.0.0
Release: alt0.1.gf8548eeb

Summary: Application to manage BMC-owned LEDs using Linux sysfs interfaces
License: Apache-2.0
Group: System/Kernel and hardware
Url: https://github.com/openbmc/
Vcs: https://github.com/openbmc/phosphor-led-sysfs.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: cmake gcc-c++
BuildRequires: meson
BuildRequires: pkgconfig(CLI11)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(phosphor-dbus-interfaces)
BuildRequires: pkgconfig(phosphor-logging)
BuildRequires: pkgconfig(sdbusplus)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(udev)

%description
This project exposes physical LEDs on dbus.

%prep
%setup

%build
export CXXFLAGS="%{optflags} -std=c++23"
%meson
%meson_build

%install
%meson_install

%preun
%preun_service phosphor-ledcontroller

%post
%post_service phosphor-ledcontroller

%files
%doc *.md
%_prefix/libexec/*
%_unitdir/*
%_datadir/dbus-1/system-services/*
%_udevrulesdir/*.rules

%changelog
* Wed Apr 23 2025 Andrew A. Vasilyev <andy@altlinux.org> 1.0.0-alt0.1.gf8548eeb
- Initial build for ALT.
