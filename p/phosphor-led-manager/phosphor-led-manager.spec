# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define _libexecdir %_usr/libexec

Name: phosphor-led-manager
Version: 1.0.0
Release: alt1.git67b186c.1

Summary: This project manages LED groups on dbus
License: Apache-2.0
Group: System/Kernel and hardware
Url: https://github.com/openbmc/
Vcs: https://github.com/openbmc/phosphor-led-manager.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: cmake gcc-c++
BuildRequires: meson
BuildRequires: pkgconfig(CLI11)
BuildRequires: cereal-devel
BuildRequires: pkgconfig(nlohmann_json)
BuildRequires: pkgconfig(sdbusplus)
BuildRequires: pkgconfig(phosphor-dbus-interfaces)
BuildRequires: pkgconfig(phosphor-logging)
BuildRequires: pkgconfig(sdeventplus)

%description
This project manages LED groups on dbus. Sometimes many LEDs must be driven
together to indicate some system state.
For example, there can be multiple identify LEDs. When the user wants to identify
the system, they should all light up together.

%prep
%setup

%build
export CXXFLAGS="%{optflags} -std=c++23"
%meson
%meson_build

%install
%meson_install

%preun
%preun_service obmc-fru-fault-monitor
%preun_service xyz.openbmc_project.LED.GroupManager

%post
%post_service obmc-fru-fault-monitor
%post_service xyz.openbmc_project.LED.GroupManager

%files
%doc *.md
%_bindir/*
%_datadir/%name/
%_libexecdir/%name/
%_unitdir/*

%changelog
* Thu Jun 26 2026 Anatoly Mukosey <mukav@altlinux.org> 1.0.0-alt1.git67b186c.1
- Merge with upstream 67b186c.
- Enable tests.

* Wed Aug 13 2025 Andrew A. Vasilyev <andy@altlinux.org> 1.0.0-alt0.2.gccca8eb3
- update from upstream/master

* Wed Apr 30 2025 Andrew A. Vasilyev <andy@altlinux.org> 1.0.0-alt0.1.g275ad18
- Initial build for ALT.
