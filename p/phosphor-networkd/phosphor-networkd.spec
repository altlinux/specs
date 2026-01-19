%define _unpackaged_files_terminate_build 1

Name:    phosphor-networkd
Version: 1.0.0
Release: alt1.gitdce7fe7

Summary: dBUS-based network manager
License: Apache-2.0
Group:   Other
Url:     https://github.com/openbmc/phosphor-networkd.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson

BuildRequires: cmake gcc-c++
BuildRequires: meson

BuildRequires: pkgconfig(phosphor-dbus-interfaces)
BuildRequires: pkgconfig(phosphor-logging)
BuildRequires: pkgconfig(sdbusplus)
BuildRequires: pkgconfig(sdeventplus)
BuildRequires: libnl-devel
BuildRequires: sdbusplus-tools

%description
A Network Manager is a daemon which handles network management operations.
It must implement the xyz.openbmc_project.Network.SystemConfiguration.interface
and org.freedesktop.DBus.ObjectManager.
When the network manager daemon comes up, it should create objects implementing
physical link/virtual interfaces such as
xyz.openbmc_project.Network.EthernetInterface or
xyz.openbmc_project.Network.VLANInterface on the system.

IP address(v4 and v6) objects must be children objects of the physical/virtual
interface object.

# Initial stage. Prepare sources
%prep
%setup

%build
%meson -Dtests=disabled
%meson_build

%install
%meson_install

%preun
%preun_service xyz.openbmc_project.Network

%post
%post_service xyz.openbmc_project.Network

%files
%_bindir/*
%_systemd_dir/network/*.network
%_unitdir/*.service
%_datadir/dbus-1/system.d/*.conf

%changelog
* Thu Jan 15 2026 Anatoly Mukosey <mukav@altlinux.org> 1.0.0-alt1.gitdce7fe7
- Initial build for Sisyphus.
