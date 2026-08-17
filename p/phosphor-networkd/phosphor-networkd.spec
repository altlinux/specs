%define _unpackaged_files_terminate_build 1

Name:    phosphor-networkd
Version: 1.0.0
Release: alt2.git09916b5.1

Summary: dBUS-based network manager
License: Apache-2.0
Group:   Other
Url:     https://github.com/openbmc/phosphor-networkd.git

Source: %name-%version.tar

Patch: fix_build_issues_memcpy_is_not_a_member_of_std.patch

BuildRequires(pre): rpm-macros-meson

BuildRequires: cmake gcc-c++
BuildRequires: meson

BuildRequires: pkgconfig(phosphor-dbus-interfaces)
BuildRequires: pkgconfig(phosphor-logging)
BuildRequires: pkgconfig(sdbusplus)
BuildRequires: pkgconfig(sdeventplus)
BuildRequires: libnl-devel
BuildRequires: sdbusplus-tools
BuildRequires: cli11-devel

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
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
# Removing unused DBus API wrappers
rm -rf %buildroot%_includedir/xyz/openbmc_project/Network

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
* Thu Jun 26 2026 Anatoly Mukosey <mukav@altlinux.org> 1.0.0-alt2.git09916b5.1
- New snapshot.
- Enable tests.

* Thu Jan 15 2026 Anatoly Mukosey <mukav@altlinux.org> 1.0.0-alt1.gitdce7fe7
- Initial build for Sisyphus.
